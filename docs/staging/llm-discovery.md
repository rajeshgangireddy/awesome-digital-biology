# LLM Discovery Log

This manual source ledger records items considered for the curated README. Entries below were verified on 2026-10-21 and proposed for human review in the associated README discovery pull request.

## Recommended candidates

| Work | README section | Type / date | Discovery source | Primary verification |
|---|---|---|---|---|
| RFD4-Proteina | Protein & Binder/Antibody Design | Software/model release; Hugging Face model repo updated 2026-10-21 09:00 UTC | [Hugging Face model page](https://huggingface.co/nvidia/RFD4-Proteina) | [Project page](https://rfd4-proteina.org/), [GitHub repository](https://github.com/RosettaCommons/RFD4-Proteina), and [model card](https://huggingface.co/nvidia/RFD4-Proteina) |
| AlphaProteo | Protein & Binder/Antibody Design | arXiv technical report, 2024-09-12 | Older-omission review | [paper](https://arxiv.org/abs/2409.08022); official [trusted-tester notebooks](https://github.com/google-deepmind/ap_trusted_testers) |
| Aptamers as a sandbox for lab-in-the-loop agentic molecular discovery | Skills and Agents | arXiv preprint, 2026-10-17 | [Google Research publication listing](https://research.google/pubs/aptamers-as-a-sandbox-for-lab-in-the-loop-agentic-molecular-discovery/) | [arXiv paper](https://arxiv.org/abs/2610.24806v1) |
| MADDIE | Skills and Agents | arXiv preprint, 2026-10-12; v2 2026-10-20 | [arXiv record](https://arxiv.org/abs/2610.16975v2) | Public [repository](https://github.com/ninglab/MADDIE) |
| Biomni | Skills and Agents | bioRxiv preprint, 2025-06-02; older omission | README gap review | [bioRxiv paper](https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1); [official repository](https://github.com/snap-stanford/Biomni) |
| CellNet | Single-Cell & Omics Foundation Models | Software/model release, 2026-10-15 | Recent [repository creation](https://github.com/daydayup-xq/CellNet) | [Project page](https://daydayup-xq.github.io/CellNet/) and repository |
| ProteinGeoBench | Datasets & Benchmarks | arXiv preprint, 2026-10-19 | Recent [GitHub repository](https://github.com/Protege-AI/ProteinGeoBench) | [arXiv paper](https://arxiv.org/abs/2610.26829v1) and benchmark repository |
| SelectBench | Datasets & Benchmarks | NeurIPS 2026 accepted paper, 2026-10-16 | [arXiv record](https://arxiv.org/abs/2610.24124v1) | Public [benchmark and data repository](https://github.com/lovetaro/selectbench) |
| spora | Datasets & Benchmarks | NeurIPS 2026 accepted paper, 2026-10-15 | [arXiv record](https://arxiv.org/abs/2610.24002v1) | [Project documentation](https://spora.epfl.ch/docs/), [data portal landing page](https://spora.bioimagearchive.org/), and [benchmark](https://github.com/bunnelab/spora-bench) |
| Therapeutics Data Commons (TDC) | Platforms & Model Hubs | NeurIPS 2021 paper and platform; older omission | README gap review | [paper](https://arxiv.org/abs/2102.09548), [repository](https://github.com/mims-harvard/TDC), and [project](https://tdcommons.ai/) |

## Considered, not recommended this run

| Work | Decision | Sources |
|---|---|---|
| DrugTargetWorld | Held; a large gated MRI component adds access and setup friction, so more directly accessible benchmarks were prioritized | [paper](https://arxiv.org/abs/2610.09558v1), [repository](https://github.com/sammargolis/DrugTargetWorld), and [Hugging Face assets](https://huggingface.co/datasets/sammargolis/drugtargetworld-assets) |
| OmicsBench | Held; the paper describes 97 tasks, while the public dataset record lists three public tasks and disables its viewer, so full benchmark availability was not verified | [paper](https://arxiv.org/abs/2610.21074v1) and [dataset record](https://huggingface.co/datasets/gideonshaked/OmicsBench) |
| AutoSciBench | Not selected; posted 2026-10-04, outside the 14-day window, and not biology-specific | [paper](https://arxiv.org/abs/2610.05140v1) |
| Eco-RNA | Not selected; preprint only, with no linked public code, data, or project artifact found | [paper](https://arxiv.org/abs/2610.13106v1) |
| Bolero | Not selected under the 10-item cap; credible alternative with an Arc announcement and preprint, but no official GitHub code repository was found and the public dataset viewer does not load | [Arc announcement](https://arcinstitute.org/news/bolero), [bioRxiv preprint](https://www.biorxiv.org/content/10.64898/2026.10.19.760026v1), and [model page](https://huggingface.co/arcinstitute/bolero-models) |
| TMB_pipeline | Not selected; repository-only lead with no separate paper or first-party launch found in this pass | [repository](https://github.com/RosettaCommons/TMB_pipeline) |
| AtomWorks Studio | Not selected; repository-only lead with no separate paper or first-party launch found in this pass | [repository](https://github.com/RosettaCommons/atomworks-studio) |

## Source coverage and cutoff

First-party pages checked included the [NVIDIA Atom feed](https://developer.nvidia.com/blog/feed/), [Arc newsroom](https://arcinstitute.org/news), [Chai news](https://www.chaidiscovery.com/news), [Google DeepMind blog index](https://deepmind.google/discover/blog/), [Meta AI blog](https://ai.meta.com/blog/), [EvolutionaryScale blog](https://www.evolutionaryscale.ai/blog) (404), and [OpenFold site](https://openfold.io/). GitHub organization inventories, repository searches, and releases were checked for relevant orgs; Hugging Face checks were targeted to candidate models/data rather than a broad date-range search. Paper checks used arXiv metadata, selected OpenAlex/Crossref lookups, and the NeurIPS 2026 program pages. No Google Scholar, broad PubMed/Semantic Scholar/Europe PMC date search, or exhaustive conference-program survey was done; some dynamic indexes and feeds were unavailable or incomplete.

The NVIDIA Atom feed's [RFD4-Proteina article](https://developer.nvidia.com/blog/design-proteins-with-rfd4-proteina-using-reward-guided-inference-time-search/) was published at 2026-10-21 12:30 UTC, after the supplied run cutoff of 12:00:25 UTC. RFD4-Proteina was included based on the Hugging Face model page updated at 09:00 UTC and the linked project/repository, not on that later article.

## Deduplication

The README, the empty local `recent-papers.md`, and open PRs [#3](https://github.com/rajeshgangireddy/awesome-digital-biology/pull/3), [#23](https://github.com/rajeshgangireddy/awesome-digital-biology/pull/23), [#28](https://github.com/rajeshgangireddy/awesome-digital-biology/pull/28), [#29](https://github.com/rajeshgangireddy/awesome-digital-biology/pull/29), [#30](https://github.com/rajeshgangireddy/awesome-digital-biology/pull/30), [#31](https://github.com/rajeshgangireddy/awesome-digital-biology/pull/31), and [#32](https://github.com/rajeshgangireddy/awesome-digital-biology/pull/32) were checked before selection. Those open PRs contained 50 candidate rows across README additions and scanner staging; none of the ten recommended candidates duplicated them.
