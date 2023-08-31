FROM ubuntu:22.04
LABEL maintainer "Neouly"


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
RUN chmod +x ${SDKMAN_DIR}"/bin/sdkman-init.sh"


# Install SDKs (must be source with sdkman-init.sh)
RUN source ${SDKMAN_DIR}/bin/sdkman-init.sh && sdk install java 11.0.19-tem && sdk install scala 2.12.17 && sdk install sbt 1.9.4
SHELL ["/bin/sh", "-c"]


# SDK Home
ENV JAVA_HOME=${SDKMAN_DIR}"/candidates/java/current"
ENV SCALA_HOME=${SDKMAN_DIR}"/candidates/scala/current"
ENV SBT_HOME=${SDKMAN_DIR}"/candidates/sbt/current"
ENV PATH=${PATH}:${JAVA_HOME}/bin:${SCALA_HOME}/bin:${SBT_HOME}/bin

RUN set -o errexit -o nounset \
    && echo "Check installed SDK(openjdk, scala, sbt)" \
    && which java && which javac && java -version && scala -version && sbt -version


# Workspace
RUN mkdir -p /workspace/my-project
WORKDIR /workspace/my-project
RUN sbt compile
