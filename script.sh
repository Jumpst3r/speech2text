#!/bin/sh
inputFile=${1}
outfile=${2}

python /input/main.py --inputFile ${inputFile} --outputFolder ${outfile}

