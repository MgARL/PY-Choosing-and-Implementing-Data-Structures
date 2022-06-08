import numpy as np

a = np.array([1,3,3])

def sum(nArr):
    if len(nArr) == 1:
        return nArr[0]
    
    return nArr[0] + sum(nArr[1:])

print(sum(a))