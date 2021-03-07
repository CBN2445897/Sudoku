import numpy as matrix
import numpy as np
import numpy as subMatrix
from array import *
import random
from random import seed
import copy

class SudokuMatrixGenerator():

    #def __init__(self):
        # Create 9x9 matrix with default value of 0

    restart = False
    defaultSudokuMatrix = matrix.full((9, 9), 0)
    sudokuMatrix = defaultSudokuMatrix
    listColumn = np.array([[1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],
                           [1,2,3,4,5,6,7,8,9],])

    listMatrix = subMatrix.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9], ])

    for currentRow in range(0, 9):
        listRow = [1,2,3,4,5,6,7,8,9]
        takenValue = 0

        while ((len(listRow)>0)):
            intersectionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            columnIndex = -1
            matrixIndex = 1

            while columnIndex < 9:
                print("columnIndex", columnIndex)
                print("currentRow", currentRow)
                print("matrixIndex", matrixIndex)
                print("listMatrix[matrixIndex]", listMatrix[matrixIndex])
                intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex+1]), set(listMatrix[matrixIndex])))
                print("intersectionList Fall 0= ", intersectionList)
                if ((len(intersectionList) == 0) and (len(listRow) == 9)):
                    print("intersection list is empty")
                    intersectionList = intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex+1])))
                    print("intersectionList Fall 1  = ", intersectionList)
                if ((len(intersectionList) == 0) and (len(listRow) == 6)):
                    print("intersection list is empty")
                    intersectionList = intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex+1]),set(listMatrix[matrixIndex +1])))
                    print("intersectionList Fall 2 = ", intersectionList)
                if ((len(intersectionList) == 0) and (len(listRow) == 3)):
                    print("intersection list is empty")
                    intersectionList = intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex+1]),set(listMatrix[matrixIndex+1])))
                    print("intersectionList Fall 3 = ", intersectionList)
                print("listRow = ", listRow)
                print("listColumn[columnIndex] = ",  listColumn[columnIndex+1])
                #takenValue = random.choice(list(set.intersection(set(listRow),set(listColumn[columnIndex+1]),set(listMatrix[matrixIndex]))))
                takenValue = random.choice(intersectionList)
                columnIndex += +1

                if (0<= currentRow <=2) and (0<= columnIndex <=2):
                    matrixIndex = 1
                if (3 <= currentRow <= 5) and (0 <= columnIndex <= 2):
                    matrixIndex = 4
                if (6 <= currentRow <= 8) and (0 <= columnIndex <= 2):
                    matrixIndex = 7
                if (0<= currentRow <=2) and (3<= columnIndex <=5):
                    matrixIndex = 2
                if (3 <= currentRow <= 5) and (3 <= columnIndex <= 5):
                    matrixIndex = 5
                if (6 <= currentRow <= 8) and (3 <= columnIndex <= 5):
                    matrixIndex = 8
                if (0<= currentRow <=2) and (6<= columnIndex <=8):
                    matrixIndex = 3
                if (3 <= currentRow <= 5) and (6 <= columnIndex <= 8):
                    matrixIndex = 6
                if (6 <= currentRow <= 8) and (6 <= columnIndex <= 8):
                    matrixIndex = 9

                print("takenValue", takenValue)

                sudokuMatrix[currentRow][columnIndex] = takenValue     #fill the current row with the takenValue

                newList = list(listColumn[columnIndex])
                newList.remove(takenValue)
                newList.append(0)
                print("newList = ", newList)

                newMatrixList = list(listMatrix[matrixIndex])
                newMatrixList .remove(takenValue)
                newMatrixList.append(100)

                listColumn[columnIndex]=np.array(newList)
                listMatrix[matrixIndex] = subMatrix.array(newMatrixList)

                print("sudokuMatrix")
                print(sudokuMatrix)
                print("subMatrix")
                print(listMatrix[matrixIndex])
                listRow.remove(takenValue)
                #intersectionList = list(set.intersection(set(listRow),set(newList)))
                #print("intersectionList = ", intersectionList)

                if (len(listRow) == 0) :
                    print("A new row will start now")
                    break
