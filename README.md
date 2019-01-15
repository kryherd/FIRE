# FIRE

Information for processing FIRE data.

Click [here](./FIRE_preprocessing.md) for information on how to pre-process FIRE data.

## Files included in this repository

### Scripts

* `extractScannerPulseTime.sh` - extracts time when the scanner started for each run.
	* Input: `XXXX_Y_Session_data.txt` where `XXXX` = subject and `Y` = run
	* Output: `scannerStartTimes.txt`, which has all of the scanner start times for a given subject.
* `create_timings.py` - creates timing files
	* Input: fixation report from DataViewer (including `ScannerPulseTime` variable)
	* Output: `sXXXX_allfMRI.1D` (AFNI-ready timing files for CFG analysis) and `sXXXX_allfMRI_NGRAM.1D` (AFNI-ready timing files for NGRAM analysis)
* `create_timings_missTR.py` - same as `create_timings.py`, except for the subjects who have 1 fewer TR in their first run than in the remaining 4 runs.
* `make_timings.sh` - file to batch create timing files
* `make_timings_missTR.sh` - file to batch create timing files for subjects where run 1 has 1 fewer TR.
* `make_NIFTI.sh` - turns raw DICOM files into NIFTI files for fMRI analysis, and puts them in BIDS-formatted directories.
* `doDecon_*.sh` - files that re-run `3dDeconvolve` using different timing files (e.g., NGRAM, demeaned CFG, demeaned NGRAM).
* `mult_NGRAM.sh` and `mult_demeaned.sh` - file to batch run `doDecon_` files.
* `WordTimings_*.txt` - files with surprisal values for each interest area in each trial.

### Sample Data

* `_SessionData.txt` files to see how `extractScannerPulseTime.sh` works
* `scannerStartTimes.txt` file to see what the output from above looks like.

### Experiment

* `ScannerReadingAug9GK.ebz` - zipped-up version of the ExperimentBuilder task built by Kayleigh and Gitte. Finished product was completed on 8/9/2017 and used on subjects between 9/29/2017 and 8/21/2018.