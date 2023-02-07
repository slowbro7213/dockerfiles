FROM python:3.7.16-bullseye

LABEL maintainer "python crontab"

ARG CRON_PATH=/etc/cron.d
ARG CRON_JOB=${CRON_PATH}/test-job.sh

# install packages
RUN apt update -y \
    && apt install -y --no-install-recommends \
        cron \
        vim \
        software-properties-common 

# requirements
RUN python3 -m pip install numpy==1.19.5 \
    && python3 -m pip install pandas==1.1.5 \
    && python3 -m pip install pyyaml \
    && python3 -m pip install elasticsearch==8.6.0

# cron job script
RUN mkdir -p ${CRON_PATH} \
    && touch ${CRON_JOB} \
    && echo "#!/bin/sh" >> ${CRON_JOB} \
    && echo "" >> ${CRON_JOB} \
    && echo "echo \$(date \"+%Y%m%d%H%M%S\") >> ~/cron-date.out" >> ${CRON_JOB} \
    && chmod +x ${CRON_JOB}

# crontab
RUN echo "* * * * * $(whoami) ${CRON_JOB}" >> /etc/crontab

# flag "-f" is required.
CMD ["cron", "-f"]
 
