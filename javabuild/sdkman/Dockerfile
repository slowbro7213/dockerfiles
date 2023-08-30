FROM ubuntu:22.04
LABEL maintainer="slowbro"


# Base
USER root
RUN apt update -y \
    && apt install -y --no-install-recommends \
        vim \
        curl zip unzip ca-certificates \
        tzdata \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
    && echo "Asia/Seoul" > /etc/timezone


# Install SDKMAN
ENV SDKMAN_DIR="/usr/local/sdkman"
SHELL ["/bin/bash", "-c"]
RUN curl -s "https://get.sdkman.io" | bash
RUN chmod +x ${SDKMAN_DIR}"/bin/sdkman-init.sh" \
    && source ${SDKMAN_DIR}"/bin/sdkman-init.sh"
SHELL ["/bin/sh", "-c"]
