import torch
import torchvision
import os
from PIL import Image
import numpy as np

class boundingBox:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculateIoU(self, other):
        return 0 # TODO: Implement

class image:
    def __init__(self, imageTensor, boundingBoxes):
        self.imageTensor = imageTensor
        self.boundingBoxes = boundingBoxes

def stripFormat():
    annotations = []
    for filename in os.listdir("Annotation"):
        with open("./Annotation/" + filename) as file:
            lines = file.readlines()

            imagePath = os.getcwd() + "/" + lines[1].split(" : ")[1][1:-2]
            image = Image.open(imagePath)
            image_np = np.asarray(image)
            imageTensor = torchvision.transforms.ToTensor()(image_np) # TODO fix non-writeable Tensors

            amountOfObjects =  int(lines[4].split(": ")[1].split(" {")[0])
            boundingBoxes = []
            for i in range(0, amountOfObjects):
                boxFormat = (lines[10 + 5*i].split(": ")[1])
                x1 = int(boxFormat.split(" - ")[0].split(", ")[0][1:])
                x2 = int(boxFormat.split(" - ")[1].split(", ")[0][1:])
                y1 = int(boxFormat.split(" - ")[0].split(", ")[1][:-1])
                y2 = int(boxFormat.split(" - ")[1].split(", ")[1][:-2])

                boundingBoxes.append(boundingBox(x1, x2, y1, y2))

            annotations.append(image(imageTensor, boundingBoxes))


    return annotations

if __name__ == '__main__':
    images = stripFormat()
    print('kaas')