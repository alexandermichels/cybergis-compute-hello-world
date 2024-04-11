#!/bin/bash

mkdir $result_folder/demo_quick_start_$SLURM_PROCID
chmod 755 $result_folder/demo_quick_start_$SLURM_PROCID
wget -P $result_folder https://raw.githubusercontent.com/alexandermichels/alexandermichels.github.io/master/assets/html/maps/CBSA.html
python main.py
