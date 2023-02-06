FROM eclipse-temurin:8-jdk-focal

LABEL maintainer "Hadoop Node"

#ENV JAVA_HOME=/opt/java/openjdk
ARG HADOOP_VER=3.3.4
ARG HADOOP_SSH=/home/hdfs/.ssh
ARG HADOOP_ROOT=/opt/hadoop
ENV HADOOP_HOME=${HADOOP_ROOT}/hadoop-${HADOOP_VER}
RUN mkdir -p ${HADOOP_ROOT}

# install packages
RUN apt update \
    && apt install openssh-server sudo -y \
    && apt install vim -y

# user add
RUN useradd hdfs \
    && passwd -d hdfs \
    && usermod -aG sudo hdfs

# setting ssh
RUN mkdir -p ${HADOOP_SSH} \
    && ssh-keygen -t rsa -P '' -f ${HADOOP_SSH}/id_rsa \
    && cat ${HADOOP_SSH}/id_rsa.pub >> ${HADOOP_SSH}/authorized_keys \
    && sed -i 's/^#PasswordAuthentication/PasswordAuthentication/' /etc/ssh/sshd_config \
    && sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config \
    && sed -i 's/^#PubkeyAuthentication/PubkeyAuthentication/' /etc/ssh/sshd_config \
    && sed -i 's/PubkeyAuthentication no/PubkeyAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i '/^#AuthorizedKeysFile.*/d' /etc/ssh/sshd_config \
    && echo "AuthorizedKeysFile ${HADOOP_SSH}/authorized_keys" >> /etc/ssh/sshd_config \
    && touch ${HADOOP_SSH}/known_hosts \
    && chmod 700 ${HADOOP_SSH} \
    && chmod 600 ${HADOOP_SSH}/id_rsa \
    && chmod 600 ${HADOOP_SSH}/id_rsa.pub \
    && chmod 600 ${HADOOP_SSH}/authorized_keys \
    && chmod 600 ${HADOOP_SSH}/known_hosts \
    && service ssh start
EXPOSE 22

# download hadoop
COPY hadoop-${HADOOP_VER}.tar.gz ${HADOOP_ROOT}
RUN test -f ${HADOOP_ROOT}/hadoop-${HADOOP_VER}.tar.gz || wget "https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VER}/hadoop-${HADOOP_VER}.tar.gz" -O ${HADOOP_ROOT}/hadoop-${HADOOP_VER}.tar.gz

WORKDIR ${HADOOP_ROOT}
RUN tar -xzvf ${HADOOP_ROOT}/hadoop-${HADOOP_VER}.tar.gz \
    && rm -rf ${HADOOP_ROOT}/hadoop-${HADOOP_VER}.tar.gz

# setting common etc/hadoop
RUN echo "export JAVA_HOME=${JAVA_HOME}" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export JAVA_OPTS=\"-Dfile.encoding=UTF-8\"" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export CLASSPATH=\".\"" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export HADOOP_HOME=${HADOOP_HOME}" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export HADOOP_NAMENODE_USER=hdfs" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export HADOOP_DATANODE_USER=hdfs" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export HADOOP_SECONDARYNAMENODE_USER=hdfs" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export HADOOP_RESOURCEMANAGER_USER=hdfs" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh \
    && echo "export HADOOP_NODEMANGER_USER=hdfs" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh

# setting Pseudo-Distributed Mode
RUN sed -i '/<configuration>/,/<\/configuration>/{/<configuration>/{n;s/.*/    <property>\n        <name>fs.defaultFS<\/name>\n        <value>hdfs:\/\/localhost:9000<\/value>\n    <\/property>\n&/};}' ${HADOOP_HOME}/etc/hadoop/core-site.xml \
    && sed -i '/<configuration>/,/<\/configuration>/{/<configuration>/{n;s/.*/    <property>\n        <name>dfs.replication<\/name>\n        <value>1<\/value>\n    <\/property>\n&/};}' ${HADOOP_HOME}/etc/hadoop/hdfs-site.xml \
    && sed -i '/<configuration>/,/<\/configuration>/{/<configuration>/{n;s/.*/    <property>\n        <name>mapred.job.tracker<\/name>\n        <value>localhost:9001<\/value>\n    <\/property>\n&/};}' ${HADOOP_HOME}/etc/hadoop/mapred-site.xml

# common 
WORKDIR ${HADOOP_HOME}
RUN chown -R hdfs:hdfs /home/hdfs && chown -R hdfs:hdfs ${HADOOP_ROOT}
USER hdfs
CMD ["sudo", "/usr/sbin/sshd", "-D"]

