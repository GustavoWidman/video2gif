#!/bin/bash

if [ ! -d "env" ]; then
	python3 -m venv env
	source env/bin/activate
	pip3 install -r requirements.txt
fi

python_version=$(python3 --version)
if [[ $python_version != *"3.11.9"* ]]; then
	echo "Warning: Python version is not 3.11.9. This script was tested with Python 3.11.9 and may not work with other versions."
fi

pip3 install nuitka

python3 -m nuitka --onefile src/main.py --static-libpython=yes --output-filename=video2gif --remove-output --deployment