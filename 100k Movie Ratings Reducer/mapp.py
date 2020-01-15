#!/usr/bin/python3.7
import sys
import re
import csv
'''mapp.py'''
# cat u.data | ./mapp.py 1 | sort -k1,1 -n | ./reduce.py | ./mapp.py 2


def mapper():
	movie_ids = {}
	movie_ratings = {}
	readData = csv.reader(sys.stdin)

	for row in readData:
		rowRegex = re.compile(r'''
			(\d+)	# movieID
			(\\\w)	#
			(\d+)	# userID
			(\\\w)	#
			(\d)	# rating
			(\\\w)	#
			(\d+)	# timestamp
			''', re.X)
		mod = rowRegex.search(str(row)) # Search the row using the reg. exp.

		movie_ids = {int(mod.group(3))}
		movie_ratings = {int(mod.group(5))}

		for movie_id in movie_ids: # Prints for capture in sort
			print(movie_id, movie_ratings, 1)


def finalMapper():
	finalFile = open('finalFile.txt', 'w') # File with the results
	readData = (sys.stdin)
	itemFile = putInArray()

	for line in readData:
		reducedRegex = re.compile(r'''
		(\d*)	# MovieID
		(\s)	# 
		([|])	# Pipeline
		(\s)	# 
		(\d+)	# Rating
		(\s)	# 
		([|])	# Pipeline
		(\s)	# 
		(\d+)	# Rating Occurances
		''', re.X)
		mvList = reducedRegex.search(str(line)) # reducedList

		titleRegex = re.compile(r''' # Regex for movie titles
		(\d*)	# MovieID
		([|])	# Pipeline
		(\w+.*?[(]?\d+[)]?)	# Movie title and year of release
		''', re.X)
		mvTitles = titleRegex.search(str(itemFile[int(mvList.group(1)) - 1])) # Movie titles

		for _i in range(int(mvList.group(9))):
			finalFile.write('{} | {} | {}'.format(
				mvList.group(1), mvList.group(5), mvTitles.group(3)) + '\n')


def putInArray():
	itemFile = open('u.item', 'rb')
	itemArray = []	
	for line in itemFile:
		itemArray.append(line)
	return itemArray


if __name__ == '__main__':
	try:
		if(sys.argv[1] == '1'):
			mapper()
		elif(sys.argv[1] == '2'):
			finalMapper()
		else:
			print('Invalid argument for mapp.py. Use 1 or 2')
	except Exception as e:
		print(e)
