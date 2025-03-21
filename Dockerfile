# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install typer rich

# Install seqtk (ensure you have the correct installation command for your OS)
RUN apt-get update && apt-get install -y seqtk && rm -rf /var/lib/apt/lists/*

# Make the script executable
RUN chmod +x subsample_fastq.py

# Command to run the script
ENTRYPOINT ["python", "subsample_fastq.py"]