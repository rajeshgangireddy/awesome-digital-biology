# Awesome Digital Biology [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg) ![Stars](https://img.shields.io/github/stars/rajeshgangireddy/awesome-digital-biology?style=social) ![Last Commit](https://img.shields.io/github/last-commit/rajeshgangireddy/awesome-digital-biology)

> A curated, **actively-maintained** list of deep learning research, models,
> tools, and datasets for **digital biology** — protein structure prediction,
> protein/binder/antibody design, molecular generation, genomics & single-cell
> foundation models, and the software that powers them.

Why this list exists: the AI-for-biology space is exploding, but resources are
scattered across dozens of narrow, often-stale lists. This repo aims to be the
**single go-to hub** — broad in scope, strict in curation, and kept fresh via
an automated scanning bot that proposes new papers every 2 days (see
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
- [Title](link) [code](code-link)
  - Authors · Institution/Company · Venue/Year
  - Keywords: ...
```

## Protein Structure Prediction

- [Highly accurate protein structure prediction with AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) [code](https://github.com/google-deepmind/alphafold)
  - Jumper et al. · Google DeepMind · Nature 2021
  - Keywords: structure prediction, Evoformer, MSA
- [Accurate structure prediction of biomolecular interactions with AlphaFold3](https://www.nature.com/articles/s41586-024-07487-w) [code](https://github.com/google-deepmind/alphafold3)
  - Abramson et al. · Google DeepMind & Isomorphic Labs · Nature 2024
  - Keywords: diffusion, biomolecular complexes
- [Language models of protein sequences at the scale of evolution enable accurate structure prediction (ESMFold)](https://www.biorxiv.org/content/10.1101/2022.07.20.500902) [code](https://github.com/facebookresearch/esm)
  - Lin et al. · Meta AI (FAIR) · bioRxiv 2022
  - Keywords: protein language model, single-sequence folding
- [ColabFold: Making protein folding accessible to all](https://www.nature.com/articles/s41592-022-01488-1) [code](https://github.com/sokrypton/ColabFold)
  - Mirdita et al. · Seoul National University & Harvard Medical School · Nature Methods 2022
  - Keywords: accessible inference, MSA search, notebooks
- [RoseTTAFold: Accurate prediction of protein structures and interactions using a three-track network](https://www.science.org/doi/10.1126/science.abj8754) [code](https://github.com/RosettaCommons/RoseTTAFold)
  - Baek et al. · University of Washington (Baker Lab) · Science 2021
  - Keywords: three-track network, structure prediction
- [OpenFold: Retraining AlphaFold2 yields new insights into its learning mechanisms](https://www.nature.com/articles/s41592-024-02272-z) [code](https://github.com/aqlaboratory/openfold)
  - Ahdritz et al. · Columbia University · Nature Methods 2024
  - Keywords: open reimplementation, trainable

## Protein & Binder/Antibody Design

- [Broadly applicable and accurate protein design by integrating structure prediction networks and diffusion generative models (RFdiffusion)](https://www.biorxiv.org/content/10.1101/2022.12.09.519842) [code](https://github.com/RosettaCommons/RFdiffusion)
  - Watson et al. · University of Washington (Baker Lab) · Nature 2023
  - Keywords: diffusion, de novo binder design, scaffolding
- [Robust deep learning-based protein sequence design using ProteinMPNN](https://www.science.org/doi/10.1126/science.add2187) [code](https://github.com/dauparas/ProteinMPNN)
  - Dauparas et al. · University of Washington (Baker Lab) · Science 2022
  - Keywords: fixed-backbone sequence design, message passing
- [De novo design of protein structure and function with RFdiffusion](https://www.nature.com/articles/s41586-023-06415-8) [code](https://github.com/RosettaCommons/RFdiffusion)
  - Watson et al. · University of Washington (Baker Lab) · Nature 2023
  - Keywords: motif scaffolding, symmetric design, binders
- [Design of protein-binding proteins from the target structure alone](https://www.nature.com/articles/s41586-022-04654-9)
  - Cao et al. · University of Washington (Baker Lab) · Nature 2022
  - Keywords: target-only binder design, de novo binders
- [Boltz-1: Democratizing biomolecular interaction modeling](https://github.com/jwohlwend/boltz) [code](https://github.com/jwohlwend/boltz)
  - Wohlwend et al. · MIT (Jameel Clinic) · 2024
  - Keywords: open-source AlphaFold3-class model, complex prediction
- [BoltzGen: generative modeling for biomolecular design](https://github.com/HannesStark/boltzgen) [code](https://github.com/HannesStark/boltzgen)
  - Stärk et al. · MIT
  - Keywords: generative model, binder/complex design
- [Conditional Antibody Design as 3D Equivariant Graph Translation](https://arxiv.org/abs/2208.06073)
  - Kong et al. · Tsinghua University · NeurIPS 2022
  - Keywords: antibody design, graph translation, CDR generation
- [Language models generalize beyond natural proteins](https://www.biorxiv.org/content/10.1101/2022.12.21.521521)
  - Verkuil et al. · Meta AI (FAIR) · bioRxiv 2022
  - Keywords: ESMFold, hallucination, fixed-backbone design

## Molecular Generation & Drug Discovery

- [Accelerated antimicrobial discovery via deep generative models and molecular dynamics simulations](https://www.nature.com/articles/s41551-021-00689-x)
  - Das et al. · IBM Research · Nature Biomedical Engineering 2021
  - Keywords: generative autoencoder, antimicrobial peptides
- [Equivariant diffusion for molecule generation in 3D (EDM)](https://arxiv.org/abs/2203.17003) [code](https://github.com/ehoogeboom/e3_diffusion_for_molecules)
  - Hoogeboom et al. · University of Amsterdam · ICML 2022
  - Keywords: 3D diffusion, equivariance, molecule generation
- [Molecule Generation For Target Protein Binding with Structural Motifs](https://openreview.net/forum?id=Rq13idF0F73)
  - Zhang et al. · Shanghai Jiao Tong University · ICLR 2023
  - Keywords: structure-based drug design, fragment generation

## Genomics / DNA & RNA Foundation Models

- [DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language](https://academic.oup.com/bioinformatics/article/37/15/2112/6128680) [code](https://github.com/jerryji1993/DNABERT)
  - Ji et al. · Northwestern University & Stony Brook University · Bioinformatics 2021
  - Keywords: DNA language model, genome representation
- [The Nucleotide Transformer: building and evaluating robust genomic foundation models](https://www.nature.com/articles/s41592-024-02523-z) [code](https://github.com/instadeepai/nucleotide-transformer)
  - Dalla-Torre et al. · InstaDeep (with NVIDIA & TU Munich) · Nature Methods 2024
  - Keywords: genomic foundation model, transformer
- [Evo: DNA foundation modeling from molecular to genome scale](https://www.science.org/doi/10.1126/science.ado9336) [code](https://github.com/evo-design/evo)
  - Nguyen et al. · Arc Institute & Stanford University · Science 2024
  - Keywords: long-context genomic model, generative DNA design

## Single-Cell & Omics Foundation Models

- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://www.nature.com/articles/s41592-024-02201-0) [code](https://github.com/bowang-lab/scGPT)
  - Cui et al. · University of Toronto · Nature Methods 2024
  - Keywords: single-cell, generative pretraining, multi-omics
- [Geneformer: transfer learning enables predictions in network biology](https://www.nature.com/articles/s41586-023-06139-9) [code](https://huggingface.co/ctheodoris/Geneformer)
  - Theodoris et al. · Harvard Medical School & Boston Children's Hospital · Nature 2023
  - Keywords: gene network, transfer learning, single-cell

## Multi-modal / Foundation Models for Biology

- [ESM3: Simulating 500 million years of evolution with a language model](https://www.science.org/doi/10.1126/science.ado9336) [code](https://github.com/evolutionaryscale/esm)
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

- [PyMOL](https://pymol.org/) — molecular visualization
- [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) — molecular visualization
- [Biotite](https://github.com/biotite-dev/biotite) — computational structural biology library
- [BioPython](https://github.com/biopython/biopython) — general bioinformatics toolkit

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
