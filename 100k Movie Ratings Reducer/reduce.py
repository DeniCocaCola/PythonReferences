#!/usr/bin/python3.7
import sys
import re
import csv
'''reduce.py'''

def reducer():
	reduceFile = open('reducedList.txt', 'w', errors='ignore')
	current_count = 1
	previous_line = '00 {0} 0 0' #
	readData = (sys.stdin)
	dataRegex = re.compile(r'(\d+)(\s)([{])(\d)([}])(\s)(\d)') #mod - movieID, {rating}, map
	for line in readData:
		mod = dataRegex.search(str(line))
		mop = dataRegex.search(str(previous_line))
		if((mod.group(1) == mop.group(1)) and (mod.group(4) == mop.group(4))): #if line movieID equals prev movieID and line rating equals prev rating
			previous_line = line
			current_count += 1
		else:
			if(mop.group(1) == '00'): #prevents default value from showing up in sys.stdin or reduced list
				previous_line = line
				current_count = 1
			else:
				reduceFile.write(mop.group(1) + ' | ' + mop.group(4) + ' | ' + str(current_count) + '\n') # movieID | rating | count
				print(mop.group(1) + ' | ' + mop.group(4) + ' | ' + str(current_count))
				previous_line = line
				current_count = 1
			
reducer()
