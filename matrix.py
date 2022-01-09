from typing import List
import math as m
from unittest import result


class martix_2x2:
    def __init__(self, ls):
        if type(ls) != list:
            raise TypeError("Must be List")
        elif len(ls) != 2:
            raise ValueError("Legth of matrix must be 2x2")
        elif len(ls[0]) != 2 or len(ls[1]) != 2:
            raise ValueError("Legth of matrix must be 2x2")
        else:
            for i in ls:
                for j in i:
                    if type(j) == str:
                        raise ValueError("Matrix can't have string")
            self._ls = ls

    def getlist(self):
        return self._ls

    def eig(self):
        b = (0-self._ls[0][0]) + (0 - self._ls[1][1])
        c = (0-self._ls[0][0]) * (0 - self._ls[1][1]) - \
            (self._ls[0][1] * self._ls[1][0])
        calbuf = b*b - 4*c
        x1 = ((b*-1) + m.sqrt(calbuf))/2
        x2 = ((b*-1) - m.sqrt(calbuf))/2
        return x1, x2

    def calreff(self, matrix):
        if matrix[0][0] != 1.0:
            for i in range(len(matrix)):
                if matrix[i][0] == 1.0:
                    buf = matrix[0]
                    matrix[0] = matrix[i]
                    matrix[i] = buf
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                if matrix[i][0] == 0:
                    calbuf = 0
                    for j in range(len(matrix[i])):
                        if matrix[i][j] != 0:
                            calbuf = matrix[i][j]
                            matrix[i][j] /= calbuf
        else:
            firstelm = matrix[0][0]
            matrix[0][0] /= firstelm
            if matrix[0][1] != 0:
                matrix[0][1] /= firstelm
                calbuf = 0
                for i in range(len(matrix)):
                    if matrix[len(matrix)-1][0] == 0 and matrix[len(matrix)-1][1] == 0:
                        break
                    else:
                        if i+1 < len(matrix):
                            calbuf = 0 - matrix[i+1][i]
                            matrix[i+1][0] = (calbuf * matrix[i]
                                              [0]) + matrix[i+1][0]
                            matrix[i+1][1] = (calbuf * matrix[i]
                                              [1]) + matrix[i+1][1]

        return matrix

    def find_nullspace(self, matrix):
        result = []
        for i in range(len(matrix)):
            
            havenum = False
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    havenum = True
            if havenum == False:
                matrix.pop(i)
                break
        
        
            
        if matrix[0][0] == 1.0:
            result.append(0-matrix[0][1])
            result.append(1)
        else:
            result.append(1)
            result.append(0-matrix[0][0])

        return result
                    
                        
                    
        

    def to2darray(self, matrix):
        result = []
        count = 0
        for i in range(0, len(matrix), 2):

            if i % 2 == 0:
                result.append([])
                result[count].append(matrix[i])
                result[count].append(matrix[i+1])
                count += 1
        return result

    def eigv(self):
        eigv = self.eig()
        matrix1 = [[self._ls[0][0] - eigv[0], self._ls[0][1]],
                   [self._ls[1][0], self._ls[1][1] - eigv[0]]]
        matrix2 = [[self._ls[0][0] - eigv[1], self._ls[0][1]],
                   [self._ls[1][0], self._ls[1][1] - eigv[1]]]
        
        v1 = self.find_nullspace(self.calreff(matrix1))
        v2 = self.find_nullspace(self.calreff(matrix2))
        result = v1+v2
        result = self.to2darray(result)

        return result