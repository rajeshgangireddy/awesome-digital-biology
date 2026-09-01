"""
fetch_papers.py

Scans arXiv and bioRxiv for new papers matching the keyword filters in
config.yaml, deduplicates against data/seen.json, and appends new candidates
to docs/staging/recent-papers.md grouped by category.

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
BIORXIV_API = "https://api.biorxiv.org/details/biorxiv/{start}/{end}/{cursor}/json"


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
        f.write("\n")


def query_arxiv(keyword, categories, max_results, since):
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    # Use an AND-of-terms match rather than a literal quoted phrase: exact
    # phrase matching is too restrictive (few abstracts contain a 3-4 word
    # phrase verbatim) and was causing the scanner to find almost nothing.
    # Requiring all words present (in any order/position) is much more
    # permissive while still filtering on topical relevance.
    words = keyword.split()
    if len(words) > 1:
        kw_query = " AND ".join(f"all:{w}" for w in words)
    else:
        kw_query = f"all:{keyword}"
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

    # arXiv rate-limits fairly aggressively; a single 429/timeout shouldn't
    # silently look identical to "genuinely no results". Retry a couple of
    # times with backoff before giving up on this keyword.
    data = None
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
            break
        except Exception as e:
            last_err = e
            if attempt < 2:
                time.sleep(10 * (attempt + 1))
    if data is None:
        print(f"  [warn] arXiv query failed for '{keyword}' after retries: {last_err}", file=sys.stderr)
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


def keyword_matches(text, keyword):
    """Match all terms in a keyword, regardless of their order."""
    text = text.casefold()
    return all(word.casefold() in text for word in keyword.split())


def query_biorxiv(source_categories, category_keywords, max_results, since):
    """Fetch recent bioRxiv records and group keyword matches by list category."""
    start = since.date().isoformat()
    end = datetime.now(timezone.utc).date().isoformat()
    wanted_sources = {category.casefold() for category in source_categories}
    matches = {category: [] for category in category_keywords}
    cursor = 0

    while True:
        url = BIORXIV_API.format(start=start, end=end, cursor=cursor)
        data = None
        last_err = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "awesome-digital-biology-bot/1.0"},
                )
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = json.load(resp)
                break
            except Exception as e:
                last_err = e
                if attempt < 2:
                    time.sleep(10 * (attempt + 1))

        if data is None:
            print(
                f"  [warn] bioRxiv query failed at cursor {cursor} after retries: {last_err}",
                file=sys.stderr,
            )
            break

        collection = data.get("collection", [])
        if not collection:
            break

        for paper in collection:
            if paper.get("category", "").casefold() not in wanted_sources:
                continue
            title = " ".join(paper.get("title", "").split())
            abstract = " ".join(paper.get("abstract", "").split())
            searchable = f"{title} {abstract}"
            matching_category = next(
                (
                    category
                    for category, keywords in category_keywords.items()
                    if any(keyword_matches(searchable, keyword) for keyword in keywords)
                ),
                None,
            )
            if matching_category is None:
                continue

            doi = paper.get("doi", "").strip()
            if not doi:
                continue
            authors = [
                author.strip()
                for author in paper.get("authors", "").split(";")
                if author.strip()
            ]
            matches[matching_category].append(
                {
                    "id": f"https://doi.org/{doi}",
                    "title": title,
                    "summary": abstract,
                    "authors": authors,
                    "published": paper.get("date", ""),
                    "link": f"https://doi.org/{doi}",
                    "source": "bioRxiv",
                    "institution": paper.get("author_corresponding_institution", ""),
                }
            )

        message = data.get("messages", [{}])[0]
        total = int(message.get("count_new_papers", "0"))
        cursor += len(collection)
        if cursor >= total:
            break
        time.sleep(1)

    return {
        category: papers[:max_results] for category, papers in matches.items()
    }


def slugify_category(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def render_entry(paper):
    authors = paper["authors"]
    author_str = authors[0] + " et al." if len(authors) > 1 else (authors[0] if authors else "Unknown")
    source = paper.get("source", "arXiv")
    institution = paper.get("institution", "")
    affiliation = f" · {institution}" if institution else ""
    return (
        f"- [{paper['title']}]({paper['link']})\n"
        f"  - {author_str}{affiliation} · {source} {paper['published']}\n"
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
    biorxiv_config = config["sources"].get("biorxiv", {})

    new_by_category = {}
    biorxiv_matches = query_biorxiv(
        biorxiv_config.get("categories", []),
        config["categories"],
        max_results,
        since,
    )
    for category, keywords in config["categories"].items():
        found = []
        for kw in keywords:
            results = query_arxiv(kw, arxiv_categories, max_results, since)
            for r in results:
                if r["id"] not in seen:
                    found.append(r)
                    seen.add(r["id"])
            time.sleep(5)  # be polite to the arXiv API
        for r in biorxiv_matches.get(category, []):
            if r["id"] not in seen:
                found.append(r)
                seen.add(r["id"])
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
