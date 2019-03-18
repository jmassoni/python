# Project 3: M/M/1

## Due Sunday, November 18, at 11:59:59 PM

## Description

In this project, you'll answer some questions about queues. A few tips:

- The calculation questions all rely on the basic formulas we derived in class. Remember that you can use the Utilization Law to calcuate the utilization, *ρ = λ * s*.

- For the calculation problems, you can edit this file to include your answers or scan a handwritten page.

- For the simulations, review our earlier notes on simulating a single-server queue. You can do this without relying on the
full discrete time-advance algorithm. See the pseudocode below to get started.


## Questions

### Practice

Given an M/M/1 queue with *λ = 10* arrivals per second and *s = 75 ms*, calculate the following quantities:

- the utilization, ρ
- the probability that an arriving customer finds the queue idle
- the average residence time, R_bar
- the average waiting time, W_bar
- the average number in the queue, Q_bar
- the average number in the queue at an arrival instant
- the average number waiting and not being served
- the average number waiting and not being served at an arrival instant

Suppose we keep *λ* fixed at 10 arrivals per second. What value of *s* is required to achieve an average residence
time of .10 seconds?

For the same *λ*, what value of *s* is required to keep *Q_bar ≤ 2*?

### Real Ultimate Power

There has been a large amount of research on reducing the economic and environmental impact caused
by the energy demands of modern datacenters.

One of the most basic strategies for conserving energy is *dynamic voltage scaling* (DVS). By reducing the
operating voltage of a processor, we can its reduce energy consumption in exchange for decreased performance.

Suppose we have a set of *k* servers, each operating as an M/M/1 queue capable of running at a maximum
rate *µ*. The total arrival rate to the entire set of servers is *λ*. Assume the service rate of each server scales
linearly with its power consumption (this is not true, but just go with it). Consider two basic operating strategies:

- Turn on all *k* servers, each running at a fraction *1 / k* of its maximum power. In this scenario, the arrival
rate at each queue is *λ / k* and each queue’s service rate is *µ / k*.

- Turn on one server at full power. The server receives all arrivals at rate *λ* and has service rate *µ*.

Of these two strategies – multiple slow servers or one fast server – which one minimizes customer residence
time? By how much? Can you provide an intuitive explanation for this result?

Tip: don't write a simulation. You can answer this using the basic M/M/1 residence time equation.

### M/M/1 Residence Time Distribution

Write a program that simulates the M/M/1 queue and create histogram of the distribution of residence time experienecd by customers.

What distribution describes residence times in the M/M/1 queue?

Here is a pseudocode review of how to implement the single-server queueing simulator. The basic method uses four lists:

- `arrival_times` which keeps track of the random arrival time of each of the `n` customers. The time between arrivals in M/M/1
  is exponentially distributed.
  
- `service_times`, an array of `n` exponentially-distributed service times

- `enter_service_times`, which records the time each customer enters service. A customer enters service immediately if it arrives
  to find the server idle. Otherwise, it waits until the previous customer departs.
  
- `departure_times`, which records the time each customer finishes service and leaves the system

```
M/M/1 Simulation Pseudocode
===========================

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
    create an array of n exponential interarrival_times with parameter arrival_rate
    calculate an array of arrival_times using the interarrival_times
    
    # Initialize service times
    generate an array of n exponential service_times at rate 1 / s_bar
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        enter_service_times[i] = max(arrival_times[i],
                                     departure_times[i - 1])
                                     
        departure_times[i] = enter_service_times[i] + service_times[i]
        
    # Calculate statistics
    residence_times = departure_times - arrival_times
    waiting_times = enter_service_times - arrival_times
    
    # Plot residence time histogram
```

### Simulation Error Part I

Running the simulator one time gives a single estimate of the value of the average residence time `R_bar`. Because the estimate is 
calculated from a finite number of data points, it contains some inherent randomness. Therefore, using only one
simulated value as a prediction of `R_bar` is unlikely to be accurate unless the number of simulated arrivals `n` is very large.

If you run the simulator multiple times with the same value of `n`, you’ll generate a set of estimates for
`R_bar`. These estimates all contain some random error that separates them from the real, true value of `R_bar`. It’s
possible to very clearly describe the behavior and statistical properties of this error.

Consider a queue with `s_bar = 1.0` and `arrival_rate = .90`. Keep `n` fixed at **1000** and run your simulator 100 times, 
recording the value of the observed average residence time in each simulation.

Plot a histogram of these 100 `R_bar` values and calculate their mean. How does this mean of the means compare to the actual
expected residence time given by

```
            s_bar
R_bar =   ---------
           1 - rho

```

