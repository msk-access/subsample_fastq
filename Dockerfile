# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    gcc \
    zlib1g-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install seqtk
RUN git clone https://github.com/lh3/seqtk.git && \
    cd seqtk && \
    make && \
    cp seqtk /usr/local/bin/ && \
    cd .. && \
    rm -rf seqtk

# Copy the rest of the application code into the container
COPY . .

# Make the script executable
RUN chmod +x subsample_fastq.py

# Command to run the script
ENTRYPOINT ["python", "subsample_fastq.py"]