ar# Candidate Projects Review

> Review-only working document. Nothing in this file has been added to
> `README.md`. Use the final column to record whether each item should be
> included, excluded, or investigated further.

## How to use this document

- **Great**: high-priority candidate; strong evidence, broad importance, and
  public code, data, or a stable project page.
- **Good**: credible and useful, but narrower, newer, less adopted, or mainly
  infrastructure.
- **Questionable / Not sure**: verify the project, link, maturity, scope, or
  public availability before inclusion.

## AlphaGenome ecosystem

> AlphaGenome is a Google DeepMind project, not an Arc Institute project.

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| AlphaGenome API and client | Model + API; regulatory genomics and variant effects | [Project](https://deepmind.google.com/science/alphagenome) · [GitHub](https://github.com/google-deepmind/alphagenome) · [Docs](https://www.alphagenomedocs.com/) · [HF collection](https://huggingface.co/collections/google/alphagenome) | Predicts expression, splicing, chromatin, TF binding, histone marks, polyadenylation, and chromatin contacts from DNA; designed for regulatory variant-effect analysis. | **Great** | **Accepted** — included in README.md via PR #5 as part of the AlphaGenome Highlight entry. |
| AlphaGenome research implementation | JAX model implementation and research code | [GitHub](https://github.com/google-deepmind/alphagenome_research) | Includes data loaders, variant scoring, in-silico mutagenesis, and notebooks for research customization and reproducibility. | **Great** | **Accepted** — included in README.md via PR #5 as part of the AlphaGenome Highlight entry. |
| Google DeepMind Science Skills | Scientific agent skills and tool integrations | [GitHub](https://github.com/google-deepmind/science-skills) | Wraps AlphaGenome, AlphaFold DB, UniProt, and many other scientific databases and tools. | **Good** | **Accepted** — included in README.md via PR #5 in the Skills and Agents section. |
| AlphaGenome PyTorch port | Community model port | [GitHub](https://github.com/genomicsxai/alphagenome-pytorch) | Useful for PyTorch users, but unofficial and potentially less current than DeepMind's implementation. | **Good / Not sure** | **Accepted** — included in README.md via PR #5 as part of the AlphaGenome Highlight entry; unofficial port. |

## Arc Institute projects

### Models, datasets, and benchmarks

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| Evo 2 | Genome foundation model | [GitHub](https://github.com/ArcInstitute/evo2) · [Arc page](https://arcinstitute.org/tools/evo) · [Nature paper](https://doi.org/10.1038/s41586-026-10176-5) | Trained on approximately 9 trillion DNA tokens; models from about 1B to 40B parameters and up to 1M-base context. Major successor to Evo 1. | **Great** | **Accepted** — included in README.md via PR #5. |
| OpenGenome2 | Genomic pretraining dataset | [Hugging Face dataset](https://huggingface.co/datasets/arcinstitute/opengenome2) | Large all-domain-of-life genomic corpus used for Evo 2. | **Great** | **Accepted** — included in README.md via PR #5. |
| STATE | Virtual-cell perturbation model | [GitHub](https://github.com/ArcInstitute/state) · [Arc page](https://arcinstitute.org/tools/state) | Predicts transcriptomic responses to genetic perturbations, drugs, and cytokines across cellular contexts. | **Great** | **Accepted** — included in README.md via PR #5. |
| Stack | Single-cell foundation model | [GitHub](https://github.com/ArcInstitute/stack) · [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.01.09.698608v1) | Uses in-context learning at inference time for single-cell perturbation prediction; peer review is pending. | **Good** | **Accepted** — included in README.md via PR #5. |
| Arc Virtual Cell Atlas | Dataset and platform | [GitHub](https://github.com/ArcInstitute/arc-virtual-cell-atlas) · [Arc page](https://arcinstitute.org/tools/virtualcellatlas) · [LaminDB](https://lamin.ai/laminlabs/arc-virtual-cell-atlas) | Atlas-scale single-cell resource combining public data, Tahoe perturbation data, and challenge datasets. | **Great** | **Accepted** — included in README.md via PR #5. |
| Virtual Cell Challenge | Benchmark and competition | [Official site](https://virtualcellchallenge.org/) · [Arc initiative](https://arcinstitute.org/virtual-cell-initiative) | CASP-like evaluation of virtual-cell models, including generalization to unseen cell contexts. | **Great** | **Rejected for now** — leave out of README.md. |

### Protein engineering and biological design

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| MULTI-evolve | ML-guided protein engineering | [GitHub](https://github.com/ArcInstitute/MULTI-evolve) · [Science paper](https://doi.org/10.1126/science.aea1820) | Combines fitness prediction, multi-mutant proposal, oligo design, and protein-language-model priors. | **Good** | |
| Proto | Generative biology programming language | [Arc tools](https://arcinstitute.org/tools) · [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.06.22.733870v1) | Composes design primitives across DNA, RNA, proteins, ligands, and interactions; public code was not located. | **Good / Not sure** | **Accepted** — included in README.md via PR #5 in the Tools section. |
| BioReason-Pro / GO-GPT | Protein-function prediction and reasoning | [Project / paper](https://bioreason.net/paper) | Multimodal protein-function reasoning system with strong preprint claims but no public code found. | **Good / Not sure** | **Accepted** — included in README.md via PR #5 with the BioReason app link. |
| CodonFM | Codon optimization and mRNA design model | [NVIDIA preprint](https://research.nvidia.com/labs/dbr/assets/data/manuscripts/nv-codonfm-preprint.pdf) | Arc/NVIDIA collaboration on codon-language models; public repository and ownership need verification. | **Good / Not sure** | **Rejected for now** — leave out of README.md. |
| SynGenome | Synthetic-DNA dataset | [Project](https://evodesign.org/syngenome/) | Large synthetic DNA resource generated with Evo; data-access details need verification. | **Good** | **Accepted** — included in README.md via PR #5. |

### Single-cell, sequencing, and evaluation infrastructure

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| cell-eval | Perturbation-model evaluation suite | [GitHub](https://github.com/ArcInstitute/cell-eval) | Metrics, baselines, data-ceiling estimation, and Virtual Cell Challenge-compatible evaluation. | **Good** | **Accepted** — included in README.md via PR #5. |
| cell-load | Single-cell perturbation data loaders | [GitHub](https://github.com/ArcInstitute/cell-load) | PyTorch loaders supporting the State and virtual-cell ecosystem. | **Good** | **Rejected for now** — leave out of README.md. |
| SRAgent | LLM-assisted SRA curation | [GitHub](https://github.com/ArcInstitute/SRAgent) · [scBaseCount paper](https://www.biorxiv.org/content/10.1101/2025.02.27.640494v1) | Uses language-model agents to extract metadata and discover linked studies; supports the Virtual Cell Atlas. | **Good** | **Accepted** — included in README.md via PR #5 in the Skills and Agents section. |
| scRecounter | scRNA-seq reprocessing pipeline | [GitHub](https://github.com/ArcInstitute/scRecounter) · [scBaseCount paper](https://www.biorxiv.org/content/10.1101/2025.02.27.640494v1) | Uniformly reprocesses public scRNA-seq datasets for atlas-scale modeling. | **Good** | **Rejected for now** — leave out of README.md. |
| cyto | High-throughput 10x Flex mapper | [GitHub](https://github.com/ArcInstitute/cyto) | Rust-based mapper intended to make large sequencing projects more efficient. | **Good** | **Rejected for now** — leave out of README.md. |
| BINSEQ | Binary sequencing data format | [GitHub](https://github.com/ArcInstitute/binseq) | Efficient binary format used by Arc's sequencing infrastructure. | **Good** | **Rejected for now** — leave out of README.md. |
| bqtools | BINSEQ processing CLI | [GitHub](https://github.com/ArcInstitute/bqtools) | Command-line tooling for BINSEQ data. | **Good** | **Rejected for now** — leave out of README.md. |
| xsra | SRA extraction CLI | [GitHub](https://github.com/ArcInstitute/xsra) | Fast extraction of SRA data into FASTA, FASTQ, and BINSEQ formats. | **Good** | **Rejected for now** — leave out of README.md. |
| ScreenPro2 | CRISPR-screen analysis | [GitHub](https://github.com/ArcInstitute/ScreenPro2) · [Docs](https://screenpro2.readthedocs.io/) | Pooled CRISPR screen processing, scoring, QC, and visualization. | **Good** | **Rejected for now** — leave out of README.md. |

### Other Arc tools and collaborations

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| Bridge RNA Designer | Genome-engineering design tool | [GitHub](https://github.com/ArcInstitute/bridge-rna-designer) · [Web tool](https://bridge.hsulab.arcinstitute.org/) · [Nature paper](https://doi.org/10.1038/s41586-024-07552-4) | Designs bridge RNAs for programmable recombination; underlying technology is supported by Nature and Science papers. | **Good** | |
| Cas13d guide design tool | RNA-targeting design tool | [Arc tools](https://arcinstitute.org/tools) · [Code](https://github.com/ArcInstitute/RNAtargeting_web_custom) | Deep-learning-assisted guide selection for Cas13d knockdown; public code is small and specialized. | **Good** | |
| APAlog | RNA-seq analysis tool | [Arc tools](https://arcinstitute.org/tools) | Differential polyadenylation analysis; published, but current public repository needs verification. | **Good / Not sure** | |
| RiboLog | Ribo-seq analysis tool | [Arc tools](https://arcinstitute.org/tools) | Ribosome-footprinting analysis; published, but current public repository needs verification. | **Good / Not sure** | |
| pyteiser | RNA-structure discovery tool | [Arc tools](https://arcinstitute.org/tools) | Discovers RNA structural elements; published in Science, but current repository needs verification. | **Good / Not sure** | |
| SwitchFinder | RNA structural-switch discovery | [Arc tools](https://arcinstitute.org/tools) | Systematic discovery of transcriptome-wide RNA structural switches; published in Nature Methods. | **Good / Not sure** | |
| RBP Browser | RNA-binding-protein analysis app | [Arc tools](https://arcinstitute.org/tools) | Shiny application for post-transcriptional regulatory modules; current code location needs verification. | **Good / Not sure** | |
| iAnalyzer | CRISPR-screen analytics | [Arc tools](https://arcinstitute.org/tools) | QC, alignment, statistics, and hit identification; no stable Arc repository was located. | **Good / Not sure** | |
| Lizard-Wizard | Calcium-imaging pipeline | [GitHub](https://github.com/ArcInstitute/Lizard-Wizard) | Specialized imaging pipeline with very low adoption signals and limited direct relevance to the current list. | **Questionable** | |
| Wizard's Staff | Calcium-imaging pipeline | [GitHub](https://github.com/ArcInstitute/Wizards-Staff) | Companion to Lizard-Wizard; very low adoption and unclear relevance to the list. | **Questionable** | |
| Savanna | Training infrastructure related to Evo 2 | [GitHub](https://github.com/Zymrael/savanna) | Open training framework associated with Evo 2, but not Arc-owned. | **Good / Not sure** | |

## GPT-Rosalind ecosystem

> GPT-Rosalind is an OpenAI life-sciences system, not an Arc Institute
> project. It should be labeled as a proprietary or gated product rather than
> presented as an open biological foundation model.

### Models and products

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| GPT-Rosalind | Life-sciences specialist LLM | [OpenAI announcement](https://openai.com/index/introducing-gpt-rosalind/) | Intended for biomedical evidence synthesis, hypotheses, experimental planning, and molecular/biological analysis; gated trusted-access program. | **Great** | |
| GPT-Rosalind-5.5 | Updated life-sciences specialist LLM | [OpenAI update](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) · [System card](https://deploymentsafety.openai.com/gpt-rosalind-5-5/gpt-rosalind-5-5.pdf) | Incrementally trained from GPT-5.5 with stronger coding, tool use, and life-sciences reasoning; still gated. | **Great** | |
| Rosalind Workbench | Research workbench and ChatGPT product | [Workbench](https://chatgpt.com/rosalind-workbench) · [Developer blog](https://developers.openai.com/blog/rosalind-workbench) | Provides structure, sequence, pathology-slide, and NGS workflows around GPT-Rosalind; research preview, not open source. | **Great** | |
| Rosalind Biodefense | Biosecurity/public-health program | [OpenAI page](https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/) | Restricted application of the system for biodefense and pandemic preparedness; details and access are limited. | **Good / Not sure** | |

### Codex plugins and skills

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| Life Sciences Research plugin | Scientific-agent skills and database integrations | [OpenAI plugins](https://github.com/openai/plugins/tree/main/plugins/life-science-research) | Covers genetics, expression, proteins, structure, pathways, chemistry, clinical data, literature, proteomics, and public databases. | **Great** | |
| Life Sciences NGS Analysis plugin | NGS analysis agent | [OpenAI update](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) · [Workbench](https://developers.openai.com/blog/rosalind-workbench) | Intended for FASTQ QC, bulk RNA-seq, single-cell analysis, differential expression, and reviewable orchestration; no separate repository located. | **Good** | |

### GPT-Rosalind-related benchmarks

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| LifeSciBench | Life-sciences AI benchmark | [OpenAI announcement](https://openai.com/index/introducing-life-sci-bench/) · [Preprint](https://doi.org/10.64898/2026.08.13.744657) | Expert-authored multi-step tasks across biological workflows and domains. | **Great** | |
| GeneBench | Genomics and quantitative-biology benchmark | [Preprint](https://doi.org/10.64898/2026.04.22.720113) | Tests multistage inference under realistic QC, confounding, and model-selection problems. | **Great** | |
| GeneBench-Pro | Extended genomics/translational benchmark | [Preprint](https://doi.org/10.64898/2026.06.29.735386) | Extension of GeneBench; preprint details and public artifacts need further verification. | **Good** | |
| BixBench | Computational-biology agent benchmark | [GitHub](https://github.com/Future-House/BixBench) · [Paper](https://arxiv.org/abs/2503.00096) · [Dataset](https://huggingface.co/datasets/futurehouse/BixBench) | Independent benchmark built from real computational-biology notebooks and multi-step analysis tasks. | **Great** | |
| LABBench / LABBench2 | Laboratory-biology benchmark | [HF predecessor](https://huggingface.co/datasets/futurehouse/lab-bench) | Practical laboratory reasoning benchmark used in GPT-Rosalind comparisons; LABBench2's public release needs verification. | **Good** | |
| MedChemBench | Medicinal-chemistry benchmark | No confirmed public repository | Used in GPT-Rosalind-5.5 evaluations for SAR, ADME, toxicity, and lead optimization. | **Good / Not sure** | |
| LabWorkBench | Wet-lab reasoning benchmark | No confirmed public repository | Proprietary or not-yet-public evaluation of experimental reasoning. | **Good / Not sure** | |

## Other scientific-agent ecosystems

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| Google DeepMind science-skills | Life-sciences agent skills | [GitHub](https://github.com/google-deepmind/science-skills) | Open skills for AlphaGenome, AlphaFold DB, UniProt, genomics, chemistry, and scientific search. | **Great** | **Accepted** — included in README.md via PR #5 in the Skills and Agents section. |
| Anthropic Life Sciences | Claude skills and MCP integrations | [GitHub](https://github.com/anthropics/life-sciences) | First-party and partner skills covering single-cell, clinical trials, chemistry, genomics, and literature. | **Great** | |
| AWS Kiro Life Sciences | MCP servers and workflow bundle | [GitHub](https://github.com/aws-samples/sample-kiro-power-life-sciences) | AWS sample bundle with database integrations, domain skills, and HealthOmics workflows. | **Great** | |
| BioAgent Bench | Bioinformatics-agent benchmark | [GitHub](https://github.com/bioagent-bench/bioagent-bench) | End-to-end pipeline tasks with corrupted-input and decoy-file robustness tests. | **Good** | |
| CompBioBench | Computational-biology benchmark | [GitHub](https://github.com/Genentech/compbiobench-runner) | Genentech benchmark covering single-cell, genomics, transcriptomics, genetics, and ML. | **Good** | |

## Wider missing projects

### Protein structure prediction

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| RoseTTAFold All-Atom | All-atom complex structure prediction | [GitHub](https://github.com/baker-laboratory/RoseTTAFold-All-Atom) | Handles proteins, nucleic acids, ligands, metals, and covalent modifications. | **Great** | |
| Chai-1 / Chai-2 | Multimolecular structure prediction and binder design | [GitHub](https://github.com/chaidiscovery/chai-lab) | Open multimolecular structure model; Chai-2 extends toward antibody design. | **Great** | |
| OmegaFold | MSA-free protein structure prediction | [GitHub](https://github.com/HeliXonProtein/OmegaFold) | Single-sequence structure prediction using a protein language model and geometry module. | **Great** | |
| RoseTTAFold2NA | Protein-nucleic-acid complex prediction | [GitHub](https://github.com/uw-ipd/RoseTTAFold2NA) | Structure prediction for protein-RNA and protein-DNA complexes. | **Great** | |
| IgFold | Antibody structure prediction | [GitHub](https://github.com/Graylab/IgFold) | Fast antibody modeling using AntiBERTy representations. | **Great** | |
| ESMC / ESMFold2 | Protein language and structure models | [Biohub ESM](https://github.com/Biohub/esm) | Newer ESM ecosystem; current repository/status should be verified separately from the existing ESM entry. | **Good / Not sure** | |
| Genie 2 | Protein-backbone generation | [GitHub](https://github.com/aqlaboratory/genie2) | Diffusion-based backbone generation and motif scaffolding. | **Good** | |
| Uni-Fold | AlphaFold-compatible training platform | [GitHub](https://github.com/dptech-corp/Uni-Fold) | Open training and inference implementation distinct from OpenFold. | **Good** | |

### Protein design and generative models

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| Chroma | Programmable all-atom protein design | [GitHub](https://github.com/generatebio/chroma) | Diffusion design with composable symmetry, shape, text, and secondary-structure constraints. | **Great** | |
| EvoDiff | Sequence-space protein design | [GitHub](https://github.com/microsoft/evodiff) | Discrete diffusion for protein sequences, including disordered proteins and motif scaffolding. | **Great** | |
| FrameFlow | SE(3) flow-matching protein generation | [GitHub](https://github.com/microsoft/protein-frame-flow) | Flow matching for backbone generation and motif scaffolding. | **Great** | |
| FrameDiff | SE(3) protein diffusion | [GitHub](https://github.com/jasonkyuyim/se3_diffusion) | Influential frame-based diffusion model underlying later protein-generation work. | **Great** | |
| LigandMPNN | Ligand-aware sequence design | [GitHub](https://github.com/dauparas/LigandMPNN) | Extends ProteinMPNN to ligands, metals, nucleic acids, and membrane proteins. | **Great** | |
| ProtTrans | Protein language-model suite | [GitHub](https://github.com/rostlab/prottrans) | ProtBERT, ProtT5, and related models used widely as protein-embedding baselines. | **Great** | |
| ProGen / ProGen2 | Autoregressive protein generation | [GitHub](https://github.com/salesforce/progen) | Early influential conditional protein language models. | **Great** | |
| LOBSTER | Protein/sequence language-model library | [GitHub](https://github.com/prescient-design/lobster) | Genentech Prescient Design library with masked, causal, and flow-matching models. | **Good** | |
| MultiFlow | Joint sequence/structure co-design | [GitHub](https://github.com/jasonkyuyim/multiflow) | Combines discrete and continuous flow matching for protein co-design. | **Good** | |
| Protpardelle-1c | All-atom protein generation | [GitHub](https://github.com/ProteinDesignLab/protpardelle-1c) | Generates backbone and side chains; successor to a deprecated repository. | **Good / Not sure** | |

### Molecular generation and drug discovery

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| DiffDock | Blind molecular docking | [GitHub](https://github.com/gcorso/DiffDock) | Diffusion over ligand poses; widely adopted docking baseline. | **Great** | |
| Uni-Mol | 3D molecular foundation model | [GitHub](https://github.com/deepmodeling/Uni-Mol) | Molecular representation, property prediction, conformation generation, and docking. | **Great** | |
| DiffSBDD | Pocket-conditioned molecule generation | [GitHub](https://github.com/arneschneuing/DiffSBDD) | Equivariant diffusion for structure-based drug design and molecular optimization. | **Great** | |
| REINVENT4 | De novo molecular design | [GitHub](https://github.com/MolecularAI/REINVENT4) | Reinforcement-learning and transfer-learning workflows for medicinal chemistry. | **Great** | |
| RDKit | Core cheminformatics library | [GitHub](https://github.com/rdkit/rdkit) | Widely used open-source toolkit for descriptors, fingerprints, search, and molecular operations. | **Great** | |
| GROVER | Molecular graph transformer | [GitHub](https://github.com/tencent-ailab/grover) | Self-supervised graph model pretrained on large molecular corpora. | **Good** | |
| EquiBind | Blind docking model | [GitHub](https://github.com/HannesStark/EquiBind) | Fast SE(3)-equivariant rigid-body docking baseline. | **Good** | |

### Genomics, DNA, and RNA

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| HyenaDNA | Long-context DNA language model | [GitHub](https://github.com/HazyResearch/hyena-dna) | Models up to million-token genomic contexts at single-nucleotide resolution. | **Great** | |
| Caduceus | Reverse-complement-equivariant DNA model | [GitHub](https://github.com/kuleshov-group/caduceus) | Mamba-based bidirectional DNA model with reverse-complement symmetry. | **Great** | |
| RNA-FM / RhoFold | RNA language and structure models | [GitHub](https://github.com/ml4bio/RNA-FM) | RNA-FM, RhoFold, RiboDiffusion, and RhoDesign ecosystem. | **Great** | |
| Enformer PyTorch | Regulatory-genomics model port | [GitHub](https://github.com/lucidrains/enformer-pytorch) | PyTorch implementation of DeepMind's long-context model for regulatory tracks; unofficial port. | **Great / verify** | |
| DNABERT-2 | DNA language model | [GitHub](https://github.com/Zhihan1996/DNABERT-2) | K-mer-free BPE-tokenized model trained across species; repository status needs verification. | **Good / verify** | |
| AIDO / GenBio models | DNA, RNA, protein, and cell models | [GitHub](https://github.com/genbio-ai/ModelGenerator) | Unified foundation-model and fine-tuning framework from GenBio AI. | **Good** | |
| EVE | Evolutionary variant-effect model | [GitHub](https://github.com/debbiemarkslab/EVE) | Unsupervised protein variant-effect prediction published in Nature. | **Good** | |
| ProtGPT2 | Autoregressive protein language model | [Hugging Face](https://huggingface.co/nferruz/ProtGPT2) | Protein generation model published in Nature Communications. | **Good** | |
| CaLM | Codon-level language model | [GitHub](https://github.com/oxpig/CaLM) | Codon-aware embeddings for protein engineering and fitness prediction. | **Good** | |

### Single-cell and omics

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| scFoundation | Single-cell foundation model | [GitHub](https://github.com/biomap-research/scFoundation) | Trained on tens of millions of cells for expression enhancement, drug response, and perturbation tasks. | **Great** | |
| scVI-tools | Probabilistic single-cell modeling | [GitHub](https://github.com/scverse/scvi-tools) | Major framework for integration, annotation, uncertainty, and spatial/single-cell modeling. | **Great** | |
| Scanpy | Single-cell analysis toolkit | [GitHub](https://github.com/scverse/scanpy) | De facto Python workflow for scalable single-cell analysis. | **Great** | |
| AnnData | Annotated data-matrix infrastructure | [GitHub](https://github.com/scverse/anndata) | Standard data structure used by Scanpy, scVI-tools, scGPT, Geneformer, and much of scverse. | **Great** | |
| GEARS | Combinatorial perturbation prediction | [GitHub](https://github.com/snap-stanford/GEARS) | Predicts transcriptional outcomes of novel multi-gene perturbations. | **Great** | |
| UCE | Universal cell embeddings | [GitHub](https://github.com/snap-stanford/UCE) | Transformer embeddings across species and cell types without task-specific fine-tuning. | **Great** | |
| CellTypist | Cell-type annotation | [GitHub](https://github.com/Teichlab/celltypist) | Practical automated cell-type annotation tool with broad adoption. | **Good** | |
| MOFA+ | Multi-omics factor analysis | [GitHub](https://github.com/bioFAM/MOFA2) | Widely used multi-omics integration and latent-factor framework. | **Good** | |
| scBERT | Single-cell language model | [GitHub](https://github.com/TencentAILabHealthcare/scBERT) | Earlier transformer model for single-cell gene-expression representations. | **Good** | |

### Multimodal biology and medical imaging

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| UNI / UNI2 | Computational pathology foundation model | [GitHub](https://github.com/mahmoodlab/UNI) | General-purpose pathology model for tile- and slide-level tasks. | **Great** | |
| CONCH | Pathology vision-language model | [GitHub](https://github.com/mahmoodlab/CONCH) | Image-text model for histopathology retrieval, classification, and segmentation. | **Great** | |
| Prov-GigaPath | Whole-slide pathology model | [GitHub](https://github.com/prov-gigapath/prov-gigapath) | Large-scale tile and slide model trained on real-world pathology data. | **Great** | |
| MedSAM | Medical-image segmentation model | [GitHub](https://github.com/bowang-lab/MedSAM) | Segment Anything adaptation for CT, MRI, ultrasound, and other medical images. | **Great** | |
| BioGPT | Biomedical language model | [GitHub](https://github.com/microsoft/BioGPT) | PubMed-trained generative model for biomedical text mining and generation. | **Good** | |

### Datasets and benchmarks

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| Therapeutics Data Commons | Drug-discovery benchmark suite | [GitHub](https://github.com/mims-harvard/TDC) | Standardized datasets and splits for ADMET, target identification, QA, and reaction prediction. | **Great** | |
| OpenProteinSet | Protein-model training data | [OpenFold context](https://github.com/aqlaboratory/openfold) | Large MSA and sequence-cluster dataset supporting AlphaFold-class retraining. | **Good** | |
| BioAgent Bench | Bioinformatics-agent benchmark | [GitHub](https://github.com/bioagent-bench/bioagent-bench) | End-to-end pipeline tasks and controlled robustness perturbations. | **Good** | |
| CompBioBench | Computational-biology benchmark | [GitHub](https://github.com/Genentech/compbiobench-runner) | Bare-environment computational-biology tasks spanning genomics, single-cell, and transcriptomics. | **Good** | |
| ProSE | Protein representation model | [GitHub](https://github.com/tbepler/prose) | Classic multitask protein embedding model with structure and function supervision. | **Good** | |

### Tools and infrastructure

| Project | Type / area | Links | Why it matters / evidence | Classification | Your notes / decision |
|---|---|---|---|---|---|
| MDAnalysis | Molecular-dynamics analysis | [GitHub](https://github.com/MDAnalysis/mdanalysis) | Major library for analyzing molecular-dynamics trajectories and structural data. | **Great** | |
| Beignet | Biological research Python/PyTorch library | [GitHub](https://github.com/Genentech/beignet) | Genentech open-source library supporting sequence, protein, and Lie-group operations. | **Good** | |
| CARP / protein sequence models | Protein sequence models | [GitHub](https://github.com/microsoft/protein-sequence-models) | CARP, MIF, MIF-ST, and related sequence/inverse-folding models. | **Good** | |

## Recommended first review batch

If you want to make decisions in stages, I suggest reviewing these first:

1. AlphaGenome API and research implementation
2. Evo 2 and OpenGenome2
3. STATE, Arc Virtual Cell Atlas, and Virtual Cell Challenge
4. Chai-1 / Chai-2 and RoseTTAFold All-Atom
5. LigandMPNN
6. DiffDock, Uni-Mol, REINVENT4, and RDKit
7. HyenaDNA, Caduceus, and RNA-FM / RhoFold
8. scFoundation, scVI-tools, Scanpy, AnnData, GEARS, and UCE
9. UNI / CONCH / Prov-GigaPath
10. Therapeutics Data Commons and MDAnalysis
11. GPT-Rosalind and its Life Sciences Research plugin

## Important verification notes

- AlphaGenome and Arc Institute are separate organizations.
- GPT-Rosalind is a gated/proprietary life-sciences system, not an open model
  repository.
- Community ports should be labeled as unofficial when an official
  implementation exists.
- New preprints without code, data, peer review, or stable project pages should
  remain in **Questionable / Not sure** until verified.
- The same project can be useful in more than one category, but should normally
  have one primary entry and cross-links rather than duplicate entries.
