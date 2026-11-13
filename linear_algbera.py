import math
import numpy as np

a = np.array([3, 4])
b = np.array([6, 8])

def dot_product(a, b):
    # if len(a) != len(b):
    #     raise ValueError("Vectors must have the same length")
    # total = 0
    # for i in range(len(a)):
    #     total += (a[i] * b[i])
    return sum(a * b)

def magnitude(vector):
    ## math.sqrt(sum(np.square(vector)))
    return np.linalg.norm(vector)

print(dot_product(a, b))

print(magnitude(a))