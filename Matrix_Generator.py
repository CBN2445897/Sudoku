import numpy as np
from array import *
import random
from random import seed
import copy
import math

class SudokuMatrixGenerator():

    sudokuMatrix = np.full((9, 9), 0)

    def matrixIndexCalculator(self, rowIndex, columnIndex):
        if (0 <= rowIndex <= 2):
            if (0 <= columnIndex <= 2): return 1
            elif (3 <= columnIndex <= 5): return 2
            elif (6 <= columnIndex <= 8): return 3
        elif (3 <= rowIndex <= 5):
            if (0 <= columnIndex <= 2): return 4
            elif (3 <= columnIndex <= 5): return 5
            elif (6 <= columnIndex <= 8): return 6
        elif (6 <= rowIndex <= 8):
            if (0 <= columnIndex <= 2): return 7
            elif (3 <= columnIndex <= 5): return 8
            elif (6 <= columnIndex <= 8): return 9

    # def matrixIndexResetor(self, matrixIndex):
    #     if (0 <= matrixIndex <= 2):
    #         matrixIndex = 0
    #     if (3 <= matrixIndex <= 5):
    #         matrixIndex = 3
    #     if (6 <= matrixIndex <= 8):
    #         matrixIndex = 6
    #     return matrixIndex

    # def resetRow(self, listColumn, sudokuMatrix, currentRow, matrixIndexCalculator, listMatrix):
    #     columnIndex = -1
    #     listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     #print("listRow = ", listRow)

    #     for resetIndex in range(0, 8):
    #         resetColumn = list(listColumn[resetIndex])
    #         resetColumn.remove(100)
    #         resetColumn.append(sudokuMatrix[currentRow][resetIndex])
    #         listColumn[resetIndex] = np.array(resetColumn)

    #         matrixIndex = matrixIndexCalculator(currentRow, resetIndex)
    #         resetMatrixList = list(listMatrix[matrixIndex])
    #         resetMatrixList.remove(100)
    #         resetMatrixList.append(sudokuMatrix[currentRow][resetIndex])
    #         listMatrix[matrixIndex] = subMatrix.array(resetMatrixList)

    #     sudokuMatrix[currentRow] = 0
    #     #print("sudokuMatrix[currentRow]", sudokuMatrix[currentRow])
    #     #print("listColumn[columnIndex] = ", listColumn[columnIndex + 1])
    #     matrixIndex = matrixIndexCalculator(currentRow, 0)
    #     #print("reset matrixIndex = ", matrixIndex)
    #     intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex + 1]),
    #                                              set(listMatrix[matrixIndex])))

    def generate_Matrix(self):
        listColumn = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9], ])

        listMatrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9], ])

        for currentRow in range(0, 9):
            listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            while ((len(listRow) > 0)):
                intersectionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                columnIndex = 0
                matrixIndex = 1

                while columnIndex < 9:
                    #print("Start -----------------------------------------!")
                    #print("columnIndex", (columnIndex + 1))
                    #print("currentRow", currentRow)
                    #print("listRow = ", listRow)
                    #print("intersectionList = ", intersectionList)

                    while (True): #and (len(listRow) % 3 != 0)):

                        matrixIndex = self.matrixIndexCalculator(currentRow, columnIndex)
                        #print("matrixIndex", matrixIndex)
                        #print("listMatrix[matrixIndex]", listMatrix[matrixIndex])

                        intersectionList = list(
                            set.intersection(set(listRow), set(listColumn[columnIndex]), set(listMatrix[matrixIndex])))

                        if (len(intersectionList) > 0):
                            break

                        #print("intersection list is empty Fall 0 , es wird auf den Anfang der Zeile zurückgesetzt")
                        columnIndex = 0
                        listRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        #print("listRow = ", listRow)
                        for resetIndex in range(0,8):
                            resetColumn = list(listColumn[resetIndex])
                            if 100 in resetColumn:
                                resetColumn.remove(100)
                            else:
                                continue
                            resetColumn.append(self.sudokuMatrix[currentRow][resetIndex])
                            listColumn[resetIndex] = np.array(resetColumn)
                            matrixIndex = self.matrixIndexCalculator(currentRow, resetIndex)
                            resetMatrixList = list(listMatrix[matrixIndex])
                            if 100 in resetMatrixList:
                                resetMatrixList.remove(100)
                            else:
                                continue
                            resetMatrixList.append(self.sudokuMatrix[currentRow][resetIndex])
                            listMatrix[matrixIndex] = np.array(resetMatrixList)
                        self.sudokuMatrix[currentRow] = 0
                        #print("sudokuMatrix[currentRow]", sudokuMatrix[currentRow])
                        #print("listColumn[columnIndex] = ", listColumn[columnIndex + 1])
                        matrixIndex = self.matrixIndexCalculator(currentRow, 0)
                        #print("reset matrixIndex = ", matrixIndex)
                        intersectionList = list(set.intersection(set(listRow), set(listColumn[columnIndex]),
                                                                set(listMatrix[matrixIndex])))
                        #print("resetListColumn = ", resetColumn[0])
                        #print("resetMatrixList = " , resetMatrixList[matrixIndex])

                    #print("listColumn[columnIndex] = ", listColumn[columnIndex + 1])

                    takenValue = random.choice(intersectionList)
                    matrixIndex = self.matrixIndexCalculator(currentRow, columnIndex)

                    #print("takenValue", takenValue)

                    self.sudokuMatrix[currentRow][columnIndex] = takenValue  # fill the current row with the takenValue

                    newListColumn = list(listColumn[columnIndex])


                    newListColumn.remove(takenValue)
                    newListColumn.append(100)
                    #print("newListColumn = ", newListColumn)
                    newMatrixList = list(listMatrix[matrixIndex])
                    newMatrixList.remove(takenValue)
                    newMatrixList.append(100)

                    listColumn[columnIndex] = np.array(newListColumn)
                    listMatrix[matrixIndex] = np.array(newMatrixList)

                    #print("sudokuMatrix")
                    #print("subMatrix")
                    #print(listMatrix[matrixIndex])
                    #print("End ----------------------------------!")

                    listRow.remove(takenValue)

                    print("*-------SUDOKU-------*")
                    print(self.sudokuMatrix)
                    if (len(listRow) == 0) or (columnIndex == 8):
                        #print("A new row will start now")
                        break

                    columnIndex += +1

    #########################################################################################
    #########################################################################################

    def getSubMatrix(self, rowIndex, columnIndex):
        subMatrix = np.full(9, 0)

        subMatrixRow = math.floor(rowIndex / 3) 
        subMatrixColumn = math.floor(columnIndex / 3)

        subMatrix[0] = self.sudokuMatrix[subMatrixRow * 3][subMatrixColumn * 3]
        subMatrix[1] = self.sudokuMatrix[subMatrixRow * 3][subMatrixColumn * 3 + 1]
        subMatrix[2] = self.sudokuMatrix[subMatrixRow * 3][subMatrixColumn * 3 + 2]
        subMatrix[3] = self.sudokuMatrix[subMatrixRow * 3 + 1][subMatrixColumn * 3]
        subMatrix[4] = self.sudokuMatrix[subMatrixRow * 3 + 1][subMatrixColumn * 3 + 1]
        subMatrix[5] = self.sudokuMatrix[subMatrixRow * 3 + 1][subMatrixColumn * 3 + 2]
        subMatrix[6] = self.sudokuMatrix[subMatrixRow * 3 + 2][subMatrixColumn * 3]
        subMatrix[7] = self.sudokuMatrix[subMatrixRow * 3 + 2][subMatrixColumn * 3 + 1]
        subMatrix[8] = self.sudokuMatrix[subMatrixRow * 3 + 2][subMatrixColumn * 3 + 2]
        return subMatrix


    def getRowMatrix(self, rowIndex):
        return self.sudokuMatrix[rowIndex]


    def getColumnMatrix(self, columnIndex):
        columnMatrix = np.full(9, 0)
        for i in range(0, 9):
            columnMatrix[i] = self.sudokuMatrix[i][columnIndex]
        return columnMatrix


    def generate_Matrix_1(self):
        currentRowIndex = 0
        lastFoundRow = list(np.full(9, 0))

        while(currentRowIndex < 9):
    
            currentColumnIndex = 0

            while(currentColumnIndex < 9):
                currentRow = self.getRowMatrix(currentRowIndex)
                currentColumn = self.getColumnMatrix(currentColumnIndex)
                currentSubmatrix = self.getSubMatrix(currentRowIndex, currentColumnIndex)

                unionSet = set([1,2,3,4,5,6,7,8,9]).difference(set.union(set(currentRow), set(currentColumn), set(currentSubmatrix)))
                unionSet.discard(0)

                if (len(unionSet) > 0):
                    takenValue = random.choice(list(unionSet))
                    self.sudokuMatrix[currentRowIndex][currentColumnIndex] = takenValue
                    currentColumnIndex = currentColumnIndex + 1
                else:
                    if ((lastFoundRow == self.sudokuMatrix[currentRowIndex]).all()):
                        currentRowIndex = 0
                        currentColumnIndex = 100  # Set currentColumnIndex to big value to reset WHILE-loop
                        self.sudokuMatrix = np.full((9, 9), 0)
                    else:
                        currentColumnIndex = 0
                        lastFoundRow = self.sudokuMatrix[currentRowIndex]
                        self.sudokuMatrix[currentRowIndex] = [0,0,0,0,0,0,0,0,0]

            if (currentColumnIndex != 100):
                currentRowIndex = currentRowIndex + 1

        return self.sudokuMatrix


sudokuMatrixGenerator = SudokuMatrixGenerator()
#sudokuMatrixGenerator.generate_Matrix()
print(sudokuMatrixGenerator.generate_Matrix_1())