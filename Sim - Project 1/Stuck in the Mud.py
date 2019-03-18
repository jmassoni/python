from random import *

die1 = [randint(1,6), True]
die2 = [randint(1,6), True]
die3 = [randint(1,6), True]
die4 = [randint(1,6), True]
die5 = [randint(1,6), True]

setOfDice = [die1, die2, die3, die4, die5]

print(setOfDice[0][0], setOfDice[1][0], setOfDice[2][0], setOfDice[3][0], setOfDice[4][0] )

total = 0
pos = 0
roundTotal = 0
	
while True:
	
	pos = 0
	while pos < 5:
		if setOfDice[pos][1] == True and setOfDice[pos][0] == 2 or setOfDice[pos][0] == 5:
			roundTotal = 0
			setOfDice[pos][1] = False
			pos = pos + 1
		else:
			roundTotal += setOfDice[pos][0]
			pos = pos + 1
		
	print(roundTotal)
	
	total += roundTotal		

	
	if setOfDice[0][1] == False	and setOfDice[1][1] == False and setOfDice[2][1] == False and setOfDice[3][1] == False and setOfDice[4][1] == False:
		break

print(total)