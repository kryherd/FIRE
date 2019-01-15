#!/bin/bash
cd ..
IFS=$'\n';
for LINE in $(cat timing_subjList_missTR.txt)
do
	sub=$(echo ${LINE} | awk '{print $1}')
    TR=$(echo ${LINE} | awk '{print $2}')
    echo ${sub}
	cd ./${sub}
	mkdir timings
	cd ./EyelinkData/${sub}_IndivEDFs/Output/
	cp ../../../../Scripts/WordTimings.txt ./
	cp ../../../../Scripts/WordTimings_NGRAM.txt ./
	cp ../../../../Scripts/create_timings_missTR.py ./
	subj=`python create_timings_missTR.py --subj ${sub} --nt ${TR}`
	cp s${sub}all*.1D ../../../timings/
	cd ../../../..
done