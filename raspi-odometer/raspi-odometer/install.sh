#!/bin/bash

echo "Installing Odometer Project..."

# update system
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git i2c-tools

# create folder
cd /home/pi
git clone https://github.com/YOURNAME/raspi-odometer.git
cd raspi-odometer

# create venv
python3 -m venv venv
source venv/bin/activate

# install python packages
pip install --upgrade pip
pip install -r requirements.txt

# enable i2c
sudo raspi-config nonint do_i2c 0

# install service
sudo bash service.sh

echo "Installation complete!"