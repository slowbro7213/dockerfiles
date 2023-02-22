FROM python:3.7.16-bullseye

LABEL maintainer "python crontab"

ARG CRON_PATH=/etc/cron.d
ARG CRON_JOB=${CRON_PATH}/test-job.sh

# packages
RUN apt update -y && apt upgrade -y \
    && apt install -y --no-install-recommends \
        cron \
        tzdata \
        vim \
        software-properties-common \
    && ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# example sync time with host
# docker run ... \
#     -v /etc/localtime:/etc/localtime:ro
#     ...

# requirements
RUN python -m pip install numpy==1.19.5 \
    && python -m pip install pandas==1.1.5 \
    && python -m pip install pyyaml \
    && python -m pip install elasticsearch==8.6.0

# cron job script
RUN mkdir -p ${CRON_PATH} \
    && touch ${CRON_JOB} \
    && echo "#!/bin/sh" >> ${CRON_JOB} \
    && echo "" >> ${CRON_JOB} \
    && echo "echo \$(date \"+%Y%m%d%H%M%S\") >> ~/cron-date.out" >> ${CRON_JOB} \
    && chmod +x ${CRON_JOB}

# crontab
RUN echo "* * * * * $(whoami) ${CRON_JOB}" >> /etc/crontab

# flag "-f" is required (foreground execution).
CMD ["cron", "-f"]
