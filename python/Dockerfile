FROM  ubuntu:xenial

WORKDIR "/application"

ENV TERM=linux


# Install selected extensions and other stuff
RUN useradd  wdata ||true


RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv python-all python-all-dev python2.7 python2.7-dev python3 python3-pip python3-dev python3.5 python3.5-dev python-pip-whl && \
    apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* 
ENV LANG en_US.utf8
ENV LC_ALL C
CMD ["bash"]