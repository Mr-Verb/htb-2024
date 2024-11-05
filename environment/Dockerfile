# This image is used for the coding/dev environment for the csc

# Builder Images
FROM vanhauser/hydra:latest AS hydra
FROM ghcr.io/oj/gobuster:latest AS gobuster

# Base image
FROM ubuntu:24.04

# Install using root user
USER 0

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV BIN_DIR=/usr/local/bin
ENV WORDLIST_DIR=/htbcsc/wordlists

# Build Args not available in image
ARG USER=htbcsc
ARG UID=2024

# Set working directory
WORKDIR /htbcsc

COPY --from=hydra /usr/local/bin/hydra $BIN_DIR/
COPY --from=hydra /usr/local/bin/pw-inspector $BIN_DIR/
COPY --from=gobuster /app/gobuster $BIN_DIR/

# Init update and upgrade && install packages
RUN \
    apt update && \
    apt upgrade -y && \
    apt install -y \
        apt-utils \
        software-properties-common \
        curl \
        tar \
        hashcat \
        build-essential \
        john \
        nmap \
        snapd \
        wget

# # Install Snap pacakges
# RUN \
#     snap install autopsy

# Install Python3.12
RUN \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && apt install -y \
        python3.12 \
        python3-venv \
        pip

# Create non-root user
RUN \
    useradd -ms /bin/bash $USER -u $UID && \
    chown -R $USER /htbcsc

# Download and install ffuf
RUN \
    curl -s -L https://github.com/ffuf/ffuf/releases/download/v2.1.0/ffuf_2.1.0_linux_amd64.tar.gz | tar xvz -C /tmp && \
    mv /tmp/ffuf $BIN_DIR/

# Download Wordlists
RUN \
    mkdir -p $WORDLIST_DIR && cd $WORDLIST_DIR && wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# Set non-root user
USER $UID
