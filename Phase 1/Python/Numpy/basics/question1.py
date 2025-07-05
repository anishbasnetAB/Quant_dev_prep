# 1. **Create a NumPy array** with integers from 1 to 20. Reshape it into a 4x5 matrix.
import numpy as np

arr = np.arange(1, 21)
print(arr)

arr = arr.reshape(4,5)
print(arr)

# 2. Extract the **third row** and the **second column** of the matrix created above.
print(arr[2])

print(arr[:,1])
