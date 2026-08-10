# Awesome Digital Biology [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg) ![Stars](https://img.shields.io/github/stars/rajeshgangireddy/awesome-digital-biology?style=social) ![Last Commit](https://img.shields.io/github/last-commit/rajeshgangireddy/awesome-digital-biology)

> A curated, **actively-maintained** list of deep learning research, models,
> tools, and datasets for **digital biology** — protein structure prediction,
> protein/binder/antibody design, molecular generation, genomics & single-cell
> foundation models, and the software that powers them.


Why this list exists: the AI-for-biology space is exploding, but resources are
scattered across dozens of narrow, often-stale lists. 
Most of the existing "awesome" repos for digital biology are not maintained. 


This repo aims to be the
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

Entry format:

```
- [Title](link) [code](code-link) ![Stars](https://img.shields.io/github/stars/owner/repo?style=flat&label=)
  - Authors · Institution/Company · Venue/Year
  - Keywords: ...
```

Papers are listed **newest first** within each section. A
![Highlight](https://img.shields.io/badge/-Highlight-blue) badge marks papers
the maintainers consider especially significant — landmark, field-defining,
or otherwise a must-read — without implying it is the *only* important paper
in the section. Badge placement is a human editorial call, not a benchmark
claim, and can be proposed/discussed via PR.

## Protein Structure Prediction

- [SimpleFold: Folding Proteins is Simpler than You Think](https://arxiv.org/abs/2509.18480) [code](https://github.com/apple/ml-simplefold) ![Stars](https://img.shields.io/github/stars/apple/ml-simplefold?style=flat&label=)
  - Wang et al. · Apple · arXiv 2025
  - Keywords: flow matching, transformer-only, no triangle attention
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [Accurate structure prediction of biomolecular interactions with AlphaFold3](https://www.nature.com/articles/s41586-024-07487-w) [code](https://github.com/google-deepmind/alphafold3) ![Stars](https://img.shields.io/github/stars/google-deepmind/alphafold3?style=flat&label=)
  - Abramson et al. · Google DeepMind & Isomorphic Labs · Nature 2024
  - Keywords: diffusion, biomolecular complexes
- [OpenFold: Retraining AlphaFold2 yields new insights into its learning mechanisms](https://www.nature.com/articles/s41592-024-02272-z) [code](https://github.com/aqlaboratory/openfold) ![Stars](https://img.shields.io/github/stars/aqlaboratory/openfold?style=flat&label=)
  - Ahdritz et al. · Columbia University · Nature Methods 2024
  - Keywords: open reimplementation, trainable
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [ColabFold: Making protein folding accessible to all](https://www.nature.com/articles/s41592-022-01488-1) [code](https://github.com/sokrypton/ColabFold) ![Stars](https://img.shields.io/github/stars/sokrypton/ColabFold?style=flat&label=)
  - Mirdita et al. · Seoul National University & Harvard Medical School · Nature Methods 2022
  - Keywords: accessible inference, MSA search, notebooks
- [Language models of protein sequences at the scale of evolution enable accurate structure prediction (ESMFold)](https://www.biorxiv.org/content/10.1101/2022.07.20.500902) [code](https://github.com/facebookresearch/esm) ![Stars](https://img.shields.io/github/stars/facebookresearch/esm?style=flat&label=)
  - Lin et al. · Meta AI (FAIR) · bioRxiv 2022
  - Keywords: protein language model, single-sequence folding
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [Highly accurate protein structure prediction with AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) [code](https://github.com/google-deepmind/alphafold) ![Stars](https://img.shields.io/github/stars/google-deepmind/alphafold?style=flat&label=)
  - Jumper et al. · Google DeepMind · Nature 2021
  - Keywords: structure prediction, Evoformer, MSA
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [RoseTTAFold: Accurate prediction of protein structures and interactions using a three-track network](https://www.science.org/doi/10.1126/science.abj8754) [code](https://github.com/RosettaCommons/RoseTTAFold) ![Stars](https://img.shields.io/github/stars/RosettaCommons/RoseTTAFold?style=flat&label=)
  - Baek et al. · University of Washington (Baker Lab) · Science 2021
  - Keywords: three-track network, structure prediction

## Protein & Binder/Antibody Design

- [BoltzGen: generative modeling for biomolecular design](https://github.com/HannesStark/boltzgen) [code](https://github.com/HannesStark/boltzgen) ![Stars](https://img.shields.io/github/stars/HannesStark/boltzgen?style=flat&label=)
  - Stärk et al. · MIT · 2025
  - Keywords: generative model, binder/complex design
- [Boltz-1: Democratizing biomolecular interaction modeling](https://github.com/jwohlwend/boltz) [code](https://github.com/jwohlwend/boltz) ![Stars](https://img.shields.io/github/stars/jwohlwend/boltz?style=flat&label=)
  - Wohlwend et al. · MIT (Jameel Clinic) · 2024
  - Keywords: open-source AlphaFold3-class model, complex prediction
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [De novo design of protein structure and function with RFdiffusion](https://www.nature.com/articles/s41586-023-06415-8) [code](https://github.com/RosettaCommons/RFdiffusion) ![Stars](https://img.shields.io/github/stars/RosettaCommons/RFdiffusion?style=flat&label=)
  - Watson et al. · University of Washington (Baker Lab) · Nature 2023 (preprint: [bioRxiv 2022](https://www.biorxiv.org/content/10.1101/2022.12.09.519842))
  - Keywords: diffusion, de novo binder design, scaffolding, motif scaffolding
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [Robust deep learning-based protein sequence design using ProteinMPNN](https://www.science.org/doi/10.1126/science.add2187) [code](https://github.com/dauparas/ProteinMPNN) ![Stars](https://img.shields.io/github/stars/dauparas/ProteinMPNN?style=flat&label=)
  - Dauparas et al. · University of Washington (Baker Lab) · Science 2022
  - Keywords: fixed-backbone sequence design, message passing
- [Design of protein-binding proteins from the target structure alone](https://www.nature.com/articles/s41586-022-04654-9)
  - Cao et al. · University of Washington (Baker Lab) · Nature 2022
  - Keywords: target-only binder design, de novo binders
- [Conditional Antibody Design as 3D Equivariant Graph Translation](https://arxiv.org/abs/2208.06073)
  - Kong et al. · Tsinghua University · NeurIPS 2022
  - Keywords: antibody design, graph translation, CDR generation
- [Language models generalize beyond natural proteins](https://www.biorxiv.org/content/10.1101/2022.12.21.521521)
  - Verkuil et al. · Meta AI (FAIR) · bioRxiv 2022
  - Keywords: ESMFold, hallucination, fixed-backbone design

## Molecular Generation & Drug Discovery

- [Molecule Generation For Target Protein Binding with Structural Motifs](https://openreview.net/forum?id=Rq13idF0F73)
  - Zhang et al. · Shanghai Jiao Tong University · ICLR 2023
  - Keywords: structure-based drug design, fragment generation
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [Equivariant diffusion for molecule generation in 3D (EDM)](https://arxiv.org/abs/2203.17003) [code](https://github.com/ehoogeboom/e3_diffusion_for_molecules) ![Stars](https://img.shields.io/github/stars/ehoogeboom/e3_diffusion_for_molecules?style=flat&label=)
  - Hoogeboom et al. · University of Amsterdam · ICML 2022
  - Keywords: 3D diffusion, equivariance, molecule generation
- [Accelerated antimicrobial discovery via deep generative models and molecular dynamics simulations](https://www.nature.com/articles/s41551-021-00689-x)
  - Das et al. · IBM Research · Nature Biomedical Engineering 2021
  - Keywords: generative autoencoder, antimicrobial peptides

## Genomics / DNA & RNA Foundation Models

- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [Evo: DNA foundation modeling from molecular to genome scale](https://www.science.org/doi/10.1126/science.ado9336) [code](https://github.com/evo-design/evo) ![Stars](https://img.shields.io/github/stars/evo-design/evo?style=flat&label=)
  - Nguyen et al. · Arc Institute & Stanford University · Science 2024
  - Keywords: long-context genomic model, generative DNA design
- [The Nucleotide Transformer: building and evaluating robust genomic foundation models](https://www.nature.com/articles/s41592-024-02523-z) [code](https://github.com/instadeepai/nucleotide-transformer) ![Stars](https://img.shields.io/github/stars/instadeepai/nucleotide-transformer?style=flat&label=)
  - Dalla-Torre et al. · InstaDeep (with NVIDIA & TU Munich) · Nature Methods 2024
  - Keywords: genomic foundation model, transformer
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language](https://academic.oup.com/bioinformatics/article/37/15/2112/6128680) [code](https://github.com/jerryji1993/DNABERT) ![Stars](https://img.shields.io/github/stars/jerryji1993/DNABERT?style=flat&label=)
  - Ji et al. · Northwestern University & Stony Brook University · Bioinformatics 2021
  - Keywords: DNA language model, genome representation

## Single-Cell & Omics Foundation Models

- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://www.nature.com/articles/s41592-024-02201-0) [code](https://github.com/bowang-lab/scGPT) ![Stars](https://img.shields.io/github/stars/bowang-lab/scGPT?style=flat&label=)
  - Cui et al. · University of Toronto · Nature Methods 2024
  - Keywords: single-cell, generative pretraining, multi-omics
- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [Geneformer: transfer learning enables predictions in network biology](https://www.nature.com/articles/s41586-023-06139-9) [code](https://huggingface.co/ctheodoris/Geneformer)
  - Theodoris et al. · Harvard Medical School & Boston Children's Hospital · Nature 2023
  - Keywords: gene network, transfer learning, single-cell

## Multi-modal / Foundation Models for Biology

- ![Highlight](https://img.shields.io/badge/-Highlight-blue) [ESM3: Simulating 500 million years of evolution with a language model](https://www.science.org/doi/10.1126/science.ado9336) [code](https://github.com/evolutionaryscale/esm) ![Stars](https://img.shields.io/github/stars/evolutionaryscale/esm?style=flat&label=)
  - Hayes et al. · EvolutionaryScale · Science 2025
  - Keywords: multimodal, sequence-structure-function, generative

## Datasets & Benchmarks

- [Protein Data Bank (PDB)](https://www.rcsb.org/)
  - Keywords: experimental structures, gold-standard benchmark
- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)
  - Keywords: predicted structures, whole-proteome coverage
- [CASP (Critical Assessment of Structure Prediction)](https://predictioncenter.org/)
  - Keywords: community benchmark, blind prediction

## Tools, Libraries & Servers

- [PyMOL](https://pymol.org/) [code](https://github.com/schrodinger/pymol-open-source) ![Stars](https://img.shields.io/github/stars/schrodinger/pymol-open-source?style=flat&label=) — molecular visualization
- [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) [code](https://github.com/RBVI/ChimeraX) ![Stars](https://img.shields.io/github/stars/RBVI/ChimeraX?style=flat&label=) — molecular visualization
- [Biotite](https://github.com/biotite-dev/biotite) [code](https://github.com/biotite-dev/biotite) ![Stars](https://img.shields.io/github/stars/biotite-dev/biotite?style=flat&label=) — computational structural biology library
- [BioPython](https://github.com/biopython/biopython) [code](https://github.com/biopython/biopython) ![Stars](https://img.shields.io/github/stars/biopython/biopython?style=flat&label=) — general bioinformatics toolkit

## Labs, Companies & Communities

- [Baker Lab (University of Washington)](https://www.bakerlab.org/) — RFdiffusion, ProteinMPNN, RoseTTAFold
- [EvolutionaryScale](https://www.evolutionaryscale.ai/) — ESM family
- [Chai Discovery](https://www.chaidiscovery.com/)
- [Google DeepMind](https://deepmind.google/) — AlphaFold family

## Related Awesome Lists

- [danielecook/Awesome-Bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics)
- [LirongWu/awesome-protein-representation-learning](https://github.com/LirongWu/awesome-protein-representation-learning)
- [opendilab/awesome-AI-based-protein-design](https://github.com/opendilab/awesome-AI-based-protein-design)
- [amorehead/awesome-molecular-generation](https://github.com/amorehead/awesome-molecular-generation)

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md)
for the entry format and guidelines before opening a PR.

This list is partly maintained by an automated scanner (every 2 days) that
proposes new papers via PR into [docs/staging/recent-papers.md](docs/staging/recent-papers.md).
See [scripts/README.md](scripts/README.md) for how it works.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, contributors have waived all copyright and
related rights to this work under [CC0](LICENSE).
