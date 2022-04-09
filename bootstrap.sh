\#!/bin/sh

#Installing Dependencies
sudo apt-get update 
sudo apt-get install python3.7 python3-pip python3.7-dev python3-setuptools virtualenv gcc libffi-dev -y

#Converting pip3 to pip
#sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

#Creating Source Directory
#mkdir muddev
#cd muddev

#Download Source
git clone https://github.com/evennia/evennia.git
#chown -R vagrant:vagrant evennia
#Should use virtualenv in production here
#virtualenv evenv
#source evenv/bin/activate

#Install Source
pip3 install --upgrade pip 
#pip install -e evennia
#pip3 install -e evennia
export PATH="/home/vagrant/.local/bin:$PATH"
pip3 install -e evennia

#Initialize Evennia Instance
#evennia --init mygame

#Load DB & Start Server
#cd mygame
#evennia migrate

sudo timedatectl set-timezone America/Montreal
