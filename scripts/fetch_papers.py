"""
fetch_papers.py

Scans arXiv (and, best-effort, bioRxiv) for new papers matching the keyword
filters in config.yaml, deduplicates against data/seen.json, and appends new
candidates to docs/staging/recent-papers.md grouped by category.

This script is intentionally dependency-light (stdlib + PyYAML + requests)
so it runs cheaply inside a GitHub Actions job. It does NOT call any LLM by
default; classification here is simple keyword-query based (the arXiv query
IS the classification). A future enhancement can pipe candidates through
GitHub Copilot CLI or a local LLM for smarter dedup/summarization -- see
scripts/README.md.
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT, "scripts", "config.yaml")
SEEN_PATH = os.path.join(ROOT, "data", "seen.json")
STAGING_PATH = os.path.join(ROOT, "docs", "staging", "recent-papers.md")

ARXIV_API = "http://export.arxiv.org/api/query"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


def load_seen():
    if os.path.exists(SEEN_PATH):
        with open(SEEN_PATH, "r") as f:
            return set(json.load(f))
    return set()


def save_seen(seen):
    os.makedirs(os.path.dirname(SEEN_PATH), exist_ok=True)
    with open(SEEN_PATH, "w") as f:
        json.dump(sorted(seen), f, indent=2)


def query_arxiv(keyword, categories, max_results, since):
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    kw_query = f'all:"{keyword}"'
    query = f"({kw_query}) AND ({cat_query})"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-digital-biology-bot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except Exception as e:
        print(f"  [warn] arXiv query failed for '{keyword}': {e}", file=sys.stderr)
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(data)
    entries = []
    for entry in root.findall("atom:entry", ns):
        arxiv_id = entry.find("atom:id", ns).text.strip()
        title = " ".join(entry.find("atom:title", ns).text.split())
        summary = " ".join(entry.find("atom:summary", ns).text.split())
        published = entry.find("atom:published", ns).text
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
        pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
        if pub_date < since:
            continue
        entries.append(
            {
                "id": arxiv_id,
                "title": title,
                "summary": summary,
                "authors": authors,
                "published": published[:10],
                "link": arxiv_id,
            }
        )
    return entries


def slugify_category(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def render_entry(paper):
    authors = paper["authors"]
    author_str = authors[0] + " et al." if len(authors) > 1 else (authors[0] if authors else "Unknown")
    return (
        f"- [{paper['title']}]({paper['link']})\n"
        f"  - {author_str} · arXiv {paper['published']}\n"
        f"  - Keywords: _unreviewed_\n"
    )


def update_staging(new_by_category):
    if not any(new_by_category.values()):
        print("No new papers found; staging file unchanged.")
        return False

    with open(STAGING_PATH, "r") as f:
        content = f.read()

    marker_start = "<!-- BOT:START -->"
    marker_end = "<!-- BOT:END -->"
    if marker_start not in content or marker_end not in content:
        print("Staging file missing bot markers; aborting write.", file=sys.stderr)
        return False

    pre, rest = content.split(marker_start, 1)
    _, post = rest.split(marker_end, 1)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    body_parts = [f"\n\n### Scan on {today}\n"]
    for category, papers in new_by_category.items():
        if not papers:
            continue
        body_parts.append(f"\n#### {category}\n\n")
        for p in papers:
            body_parts.append(render_entry(p))

    new_block = marker_start + "".join(body_parts) + "\n" + marker_end
    with open(STAGING_PATH, "w") as f:
        f.write(pre + new_block + post)
    return True


def main():
    config = load_config()
    seen = load_seen()
    lookback_days = config.get("lookback_days", 3)
    since = datetime.now(timezone.utc) - timedelta(days=lookback_days)
    max_results = config.get("max_results_per_category", 15)
    arxiv_categories = config["sources"]["arxiv"]["categories"]

    new_by_category = {}
    for category, keywords in config["categories"].items():
        found = []
        for kw in keywords:
            results = query_arxiv(kw, arxiv_categories, max_results, since)
            for r in results:
                if r["id"] not in seen:
                    found.append(r)
                    seen.add(r["id"])
            time.sleep(3)  # be polite to the arXiv API
        # de-dup within category by id, keep order
        dedup = {r["id"]: r for r in found}
        new_by_category[category] = list(dedup.values())
        print(f"{category}: {len(new_by_category[category])} new paper(s)")

    changed = update_staging(new_by_category)
    save_seen(seen)

    if changed:
        print("Staging file updated.")
    else:
        print("Nothing to update.")


if __name__ == "__main__":
    main()
