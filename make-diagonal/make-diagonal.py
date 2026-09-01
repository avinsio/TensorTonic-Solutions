import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    m = len(v)
    matrix = np.zeros((m,m))
    for i in range(m):
        matrix[i,i] = v[i]
    return matrix