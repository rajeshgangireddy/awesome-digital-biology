# Contributing to Awesome Digital Biology

Thanks for helping make this the go-to list for AI-driven digital biology! 🎉

## Quick rules

1. **One entry per PR** (small PRs are reviewed faster). Batches are fine for
   automated/bot PRs only.
2. **Search first** — make sure the resource isn't already listed.
3. **Follow the entry format** exactly (see below).
4. Add each entry to the correct section, ordered **newest first** (most
   recently published paper at the top).
5. The resource should be **relevant, high quality, and either has code, a
   dataset, or a notable publication** behind it. We do not list low-effort
   blog posts, unpublished/uncited preprints with no code, or promotional
   content.
6. Run a link-check locally if possible before submitting.

## Entry format

```
- [Title](paper-or-repo-link) [code](code-link-if-different) ![Stars](https://img.shields.io/github/stars/owner/repo?style=social)
  - Authors (first author et al.) · Institution/Company · Venue/Year
  - Keywords: keyword1, keyword2, keyword3
```

The `![Stars]` badge is optional but recommended whenever the resource has a
public GitHub repo — use the shields.io dynamic badge (`?style=social`)
so the count stays up to date automatically; don't hardcode a star number.

Example:

```
- [Robust deep learning-based protein sequence design using ProteinMPNN](https://www.science.org/doi/10.1126/science.add2187) [code](https://github.com/dauparas/ProteinMPNN) ![Stars](https://img.shields.io/github/stars/dauparas/ProteinMPNN?style=social)
  - Dauparas et al. · University of Washington (Baker Lab) · Science 2022
  - Keywords: fixed-backbone design, message-passing, structure-conditioned
```

## The Highlight badge

Maintainers may add a `![Highlight](https://img.shields.io/badge/-Highlight-blue)`
badge before the title of a paper they consider especially significant —
landmark, field-defining, or otherwise a must-read:

```
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [Title](link) [code](code-link)
  - Authors · Institution/Company · Venue/Year
  - Keywords: ...
```

This is an editorial call, not a benchmark/SOTA claim — it does not imply
other unbadged papers are unimportant. Use it for papers that set a
direction, defined a sub-field, or are simply must-reads for newcomers,
regardless of publication date. Propose new Highlight badges via PR
discussion rather than adding them as part of a routine paper addition.

## Adding a new section

If you think a new top-level category is needed, open an issue first to
discuss — we intentionally keep the taxonomy tight to avoid the list
becoming an unstructured dump.

## Bot-sourced "Recent Papers" section

Entries in `docs/staging/recent-papers.md` are proposed automatically every
two days by our scanning workflow. Feel free to:

- Move a strong candidate from staging into its permanent section (with a
  proper entry format) via PR.
- Remove stale/irrelevant staged entries.

## Code of Conduct

Please note this project follows a [Code of Conduct](CODE_OF_CONDUCT.md).
