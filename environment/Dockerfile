# This image is used for the coding/dev environment for the csc

# Base image
FROM ubuntu:24.04

# Install using root user
USER 0

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV BIN_DIR=/usr/local/bin

# Build Args not available in image
ARG USER=htbcsc
ARG UID=2024

# Set working directory
WORKDIR /htbcsc

# Init update and upgrade
RUN \
    apt update && apt upgrade -y

# Install packages
RUN \
    apt install -y \
        apt-utils \
        software-properties-common \
        curl \
        tar 

# Install Python3.12
RUN \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && apt install -y \
        python3.12

# Create non-root user
RUN \
    useradd -ms /bin/bash $USER -u $UID && \
    chown -R $USER /htbcsc

# Download and install ffuf
RUN \
    curl -s -L https://github.com/ffuf/ffuf/releases/download/v2.1.0/ffuf_2.1.0_linux_amd64.tar.gz | tar xvz -C /tmp && \
    mv /tmp/ffuf $BIN_DIR/

# Set non-root user
USER $UID
