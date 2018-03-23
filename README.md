# QSim
Simulation of a single queue with multiple workers

# How to run
First import the Simulation class, this is the entrypoint to running the simulations

````
import Simulation as sim
````

The Simulation class takes two parameters:
1. the number of minutes to run the simulation
2. the probability that for every minute passed a new user is arriving

````
simTenPercent = sim.Simulation(21600, 0.1) 
````

To run the simulation call the loop methods

````
simTenPercent.loop()
````

Two queues is maintained, a waiting queue and a queue with all completed cases. To get a histogram of the waiting times for users in both queues do as follows:

````
waitingTime = []
for user in simTenPercent.queue.waitingQueue + simTenPercent.queue.completed:
   wait = math.ceil(user.waitingTime / 360)
   waitingTime.append(wait)
````

The reason we are dividing by 360 in the above example, is that it is assumed that each case worker can work for 6 hours a day i.e. 360 minutes.
