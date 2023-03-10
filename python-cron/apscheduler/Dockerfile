FROM ubuntu:18.04

LABEL maintainer "Python Daemon"

ENV DEBIAN_FRONTEND noninteractive
ENV PROJECT_HOME=/python-project

# install python base
RUN apt update -y && apt upgrade -y \
    && apt install -y --no-install-recommends \
        vim \
        software-properties-common \
        tzdata \
    && apt-get install -y --no-install-recommends python3-pip \
    && echo "alias python=python3" >> ~/.bashrc \
    && ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
    && echo "Asia/Seoul" > /etc/timezone
    
# python package requirements
RUN python3 -m pip install python-dateutil \
    && python3 -m pip install apscheduler \
    && python3 -m pip install pyyaml

# WORKDIR (project home)
RUN mkdir ${PROJECT_HOME} \
    && mkdir -p ${PROJECT_HOME}/logs \
    && mkdir -p ${PROJECT_HOME}/conf \
    && mkdir -p ${PROJECT_HOME}/src \
    && mkdir -p ${PROJECT_HOME}/sbin
COPY main.py ${PROJECT_HOME}
COPY src/. ${PROJECT_HOME}/src
COPY sbin/. ${PROJECT_HOME}/sbin

WORKDIR ${PROJECT_HOME}
CMD [ "/bin/bash", "./sbin/start-daemon.sh" ]
