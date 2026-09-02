# Contributing to Awesome Digital Biology

Thanks for helping make this the go-to list for AI-driven digital biology!

## Quick rules

1. **One entry per PR** (small PRs are reviewed faster). Batches are fine for
   automated/bot PRs only.
2. **Search first** — make sure the resource is not already listed.
3. Add the entry to the most relevant section and follow the table format
   below.
4. Keep entries ordered **newest first** within each section. Use the
   publication or release year; use `—` when a year does not apply.
5. The resource should be **relevant, high quality, and either have code, a
   dataset, or a notable publication** behind it. We do not list low-effort
   blog posts, unpublished/uncited preprints with no code, or promotional
   content.
6. Run a link check locally if possible before submitting.

## Table entry format

Add one row to the table in the appropriate section:

```markdown
| **Canonical name** — Short descriptor | [paper](paper-link) · [code](code-link) | 2025 | Authors · Organization | Short summary or keywords |
```

Use the canonical project name or work title in the first column. For
paper-centric entries, include the full title after the canonical name when it
helps identify the work. Links are intentionally flexible: include one primary
link and only one or two useful complementary links, choosing labels such as
`[paper]`, `[code]`, `[project]`, `[dataset]`, `[demo]`, or `[benchmark]` as
appropriate. Do not add documentation, API, weights, or other links unless
they are genuinely useful for that resource.

The `![Stars](https://img.shields.io/github/stars/owner/repo?style=social)`
badge is optional and should appear immediately after the primary GitHub/code
link when a public repository exists. Use the dynamic shields.io badge; do
not hardcode a star count.

Tables are manually ordered and are **not interactively sortable** by clicking
their headers on GitHub.

## Example

```markdown
| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **ProteinMPNN** — Robust deep learning-based protein sequence design | [paper](https://www.science.org/doi/10.1126/science.add2187) · [code](https://github.com/dauparas/ProteinMPNN) ![Stars](https://img.shields.io/github/stars/dauparas/ProteinMPNN?style=social) | 2022 | Dauparas et al. · University of Washington (Baker Lab) | Fixed-backbone sequence design |
```

## The Highlight badge

Maintainers may add a
`![Highlight](https://img.shields.io/badge/-Highlight-orange)` badge at the
beginning of the Project / work cell for a particularly significant resource:
a landmark, field-defining work, or must-read for newcomers.

```markdown
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **Canonical name** | [paper](link) | 2025 | Authors · Organization | Why it matters |
```

Highlight is an editorial signal, not a benchmark or SOTA claim. It does not
imply that entries without the badge are unimportant. Propose new Highlight
badges through PR discussion rather than adding them as part of a routine
entry update.

## Adding a new section

If you think a new top-level category is needed, open an issue first to
discuss it. We intentionally keep the taxonomy tight to avoid the list
becoming an unstructured dump.

## Bot-sourced "Recent Papers" section

Entries in `docs/staging/recent-papers.md` are proposed automatically every
two days by the scanning workflow. Feel free to:

- Move a strong candidate from staging into its permanent section as a table
  row via PR.
- Remove stale or irrelevant staged entries.

## Code of Conduct

Please note this project follows the [Code of Conduct](CODE_OF_CONDUCT.md).
