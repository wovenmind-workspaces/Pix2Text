# Use the official Python base image with version 3.7
FROM python:3.11-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    sudo \
    git \
    git-lfs \
    zip \
    unzip \
    htop \
    python3-pip \
    bzip2 \
    libx11-6 \
    build-essential \
    libsndfile-dev \
    software-properties-common \
    curl \
    tree \
    iputils-ping \
    vim \
    jq \
    libatomic1 \
    netcat \
    pciutils \
    wget \
    zsh \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install miniforge
ENV CONDA_DIR /opt/conda
RUN curl -L -o miniforge_installer.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh \
    && chmod +x miniforge_installer.sh \
    && ./miniforge_installer.sh -b -p $CONDA_DIR \
    && rm miniforge_installer.sh

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

# Create conda environment
RUN conda install -n base pytorch cpuonly -c pytorch
