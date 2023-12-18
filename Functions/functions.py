import numpy as np
from scipy.linalg import lu
import sympy as sp

def calcDeterminant(matrix):
    return np.round(np.linalg.det(np.matrix(matrix)),2)


def calcGauss(matrix):
    m = sp.Matrix(matrix)
    m_gauss, k = m.rref()
    m_gauss_np = np.array(m_gauss).astype(float)
    rounded_array = np.round(m_gauss_np, 2)

    return rounded_array


def calcInverse(matrix):
    return np.round((np.linalg.inv(np.matrix(matrix))),2) 



def calcRank(matrix):
    return np.linalg.matrix_rank(np.matrix(matrix))


def calcTranspose(matrix):
    return np.matrix.transpose(np.matrix(matrix))
    
    


def calcMultiply(matrix_1, matrix_2):
    try:
        return np.matmul(matrix_1,matrix_2)
    except:
        return np.matmul(matrix_2,matrix_1)

def calcAdd(matrix_1, matrix_2):
    for i, row in enumerate(matrix_1):
        for k, element in enumerate(row):
            matrix_1[i][k] += matrix_2[i][k]

    return np.matrix(matrix_1)

matrix = [
    [3, 7, 2],
    [1, 4, 8],
    [6, 9, 3]
]

matrix2 = [
    [3, 7, 2],
    [1, 4, 8],
    [6, 9, 4]
]


calcAdd(matrix, matrix2)



