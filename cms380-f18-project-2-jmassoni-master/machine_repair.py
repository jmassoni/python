# Simulate the machine repair model

from random import random
from Queue import PriorityQueue
from math import sqrt

def rand_lifetime(p):
    
    ''' Generate a random lifetime for a machine
    
        input: p, prob. of breaking on each day
        output: random number of days until break
    '''

    count = 1  # Minimum lifetime is one day
    
    # Generate random trials
    # With prob. 1 - p, the machine survives one more day
    while random() < 1 - p:
        count += 1

    return count

    
def main():
    
    # Declare parameters
    num_machines = 2
    prob_break = .10
    repair_service_time = 5
    repair_queue = []
    time = 0
    max_time = 100000
    
    # For each machine, keep track of when it entered and
    # exited the repair queue
    enter_queue_time = {}
    exit_queue_time = {}
    
    queue = PriorityQueue()
    
    # All machines are initially running
    # Generate random lifetimes
    for machine in range(num_machines):
        lifetime = rand_lifetime(prob_break)
        
        # The data for the event is 'breakdown' and the machine number
        event = (lifetime, ('breakdown', machine))
        
        # Insert into the queue
        queue.put(event)
        
        # Intialize empty lists for enter and exit times
        enter_queue_time[machine] = []
        exit_queue_time[machine] = []
        
    # Loop until end of simulated time
    while time < max_time and not queue.empty():
        
        # Pop the next event from the priority queue
        event = queue.get()
        
        # Advance time
        time = event[0]
        
        type = event[1][0]
        machine = event[1][1]
        
        print time, type, machine, repair_queue
        
        # Process breakdown events
        if type == 'breakdown':
            
            # Track the time the machine entered the queue
            enter_queue_time[machine].append(time)
            
            # Increment number in queue
            repair_queue.append(machine)
            
            # If there is only one machine waiting, put it into service
            if len(repair_queue) == 1:
                event = (time + repair_service_time, ('repair', machine))
                queue.put(event)
   
            # If the queue is not empty, the machine will wait for its turn
            # to be serviced
                    
        # Process repair events
        elif type == 'repair':
            
            # Track the time the machine exited the queue
            exit_queue_time[machine].append(time)
            
            # Generate a future breakdown event for the repaired machine
            repaired_machine = repair_queue.pop(0)
            lifetime = rand_lifetime(prob_break)
            event = (time + lifetime, ('breakdown', repaired_machine))
            queue.put(event)
            
            # If there is another machine waiting, generate its repair event
            if len(repair_queue) > 0:
                next_machine = repair_queue[0]
                event = (time + repair_service_time, ('repair', next_machine))
                queue.put(event)

    # Statistics
    num_events = 0
    sum_residence_times = 0
    
    for machine in range(num_machines):
        residence_times = [exit_queue_time[machine][i] - enter_queue_time[machine][i]
                           for i in range(len(exit_queue_time[machine]))]
        
        num_events += len(residence_times)
        sum_residence_times += sum(residence_times)
    
    avg_residence_time = sum_residence_times / float(num_events)
    print 'average residence time = %f' % avg_residence_time
    
    
if __name__ == '__main__':
    main()