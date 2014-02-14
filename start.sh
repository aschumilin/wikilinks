#!/bin/bash

mkdir -p wikilinks_cleaned
mkdir -p results
python clean1.py &
python clean2.py 

python parse.py
