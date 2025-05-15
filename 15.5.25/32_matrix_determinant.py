import numpy as np

matrix = np.random.randint(1, 10, (4, 4))
determinant = np.linalg.det(matrix)

print("Matrix:\n", matrix)
print("Determinant:", determinant)