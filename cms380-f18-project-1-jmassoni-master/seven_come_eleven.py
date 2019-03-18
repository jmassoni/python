# Simulate a game of Craps using the Pass betting style

from random import *

# Define a dice rolling function to generate a total from two rolled dice multiple times during run
totalWins = 0

def roll_dice():
	die1 = randint(1,6)
	die2 = randint(1,6)
	
	total = die1 + die2
	return total

for x in range(0, 99999):
	# Instantiate the Come Out Roll as the initial dice roll
		
	comeOutRoll = roll_dice()

	# If/elif statements account for immediate winning and losing rolls
	# Else statement accounts for having to continue rolling

	if comeOutRoll == 7 or comeOutRoll == 11:
		totalWins = totalWins + 1
	elif comeOutRoll == 2 or comeOutRoll == 3 or comeOutRoll == 12:
		continue
	else:
		
		# Rename the comeOutRoll point for consistency
		# Instantiate a count to make individual rolls easier to readk
			
		point = comeOutRoll
		count = 2
		
		# Roll 2nd time
		
		attempt = roll_dice()
		
		# While statement checks for point and losing 7
		# If neither of those are equal to the 2nd attempt the loop continues rolling and incrememnting the count
		
		while attempt != point and attempt != 7:
			attempt = roll_dice()
			count = count + 1
		
		# The loop exits due to one of the conditions being met
		# An if/elif statement prints the appropriate statement based on a win/loss
			
		if attempt == 7:
			continue
		elif attempt == point:
			totalWins = totalWins + 1
			
# Divide the total number of wins by the total number of simulated games
# Then multiply by 100 and print to present a traditional depiction of winning percentage			

winningChance = (float(totalWins)/100000.0) * 100
print("Your chances of winning are at " + str(winningChance) + "%" )
