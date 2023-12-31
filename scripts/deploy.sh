#!/bin/bash

# Required package install
echo "apt-get update execution"
sudo apt-get update 

# lion 유저를 sudo 그룹에 추가
sudo usermod -aG sudo lion
echo "lion has been aded to sudo group"

echo "apt-get install curl execution"
sudo apt-get install -y curl

echo "apt-get install docker execution"
sudo apt-get install -y docker.io docker-compose

# git clone
echo "Start to clone"
git clone https://github.com/IvaninITworld/Dev_django_app.git dev_django_app
cd dev_django_app

# venv 설치
echo "Start to install venv"
sudo apt-get update
sudo apt install -y python3.8-venv

# venv 구성
echo "Start to make venv"
python3 -m venv venv

# 가상환경 작동
echo "Start to activate venv"
source venv/bin/activate

# pip install
echo "start to install requirements"
pip install -r requirements.txt

# # runserver 기존작업에 제외 -> nginx로 서버를 띄울거니까
# echo "Start to runserver"
# cd lion_app
# python3 manage.py runserver 0.0.0.0:8000

# execute Dockerfile
sudo docker build

# docker run -p 8000:8000 -d -v ~/.aws:/root/.aws:ro --env-file .envs/prod/django --env-file .envs/prod/db --env-file .envs/prod/server --name lion-app-dc likelion-cr-mh.kr.ncr.ntruss.com/lion-app:latest ./lion_app/scripts/start

