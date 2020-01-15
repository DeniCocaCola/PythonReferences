#!/usr/bin/python3.7
'''slot machine'''
import random
import sys
import os


def placeBets(coinsDict):
	coinsDict["currentBet"] = input('Place your bet: ')
	if coinsDict["coinTotal"] == 0:
		print('Out of coins. Better luck next time!')
		sys.exit(0)
	elif int(coinsDict["currentBet"]) < 1:
		print('Betting MINIMUM')
		coinsDict["currentBet"] = 1
		determineOutput(coinsDict)
	elif int(coinsDict["currentBet"]) > coinsDict["coinTotal"]:
		print('Betting TOTAL')
		coinsDict["currentBet"] = coinsDict["coinTotal"]
		determineOutput(coinsDict)
	else:
		print('Betting {} coins.'.format(coinsDict["currentBet"]))
		determineOutput(coinsDict)


def determineOutput(coinsDict):
	i = 0
	slotOutput = []
	slotPosition = 0
	winCounter = 0
	for i in range(10):
		slotOutput.append(random.randint(0,7))
	printSlots(slotOutput, coinsDict)
	checkCombinations(slotOutput, coinsDict)


def printSlots(slotOutput, coinsDict):
	slotDisplay = slotOutput
	print('|-----------------|')
	print('|----HOT SLOTS----|')
	print('|-----------------|')
	print('|--**--*****--**--|')
	print('|_{}__|___{}___|__{}_|'.format(slotDisplay[0], slotDisplay[1], slotDisplay[2]))
	print('|_{}__|___{}___|__{}_|'.format(slotDisplay[3], slotDisplay[4], slotDisplay[5]))
	print('|_{}__|___{}___|__{}_|'.format(slotDisplay[6], slotDisplay[7], slotDisplay[8]))
	print('|--**--*****--**--|')
	print('|--{}---------{}--|'.format(str(coinsDict["currentBet"]),str(coinsDict["coinTotal"])))
	print('|_________________|')

	
def checkCombinations(slotOutput, coinsDict):
	coinsDict["winCounter"] = 0
	coinsDict["coinsWon"] = 0
	i = x = 0
	y = 1
	z = 2
	while i < 3: # horizontal wins
		if(slotOutput[x] == slotOutput[y]
		and slotOutput[x] == slotOutput[z] 
		and slotOutput[y] == slotOutput[z]):
			if slotOutput[x] and slotOutput[y] and slotOutput[z] == 7:
				print('DIVINE BONUS! *7-7-7* - ' + str(int(coinsDict["currentBet"]) * 7) + ' coins!')
				payoutCoins(coinsDict, 7)
			elif slotOutput[x] and slotOutput[y] and slotOutput[z] == 6:
				print('DELIGHTFULLY DEVILISH! *6-6-6* - ' + str(int(coinsDict["currentBet"]) * 6) + ' coins!')
				payoutCoins(coinsDict, 6)
			else:
				payoutCoins(coinsDict, 3)
			print('Winning line horiz: ' + str(slotOutput[x]) + '-' + str(slotOutput[y]) + '-' + str(slotOutput[z]))
		i += 1 
		x += 3
		y += 3
		z += 3

	x = 0
	y = 3
	z = 6
	while i < 6: # vertical wins
		if(slotOutput[x] == slotOutput[y] 
		and slotOutput[x] == slotOutput[z] 
		and slotOutput[y] == slotOutput[z]):
			if slotOutput[x] and slotOutput[y] and slotOutput[z] == 7:
				print('DIVINE BONUS! *7-7-7* - ' + str(int(coinsDict["currentBet"]) * 7) + ' coins!')
				payoutCoins(coinsDict, 7)
			elif slotOutput[x] and slotOutput[y] and slotOutput[z] == 6:
				print('DELIGHTFULLY DEVILISH! *6-6-6* - ' + str(int(coinsDict["currentBet"]) * 6) + ' coins!')
				payoutCoins(coinsDict, 6)
			else:
				payoutCoins(coinsDict, 3)
			print('Winning line vert: ' + str(slotOutput[x]) + '-' + str(slotOutput[y]) + '-' + str(slotOutput[z]))
		i += 1 
		x += 1
		y += 1
		z += 1

	x = 0
	y = 4
	z = 8
	while i < 8: # diagonal wins
		if(slotOutput[x] == slotOutput[y] 
		and slotOutput[x] == slotOutput[z] 
		and slotOutput[y] == slotOutput[z]):
			if slotOutput[x] and slotOutput[y] and slotOutput[z] == 7:
				print('DIVINE BONUS! *7-7-7* - ' + str(int(coinsDict["currentBet"]) * 7) + ' coins!')
				payoutCoins(coinsDict, 7)
			elif slotOutput[x] and slotOutput[y] and slotOutput[z] == 6:
				print('DELIGHTFULLY DEVILISH! *6-6-6* - ' + str(int(coinsDict["currentBet"]) * 6) + ' coins!')
				payoutCoins(coinsDict, 6)
			else:
				payoutCoins(coinsDict, 3)
			print('Winning line diag: ' + str(slotOutput[x]) + '-' + str(slotOutput[y]) + '-' + str(slotOutput[z]))
		i += 1
		x = 6
		z = 2

	if int(coinsDict["winCounter"]) > 3 :
		print('BIG WINNER! Recieved bonus of: 50 coins')
		coinsDict["coinsWon"] += 50
		coinsDict["coinTotal"] += 50
		coinsDict["totalWinnings"] += 50
		print('Won ' + str(coinsDict["coinsWon"]) + '. Remaining: ' + str(coinsDict["coinTotal"]))
		tryAgain(coinsDict)
	elif int(coinsDict["winCounter"]) > 0:
		print('Won ' + str(coinsDict["coinsWon"]) + '. Remaining: ' + str(coinsDict["coinTotal"]))
		tryAgain(coinsDict)
	elif int(coinsDict["winCounter"]) == 0:
		coinsDict["coinTotal"] -= int(coinsDict["currentBet"])
		coinsDict["totalWinnings"] -= int(coinsDict["currentBet"])
		print('Loss of ' + str(coinsDict["currentBet"]) + ' coins. Remaining: ' + str(coinsDict["coinTotal"]))
		coinsDict["totalLosses"] += 1
		tryAgain(coinsDict)


def payoutCoins(coinsDict, betMultiplier):
	coinsDict["coinTotal"] += (int(coinsDict["currentBet"]) * betMultiplier)
	coinsDict["totalWinnings"] += (int(coinsDict["currentBet"]) * betMultiplier)
	coinsDict["coinsWon"] += (int(coinsDict["currentBet"]) * betMultiplier)
	coinsDict["winCounter"] += 1
	coinsDict["totalWins"] += 1


def tryAgain(coinsDict):
	tryAgainYN = input('Try again? (Y)es/(Q)uick/(S)tats/(N)o: ')
	if tryAgainYN == 'Y' or tryAgainYN == 'y':
		print('Your current total winnings are ' + str(coinsDict["totalWinnings"]) + ' coins.')
		if coinsDict["coinTotal"] == 0:
			print('Out of coins. Better luck next time!')
			end()
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			placeBets(coinsDict)	
	elif tryAgainYN == 'Q' or tryAgainYN == 'q':
		if coinsDict["coinTotal"] == 0:
			print('Out of coins. Better luck next time!')
			
		elif int(coinsDict["currentBet"]) > int(coinsDict["coinTotal"]):
			print('Not enough coins.')
			placeBets(coinsDict)
		else:
			print('Your current total winnings are ' + str(coinsDict["totalWinnings"]) + ' coins.')
			os.system('cls' if os.name == 'nt' else 'clear')
			determineOutput(coinsDict)
	elif tryAgainYN == 'S' or tryAgainYN == 's':
		getStats()
		tryAgain(coinsDict)
	else:
		print('Your total winnings were ' + str(coinsDict["totalWinnings"]) + ' coins, with ' + str(coinsDict["coinTotal"]) + ' remaining.')
		print()
			

def getStats():
	print('---STATS---')
	print('Win/Loss: {}/{}'.format(str(coinsDict["totalWins"]), str(coinsDict["totalLosses"])))
	print('Total winnings: {} coins.'.format(str(coinsDict["totalWinnings"])))
	print('-----------')


coinsDict = {
	"coinTotal": 500,
	"totalWinnings": 0,
	"totalWins": 0,
	"totalLosses": 0,
	"currentBet": 1,
	"coinsWon": 0,
	"winCounter": 0
	}
def start():
	print('Total coins: ' + str(coinsDict["coinTotal"]))
	placeBets(coinsDict)
	end()


def end(): # Also for when imported 
	getStats()


if __name__ == '__main__':
	start()
