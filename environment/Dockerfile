# This image is used for the coding/dev environment for the csc

# Builder Images
FROM vanhauser/hydra:latest AS hydra
FROM ghcr.io/oj/gobuster:latest AS gobuster

# Base image
FROM kalilinux/kali-rolling:latest

# Install using root user
USER 0

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV BIN_DIR=/usr/local/bin
ENV WORDLIST_DIR=/wordlists

# Build Args not available in image
ARG USER=htbcsc
ARG UID=2024

# Set working directory
WORKDIR /htbcsc

COPY --from=hydra /usr/local/bin/hydra $BIN_DIR/
COPY --from=hydra /usr/local/bin/pw-inspector $BIN_DIR/
COPY --from=gobuster /app/gobuster $BIN_DIR/

RUN \
    apt update && \
    apt -y install \
        kali-linux-headless \
        seclists

# Init update and upgrade && install packages
RUN \
    apt update && \
    apt upgrade -y && \
    apt install -y \
        apt-utils \
        curl \
        tar \
        hashcat \
        build-essential \
        john \
        snapd \
        wget

# Install Python3.12 and name-that-hash
RUN \
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

RUN \
    chown -R $UID /usr/lib/nmap/nmap

RUN \
    apt-get update && \
    apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade pwntools

# Set non-root user
USER $UID
