FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update 
RUN apt-get install -y python3 python3-pip python3-venv
RUN apt-get clean

USER jenkins

RUN python3 -m venv /home/jenkins/venv
RUN /home/jenkins/venv/bin/pip install --upgrade pip
RUN /home/jenkins/venv/bin/pip install flask psycopg2-binary
ENV PATH="/home/jenkins/venv/bin:${PATH}"

