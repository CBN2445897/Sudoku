import numpy as np
import random
import copy

class SudokuMatrixGenerator():

    def __init__(self):
        # Create 9x9 matrix with default value of 0
        self.__defaultSudokuMatrix = np.full((9, 9), 0)
        self.__sudokuMatrix = self.__defaultSudokuMatrix


    def generateMatrix(self):
        self.__generateSudokuMatrixWithoutValilationSubcell()
        return self.__sudokuMatrix;


    def __generateSudokuMatrixWithoutValilationSubcell(self):
        self.__sudokuMatrix = self.__defaultSudokuMatrix

        for row in range(0,9): 
            isSuccessful = False
            self.__sudokuMatrix[row] = [0,0,0,0,0,0,0,0,0]
            while (isSuccessful == False):
                poolOfNumber = [1,2,3,4,5,6,7,8,9]
                for currentColumn in range(0,9): 

                    # When only having one number left, skip randomize
                    if len(poolOfNumber) == 1: 
                        takenIndex = 0
                    else:
                        takenIndex = random.randint(0, (len(poolOfNumber) - 1))

                    takenValue = poolOfNumber[takenIndex]
                    isSuccessful = True

                    if row > 0:
                        for lastRow in range(0, row):
                            if (self.__sudokuMatrix[lastRow][currentColumn] == takenValue): 
                                isSuccessful = False
                    
                    if (isSuccessful == True):
                        self.__sudokuMatrix[row][currentColumn] = takenValue
                        poolOfNumber.remove(takenValue)
                    else:
                        break


    def __validateSudokuMatrixSubcell(self):
        isValid = False
        checkCount = 0

        while (checkCount < 300):
            self.__randomlySwapSudokuMatrix()
            sumMatrix = self.__calculateSumOfSubcell()
            if (self.__checkSumOfSubcell(sumMatrix) == False):
                checkCount = checkCount + 1
            else:
                checkCount = 999
                isValid = True

        return isValid


    def __randomlySwapSudokuMatrix(self):
        poolOfIndex = [0,1,2,3,4,5,6,7,8]
        firstIndexRow = random.randint(0, 8)
        poolOfIndex.remove(poolOfIndex[firstIndexRow])
        secondIndexRow = random.randint(0, 7)
        temp = self.__sudokuMatrix[firstIndexRow].copy()
        self.__sudokuMatrix[firstIndexRow] = self.__sudokuMatrix[secondIndexRow].copy()
        self.__sudokuMatrix[secondIndexRow] = temp.copy()

        self.__sudokuMatrix.transpose()
        poolOfIndex = [0,1,2,3,4,5,6,7,8]
        firstIndexRow = random.randint(0, 8)
        poolOfIndex.remove(poolOfIndex[firstIndexRow])
        secondIndexRow = random.randint(0, 7)
        temp = self.__sudokuMatrix[firstIndexRow].copy()
        self.__sudokuMatrix[firstIndexRow] = self.__sudokuMatrix[secondIndexRow].copy()
        self.__sudokuMatrix[secondIndexRow] = temp.copy()
        self.__sudokuMatrix.transpose()


    def __checkSumOfSubcell(self, sumMatrix):
        for i in range(0,3):
            for j in range(0,3):
                if (sumMatrix[i][j] != 15):
                    return False

        return True


    def __calculateSumOfSubcell(self):
        sumMatrix = np.full((3, 3), 0)

        for i in range(0,3):
            for j in range(0,3):
                lowerLimitX, upperLimitX = i*3 + 0, i*3 + 2
                lowerLimitY, upperLimitY = j*3 + 0, j*3 + 2
                sumMatrix[i][j] = np.sum(self.__sudokuMatrix[lowerLimitX:upperLimitX,lowerLimitY:upperLimitY])

        return sumMatrix


############################################
smg = SudokuMatrixGenerator()
print(smg.generateMatrix())
