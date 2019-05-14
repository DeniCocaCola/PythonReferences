import re
import random

def diceRoller():
    print('''Dice: D4, D6, D8, D10, D12, D20, D00
    Example: "4x3" will roll D4 3 times. "00x5" will roll D100 5 times.
    ''')
    diceType = [4, 6, 8, 10, 12, 20, 00]  #This isn't necessary, just a reference
    diceAmount = 0
    diceRoll = input("Input: ")
    
    pattern = "(\d{1,3})(x)(\d{1,3})"
    a = re.search(pattern, diceRoll)
    print(a.group(1))
    if a.group(1) == "4":
        print("Rolling D4 " + a.group(3) + " times.")
        for x in range(int(a.group(3))):
            print (random.randint(1, 5), end=",")

    elif a.group(1) == "6":
        print("Rolling D6 " + a.group(3) + " times.")
        for x in range(int(a.group(3))):
            print(random.randint(1, 7), end=",")

    elif a.group(1) == "8":
        print("Rolling D8" + a.group(3) + " times.")
        for x in range(int(a.group(3))):
            print(random.randint(1, 9), end=",")

    elif a.group(1) == "10":
        print("Rolling D10 " + a.group(3) + " times.")
        for x in range(int(a.group(3))):
            print (random.randint(1, 11), end=",")

    elif a.group(1) == "12":
        print ("Rolling D12 " + a.group(3) + " times.")
        for x in range(int(a.group(3))):
            print(random.randint(1, 13), end=",")

    elif a.group(1) == "20":
        print("Rolling D20 "+a.group(3)+" times")
        for x in range(int(a.group(3))):
            print(random.randint(1, 21), end=",")

    elif a.group(1) == "00":
        print ("Rolling Percentile D100 " + a.group(3) + " times.")
        for x in range(int(a.group(3))):
            print(random.randint(1, 101), end="%,")

    else:
        print("Invalid input. Perhaps incorrect dice type?")
        
diceRoller()        
