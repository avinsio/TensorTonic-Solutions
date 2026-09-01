import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    m = len(x)
    total = 0
    for i in range(m):
        d = abs(x[i]- y[i])
        total += d
    return float(total)