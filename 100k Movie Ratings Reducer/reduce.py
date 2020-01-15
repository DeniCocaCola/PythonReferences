#!/usr/bin/python3.7
import sys
import re
import csv
'''reduce.py'''


def reducer():
	reduceFile = open('reducedList.txt', 'w')
	current_count = 1
	previous_line = '00 {0} 0 0' #
	readData = (sys.stdin)
	dataRegex = re.compile(r'''
	(\d+)	# MovieID
	(\s)	#
	([{])	#
	(\d)	# Rating
	([}])	#
	(\s)	#
	(\d)	# Count
	''', re.X)

	for line in readData:
		lineSearch = dataRegex.search(str(line))
		previousSearch = dataRegex.search(str(previous_line))

		if(lineSearch.group(1) == previousSearch.group(1) # If current movieID equals previous movieID..
		and lineSearch.group(4) == previousSearch.group(4)): #  ..and current rating equals previous rating
			previous_line = line
			current_count += 1
		else:
			if(previousSearch.group(1) == '00'): # Prevents default value from showing up in sys.stdin or reduced list
				previous_line = line
				current_count = 1
			else:
				reduceFile.write('{} | {} | {}'.format(
					previousSearch.group(1), previousSearch.group(4), current_count) + '\n')
				print('{} | {} | {}'.format(
					previousSearch.group(1), previousSearch.group(4), current_count))
				previous_line = line
				current_count = 1
			
reducer()
