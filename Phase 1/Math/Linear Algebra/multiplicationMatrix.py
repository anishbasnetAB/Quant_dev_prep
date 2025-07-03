def multiplicationMatrix(A, B):
    # Step 1: Check if multiplication is possible
    if len(A[0]) != len(B):
        print("Matrix dimensions do not allow multiplication")
        return None

    # Step 2: Create an empty result matrix
    result = []
    
    # Step 3: Loop through rows of A
    for i in range(len(A)):
        row = []
        
        # Step 4: Loop through columns of B
        for j in range(len(B[0])):
            sum_product = 0
            
            # Step 5: Compute the dot product of row A[i] and column B[][j]
            for k in range(len(B)):
                sum_product += A[i][k] * B[k][j]
            
            # Step 6: Add the computed value to the current row
            row.append(sum_product)
        
        # Step 7: Add the row to the result matrix
        result.append(row)

    return result

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print(multiplicationMatrix(A, B))