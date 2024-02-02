FROM jenkins/jenkins:lts
USER root

# Docker 저장소 설정
RUN apt-get update && apt-get install -y apt-transport-https \
       ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Docker CLI 설치
RUN apt-get update && apt-get install -y docker-ce-cli

# Jenkins 사용자로 전환
USER jenkins
