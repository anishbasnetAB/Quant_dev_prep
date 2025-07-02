📓 My Linear Algebra + Python Notes (Quant Prep)
Date: July 1, 2025

─────────────────────────────────────────────
🔹 Scalars, Vectors, and Matrices

• Scalar: Just a number. E.g., 5

• Vector: List of numbers (1D)
  Example: v = [1, 3, 5]

• Matrix: 2D list (rows × columns)
  Example: A = [[1, 2], [3, 4]]

─────────────────────────────────────────────
➕ Matrix Addition

Only works if matrices are the same shape.

Example:
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

A + B = [[6, 8],
         [10, 12]]

Python Code:

def addition_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Shape mismatch")
        return None
    result = []
    for i in range(len(A)):
        row = [A[i][j] + B[i][j] for j in range(len(A[0]))]
        result.append(row)
    return result

─────────────────────────────────────────────
✖️ Matrix Multiplication (A · B)

Rule: Multiply rows of A with columns of B
Only possible if: A's columns == B's rows

Example:
A = [[1, 2],
     [3, 4]]

B = [[2, 0],
     [1, 2]]

A · B = [[4, 4],
         [10, 8]]

Python Code:

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Incompatible dimensions")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

─────────────────────────────────────────────
🔄 Matrix Transpose

Flips rows into columns.

Example:
A = [[1, 2, 3],
     [4, 5, 6]]

Transpose:
[[1, 4],
 [2, 5],
 [3, 6]]

Python Code:

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

─────────────────────────────────────────────
📐 Determinant (2x2 only)

For matrix:
[[a, b],
 [c, d]]

Det = ad - bc

Python Code:

def determinant_2x2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

─────────────────────────────────────────────
🔁 Inverse (2x2 only)

Only valid if determinant ≠ 0

Inverse Formula:
1/(ad - bc) * [[d, -b], [-c, a]]

Python Code:

def inverse_2x2(matrix):
    det = determinant_2x2(matrix)
    if det == 0:
        raise ValueError("Matrix not invertible")
    a, b = matrix[0]
    c, d = matrix[1]
    return [[d/det, -b/det],
            [-c/det, a/det]]

─────────────────────────────────────────────
⚫ Dot Product

Multiply corresponding elements and sum.

Example:
[1, 2, 3] · [4, 5, 6] = 1*4 + 2*5 + 3*6 = 32

Python Code:

def dot_product(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

─────────────────────────────────────────────
🔢 Matrix × Vector

Multiply matrix with column vector.

Example:
A = [[1, 2],
     [3, 4]]

v = [2, 1]

A · v = [4, 10]

Python Code:

def matrix_vector_multiply(matrix, vector):
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]

─────────────────────────────────────────────
🧠 Things I Understood Clearly

• Matrix operations require shape compatibility.
• I can code all of these without NumPy — important for understanding how matrix math works internally.
• These operations relate directly to quant finance problems:
  - Dot product → portfolio return
  - Matrix mult → variance/covariance
  - Transpose/inverse → used in regression and factor models

─────────────────────────────────────────────
✅ What I Can Do Now

• Add, multiply, and transpose matrices in Python
• Compute dot products, determinants, and inverses (2x2)
• Apply linear algebra logic in finance

─────────────────────────────────────────────
