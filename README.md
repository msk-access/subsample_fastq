# subsample_fastq
Subsample Fastq Files using seqtk(https://github.com/lh3/seqtk)

## Usage
❯ python fastq_subsample.py --help

```bash
 Usage: fastq_subsample.py [OPTIONS] R1 R2

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
