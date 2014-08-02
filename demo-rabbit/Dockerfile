# Dockerizing RabbitMQ: Dockerfile for building RabbitMQ images
# Based on ubuntu:14.04, installs RabbitMQ following the instructions from:
# http://www.rabbitmq.com/install-debian.html
FROM       ubuntu:14.04
MAINTAINER Radik Fattakhov <radikft@gmail.com>
RUN        apt-get update
RUN        apt-get install -y -q wget
RUN        echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee -a /etc/apt/sources.list
RUN        wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
RUN        apt-key add rabbitmq-signing-key-public.asc 
RUN        apt-get update
RUN        apt-get install -y -q rabbitmq-server
RUN        rabbitmq-plugins enable rabbitmq_management
EXPOSE     5672 15672
ENTRYPOINT ["rabbitmq-server"]
