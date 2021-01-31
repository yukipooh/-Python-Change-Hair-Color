import numpy as np

ndr = np.ndarray((2,5))
for i in range(2):
    for j in range(5):
        ndr[i,j] = j
print(ndr.item(9))