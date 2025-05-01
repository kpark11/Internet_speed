#!/bin/bash


# Change to the directory containing the Python script
cd /mnt/c/Users/brian/OneDrive\ -\ University\ of\ Tennessee/Desktop/Research/Python\ program/Internet_Speed

# Get into the virtual environment
source env/bin/activate

# Run the Python script
nohup python3 check_internet_speed.py > /dev/null 2>&1 & 
nohup python3 livePlot.py > /dev/null 2>&1 &

