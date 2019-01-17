echo "Subject Run n_TRs" > "TR_list.txt"

for subj in 6063 6020 6046 6049 6032 6006 6038 6051 6014 6003 6043 6028 6009 6018 6011 6059
do
	for run in 1 2 3 4 5
	do
		nt=`3dinfo -nt /Volumes/EEG/FIRE_fMRI/Data/${subj}/fire/s${subj}_run-0${run}_bold.nii`
		echo ${subj} ${run} ${nt} >> "TR_list.txt"
	done
done