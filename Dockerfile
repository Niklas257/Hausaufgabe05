FROM ubuntu:22.04

RUN apt-get update 
# Install essential Ubuntu packages
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip

# Install essential Python packages
RUN python3 -m pip --no-cache-dir install \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    pytest
