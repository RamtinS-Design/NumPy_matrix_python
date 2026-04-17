import numpy as np

matrix_a = np.array([[2, 3],[1, 4]])
matrix_b = np.array([[5, 2],[3, 1]])

print('Matrix A:')
print(matrix_a)

print('\nMatrix B:')
print(matrix_b)

multiplication = np.dot(matrix_a, matrix_b)

print('\nMatrix Multiplication (A * B):')
print(multiplication)

det_a = np.linalg.det(matrix_a)
det_b = np.linalg.det(matrix_b)

print('\nDeterminant of Matrix A:', det_a)
print('Determinant of Matrix B:', det_b)

coefficients = np.array([[2, 3],[1, 4]])
constants = np.array([5, 6])
solution = np.linalg.solve(coefficients, constants)

print('\nSolution of Linear Equations:')
print('x =', solution[0])
print('y =', solution[1])
