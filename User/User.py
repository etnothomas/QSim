import numpy as np

class User:
    def __init__(self, arrivalTime):
        self.arrivalTime = arrivalTime
        self.waitingTime = 0
        self.caseHandlingTime = np.random.poisson(35)
        self.handled = False

    def incrementWaitingTime(self):
        self.waitingTime += 1

    def setServiceTime(self, serviceTime):
        self.serviceTime = serviceTime

    def setFinalWaitingTime(self):
        self.waitingTime = self.waitingTime + self.caseHandlingTime

    def getHandlingTime(self):
        return self.handlingTime

    def setHandledToTrue(self):
        self.handled = True
