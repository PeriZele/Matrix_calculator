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



matrix = [
    [3, 7, 2],
    [1, 4, 8],
    [6, 9, 3]
]

calcRank(matrix)
