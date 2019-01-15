foreach sub (`cat demean_subj.txt`)
	echo $sub
	cd /Volumes/EEG/FIRE_fMRI/Data/${sub}/timings
	cp /Volumes/EEG/FIRE_fMRI/Data/Scripts/demean_timings.py ./
	python demean_timings.py --subj ${sub}
	cp /Volumes/EEG/FIRE_fMRI/Data/${sub}/timings/*_demeaned* /Volumes/EEG/FIRE_fMRI/Data/${sub}/subject_results/group.FIRE/subj.s${sub}/s${sub}.results/stimuli 
	cp /Volumes/EEG/FIRE_fMRI/Data/Scripts/doDecon_cfg_demeaned.sh /Volumes/EEG/FIRE_fMRI/Data/${sub}/subject_results/group.FIRE/subj.s${sub}/s${sub}.results/
	cp /Volumes/EEG/FIRE_fMRI/Data/Scripts/doDecon_ngram_demeaned.sh /Volumes/EEG/FIRE_fMRI/Data/${sub}/subject_results/group.FIRE/subj.s${sub}/s${sub}.results/
	cd /Volumes/EEG/FIRE_fMRI/Data/${sub}/subject_results/group.FIRE/subj.s${sub}/s${sub}.results/
	tcsh doDecon_cfg_demeaned.sh s${sub}
	tcsh doDecon_ngram_demeaned.sh s${sub}
end
	