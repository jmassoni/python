# Simulate a game of Nim

from random import *

# Instantiate list with 3 random numbers and print original set

piles = [randint(1,1000), randint(1,1000),randint(1,1000)]

print("")
print(piles)

# Instantiate global variables to shift between players and a count to assist with error handling

player1 = True
count = 0

# This while loop will execute until all piles are empty

while piles[0] > 0 or piles[1] > 0 or piles[2] > 0:
	
	# If/else statment prompts the player and remprompts appropriately when input errors occur
	
	if player1 == True:
		if count == 0:
			print("Your turn player 1...")
		else:
			print("Let's try this again bud...")
			count = 0
	else:
		if count == 0:
			print("Ok, your turn player 2...")
		else:
			print("Let's try this again friend...")
			count = 0
			
	# The outer try/except statement checks for input of non integers
	# The user is prompted to choose a pile
	# Internal if statements account for input errors related to calling for piles outside of range or empty piles		
			
	try:
		pile_number = raw_input("Which pile would you like to pick? ")
		if int(pile_number) > 3 or int(pile_number) < 1:
			print("There is no pile " + pile_number + ".")
			print("")
			count = count + 1
			continue
		if piles[int(pile_number) - 1] == 0:
			print("That pile is already empty.")
			print("")
			count = count + 1
			continue
	except ValueError:
		print("That's not even a number.")
		print("")
		count = count + 1
		continue
		
	pile_size = piles[int(pile_number) - 1]
	
	# The outer try/except statement, again, checks for input of non integers
	# The user is prompted to decide how many stones they'd like to remove from the pile
	# Internal if statements account for input errors related to range of stones available in pile
	
	try:
		stones_removed = raw_input("How many stones would you like removed? ")
		if int(stones_removed) > pile_size:
			print("That's too many stones!")
			print("")
			count = count + 1
			continue
		if int(stones_removed) < 1:
			print("That doesn't make any sense.")
			print("")
			count = count + 1
			continue
	except ValueError:
		print("That's not even a number.")
		print("")
		count = count + 1
		continue
	
	# The pile_number variable is converted to an int and 1 is subtracted to indicate appropriate index in list
	# The player action is printed, the appropriate number in the list is adjusted and the new set of piles is printed

	pile_num = int(pile_number) - 1	
	
	print("Removed " + stones_removed + " stones from pile number " + pile_number)
	
	piles[pile_num] = piles[pile_num] - int(stones_removed)
	
	print("")
	print(piles)
	
	# This if statement allows me to switch between players at the end of each loop
	
	if player1 == True:
		player1 = False
	else:
		player1 = True

# This if statement essentially checks who made the last move and pronounces them the winner
		
if player1 == True:
	print("Player 2 wins! GG.")
else:
	print("Player 1 won. Weeee!")
