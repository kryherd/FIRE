#!/usr/bin/env python
import re
import numpy as np 
import sys
import argparse
import pandas as pd
import numpy as np

# passes the subject number into python as a variable
parser = argparse.ArgumentParser()
parser.add_argument('--subj', action='store', type=str, help="Subject Number")
parser.add_argument('--nt', action='store', type=int, help="number of TRs")
args=parser.parse_args()

onsets = "Onsets_%s.txt" % (args.subj)
surprisal = "WordTimings.txt"
ngram = "WordTimings_NGRAM.txt"
sup = pd.read_table(surprisal)
ng = pd.read_table(ngram)

def create_timing(data):
	df=pd.read_table(data)
	# remove trials where participant was not looking at screen
	df = df.loc[df['CURRENT_FIX_INTEREST_AREA_ID'] != '.']
	# change types
	df['CURRENT_FIX_INTEREST_AREA_ID'] = pd.to_numeric(df['CURRENT_FIX_INTEREST_AREA_ID'])
	# renumber trials
	df['Trial'] = (df['scanrun']-1)*6+df['TRIAL_INDEX']
	# calculate fixation start
	df['FixStart'] = (df['TRIAL_START_TIME'] - df['ScannerPulseTime'] + df['CURRENT_FIX_START'])/1000
	# merge with surprisal values
	df2 = df.merge(sup, 'left', ['Trial', 'CURRENT_FIX_INTEREST_AREA_ID'])
	# drop trials not in a fixation area
	df2 = df2.dropna()
	# change duration to seconds
	df2['FixDur'] = df2['CURRENT_FIX_DURATION']/1000
	# calculate number of seconds to add, based on the scanrun
	df2['add'] = np.nan
	# if it's the first run, add no seconds
	df2.loc[df2.scanrun==1, 'add'] = 0
	# add 1.85*number of TRs in a run*(scanrun-1) to the starting time
	df2.loc[df2.scanrun>1, 'add'] = (df2['scanrun']-1)*(args.nt*1.85)
	# add these together
	df2['Start'] = df2['FixStart'] + df2['add']
	# format as start_time*surprisal_value:duration
	df2['timing'] = df2['Start'].astype(str) + "*" + df2['Surprisal'].astype(str) + ":" + df2['FixDur'].astype(str)
	# select only that column for the timing file
	df_write = df2['timing']
	return df_write;
	
def create_timing_NGRAM(data):
	df=pd.read_table(data)
	# remove trials where participant was not looking at screen
	df = df.loc[df['CURRENT_FIX_INTEREST_AREA_ID'] != '.']
	# change types
	df['CURRENT_FIX_INTEREST_AREA_ID'] = pd.to_numeric(df['CURRENT_FIX_INTEREST_AREA_ID'])
	# renumber trials
	df['Trial'] = (df['scanrun']-1)*6+df['TRIAL_INDEX']
	# calculate fixation start
	df['FixStart'] = (df['TRIAL_START_TIME'] - df['ScannerPulseTime'] + df['CURRENT_FIX_START'])/1000
	df2 = df.merge(ng, 'left', ['Trial', 'CURRENT_FIX_INTEREST_AREA_ID'])
	df2 = df2.dropna()
	df2['FixDur'] = df2['CURRENT_FIX_DURATION']/1000
	df2['add'] = np.nan
	df2.loc[df2.scanrun==1, 'add'] = 0
	df2.loc[df2.scanrun>1, 'add'] = (df2['scanrun']-1)*(args.nt*1.85)
	df2['Start'] = df2['FixStart'] + df2['add']
	df2['timing'] = df2['Start'].astype(str) + "*" + df2['Surprisal'].astype(str) + ":" + df2['FixDur'].astype(str)
	df_write = df2['timing']
	return df_write;
	
timings = create_timing(onsets)
timings.to_csv('s' + args.subj + "allfMRI.1D", index=False, header=False, sep='\t')

timings = create_timing_NGRAM(onsets)
timings.to_csv('s' + args.subj + "allfMRI_NGRAM.1D", index=False, header=False, sep='\t')