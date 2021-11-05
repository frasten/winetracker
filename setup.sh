#!/bin/sh

sudo apt install python3-pip

pip3 install virtualenv
python3 -m venv env

source env/bin/activate

python -m pip install requests
python -m pip install beautifulsoup4
