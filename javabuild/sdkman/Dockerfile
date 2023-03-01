FROM ubuntu:22.04

LABEL maintainer="slowbro"
LABEL description="java build with sdkman, ignore SSL certificate"

ENV WORKSPACE=/workspace
ENV SDKMAN_DIR=/usr/local/sdkman
ARG INSTALL_SH=/usr/local/sdkman-install.sh

RUN apt update -y && apt upgrade -y \
    && apt-get install -y --no-install-recommends \
        zip unzip curl \
    && curl -o ${INSTALL_SH} -s -k 'https://get.sdkman.io' \
    && sed -i 's/curl -/curl -k -/' ${INSTALL_SH} \
    && chmod +x ${INSTALL_SH} \
    && /bin/bash ${INSTALL_SH}
