# Project 1: The Compleat Gamester

## Due Thursday, 9/13, at 11:59:59 PM

## Honor Code

Edit this file to include your name and a statement of the Honor Code.

“On my honor, I have not given, nor received, nor witnessed any unauthorized assistance on this work.”
-Joey Massoni

## Instructions

Complete Python programs that answer the following questions. Each one of your programs should be a separate `.py` script.

Use appropriate style, comments, etc. I reserve the right to deduct points from submissions that use ugly or unclear style.

Do not include any debugging messages in your output: I will definitely take off points for programs that have cluttered output
streams. Just print what you need to print to answer the question. Note that it's fine to add extra print statements while you're 
writing the code, just take them out before you submit the final programs.

## Problems

### Passe-Dix

French for "pass ten" and one of the most ancient games of chance. Sometimes called "passage" in English, it was described by Charles
Cotton in his book *The Compleat Gamester* written in 1674. Cotton reports a legend that it was the game used by Roman soldiers to
divide the clothes of Jesus at the Crucifixion.

The rules are simple: a player rolls three six-sided dice. If the sum of the three **exceeds** 10, he wins; otherwise he loses.

Use a simulation program to evaluate the probability of winning at passe-dix.

Tip: the `random` module has a useful function for generating random integers. Look up its documentation.

### 7 Come 11

Craps is one of the most popular dice games in North American casinos. Craps has, like, 100 million different things you can bet on, but 
the fundamental bet is called the "Pass" bet; it pays even money and has some of the best odds of any common casino game.

Here are the basic rules for the Pass bet in craps:

- The player rolls two six-sided dice. This first roll is called the "come-out roll".
- If the roll is a 7 or 11, the bet immediately wins. If it is a 2, 3, or 12, the bet immediately loses.
- If the come-out roll is any other value (4, 5, 6, 8, 9, 10), that value becomes the "point".
- The player continues rolling, now trying to achieve the point a second time before rolling a 7. If he does roll the point value again,
he wins, but if he rolls a 7 first, he loses.

Use a simulation program to estimate the odds of winning the pass bet in craps.

### Nim

The game of Nim is played with two players and one or more piles of stones. On a player's turn, she can remove as many stones as she wishes from one of the piles. The player forced to take the last stone **loses**.

Write a Python script that allows two users to play Nim with three piles of stones. Randomly generate the number of stones in each pile at the start of the game.

On each turn, your program should print the number of stones in each pile, then ask the player to choose one of the piles and a number of stones to remove from that pile. Repeat until one player leaves behind three empty piles, then declare the winner.

Make sure to check for valid input: the number of stones must be a positive whole number (greater than 0), you can't remove stones from any empty pile, and you can't remove more stones than are currently in the pile. If the player makes a mistake, prompt them for a
better value.

Nim has been completely solved. For any starting configuration of piles and stones, there's an optimal playing strategy and a guaranteed winner.

Tips:
- Use `raw_input`. You can turn the user's response into a number using `int()`.
- Use a three-element list to keep track of the number of stones in each pile.

## Grading

I will grade your project by cloning your private repository to my workspace and running each of your Python scripts. If all of your scripts run and produce appropriate output, you'll get full credit. I will also check your code for style, etc.

I can only grade programs that run. Make sure that your programs run even if they aren't perfect.

As a general rule, you'll lose 5 points for each deviation from the problem specifications. For example, if your Nim program allows removing stones from piles that are already empty, you'd lose 5 points.
