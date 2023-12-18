import numpy as np
import sympy as sp

def calcGauss(matrix):
    m = sp.Matrix(matrix)
    m_gauss, k = m.rref()

    # Convert SymPy matrix to NumPy array and round the values
    m_gauss_np = np.array(m_gauss).astype(float)
    rounded_array = np.round(m_gauss_np, 2)

    return rounded_array

matrix = [
    [3, 7, 2, 5],
    [1, 4, 8, 2],
    [6, 9, 3, 7]
]


