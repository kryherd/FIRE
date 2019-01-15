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
args=parser.parse_args()

cfg = "s%sallfMRI.1D" % (args.subj)
ngram = "s%sallfMRI_NGRAM.1D" % (args.subj)

def demean_timing(data):
	df = pd.read_table(data, header = None, names = ['timing'])
	elem = pd.DataFrame(df['timing'].str.replace('*', ':').astype('str').str.split(':').tolist(), columns="onset surprisal duration".split())
	s = elem['surprisal'].values.astype(float)
	mn_s = np.mean(s)
	elem['surprisal'] = pd.to_numeric(elem['surprisal'])
	elem['sup_dem'] = elem['surprisal'] - mn_s
	elem['timing'] = elem['onset'].astype(str) + "*" + elem['sup_dem'].astype(str) + ":" + elem['duration'].astype(str)
	write = elem['timing']
	return write;
	
timings = demean_timing(cfg)
timings.to_csv('s' + args.subj + "allfMRI_demeaned.1D", index=False, header=False, sep='\t')

timings = demean_timing(ngram)
timings.to_csv('s' + args.subj + "allfMRI_demeaned_NGRAM.1D", index=False, header=False, sep='\t')
