#!/bin/bash
echo "Installing Python..."
sudo apt install python3 -y
echo "Installing Pip..."
sudo apt install python3-pip -y
echo "Starting Cloud Migration Demo..."
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Starting Flask application..."
python3 app.py
