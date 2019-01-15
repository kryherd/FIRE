#!/bin/bash
# takes raw DICOM data, converts to NIFTI, and stores in the BIDS data structure

cd ..
pwd
for sub in $(cat maken_subjList.txt)
do
	echo $sub
	pwd
	for subdir in "anat" "fire"
	do
	 #-p makes all the parents files as well
		mkdir -p ./${sub}/${subdir}
	done
	for run in 6 7 8 9 10 11
	do
		cd ./$sub/RawData/$run/
		dcm2niix *.dcm
		cd ../../..
		pwd
	done
	pwd
	cp ./$sub/RawData/6/*.nii ./$sub/anat/s${sub}_run-01_T1w.nii
	cp ./$sub/RawData/7/7*.nii ./$sub/fire/s${sub}_run-01_bold.nii
	cp ./$sub/RawData/8/8*.nii ./$sub/fire/s${sub}_run-02_bold.nii
	cp ./$sub/RawData/9/9*.nii ./$sub/fire/s${sub}_run-03_bold.nii
	cp ./$sub/RawData/10/10*.nii ./$sub/fire/s${sub}_run-04_bold.nii
	cp ./$sub/RawData/11/11*.nii ./$sub/fire/s${sub}_run-05_bold.nii
done
