import random

class Trainer:
    def __init__(self, annotations):
        self.annotations = annotations
        self.splitTrainTest()

    # ratio : ratio between test and training
    def splitTrainTest(self, ratio=0.1):
        self.testSet = []
        self.trainSet = []

        for i in range(0, self.annotations.size):
            if random.random() < ratio:
                self.testSet.add(self.annotations[i])
            else:
                self.trainSet.add(self.annotations[i])

    def train(self):
        return 0