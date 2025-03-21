import subprocess
import gzip
import typer
import logging
import os
from pathlib import Path
from rich.logging import RichHandler
from rich.console import Console

# Set up Rich Console
console = Console()

# Set up logging with Rich
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console)],
)

log = logging.getLogger("rich")


def count_reads(fastq_file: Path) -> int:
    """Count the number of reads in a FASTQ file."""
    try:
        with gzip.open(fastq_file, "rt") as f:
            return sum(1 for _ in f) // 4
    except Exception as e:
        log.exception(f"Error counting reads in {fastq_file}: {e}")
        raise


def run_seqtk(
    fastq_file: Path, proportion: float, seed: int, output_prefix: str, output_dir: Path
) -> Path:
    """Run the seqtk command to sample a FASTQ file and gzip the result."""
    output_file = output_dir / f"{output_prefix}_{fastq_file.name}"
    command = f"seqtk sample -s {seed} {fastq_file} {proportion} > {output_file}"
    try:
        log.info(
            f"Running seqtk on {fastq_file} with proportion {proportion:.6f} and seed {seed}..."
        )
        subprocess.run(command, shell=True, check=True)
        log.info(f"Successfully generated sub-sampled file for {fastq_file}")

        # Gzip the output file
        log.info(f"Gzipping {output_file}...")
        with open(output_file, "rb") as f_in:
            with gzip.open(f"{output_file}.gz", "wb") as f_out:
                f_out.writelines(f_in)
        os.remove(output_file)  # Remove the unzipped file
        log.info(f"Successfully gzipped {output_file}")

        return Path(f"{output_file}.gz")

    except subprocess.CalledProcessError as e:
        log.exception(f"Error running seqtk on {fastq_file}: {e}")
        raise


def main(
    r1: Path = typer.Argument(
        ..., help="Path to R1 FASTQ.gz file", exists=True, dir_okay=False, readable=True
    ),
    r2: Path = typer.Argument(
        ..., help="Path to R2 FASTQ.gz file", exists=True, dir_okay=False, readable=True
    ),
    threshold: int = typer.Option(120_000_000, help="Read count threshold", min=101),
    seed: int = typer.Option(11, help="Random seed for seqtk"),
    output_prefix: str = typer.Option(
        "subsampled", help="Prefix for the sub-sampled output files"
    ),
    output_dir: Path = typer.Option(Path.cwd(), help="Directory to save output files"),
) -> None:
    """Main function to process FASTQ files."""
    log.info("Starting the FASTQ subsampling process.")

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    r1_count = count_reads(r1)
    log.info(f"Number of reads in R1: {r1_count}")

    if r1_count > threshold:
        proportion = threshold / r1_count
        log.info(f"Proportion to sample: {proportion:.6f}")

        # Run seqtk on both R1 and R2
        r1_output = run_seqtk(r1, proportion, seed, output_prefix, output_dir)
        r2_output = run_seqtk(r2, proportion, seed, output_prefix, output_dir)

        log.info(f"Sub-sampled FASTQ files generated: {r1_output} and {r2_output}")
    else:
        log.info(
            "R1 has less than or equal to the threshold of reads. No subsampling needed."
        )

        # Copy and rename the files
        r1_output = output_dir / f"{output_prefix}_{r1.name}"
        r2_output = output_dir / f"{output_prefix}_{r2.name}"

        try:
            log.info(f"Copying {r1} to {r1_output}...")
            subprocess.run(["cp", str(r1), str(r1_output)], check=True)
            log.info(f"Copying {r2} to {r2_output}...")
            subprocess.run(["cp", str(r2), str(r2_output)], check=True)
            log.info(f"Files copied and renamed to {r1_output} and {r2_output}")
        except subprocess.CalledProcessError as e:
            log.exception(f"Error copying files: {e}")
            raise


if __name__ == "__main__":
    typer.run(main)
