FROM tensorflow/tensorflow:2.6.0rc1-gpu

LABEL compatibility "ubuntu:18.04-tensorflow:2.6.0rc1-cuda:11.2"

ENV DEBIAN_FRONTEND noninteractive

# GPG Public Key Setting
RUN apt-key del 7fa2af80 && apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub

# install python base
RUN apt update -y && apt upgrade -y \
    && apt install -y --no-install-recommends \
        software-properties-common \
        tzdata \
    && python -m pip install --upgrade pip \
    && ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
    && echo "Asia/Seoul" > /etc/timezone

# python package requirements
RUN python -m pip install elasticsearch==7.14.0 \
    && python -m pip install python-dateutil==2.8.1 \
    && python -m pip install apscheduler \
    && python -m pip install PyYAML==5.4.1 \
    && python -m pip install numpy==1.19.5 \
    && python -m pip install pandas==1.1.5 \
    \
    && python -m pip install cupy-cuda102==9.6.0 \
    && python -m pip install cupy-cuda110==9.6.0 \
    && python -m pip install cupy-cuda112==9.6.0 \
    && python -m pip install keras-adamw==1.38 \
    && python -m pip install tensorflow==2.6.0rc1 \
    && python -m pip install Bottleneck==1.3.2 \
    && python -m pip cache purge
