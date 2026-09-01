import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    m = len(x)
    sum = 0
    for i in range(m):
        product = x[i] * y[i]
        sum += product
    return float(sum)
    