class CaseHandler:

    def __init__(self):
        self.available = True
        self.caseHandlingTime = 0

    def isAvailable(self):
        return self.available

    def setAvailableToFalse(self):
        self.available = False

    def setAvailableToTrue(self):
        self.available = True

    def setCaseHandlingTime(self, time):
        self.caseHandlingTime = time

    def decrementCaseHandlingTime(self):
        self.caseHandlingTime -= 1