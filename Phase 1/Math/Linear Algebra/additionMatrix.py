def addition_matrix(A, B):
    result = []

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Length does not match")
        return None

    for i in range(len(A)):
        row_sum = []
        for j in range(len(A[0])):  # Fix here: loop through columns
            row_sum.append(A[i][j] + B[i][j])
        result.append(row_sum)
    return result

# Function to take 2D input from user
def read_matrix(rows, cols):
    matrix = []
    print(f"Enter {rows} rows of {cols} integers separated by spaces:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            raise ValueError("Row length doesn't match number of columns.")
        matrix.append(row)
    return matrix

# Take matrix sizes
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Read two matrices
print("Matrix A:")
A = read_matrix(rows, cols)

print("Matrix B:")
B = read_matrix(rows, cols)

# Add and print result
print("Sum of the matrices:")
result = addition_matrix(A, B)
for row in result:
    print(row)
