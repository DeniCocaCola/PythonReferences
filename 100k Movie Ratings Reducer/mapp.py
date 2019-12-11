#!/usr/bin/python3.7
import sys
import re
import csv
'''mapp.py'''
#cat u.data | python3 mapp.py 1 | sort -k1,1 -n | python3 reduce.py | ./mapp.py 2

def mapper():
	logFile = open('logFile.txt', 'w', errors='ignore')
	movie_ids = {}
	movie_ratings = {}
	readData = csv.reader(sys.stdin)
	for row in readData:
		rowRegex = re.compile(r'(\d+)(\\\w)(\d+)(\\\w)(\d)(\\\w)(\d+)')
		mod = rowRegex.search(str(row))
		movie_ids = {int(mod.group(3))}
		movie_ratings = {int(mod.group(5))}
		for movie_id in movie_ids:
			print(movie_id, movie_ratings, 1)

############
def finalMapper():
	finalFile = open('finalFile.txt', 'w')
	readData = (sys.stdin)
	itemFile = putInArray()
	for line in readData:
		reducedRegex = re.compile(r'(\d*)(\s)([|])(\s)(\d+)(\s)([|])(\s)(\d+)') #reducedList regex
		mvList = reducedRegex.search(str(line)) #reducedList

		titleRegex = re.compile(r'(\d*)([|])(\w+.*?[(]?\d+[)]?)') #movie titles
		mvTitles = titleRegex.search(str(itemFile[int(mvList.group(1)) - 1]))#movie titles

		i = 0
		while i < int(mvList.group(9)):
			finalFile.write(mvList.group(1) + ' | ' + mvList.group(5) + ' | ' + mvTitles.group(3) + '\n')
			i += 1

############
def putInArray():
	itemFile = open('u.item', 'rb')
	itemArray = []
	for line in itemFile:
		itemArray.append(line)
	print('items added to itemArray')
	return itemArray

try:
	if(sys.argv[1] == '1'):
		mapper()
	elif(sys.argv[1] == '2'):
		finalMapper()
	elif(sys.argv[1] == '3'):
		putInArray()
	else:
		print('Invalid argument for mapp.py. Use 1 or 2')
except Exception as e:
	print(e)
