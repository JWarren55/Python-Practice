import math
import numpy as np

a = np.array([3, 4])
b = np.array([6, 8])

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    # total = 0
    # for i in range(len(a)):
    #     total += (a[i] * b[i])
    return sum(a * b)

def magnitude(vector):
    ## math.sqrt(sum(np.square(vector)))
    return np.linalg.norm(vector)

def cosine_similarity(a, b):
    mag_a = magnitude(a)
    mag_b = magnitude(b)

    if mag_a == 0 or mag_b == 0:
        raise ValueError("Cannot calculate cosine similarity with a zero vector")
    return (dot_product(a, b) /
            np.dot(mag_a(a), mag_b(b)) )

print(dot_product(a, b))

print(magnitude(a))

print(cosine_similarity(a, b))