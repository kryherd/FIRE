#!/bin/tcsh

foreach run (1 2 3 4 5)
	cat *_{$run}_Session_Data.txt | grep KEYBOARD_SCANNER | awk -v myRun=$run '{print myRun, $2}' >> scannerStartTimes.txt
end
