# subsample_fastq
Subsample fastq files using [seqtk](https://github.com/lh3/seqtk)

## Python Project Requirements

This document lists the required Python packages for the project.

### Requirements

- **Python**
  - Version = `3.11`
  
- **typer**: A library for building command-line interfaces (CLI).
  - Version: `0.4.0`
  
- **rich**: A library for rich text and beautiful formatting in the terminal.
  - Version: `13.3.1`

### Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage
❯ python subsample_fastq.py --help

```bash
 Usage: subsample_fastq.py [OPTIONS] R1 R2

 Main function to process FASTQ files.

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    r1      FILE  Path to R1 FASTQ.gz file [default: None] [required]                                                                                                                                                                │
│ *    r2      FILE  Path to R2 FASTQ.gz file [default: None] [required]                                                                                                                                                                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --threshold            INTEGER RANGE [x>=101]  Read count threshold [default: 120000000]                                                                                                                                              │
│ --seed                 INTEGER                 Random seed for seqtk [default: 11]                                                                                                                                                    │
│ --output-prefix        TEXT                    Prefix for the sub-sampled output files [default: subsampled]                                                                                                                          │
│ --output-dir           PATH                    Directory to save output files [default: /juno/cmo/cci/shahr2/test/subsample_Test]                                                                                                     │
│ --help                                         Show this message and exit.                                                                                                                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
