# Awesome Digital Biology [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg) ![Stars](https://img.shields.io/github/stars/rajeshgangireddy/awesome-digital-biology?style=social) ![Last Commit](https://img.shields.io/github/last-commit/rajeshgangireddy/awesome-digital-biology)

> A curated, **actively-maintained** list of deep learning research, models,
> tools, and datasets for **digital biology** — protein structure prediction,
> protein/binder/antibody design, molecular generation, genomics & single-cell
> foundation models, and the software that powers them.

Why this list exists: the AI-for-biology space is exploding, but resources are
scattered across dozens of narrow, often-stale lists. This repo aims to be the
**single go-to hub** — broad in scope, strict in curation, and kept fresh via
an automated scanning bot that creates a PR for new papers every 2 days (see
[Recent Papers](docs/staging/recent-papers.md), triaged into the sections
below by maintainers/contributors).

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Table of Contents

- [Protein Structure Prediction](#protein-structure-prediction)
- [Protein & Binder/Antibody Design](#protein--binderantibody-design)
- [Molecular Generation & Drug Discovery](#molecular-generation--drug-discovery)
- [Genomics / DNA & RNA Foundation Models](#genomics--dna--rna-foundation-models)
- [Single-Cell & Omics Foundation Models](#single-cell--omics-foundation-models)
- [Multi-modal / Foundation Models for Biology](#multi-modal--foundation-models-for-biology)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Tools, Libraries & Servers](#tools-libraries--servers)
- [Labs, Companies & Communities](#labs-companies--communities)
- [Recent Papers (unreviewed, bot-updated)](docs/staging/recent-papers.md)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)

## Entry format

Each entry uses the canonical project or work name first, followed by a short
descriptor when it adds context. Links are project-specific: include the
primary link and only useful complementary links such as a paper, code,
dataset, project page, demo, or benchmark.

```markdown
| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Project name** — Short descriptor | [paper](...) · [code](...) ![Stars](...) | 2025 | Authors · Organization | Keywords or summary |
```

Papers and releases are listed **newest first** within each section. A
![Highlight](https://img.shields.io/badge/-Highlight-orange) badge at the
beginning of the Project / work cell marks an especially significant
landmark, field-defining work, or must-read resource. A dynamic
![Stars](https://img.shields.io/github/stars/owner/repo?style=social) badge
belongs next to the relevant primary GitHub link and is included only when a
public repository exists. Badges are editorial and popularity signals, not
quality guarantees.

## Protein Structure Prediction

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **SimpleFold** — Folding Proteins is Simpler than You Think | [paper](https://arxiv.org/abs/2509.18480) · [code](https://github.com/apple/ml-simplefold) ![Stars](https://img.shields.io/github/stars/apple/ml-simplefold?style=social) | 2025 | Wang et al. · Apple | Flow matching, transformer-only, no triangle attention |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **AlphaFold 3** — Accurate structure prediction of biomolecular interactions | [paper](https://www.nature.com/articles/s41586-024-07487-w) · [code](https://github.com/google-deepmind/alphafold3) ![Stars](https://img.shields.io/github/stars/google-deepmind/alphafold3?style=social) | 2024 | Abramson et al. · Google DeepMind & Isomorphic Labs | Nature; diffusion, biomolecular complexes |
| **OpenFold** — Retraining AlphaFold2 yields new insights into its learning mechanisms | [paper](https://www.nature.com/articles/s41592-024-02272-z) · [code](https://github.com/aqlaboratory/openfold) ![Stars](https://img.shields.io/github/stars/aqlaboratory/openfold?style=social) | 2024 | Ahdritz et al. · Columbia University | Nature Methods; open reimplementation, trainable |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **ColabFold** — Making protein folding accessible to all | [paper](https://www.nature.com/articles/s41592-022-01488-1) · [code](https://github.com/sokrypton/ColabFold) ![Stars](https://img.shields.io/github/stars/sokrypton/ColabFold?style=social) | 2022 | Mirdita et al. · Seoul National University & Harvard Medical School | Nature Methods; accessible inference, MSA search, notebooks |
| **ESMFold** — Language models of protein sequences at the scale of evolution enable accurate structure prediction | [paper](https://www.biorxiv.org/content/10.1101/2022.07.20.500902) · [code](https://github.com/facebookresearch/esm) ![Stars](https://img.shields.io/github/stars/facebookresearch/esm?style=social) | 2022 | Lin et al. · Meta AI (FAIR) | Protein language model, single-sequence folding |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **AlphaFold** — Highly accurate protein structure prediction | [paper](https://www.nature.com/articles/s41586-021-03819-2) · [code](https://github.com/google-deepmind/alphafold) ![Stars](https://img.shields.io/github/stars/google-deepmind/alphafold?style=social) | 2021 | Jumper et al. · Google DeepMind | Nature; structure prediction, Evoformer, MSA |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **RoseTTAFold** — Accurate prediction of protein structures and interactions using a three-track network | [paper](https://www.science.org/doi/10.1126/science.abj8754) · [code](https://github.com/RosettaCommons/RoseTTAFold) ![Stars](https://img.shields.io/github/stars/RosettaCommons/RoseTTAFold?style=social) | 2021 | Baek et al. · University of Washington (Baker Lab) | Science; three-track network, structure prediction |

</details>

## Protein & Binder/Antibody Design

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **BoltzGen** — Generative modeling for biomolecular design | [project](https://github.com/HannesStark/boltzgen) ![Stars](https://img.shields.io/github/stars/HannesStark/boltzgen?style=social) | 2025 | Stärk et al. · MIT | Generative model, binder/complex design |
| **Boltz-1** — Democratizing biomolecular interaction modeling | [project](https://github.com/jwohlwend/boltz) ![Stars](https://img.shields.io/github/stars/jwohlwend/boltz?style=social) | 2024 | Wohlwend et al. · MIT (Jameel Clinic) | Open-source AlphaFold3-class model |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **RFdiffusion** — De novo design of protein structure and function | [paper](https://www.nature.com/articles/s41586-023-06415-8) · [code](https://github.com/RosettaCommons/RFdiffusion) ![Stars](https://img.shields.io/github/stars/RosettaCommons/RFdiffusion?style=social) | 2023 | Watson et al. · University of Washington (Baker Lab) | Nature; diffusion, binders, scaffolding; [preprint](https://www.biorxiv.org/content/10.1101/2022.12.09.519842) |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **ProteinMPNN** — Robust deep learning-based protein sequence design | [paper](https://www.science.org/doi/10.1126/science.add2187) · [code](https://github.com/dauparas/ProteinMPNN) ![Stars](https://img.shields.io/github/stars/dauparas/ProteinMPNN?style=social) | 2022 | Dauparas et al. · University of Washington (Baker Lab) | Science; fixed-backbone sequence design |
| **De novo binders** — Design of protein-binding proteins from the target structure alone | [paper](https://www.nature.com/articles/s41586-022-04654-9) | 2022 | Cao et al. · University of Washington (Baker Lab) | Nature; target-only binder design |
| **Conditional Antibody Design** — 3D equivariant graph translation | [paper](https://arxiv.org/abs/2208.06073) | 2022 | Kong et al. · Tsinghua University | NeurIPS; antibody design, CDR generation |
| **Protein language model hallucination** — Language models generalize beyond natural proteins | [paper](https://www.biorxiv.org/content/10.1101/2022.12.21.521521) | 2022 | Verkuil et al. · Meta AI (FAIR) | bioRxiv; ESMFold, hallucination, fixed-backbone design |

</details>

## Molecular Generation & Drug Discovery

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Molecule generation with structural motifs** — Molecule Generation For Target Protein Binding with Structural Motifs | [paper](https://openreview.net/forum?id=Rq13idF0F73) | 2023 | Zhang et al. · Shanghai Jiao Tong University | ICLR; structure-based drug design, fragment generation |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **EDM** — Equivariant diffusion for molecule generation in 3D | [paper](https://arxiv.org/abs/2203.17003) · [code](https://github.com/ehoogeboom/e3_diffusion_for_molecules) ![Stars](https://img.shields.io/github/stars/ehoogeboom/e3_diffusion_for_molecules?style=social) | 2022 | Hoogeboom et al. · University of Amsterdam | ICML; 3D diffusion, equivariance |
| **Antimicrobial peptide generation** — Accelerated antimicrobial discovery via deep generative models and molecular dynamics simulations | [paper](https://www.nature.com/articles/s41551-021-00689-x) | 2021 | Das et al. · IBM Research | Nature Biomedical Engineering; generative autoencoder, antimicrobial peptides |

</details>

## Genomics / DNA & RNA Foundation Models

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **Evo** — DNA foundation modeling from molecular to genome scale | [paper](https://www.science.org/doi/10.1126/science.ado9336) · [code](https://github.com/evo-design/evo) ![Stars](https://img.shields.io/github/stars/evo-design/evo?style=social) | 2024 | Nguyen et al. · Arc Institute & Stanford University | Long-context genomic model, generative DNA design |
| **Nucleotide Transformer** — Building and evaluating robust genomic foundation models | [paper](https://www.nature.com/articles/s41592-024-02523-z) · [code](https://github.com/instadeepai/nucleotide-transformer) ![Stars](https://img.shields.io/github/stars/instadeepai/nucleotide-transformer?style=social) | 2024 | Dalla-Torre et al. · InstaDeep, NVIDIA & TU Munich | Genomic foundation model |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **DNABERT** — Pre-trained bidirectional representations for DNA language | [paper](https://academic.oup.com/bioinformatics/article/37/15/2112/6128680) · [code](https://github.com/jerryji1993/DNABERT) ![Stars](https://img.shields.io/github/stars/jerryji1993/DNABERT?style=social) | 2021 | Ji et al. · Northwestern University & Stony Brook University | DNA language model, genome representation |

</details>

## Single-Cell & Omics Foundation Models

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **scGPT** — Toward building a foundation model for single-cell multi-omics using generative AI | [paper](https://www.nature.com/articles/s41592-024-02201-0) · [code](https://github.com/bowang-lab/scGPT) ![Stars](https://img.shields.io/github/stars/bowang-lab/scGPT?style=social) | 2024 | Cui et al. · University of Toronto | Single-cell, generative pretraining, multi-omics |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **Geneformer** — Transfer learning enables predictions in network biology | [paper](https://www.nature.com/articles/s41586-023-06139-9) · [code](https://huggingface.co/ctheodoris/Geneformer) | 2023 | Theodoris et al. · Harvard Medical School & Boston Children's Hospital | Gene network, transfer learning, single-cell |

</details>

## Multi-modal / Foundation Models for Biology

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **ESM3** — Simulating 500 million years of evolution with a language model | [paper](https://www.science.org/doi/10.1126/science.ado9336) · [code](https://github.com/evolutionaryscale/esm) ![Stars](https://img.shields.io/github/stars/evolutionaryscale/esm?style=social) | 2025 | Hayes et al. · EvolutionaryScale | Multimodal, sequence-structure-function, generative |

</details>

## Datasets & Benchmarks

<details open>
<summary>Datasets and evaluation resources</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Protein Data Bank (PDB)** | [dataset](https://www.rcsb.org/) | — | RCSB PDB | Experimental structures, gold-standard benchmark |
| **AlphaFold Protein Structure Database** | [dataset](https://alphafold.ebi.ac.uk/) | — | EMBL-EBI & Google DeepMind | Predicted structures, whole-proteome coverage |
| **CASP** — Critical Assessment of Structure Prediction | [benchmark](https://predictioncenter.org/) | — | CASP community | Community benchmark, blind prediction |

</details>

## Tools, Libraries & Servers

<details open>
<summary>Tools, libraries, and servers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **PyMOL** | [project](https://pymol.org/) · [code](https://github.com/schrodinger/pymol-open-source) ![Stars](https://img.shields.io/github/stars/schrodinger/pymol-open-source?style=social) | — | Schrödinger | Molecular visualization |
| **ChimeraX** | [project](https://www.cgl.ucsf.edu/chimerax/) · [code](https://github.com/RBVI/ChimeraX) ![Stars](https://img.shields.io/github/stars/RBVI/ChimeraX?style=social) | — | UCSF RBVI | Molecular visualization |
| **Biotite** | [project](https://github.com/biotite-dev/biotite) · [code](https://github.com/biotite-dev/biotite) ![Stars](https://img.shields.io/github/stars/biotite-dev/biotite?style=social) | — | Biotite contributors | Computational structural biology library |
| **BioPython** | [project](https://github.com/biopython/biopython) · [code](https://github.com/biopython/biopython) ![Stars](https://img.shields.io/github/stars/biopython/biopython?style=social) | — | Biopython contributors | General bioinformatics toolkit |

</details>

## Labs, Companies & Communities

<details open>
<summary>Organizations and communities</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Baker Lab** — University of Washington | [website](https://www.bakerlab.org/) | — | University of Washington | RFdiffusion, ProteinMPNN, RoseTTAFold |
| **EvolutionaryScale** | [website](https://www.evolutionaryscale.ai/) | — | EvolutionaryScale | ESM family |
| **Chai Discovery** | [website](https://www.chaidiscovery.com/) | — | Chai Discovery | Biomolecular structure and design |
| **Google DeepMind** | [website](https://deepmind.google/) | — | Google DeepMind | AlphaFold family |

</details>

## Recent Papers (unreviewed, bot-updated)

See [docs/staging/recent-papers.md](docs/staging/recent-papers.md). These
automatically discovered candidates are not part of the curated list until
reviewed by a maintainer or contributor.

## Related Awesome Lists

<details open>
<summary>Related lists</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Awesome-Bioinformatics** | [repository](https://github.com/danielecook/Awesome-Bioinformatics) | — | danielecook | General bioinformatics |
| **Awesome Protein Representation Learning** | [repository](https://github.com/LirongWu/awesome-protein-representation-learning) | — | LirongWu | Protein representation learning |
| **Awesome AI-based Protein Design** | [repository](https://github.com/opendilab/awesome-AI-based-protein-design) | — | OpenDILab | AI-based protein design |
| **Awesome Molecular Generation** | [repository](https://github.com/amorehead/awesome-molecular-generation) | — | amorehead | Molecular generation |

</details>

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md)
for the table entry format and guidelines before opening a PR.

This list is partly maintained by an automated scanner (every 2 days) that
proposes new papers via PR into [docs/staging/recent-papers.md](docs/staging/recent-papers.md).
See [scripts/README.md](scripts/README.md) for how it works.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, contributors have waived all copyright and
related rights to this work under [CC0](LICENSE).
