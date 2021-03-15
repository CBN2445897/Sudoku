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

    should_restart = True
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
                           [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [1, 2, 3, 4, 5, 6, 7, 8, 9], ])

    def matrixIndexCalculator(currentRow, columnIndex):
        if (0 <= currentRow <= 2) and (0 <= columnIndex <= 2):
            return 1
        if (3 <= currentRow <= 5) and (0 <= columnIndex <= 2):
            return 4
        if (6 <= currentRow <= 8) and (0 <= columnIndex <= 2):
            return 7
        if (0 <= currentRow <= 2) and (3 <= columnIndex <= 5):
            return 2
        if (3 <= currentRow <= 5) and (3 <= columnIndex <= 5):
            return 5
        if (6 <= currentRow <= 8) and (3 <= columnIndex <= 5):
            return 8
        if (0 <= currentRow <= 2) and (6 <= columnIndex <= 8):
            return 3
        if (3 <= currentRow <= 5) and (6 <= columnIndex <= 8):
            return 6
        if (6 <= currentRow <= 8) and (6 <= columnIndex <= 8):
            return 9

    def matrixIndexResetor(self, matrixIndex):
        if (0 <= matrixIndex <= 2):
            matrixIndex = 0
        if (3 <= matrixIndex <= 5):
            matrixIndex = 3
        if (6 <= matrixIndex <= 8):
            matrixIndex = 6
        return matrixIndex

    def resetRow(self, listColumn, sudokuMatrix, currentRow, matrixIndexCalculator, listMatrix):
        columnIndex = -1
        listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #print("listRow = ", listRow)

        for resetIndex in range(0, 8):
            resetColumn = list(listColumn[resetIndex])
            resetColumn.remove(100)
            resetColumn.append(sudokuMatrix[currentRow][resetIndex])
            listColumn[resetIndex] = np.array(resetColumn)

            matrixIndex = matrixIndexCalculator(currentRow, resetIndex)
            resetMatrixList = list(listMatrix[matrixIndex])
            resetMatrixList.remove(100)
            resetMatrixList.append(sudokuMatrix[currentRow][resetIndex])
            listMatrix[matrixIndex] = subMatrix.array(resetMatrixList)

        sudokuMatrix[currentRow] = 0
        #print("sudokuMatrix[currentRow]", sudokuMatrix[currentRow])
        #print("listColumn[columnIndex] = ", listColumn[columnIndex + 1])
        matrixIndex = matrixIndexCalculator(currentRow, 0)
        #print("reset matrixIndex = ", matrixIndex)
        intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex + 1]),
                                                 set(listMatrix[matrixIndex])))


    counter = 0
    while (counter <9):
        for currentRow in range(0, 9):
            listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            counter += 1
            takenValue = 0

            while ((len(listRow) > 0)):
                intersectionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                columnIndex = -1
                matrixIndex = 1

                while columnIndex < 9:
                    #print("Start -----------------------------------------!")
                    #print("columnIndex", (columnIndex + 1))
                    #print("currentRow", currentRow)
                    #print("listRow = ", listRow)
                    tempColumn = columnIndex + 1


                    matrixIndex = matrixIndexCalculator(currentRow, tempColumn)
                    #print("matrixIndex", matrixIndex)
                    #print("listMatrix[matrixIndex]", listMatrix[matrixIndex])

                    intersectionList = list(
                        set.intersection(set(listRow), set(listColumn[columnIndex + 1]), set(listMatrix[matrixIndex])))
                    #print("intersectionList = ", intersectionList)

                    if ((len(intersectionList) == 0)): #and (len(listRow) % 3 != 0)):
                        #print("intersection list is empty Fall 0 , es wird auf den Anfang der Zeile zurückgesetzt")
                        columnIndex = -1
                        listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        #print("listRow = ", listRow)
                        for resetIndex in range(0,8):
                            resetColumn = list(listColumn[resetIndex])
                            if 100 in resetColumn:
                                resetColumn.remove(100)
                            else:
                                continue
                            resetColumn.append(sudokuMatrix[currentRow][resetIndex])
                            listColumn[resetIndex] = np.array(resetColumn)
                            matrixIndex = matrixIndexCalculator(currentRow, resetIndex)
                            resetMatrixList = list(listMatrix[matrixIndex])
                            if 100 in resetMatrixList:
                                resetMatrixList.remove(100)
                            else:
                                continue
                            resetMatrixList.append(sudokuMatrix[currentRow][resetIndex])
                            listMatrix[matrixIndex] = subMatrix.array(resetMatrixList)
                        sudokuMatrix[currentRow] = 0
                        #print("sudokuMatrix[currentRow]", sudokuMatrix[currentRow])
                        #print("listColumn[columnIndex] = ", listColumn[columnIndex + 1])
                        matrixIndex = matrixIndexCalculator(currentRow, 0)
                        #print("reset matrixIndex = ", matrixIndex)
                        intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex + 1]),
                                                                 set(listMatrix[matrixIndex])))
                        #print("resetListColumn = ", resetColumn[0])
                        #print("resetMatrixList = " , resetMatrixList[matrixIndex])

                    #print("listColumn[columnIndex] = ", listColumn[columnIndex + 1])

                    #if (len(intersectionList) == 0):
                        #break
                    takenValue = random.choice(intersectionList)
                    columnIndex += +1
                    if (0 <= currentRow <= 2) and (0 <= columnIndex <= 2):
                        matrixIndex = 1
                    if (3 <= currentRow <= 5) and (0 <= columnIndex <= 2):
                        matrixIndex = 4
                    if (6 <= currentRow <= 8) and (0 <= columnIndex <= 2):
                        matrixIndex = 7
                    if (0 <= currentRow <= 2) and (3 <= columnIndex <= 5):
                        matrixIndex = 2
                    if (3 <= currentRow <= 5) and (3 <= columnIndex <= 5):
                        matrixIndex = 5
                    if (6 <= currentRow <= 8) and (3 <= columnIndex <= 5):
                        matrixIndex = 8
                    if (0 <= currentRow <= 2) and (6 <= columnIndex <= 8):
                        matrixIndex = 3
                    if (3 <= currentRow <= 5) and (6 <= columnIndex <= 8):
                        matrixIndex = 6
                    if (6 <= currentRow <= 8) and (6 <= columnIndex <= 8):
                        matrixIndex = 9

                    #print("takenValue", takenValue)

                    sudokuMatrix[currentRow][columnIndex] = takenValue  # fill the current row with the takenValue

                    newListColumn = list(listColumn[columnIndex])

                    try:
                        newListColumn.remove(takenValue)
                        newListColumn.append(100)
                        #print("newListColumn = ", newListColumn)
                        newMatrixList = list(listMatrix[matrixIndex])
                        newMatrixList.remove(takenValue)
                        newMatrixList.append(100)

                        listColumn[columnIndex] = np.array(newListColumn)
                        listMatrix[matrixIndex] = subMatrix.array(newMatrixList)

                        #print("sudokuMatrix")

                        #print("subMatrix")
                        #print(listMatrix[matrixIndex])
                        #print("End ----------------------------------!")
                        listRow.remove(takenValue)
                    # intersectionList = list(set.intersection(set(listRow),set(newListColumn)))
                    # #print("intersectionList = ", intersectionList)
                        print("*-------SUDOKU-------*")
                        print(sudokuMatrix)
                        if (len(listRow) == 0) or (columnIndex == 8):
                            #print("A new row will start now")
                            break



                    except ValueError:
                        #print("Restart")
                        should_restart = True
