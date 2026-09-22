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
- [Skills and Agents](#skills-and-agents)
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
| **OpenFold-3** — Open-source AlphaFold3-style biomolecular structure prediction model | [project](https://github.com/aqlaboratory/openfold-3) ![Stars](https://img.shields.io/github/stars/aqlaboratory/openfold-3?style=social) · [release](https://github.com/OpenBind-Consortium/OpenBind-0-model-release-info) · [benchmark](https://github.com/OpenBind-Consortium/EV-A71_2A_benchmark) · [data](https://zenodo.org/records/22037460) | 2026 | AlQuraishi Lab · OpenFold Consortium | Open AlphaFold3-style model with open training code; OpenBind-0 is the default model (as of September 2026); [announcement](https://openbind.uk/news/blog-openbind-0-advancing-open-molecular-structure-prediction/); Apache 2.0; 717 discovery-relevant ligand-bound structures |
| **AtlasFold** — Protein folding with metagenomic-scale language models | [paper](https://www.biorxiv.org/content/10.64898/2026.09.04.749352v2) · [code](https://github.com/SeonghwanSeo/atlasfold) ![Stars](https://img.shields.io/github/stars/SeonghwanSeo/atlasfold?style=social) | 2026 | Seo et al. · KAIST / K-Fold initiative | MIT-licensed, trainable protein-language-model family for MSA-free monomer folding and protein-complex prediction, with released checkpoints, data, and benchmark artifacts |
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
| **BindCraft2 (BC2)** — Multi-modal protein binder design suite | [code](https://github.com/PacesaLab/BindCraft2) ![Stars](https://img.shields.io/github/stars/PacesaLab/BindCraft2?style=social) · [release](https://github.com/PacesaLab/BindCraft2/releases/tag/v1.0.1) | 2026 | PacesaLab | Software release; AlphaFold2/ProteinMPNN optimization and structural filtering for de novo, scaffolded, cyclic-peptide, and multistate binder design |
| **MULTI-evolve** — Model-guided engineering of multi-mutant proteins | [paper](https://doi.org/10.1126/science.aea1820) · [code](https://github.com/ArcInstitute/MULTI-evolve) ![Stars](https://img.shields.io/github/stars/ArcInstitute/MULTI-evolve?style=social) | 2026 | Tran et al. · Arc Institute & Patrick Hsu Lab | End-to-end workflow using protein language models, epistatic modeling, and MULTI-assembly for targeted multi-mutant design; Science |
| **Proteina-Complexa** — Atomistic protein binder design with generative pretraining and test-time search | [paper](https://openreview.net/forum?id=qmCpJtFZra) · [code](https://github.com/NVIDIA-BioNeMo/Proteina-Complexa) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/Proteina-Complexa?style=social) · [project](https://research.nvidia.com/labs/genair/proteina-complexa/) | 2026 | Didi et al. · NVIDIA BioNeMo & collaborators | Flow-based generation jointly models binder backbones, side chains, and sequences, with search-based optimization and experimental validation; ICLR 2026 oral paper |
| **DISCO** — Diffusion for sequence-structure co-design | [paper](https://arxiv.org/abs/2604.05181) · [code](https://github.com/DISCO-design/DISCO) ![Stars](https://img.shields.io/github/stars/DISCO-design/DISCO?style=social) · [model](https://huggingface.co/DISCO-Design/DISCO) | 2026 | Rector-Brooks et al. · DISCO Design collaborators | Multimodal generation jointly co-designs protein sequence and structure around ligands, DNA, or RNA; arXiv preprint |
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
| **PackFlow** — Generative molecular crystal structure prediction | [paper](https://arxiv.org/abs/2602.20140) · [code](https://github.com/learningmatter-mit/packflow) ![Stars](https://img.shields.io/github/stars/learningmatter-mit/packflow?style=social) | 2026 | Subramanian et al. · MIT & affiliated collaborators | arXiv; flow matching with reinforcement-learning alignment for crystal packing |
| **Contrastive KERMT** — Molecular graph foundation model for ADMET prediction | [paper](https://arxiv.org/abs/2606.11508) · [code](https://github.com/NVIDIA-BioNeMo/KERMT) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/KERMT?style=social) · [model](https://huggingface.co/nvidia/NV-KERMT-70M-v2) | 2026 | Xue et al. · NVIDIA BioNeMo | Contrastive graph-transformer pretraining for downstream multi-task ADMET property prediction; model v2 release |
| **GenMol** — Drug-discovery generalist with discrete diffusion | [paper](https://arxiv.org/abs/2501.06158) · [code](https://github.com/NVIDIA-BioNeMo/genmol) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/genmol?style=social) · [model](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara/resources/genmol_v2) | 2025 | Lee et al. · NVIDIA | Masked discrete diffusion over SAFE molecular sequences with fragment remasking and molecular-context guidance; ICML |
| **Molecule generation with structural motifs** — Molecule Generation For Target Protein Binding with Structural Motifs | [paper](https://openreview.net/forum?id=Rq13idF0F73) | 2023 | Zhang et al. · Shanghai Jiao Tong University | ICLR; structure-based drug design, fragment generation |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **EDM** — Equivariant diffusion for molecule generation in 3D | [paper](https://arxiv.org/abs/2203.17003) · [code](https://github.com/ehoogeboom/e3_diffusion_for_molecules) ![Stars](https://img.shields.io/github/stars/ehoogeboom/e3_diffusion_for_molecules?style=social) | 2022 | Hoogeboom et al. · University of Amsterdam | ICML; 3D diffusion, equivariance |
| **Antimicrobial peptide generation** — Accelerated antimicrobial discovery via deep generative models and molecular dynamics simulations | [paper](https://www.nature.com/articles/s41551-021-00689-x) | 2021 | Das et al. · IBM Research | Nature Biomedical Engineering; generative autoencoder, antimicrobial peptides |

</details>

## Genomics / DNA & RNA Foundation Models

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **RNAPro** — RNA 3D structure prediction with templates and RNA foundation-model features | [paper](https://www.biorxiv.org/content/10.64898/2025.12.30.696949v1) · [code](https://github.com/NVIDIA-BioNeMo/RNAPro) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/RNAPro?style=social) · [model](https://huggingface.co/nvidia/RNAPro-Public-Best-500M) | 2026 | Lee et al. · NVIDIA BioNeMo & collaborators | RNA structure prediction combining templates, MSAs, RibonanzaNet2, and Protenix; bioRxiv preprint and released checkpoints |
| **JEPA-DNA** — Joint-embedding predictive genomic foundation model | [paper](https://arxiv.org/abs/2602.17162) · [code](https://github.com/NVIDIA-BioNeMo/JEPA-DNA) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/JEPA-DNA?style=social) · [model](https://huggingface.co/collections/nvidia/jepa-dna) | 2026 | Larey et al. · NVIDIA & collaborators | Combines generative pretraining with a joint-embedding predictive objective for DNA representation learning; arXiv preprint |
| **RIBOSPAN** — Long-context RNA foundation model | [paper](https://arxiv.org/abs/2608.22849) · [code](https://github.com/GAIR-NLP/RIBOSPAN-FM) ![Stars](https://img.shields.io/github/stars/GAIR-NLP/RIBOSPAN-FM?style=social) | 2026 | Wang et al. · GAIR-NLP | 1.61B-parameter bidirectional RNA model with single-nucleotide tokenization and native 10,240-nt context; arXiv preprint |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **Evo 2** — Genome foundation model at billion-to-trillion-base scale | [paper](https://doi.org/10.1038/s41586-026-10176-5) · [code](https://github.com/ArcInstitute/evo2) ![Stars](https://img.shields.io/github/stars/ArcInstitute/evo2?style=social) · [project](https://arcinstitute.org/tools/evo) | 2026 | Arc Institute | Approximately 9T DNA tokens; up to 1M-base context |
| **GENA-LM / modernGENA** — Long-context genomic language models | [code](https://github.com/AIRI-Institute/GENA_LM) ![Stars](https://img.shields.io/github/stars/AIRI-Institute/GENA_LM?style=social) · [models](https://huggingface.co/AIRI-Institute) | 2025 | AIRI Institute & collaborators | Long-context DNA language-model family for genomic representation learning and downstream regulatory-genomics tasks |
| **JanusDNA** — Bidirectional DNA foundation model | [code](https://github.com/Qihao-Duan/JanusDNA) ![Stars](https://img.shields.io/github/stars/Qihao-Duan/JanusDNA?style=social) | 2025 | Duan et al. | DNA foundation model with bidirectional sequence modeling for genomic representation and prediction |
| **CodonFM** — Foundation models for codon sequences | [paper](https://research.nvidia.com/labs/dbr/assets/data/manuscripts/nv-codonfm-preprint.pdf) · [code](https://github.com/NVIDIA-BioNeMo/CodonFM) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/CodonFM?style=social) · [model](https://huggingface.co/nvidia/NV-CodonFM-Encodon-1B-v1) | 2025 | Darabi et al. · NVIDIA & academic collaborators | Open codon-resolution language models, 80M–1B parameters; coding-sequence representation and downstream prediction |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **AlphaGenome** — Regulatory genomics model and ecosystem | <br>- API: [project](https://deepmind.google.com/science/alphagenome) · [client](https://github.com/google-deepmind/alphagenome) ![Stars](https://img.shields.io/github/stars/google-deepmind/alphagenome?style=social)<br>- Research: [code](https://github.com/google-deepmind/alphagenome_research) ![Stars](https://img.shields.io/github/stars/google-deepmind/alphagenome_research?style=social)<br>- PyTorch port: [code](https://github.com/genomicsxai/alphagenome-pytorch) ![Stars](https://img.shields.io/github/stars/genomicsxai/alphagenome-pytorch?style=social) | 2025 | Google DeepMind; community port by GenomicsXAI | Expression, splicing, chromatin, TF binding, variant effects; the PyTorch port is unofficial |
| **RiNALMo** — RNA language model for sequence and structure-aware prediction | [code](https://github.com/lbcb-sci/RiNALMo) ![Stars](https://img.shields.io/github/stars/lbcb-sci/RiNALMo?style=social) · [model](https://huggingface.co/lbcb/RiNALMo) | 2024 | Lbcb-SCI & collaborators | RNA foundation model trained on diverse transcript sequences for structure, function, and downstream RNA prediction tasks |
| **Caduceus** — Bi-directional equivariant long-range DNA modeling | [paper](https://arxiv.org/abs/2403.03234) · [code](https://github.com/kuleshov-group/caduceus) ![Stars](https://img.shields.io/github/stars/kuleshov-group/caduceus?style=social) | 2024 | Schiff et al. · Kuleshov Group | Reverse-complement-equivariant Mamba model for long-context DNA representation learning |
| **Nucleotide Transformer** — Building and evaluating robust genomic foundation models | [paper](https://www.nature.com/articles/s41592-024-02523-z) · [code](https://github.com/instadeepai/nucleotide-transformer) ![Stars](https://img.shields.io/github/stars/instadeepai/nucleotide-transformer?style=social) | 2024 | Dalla-Torre et al. · InstaDeep, NVIDIA & TU Munich | Genomic foundation model |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **Evo** — DNA foundation modeling from molecular to genome scale | [paper](https://www.science.org/doi/10.1126/science.ado9336) · [code](https://github.com/evo-design/evo) ![Stars](https://img.shields.io/github/stars/evo-design/evo?style=social) | 2024 | Nguyen et al. · Arc Institute & Stanford University | Long-context genomic model, generative DNA design |
| **HyenaDNA** — Long-range genomic language model at single-nucleotide resolution | [paper](https://arxiv.org/abs/2306.15794) · [code](https://github.com/HazyResearch/hyena-dna) ![Stars](https://img.shields.io/github/stars/HazyResearch/hyena-dna?style=social) | 2023 | Nguyen et al. · Stanford University & collaborators | Subquadratic long-context DNA modeling with single-nucleotide tokenization |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **DNABERT** — Pre-trained bidirectional representations for DNA language | [paper](https://academic.oup.com/bioinformatics/article/37/15/2112/6128680) · [code](https://github.com/jerryji1993/DNABERT) ![Stars](https://img.shields.io/github/stars/jerryji1993/DNABERT?style=social) | 2021 | Ji et al. · Northwestern University & Stony Brook University | DNA language model, genome representation |

</details>

## Single-Cell & Omics Foundation Models

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **SCENE** — Interpretable cell-gene embeddings for single-cell RNA-seq | [paper](https://doi.org/10.64898/2026.09.12.750699) · [code](https://github.com/oscarmoeberg/SCENE) ![Stars](https://img.shields.io/github/stars/oscarmoeberg/SCENE?style=social) · [reproducibility](https://github.com/oscarmoeberg/SCENE-reproducibility) | 2026 | Moberg et al. · Technical University of Denmark | bioRxiv; graph representation learning with joint cell and gene embeddings from UMI counts |
| **scVision** — Vision foundation model for single-cell biology | [paper](https://arxiv.org/abs/2607.14163) · [project](https://islamlab.org/scvision/) | 2026 | Yesiloglu et al. · Islam Lab, Stanford Medicine | Interesting concept; Represent entire cell as an image and do processing on/with that image; pretrained on 72 million human cells; no public code repository located |
| **Stack** — In-context learning for single-cell perturbation prediction | [code](https://github.com/ArcInstitute/stack) ![Stars](https://img.shields.io/github/stars/ArcInstitute/stack?style=social) · [preprint](https://www.biorxiv.org/content/10.64898/2026.01.09.698608v1) | 2026 | Arc Institute | Single-cell foundation model; peer review pending |
| **STATE** — Predicting cellular responses to perturbations | [code](https://github.com/ArcInstitute/state) ![Stars](https://img.shields.io/github/stars/ArcInstitute/state?style=social) · [project](https://arcinstitute.org/tools/state) | 2025 | Arc Institute | Virtual-cell model for genetic, drug, and cytokine perturbations |
| **cell-eval** — Evaluation suite for perturbation models | [code](https://github.com/ArcInstitute/cell-eval) ![Stars](https://img.shields.io/github/stars/ArcInstitute/cell-eval?style=social) | — | Arc Institute | Metrics, baselines, data-ceiling estimation, and challenge-compatible evaluation |
| **scGPT** — Toward building a foundation model for single-cell multi-omics using generative AI | [paper](https://www.nature.com/articles/s41592-024-02201-0) · [code](https://github.com/bowang-lab/scGPT) ![Stars](https://img.shields.io/github/stars/bowang-lab/scGPT?style=social) | 2024 | Cui et al. · University of Toronto | Single-cell, generative pretraining, multi-omics |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **Geneformer** — Transfer learning enables predictions in network biology | [paper](https://www.nature.com/articles/s41586-023-06139-9) · [code](https://huggingface.co/ctheodoris/Geneformer) | 2023 | Theodoris et al. · Harvard Medical School & Boston Children's Hospital | Gene network, transfer learning, single-cell |

</details>

## Multi-modal / Foundation Models for Biology

<details open>
<summary>Projects and papers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **BioReason** — Multimodal protein-function reasoning with GO-GPT | [paper](https://bioreason.net/paper) · [app](https://app.bioreason.net/auth?callbackUrl=https%3A%2F%2Fapp.bioreason.net%2F) | 2026 | BioReason team | Protein-function prediction, structured reasoning, functional summaries |
| ![Highlight](https://img.shields.io/badge/-Highlight-orange) **ESM3** — Simulating 500 million years of evolution with a language model | [paper](https://www.science.org/doi/10.1126/science.ado9336) · [code](https://github.com/evolutionaryscale/esm) ![Stars](https://img.shields.io/github/stars/evolutionaryscale/esm?style=social) | 2025 | Hayes et al. · EvolutionaryScale | Multimodal, sequence-structure-function, generative |
| **MAMMAL** — Multi-modal biomedical foundation model | [paper](https://arxiv.org/abs/2410.22367) · [code](https://github.com/BiomedSciAI/biomed-multi-alignment) ![Stars](https://img.shields.io/github/stars/BiomedSciAI/biomed-multi-alignment?style=social) · [model](https://huggingface.co/ibm/biomed.omics.bl.sm.ma-ted-458m) | 2024 | Shoshan et al. · IBM Research | Unified promptable pretraining across proteins, small molecules, and single-cell gene expression |

</details>

## Skills and Agents

<details open>
<summary>Scientific skills and agents</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Drug Discovery Agent Skills** — Agent skills for computational drug discovery | [code](https://github.com/K-Dense-AI/drug-discovery-agent-skills) ![Stars](https://img.shields.io/github/stars/K-Dense-AI/drug-discovery-agent-skills?style=social) · [release](https://github.com/K-Dense-AI/drug-discovery-agent-skills/releases/tag/v1.3.0) | 2026 | K-Dense AI | 37 interoperable skills spanning target discovery, chemistry, docking, simulation, ADMET, and therapeutic design |
| **NVIDIA BioNeMo Agent Toolkit** — Agent-callable skills for computational biology and drug discovery | [code](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/bionemo-agent-toolkit?style=social) · [announcement](https://developer.nvidia.com/blog/run-nvidia-bionemo-nim-microservices-for-protein-structure-prediction-in-claude-science/) | 2026 | NVIDIA BioNeMo | Reusable skills and workflows for protein folding, docking, generative chemistry, genomics, protein design, and biomarker discovery |
| **PDBe MCP Servers** — Structural-biology data servers for model-context-protocol agents | [code](https://github.com/PDBeurope/PDBe-MCP-Servers) ![Stars](https://img.shields.io/github/stars/PDBeurope/PDBe-MCP-Servers?style=social) · [announcement](https://www.ebi.ac.uk/training/events/bringing-structural-biology-ai-exploring-pdbe-mcp-servers/) | 2026 | PDBe · EMBL-EBI | API, search, and graph MCP servers that expose PDBe structural-biology resources to scientific agents |
| **Google DeepMind Science Skills** — Scientific agent skills and tool integrations | [code](https://github.com/google-deepmind/science-skills) ![Stars](https://img.shields.io/github/stars/google-deepmind/science-skills?style=social) | — | Google DeepMind | Skills for AlphaGenome, AlphaFold DB, UniProt, genomics, chemistry, and scientific search |
| **SRAgent** — LLM-assisted SRA curation | [code](https://github.com/ArcInstitute/SRAgent) ![Stars](https://img.shields.io/github/stars/ArcInstitute/SRAgent?style=social) · [paper](https://www.biorxiv.org/content/10.1101/2025.02.27.640494v1) | 2025 | Arc Institute | Extracts metadata and discovers linked studies for atlas-scale biology |

</details>

## Datasets & Benchmarks

<details open>
<summary>Datasets and evaluation resources</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Virtual Cell Challenge 2026** — Benchmarking zero-shot generalization across cellular contexts | [paper](https://doi.org/10.1016/j.cell.2026.08.004) · [benchmark](https://virtualcellchallenge.org/) | 2026 | Arc Institute & collaborators | Cell; open benchmark for AI models predicting perturbation responses across cell contexts |
| **Terminal-Bench-Science** — Benchmark for AI agents on scientific workflows | [benchmark](https://www.terminal-bench-science.ai/) · [code](https://github.com/harbor-framework/terminal-bench-science) ![Stars](https://img.shields.io/github/stars/harbor-framework/terminal-bench-science?style=social) · [dataset](https://doi.org/10.5281/zenodo.22110253) | 2026 | Terminal-Bench-Science team · Stanford, Harbor & Laude Institute | Expert-curated agent tasks across scientific domains, including life-science workflows |
| **BixBench** — Benchmark for LLM-based agents in computational biology | [paper](https://arxiv.org/abs/2503.00096) · [code](https://github.com/Future-House/BixBench) ![Stars](https://img.shields.io/github/stars/Future-House/BixBench?style=social) · [dataset](https://huggingface.co/datasets/futurehouse/BixBench) | 2025 | FutureHouse & ScienceMachine | Open-ended bioinformatics tasks built from real-world analysis notebooks, with a public dataset and reproducible agent-evaluation harness |
| **OpenGenome2** — Genomic pretraining dataset | [dataset](https://huggingface.co/datasets/arcinstitute/opengenome2) | — | Arc Institute | Large all-domain-of-life genomic corpus used for Evo 2 |
| **Arc Virtual Cell Atlas** — Atlas-scale single-cell data platform | [code](https://github.com/ArcInstitute/arc-virtual-cell-atlas) ![Stars](https://img.shields.io/github/stars/ArcInstitute/arc-virtual-cell-atlas?style=social) · [project](https://arcinstitute.org/tools/virtualcellatlas) · [dataset](https://lamin.ai/laminlabs/arc-virtual-cell-atlas) | — | Arc Institute | Public data, Tahoe perturbation data, and challenge datasets |
| **SynGenome** — Synthetic-DNA dataset | [project](https://evodesign.org/syngenome/) | — | EvolutionaryScale | Large synthetic DNA resource generated with Evo |
| **Protein Data Bank (PDB)** | [dataset](https://www.rcsb.org/) | — | RCSB PDB | Experimental structures, gold-standard benchmark |
| **AlphaFold Protein Structure Database** | [dataset](https://alphafold.ebi.ac.uk/) | — | EMBL-EBI & Google DeepMind | Predicted structures, whole-proteome coverage |
| **CASP** — Critical Assessment of Structure Prediction | [benchmark](https://predictioncenter.org/) | — | CASP community | Community benchmark, blind prediction |

</details>

## Tools, Libraries & Servers

<details open>
<summary>Tools, libraries, and servers</summary>

| Project / work | Links | Year | Authors / organization | Notes |
|---|---|---:|---|---|
| **Fold-CP** — Context parallelism for biomolecular modeling | [paper](https://research.nvidia.com/labs/dbr/assets/data/manuscripts/fold_cp.pdf) · [code](https://github.com/NVIDIA-BioNeMo/boltz-cp) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/boltz-cp?style=social) | 2026 | NVIDIA BioNeMo | MIT-licensed, CUDA-focused distributed inference and training framework for Boltz-2 using data and context parallelism; proof-of-concept for multi-GPU large-complex modeling |
| **Rosetta Foundry** — Infrastructure for protein design models | [project](https://rosettacommons.github.io/foundry/) · [code](https://github.com/RosettaCommons/foundry) ![Stars](https://img.shields.io/github/stars/RosettaCommons/foundry?style=social) | 2025 | Rosetta Commons · Institute for Protein Design | BSD-3-Clause framework providing shared training and inference tooling for RFD3, RF3, ProteinMPNN, and LigandMPNN |
| **BioNeMo Inference Runtime** — GPU-accelerated structure-prediction inference | [code](https://github.com/NVIDIA-BioNeMo/BioNeMo-Inference-Runtime) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/BioNeMo-Inference-Runtime?style=social) · [project](https://docs.nvidia.com/bionemo/inference-runtime/overview/) | 2026 | NVIDIA BioNeMo | NVIDIA GPU-specific inference infrastructure for protein, nucleic-acid, and ligand structure-prediction models, with published speed and memory benchmarks |
| **nvMolKit** — GPU-accelerated molecular-computation library | [code](https://github.com/NVIDIA-BioNeMo/nvMolKit) ![Stars](https://img.shields.io/github/stars/NVIDIA-BioNeMo/nvMolKit?style=social) · [project](https://nvidia-bionemo.github.io/nvMolKit/) | 2026 | NVIDIA BioNeMo | NVIDIA CUDA-specific, RDKit-compatible infrastructure for molecular fingerprints, similarity, conformer generation, geometry relaxation, clustering, and substructure search |
| **Helical** — Framework for pretrained bio foundation models | [code](https://github.com/helicalAI/helical) ![Stars](https://img.shields.io/github/stars/helicalAI/helical?style=social) · [project](https://helical.readthedocs.io/) | 2026 | Helical team | Python framework for genomics, transcriptomics, and single-cell foundation models, with model cards, tutorials, and Helix-mRNA-v0 integration |
| **AlphaFast** — High-throughput AlphaFold 3 inference with GPU-accelerated MSA search | [paper](https://www.biorxiv.org/content/10.64898/2026.02.17.706409v1) · [code](https://github.com/RomeroLab/alphafast) ![Stars](https://img.shields.io/github/stars/RomeroLab/alphafast?style=social) | 2026 | Perry et al. · Romero Lab, Duke University | Drop-in AF3 framework replacing CPU-bound JackHMMER with GPU-accelerated MMseqs2 for high-throughput inference; bioRxiv preprint |
| **Proto** — Generative biology programming language | [paper](https://www.biorxiv.org/content/10.64898/2026.06.22.733870v1) · [project](https://proto.evodesign.org/landing) | 2026 | EvolutionaryScale / Arc Institute | Composes design primitives across DNA, RNA, proteins, ligands, and interactions |
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
