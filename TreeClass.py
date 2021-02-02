from random import seed
import random
from array import *
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

if leftChildNumber == rootNumber :
    leftChildNumber = random.randint(1, 9)
if rightChildNumber == rootNumber or rightChildNumber == leftChildNumber :
    rightChildNumber = random.randint(1, 9)

tree = BinaryTree('root',rootNumber)
tree.insertLeft('leftChild', leftChildNumber)
tree.insertRight('rightChild', rightChildNumber)
tree.leftChild.insertLeft('leftChild13', 13)
tree.rightChild.insertLeft('leftChild11', 11)

Row = TwoDimenMatrix.DynamicRow()
Column01= TwoDimenMatrix.DynamicRow()
#Column[1]= TwoDimenMatrix.DynamicRow()


Matrix = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],]
Column = [[], []]
#n = 5
#matrix = np.zeros((n,9)) # Pre-allocate matrix
#for i in range(1,n):
    #matrix[i] = [i, i, i,9]
#print(matrix)

List = [1,2,3,4,5,6,7,8,9]
x = 0
while len(List) > 0:
    randomNumber = random.randint(1, 9)
    if randomNumber in List:
        print('x = ',x)
        print('randomNumber', randomNumber)
        List.remove(randomNumber)
        print('List =', List)
        Row.append(randomNumber)
        Matrix[0][x] = randomNumber
        x = x + 1
        #Column[x].append(randomNumber)
List = [1,2,3,4,5,6,7,8,9]
x = 0
while len(List) > 0:
    randomNumber = random.randint(1, 9)
    if randomNumber in List:
        print('x = ',x)
        print('randomNumber', randomNumber)
        List.remove(randomNumber)
        print('List =', List)
        Row.append(randomNumber)
        Matrix[2][x] = randomNumber
        x = x + 1

print('Matrix', Matrix[0])
print('Matrix', Matrix[2])
#print('Matrix 1', Matrix[1])
#print('Column 0', Column[0])
#print('Column 1', Column[1])


#for i in Matrix[1]:
 #   ColumnDyna.append(1)
  #  print('ColumnDyna[i]', ColumnDyna)







#tree.leftChild.insertLeft('leftChild1', leftChildNumber)
#print('root', tree.getNumber())
#print(tree.leftChild.getRootVal(), tree.leftChild.getNumber())
#print(tree.rightChild.getRootVal(), tree.rightChild.getNumber())
#print(tree.rightChild.leftChild.getRootVal(), tree.rightChild.leftChild.getNumber())

