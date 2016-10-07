###=========================================================================
### File: Dockerfile
###
### Author(s):
###   - Enrique Fernandez <efcasado@gmail.com>
###=========================================================================
FROM phusion/baseimage:0.9.19

# Install CollectD
RUN apt-get update     && \
    apt-get install -y    \
    	    collectd   && \
    apt-get clean      && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install CollectD's RabbitMQ plugin
RUN apt-get update                 && \
    apt-get install -y                \
    	    python-setuptools      && \
    apt-get clean                  && \
    easy_install collectd-rabbitmq && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Start CollectD
CMD [ "collectd", "-f" ]
