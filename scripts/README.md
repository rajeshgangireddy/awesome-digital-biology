# Automation scripts

## `fetch_papers.py`

Queries the arXiv and bioRxiv APIs for new papers matching the keyword filters
defined in `config.yaml`, deduplicates against `data/seen.json`, and appends
new candidates into `docs/staging/recent-papers.md` grouped by category. Run
by `.github/workflows/daily-scan.yml` every 2 days, which then opens a PR with
the changes (never commits directly to `main`).

Run locally:

```bash
pip install -r scripts/requirements.txt
python scripts/fetch_papers.py
```

## Roadmap / nice-to-haves

- Pipe each candidate through an LLM (GitHub Copilot CLI headless mode or a
  local Ollama model) to: generate a one-line summary, extract keywords, and
  auto-classify into the closest permanent section instead of a flat keyword
  bucket. Keep human-in-the-loop via PR review either way.
- Add medRxiv API support.
- Add a `awesome-lint`/`lychee` link-checker workflow (see
  `.github/workflows/lint-links.yml`).
