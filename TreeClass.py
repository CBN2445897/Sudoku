from random import seed
import random
from array import *
from turtle import goto
import numpy as np
from pip._vendor.msgpack.fallback import xrange

import TwoDimenMatrix
class BinaryTree():
    def __init__(self,rootObj,number):
        self.key = rootObj
        self.number = number
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode, number):
        if self.leftChild == None:
           self.leftChild = BinaryTree(newNode,number)
        else:
           t = BinaryTree(newNode, number)
           t.leftChild = newNode
           t.number =number
           self.leftChild = t

    def insertRight(self, newNode, number):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode, number)
        else:
            t = BinaryTree(newNode, number)
            t.rightChild = newNode
            t.number = number
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key
    def getNumber(self):
        return self.number

rootNumber = random.randint(1, 9)
leftChildNumber = random.randint(1,9)
rightChildNumber = random.randint(1,9)


Matrix = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],]

SmallMatrix = [[0,0,0,],
               [0,0,0,],
               [0,0,0,],]
MatrixTemp = [0,0,0]
MatrixTemp1 = [0,0,0]

List = [1,2,3,4,5,6,7,8,9]
x = 0
while len(List) > 0:
    randomNumber = random.randint(1, 9)
    if randomNumber in List:
        List.remove(randomNumber)
        Matrix[0][x] = randomNumber
        if x < 3:
            SmallMatrix[0][x] = Matrix[0][x]
        x = x + 1
print('Matrix[0]', Matrix[0])
#print('SmallMatrix', SmallMatrix)

List = [1,2,3,4,5,6,7,8,9]
Differ_List = list(set(List) - set(SmallMatrix[0]))
#print('Differ_List', Differ_List)
x = 0
counter = 9
while counter > 0:
    if x < 6:
        randomNumber = random.choice(Differ_List)
        counter = counter -1
        Matrix[1][x] = randomNumber
        Differ_List.remove(randomNumber)
        SmallMatrix[1][0:3] = Matrix[1][0:3]
        MatrixTemp = SmallMatrix[1][0:3]
        x = x + 1
    if x >= 6:
        randomNumber = random.choice(MatrixTemp)
        counter = counter -1
        Matrix[1][x] = randomNumber
        MatrixTemp.remove(randomNumber)
        x = x + 1
#print('SmallMatrix', SmallMatrix)
print('Matrix[1]', Matrix[1])

List = [1,2,3,4,5,6,7,8,9]
Differ_List = list(set(List) - set(SmallMatrix[0])- set(SmallMatrix[1]))
#print('Differ_List', Differ_List)
x = 0
counter = 9
while counter > 0:
    if x < 3:
        randomNumber = random.choice(Differ_List)
        counter = counter -1
        Matrix[2][x] = randomNumber
        #print(Matrix[2][x])
        Differ_List.remove(randomNumber)
        SmallMatrix[2][0:3] = Matrix[2][0:3]
        #print('SmallMatrix[2][x]', SmallMatrix[2][x])
        MatrixTemp = list(set(List) - set(SmallMatrix[2][0:3]))
        x = x + 1
    if x >= 3:
        #print('MatrixTemp', MatrixTemp)
        randomNumber = random.choice(MatrixTemp)
        counter = counter -1
        Matrix[2][x] = randomNumber
        MatrixTemp.remove(randomNumber)
        x = x + 1
print('Matrix[2]', Matrix[2])


