#!/bin/bash

set -e

# Read configuration from file
config_file="config.ini"

# Read values from the configuration file
player_file=$(awk -F "=" '/player_file/ {print $2}' "$config_file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
p_dir=$(awk -F "=" '/output_directory/ {print $2}' "$config_file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
p_name=$(awk -F "=" '/player_name/ {print $2}' "$config_file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

train_frac=90
val_frac=10

split_dir=$p_dir/split

mkdir -p ${p_dir}
mkdir -p ${split_dir}

echo "${p_name} to ${p_dir}"

python split_by_player.py
python pgn_fractional_split.py

for c in "white" "black"; do
  cd $p_dir
  mkdir -p pgns
  
  for s in "train" "validate"; do
    mkdir -p $s
    mkdir -p $s/$c
    
    # using tool from:
    # https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/
    bzcat $split_dir/${s}_${c}.pgn.bz2 | pgn-extract -7 -C -N -#1000
    
    cat *.pgn > pgns/${s}_${c}.pgn
    rm -v *.pgn
    
    # using tool from:
    # https://github.com/DanielUranga/trainingdata-tool
    cd ${s}/${c}
    trainingdata-tool -v ../../pgns/${s}_${c}.pgn
    
    cd ../../
  done
  
  cd -
done