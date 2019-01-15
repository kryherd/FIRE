foreach sub (`cat NGRAM_subs.txt`)
	echo $sub
	cd /Volumes/EEG/FIRE_fMRI/Data/${sub}/subject_results/group.FIRE/subj.s${sub}/s${sub}.results/
	cp /Volumes/EEG/FIRE_fMRI/Data/${sub}/timings/s${sub}allfMRI_NGRAM.1D /Volumes/EEG/FIRE_fMRI/Data/${sub}/subject_results/group.FIRE/subj.s${sub}/s${sub}.results/stimuli 
	cp /Volumes/EEG/FIRE_fMRI/Data/Scripts/doDecon_NGRAM.sh /Volumes/EEG/FIRE_fMRI/Data/${sub}/subject_results/group.FIRE/subj.s${sub}/s${sub}.results/
	tcsh doDecon_NGRAM.sh s${sub}
end
	