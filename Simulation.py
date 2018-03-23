import numpy as np
import math
from User import User
from Queue import Queue
import seaborn as sbn
import pandas as pd

def writeCsvToDisk(path, data):
    with open(path, 'wb') as f:
        writer = csv.writer(f)
        for elem in data:
            writer.writerow(elem)



class Simulation:

    def __init__(self, iterations, newUserProbablity):
        self.queue = Queue.Queue(4)
        self.queue.initiateCaseHandlers()
        self.iterations = iterations
        self.newUserProbability = newUserProbablity

    def addNewUser(self):
        pass

    def loop(self):
        for i in range(self.iterations):
            # determine if a new user enters the queue
            prop = np.random.uniform(0, 1)
            if prop < self.newUserProbability:
                self.queue.addUserToWaitingQueue(User.User(i))

            # check if there are users in the queue
            # check if all workers are busy,if not assign a new user to the worker
            # and remove that user from the queue, in a round robin manner
            for casehandler in self.queue.casehandlers:
                if casehandler.isAvailable():
                    if len(self.queue.waitingQueue) > 0:
                        user = self.queue.getNextUser()
                        user.setFinalWaitingTime()
                        user.setHandledToTrue()
                        self.queue.removeUserFromWaitingQueue()
                        self.queue.addUserToCompleted(user)
                        casehandler.setAvailableToFalse()
                        casehandler.setCaseHandlingTime(user.caseHandlingTime)
                else:
                    # decrease the case handling time for all busy workers and make
                    # the workers with 0 case handling time available
                    casehandler.decrementCaseHandlingTime()
                    if casehandler.caseHandlingTime == 0:
                        casehandler.setAvailableToTrue()

            # increment the waiting time for users in the waiting queue if queue is not empty
            if len(self.queue.waitingQueue) > 0:
                [user.incrementWaitingTime() for user in self.queue.waitingQueue]


if __name__ == "__main__":

    import Simulation as sim
    simTenPercent = sim.Simulation(21600, 0.20) # 360 casehandler minutes per day, times 60 working days
    simTenPercent.loop()

    waitingTime = []
    for user in simTenPercent.queue.completed:
        wait = math.ceil(user.waitingTime / 360)
        day = math.ceil(user.arrivalTime / 360)
        waitingTime.append((day, wait))

    waitingAndArrivalTimeDataFrame = pd.DataFrame(waitingTime, columns=['day', 'waitingtime'])

    avgWaitingTimeByDayOfEntry = waitingAndArrivalTimeDataFrame.groupby('day', as_index=False).mean()

    sbn.barplot(x='day', y='waitingtime', data=avgWaitingTimeByDayOfEntry)






