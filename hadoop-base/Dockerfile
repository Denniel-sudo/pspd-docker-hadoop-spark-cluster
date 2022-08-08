FROM ubuntu:latest
LABEL key="lewuathe"

USER root

# install dev tools
RUN apt-get update 
RUN apt-get install -y curl tar sudo openssh-server openssh-client rsync \ 
    python3 python3-pip python3-dev make \ 
    && python3 -m pip install pyspark

# passwordless ssh
RUN rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key /root/.ssh/id_rsa
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

# java
RUN sudo apt install -y openjdk-8-jdk
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64


# Atualizar o PATH
ENV PATH $PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Installation and configuration Hadoop

ENV HADOOP_VERSION 3.3.0
ENV HADOOP_MINOR_VERSION 3
ADD hadoop-${HADOOP_VERSION}.tar.gz /usr/local/
WORKDIR /usr/local
RUN ln -s /usr/local/hadoop-${HADOOP_VERSION} /usr/local/hadoop

ENV HADOOP_HOME /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_YARN_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV YARN_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV HADOOP_LOG_DIR /var/log/hadoop

RUN mkdir /var/log/hadoop

RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=$JAVA_HOME\nexport H=${HADOOP_HOME}\nexport HADOOP_HOME=${HADOOP_HOME}\n:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export HADOOP_CONF_DIR=${HADOOP_CONF_DIR}:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh
#RUN . $HADOOP_HOME/etc/hadoop/hadoop-env.sh

RUN mkdir $HADOOP_HOME/input
RUN cp $HADOOP_HOME/etc/hadoop/*.xml $HADOOP_HOME/input

ADD core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
ADD hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
ADD mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
ADD yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
ADD log4j.properties $HADOOP_HOME/etc/hadoop/log4j.properties

RUN $HADOOP_HOME/bin/hdfs namenode -format

# Config SPARK
ENV SPARK_VERSION 3.3.0
ENV SPARK_DIR /usr/local/spark-${SPARK_VERSION}
ENV SPARK_HOME /usr/local/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MINOR_VERSION}
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"

RUN wget \
    "http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MINOR_VERSION}.tgz" \
    && mkdir ${SPARK_DIR} \
    && tar zvxf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MINOR_VERSION}.tgz -C ${SPARK_DIR} \
    && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MINOR_VERSION}.tgz \
    && chown -R root:root ${SPARK_DIR}

# Configuracoes do pyspark
ENV PYSPARK_PYTHON python3
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:/usr/bin/python3
ENV PATH $PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin:$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip

# Config SSH
ADD ssh_config /root/.ssh/config
RUN chmod 600 /root/.ssh/config
RUN chown root:root /root/.ssh/config

# workingaround docker.io build error
RUN ls -la ${HADOOP_HOME}/etc/hadoop/*-env.sh
RUN chmod +x ${HADOOP_HOME}/etc/hadoop/*-env.sh
RUN ls -la ${HADOOP_HOME}/etc/hadoop/*-env.sh

RUN echo "Port 2122" >> /etc/ssh/sshd_config

RUN service ssh start

# Hdfs ports
EXPOSE 9000 50010 50020 50070 50075 50090
# See https://issues.apache.org/jira/browse/HDFS-9427
EXPOSE 9871 9870 9820 9869 9868 9867 9866 9865 9864
# Mapred ports
EXPOSE 19888
#Yarn ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088 8188
#Other ports
EXPOSE 49707 2122
