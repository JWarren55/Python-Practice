a = [3, 4]
b = [6, 8]

def dot_product(a, b):
    """
    Calculate the dot product of 2 vectors
    
    Args:
        a: first vector
        b: second vector
        
    Returns:
        Dot of 2 Vectors
        
    Raises:
        Value Error, if length do not match
    """
    
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    total = 0
    for i in range(len(a)):
        total += (a[i] * b[i])
    
    return total

print(dot_product(a, b))