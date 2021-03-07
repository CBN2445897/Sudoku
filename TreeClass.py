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

SmallMatrix = [[[0,0,0,],
               [0,0,0,],
               [0,0,0,],],
               [[0,0,0,],
               [0,0,0,],
               [0,0,0,],],
               [[0,0,0,],
                [0,0,0,],
                [0,0,0,],]]

List = [1,2,3,4,5,6,7,8,9]
x = 0
while len(List) > 0:
    randomNumber = random.randint(1, 9)
    if randomNumber in List:
        List.remove(randomNumber)
        Matrix[0][x] = randomNumber
        if x in range (0,3):
            SmallMatrix[0][0][x] = Matrix[0][x]         #The first row of the smallmatrix[0]
            #print('SmallMatrix 0', SmallMatrix[0])
        if x in range (3,6):
            SmallMatrix[1][0][x-3]= (Matrix[0][x])        #The first row of the smallmatrix[1]
            #print('SmallMatrix 1', SmallMatrix[1])
        if x in range (6,9):
            SmallMatrix[2][0][x-6]= (Matrix[0][x])        #The first row of the smallmatrix[2]
            #print('SmallMatrix 2', SmallMatrix[2])
        x = x + 1

# Create the 2. row of the Matrix
List = [1,2,3,4,5,6,7,8,9]          # Second row of the Matrix
x = 0
counter = 9
while x < 10:
        if x in range (0,3):
            Differ_List = list(set(List) - set(SmallMatrix[0][0])- set(Matrix[1]))
            #print('Differ_List = ', Differ_List)  # print('SmallMatrix 1', SmallMatrix[0])
            #print('SmallMatrix[0][0] =', SmallMatrix[0][0])
            Matrix[1][x] = random.choice(Differ_List)
            #print('Matrix[1][x]', Matrix[1][x])
            SmallMatrix[0][1][x] = Matrix[1][x]         #The second row of the smallmatrix[0]
            #x += 1
        if x in range (3,6):
            Differ_List = list(set(List) - set(SmallMatrix[0][1])-set(SmallMatrix[1][0])- set(Matrix[1]))
            Matrix[1][x] = random.choice(Differ_List)
            SmallMatrix[1][1][x-3]= (Matrix[1][x])        #The second row of the smallmatrix[1]
            #x += 1
            #print('SmallMatrix 1', SmallMatrix[1])
        if x in range (6,9):
            Differ_List = list(set(List) - set(SmallMatrix[0][1]) - set(SmallMatrix[1][1])- set(Matrix[1]))
            Matrix[1][x] = random.choice(Differ_List)
            SmallMatrix[2][1][x-6]= (Matrix[1][x])        #The second row of the smallmatrix[2]
            #x += 1
            #print('SmallMatrix 2', SmallMatrix[2])
        x = x + 1
print('Matrix[0]', Matrix[0])
print('Matrix[1]', Matrix[1])

# Create the 3. row of the Matrix
List = [1,2,3,4,5,6,7,8,9]          # Second row of the Matrix
x = 0
counter = 9
while x < 10:
        if x in range (0,3):
            Differ_List = list(set(List) - set(SmallMatrix[0][0])-set(SmallMatrix[0][1])- set(Matrix[2]))
            Matrix[2][x] = random.choice(Differ_List)
            SmallMatrix[0][2][x] = Matrix[2][x]         #The third row of the smallmatrix[0]
        if x in range (3,6):
            Differ_List = list(set(List) - set(SmallMatrix[1][0]) - set(SmallMatrix[1][1])- set(Matrix[2]))
            print('Differ_List', Differ_List)
            print('Matrix[2]', Matrix[2])
            Matrix[2][x] = random.choice(Differ_List)
            SmallMatrix[1][2][x-3]= (Matrix[2][x])        #The third row of the smallmatrix[1]
        if x in range (6,9):
            Differ_List = list(set(List) - set(SmallMatrix[2][0]) - set(SmallMatrix[2][1])- set(Matrix[2]))
            Matrix[2][x] = random.choice(Differ_List)
            SmallMatrix[2][2][x-6]= (Matrix[2][x])        #The third row of the smallmatrix[2]
        x = x + 1
print('Matrix[2]', Matrix[2])
#print('SmallMatrix', SmallMatrix)


# Create the 4. row of the Matrix
List = [1,2,3,4,5,6,7,8,9]          # Second row of the Matrix
x = 0
counter = 9
while x < 10:
        if x in range (0,3):
            Differ_List = list(set(List) - set(SmallMatrix[0][0])-set(SmallMatrix[0][1])- set(Matrix[2]))
            Matrix[2][x] = random.choice(Differ_List)
            SmallMatrix[0][2][x] = Matrix[2][x]         #The third row of the smallmatrix[0]
        if x in range (3,6):
            Differ_List = list(set(List) - set(SmallMatrix[1][0]) - set(SmallMatrix[1][1])- set(Matrix[2]))
            print('Differ_List', Differ_List)
            print('Matrix[2]', Matrix[2])
            Matrix[2][x] = random.choice(Differ_List)
            SmallMatrix[1][2][x-3]= (Matrix[2][x])        #The third row of the smallmatrix[1]
        if x in range (6,9):
            Differ_List = list(set(List) - set(SmallMatrix[2][0]) - set(SmallMatrix[2][1])- set(Matrix[2]))
            Matrix[2][x] = random.choice(Differ_List)
            SmallMatrix[2][2][x-6]= (Matrix[2][x])        #The third row of the smallmatrix[2]
        x = x + 1
print('Matrix[2]', Matrix[2])
#print('SmallMatrix', SmallMatrix)