import numpy as np
from numpy.linalg import det, inv

def usingNumpy():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    # Matrix Addition
    C = A + B
    print("Addition:\n", C)

    # Matrix Multiplication (dot product)
    C = np.dot(A, B)
    print("Multiplication (np.dot):\n", C)

    # Matrix Multiplication using @
    C = A @ B
    print("Multiplication (A @ B):\n", C)

    # Transpose
    C = A.T
    print("Transpose of A:\n", C)

    # Determinant
    D = det(A)
    print(f"Determinant of A: {D}")

    # Inverse
    A_inv = inv(A)
    print("Inverse of A:\n", A_inv)

# Call the function
usingNumpy()
