from CaseHandler import CaseHandler


class Queue:
    def __init__(self, numberOfWorkers):
        self.numberOfWorkers = numberOfWorkers
        self.waitingQueue = []
        self.completed = []
        self.casehandlers = []

    def addUserToWaitingQueue(self, user):
        self.waitingQueue.append(user)

    def addUserToCompleted(self, user):
        self.completed.append(user)

    def getNextUser(self):
        return self.waitingQueue[0]

    def removeUserFromWaitingQueue(self):
        self.waitingQueue.pop(0)

    def initiateCaseHandlers(self):
        for worker in range(self.numberOfWorkers):
            newCaseHandler = CaseHandler.CaseHandler()
            self.casehandlers.append(newCaseHandler)

    def addUserToInProgress(self, user):
        self.inProgress.append(user)