# Simulate a game of Passe Dix

from random import *

# Instantiate a global variable to act as a count for individual wins across sample
# Create for loop to simulate 100,000 games of Passe Dix

totalWins = 0

for x in range(0, 99999):
	# Instantiate dice using random ints between 1 and 6

	die1 = randint(1,6)
	die2 = randint(1,6)
	die3 = randint(1,6)

	# Calculate the total value of the dice rolls
	
	total = die1 + die2 + die3
	
	# An if/else statement checks for losing values first for potential (nominal) performance gain

	if total >= 10:
		totalWins = totalWins + 1
		
# Divide the total number of wins by the total number of simulated games
# Then multiply by 100 and print to present a traditional depiction of winning percentage
				
winningChance = (float(totalWins)/100000.0) * 100
print("Your chances of winning are at " + str(winningChance) + "%" )
