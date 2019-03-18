#!/usr/bin/python

# Example of using input in Python

# basic input function in Python 2 is raw_input
msg = raw_input('Say something: ')

test = msg [::-1] * 3

print test

if test == "ththth":
	print "ok then"
elif test == "hththt":
	print "ok i guess"
else:
	print "nope"