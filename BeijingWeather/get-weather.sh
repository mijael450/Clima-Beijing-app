#!/bin/bash

python_path="/home/mijael/miniforge3/envs/iccd332/bin/python3"
script_path="/home/mijael/CityWeather/Proyecto-final/main.py"
log_file="/home/mijael/CityWeather/Proyecto-final/output.log"
$python_path $script_path >> $log_file 2>&1
