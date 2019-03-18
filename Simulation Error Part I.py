#!/usr/bin/python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
from math import log
from random import random

residence_times_aggregate = []
final_residence_time = 0

# Calculate exponential random variables using inverse CDF method
def rand_exp(mu):

	return -log(random()) / mu
	
# Simulate an M/M/1 queue with parameters
#
#   arrival_rate
#   average service time s_bar
#   
def simulation(arrival_rate, s_bar, n):

	# Initialize arrival times
	
	interarrival_times = []
	arrival_times = []
	service_times = []
	enter_service_times = []
	departure_times = []
	residence_times = []
	waiting_times = []

	
	# create an array of n exponential interarrival_times with parameter arrival_rate
	for i in range(n):
		interarrival_times.append(rand_exp(arrival_rate))

		
	# calculate an array of arrival_times using the interarrival_times
	arrival_times.append(interarrival_times[0])

	for i in range(1, n):
		arrival_times.append(arrival_times[-1] + interarrival_times[i])
	
	
	# Initialize service times
	
	# generate an array of n exponential service_times at rate 1 / s_bar
	for i in range(n):
		service_times.append(rand_exp(1 / s_bar))

	
	# Setup for first arrival
	enter_service_times.append(arrival_times[0])
	departure_times.append(enter_service_times[0] + service_times[0])
	
	# Loop over all other arrivals
	for i in range(1, n):
		

		enter_service_times.append(max(arrival_times[i], departure_times[i - 1]))
									 
		departure_times.append(enter_service_times[i] + service_times[i])
		
	# Calculate statistics
	
	for i in range (1, n):
		
		residence_times.append(departure_times[i] - arrival_times[i])
		waiting_times.append(enter_service_times[i] - arrival_times[i])
	 
	# Plot residence time histogram
	
	average_residence_time = 0;
	average_residence_time = reduce(lambda x, y: x + y, residence_times) / len(residence_times)
	residence_times_aggregate.append(average_residence_time)

for i in range(99):
	
	simulation(.9, 1, 1000)
	

final_residence_time = reduce(lambda x, y: x + y, residence_times_aggregate) / len(residence_times_aggregate)
print final_residence_time
