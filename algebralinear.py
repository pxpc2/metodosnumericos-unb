import numpy as np
import matplotlib as plt

# Resolver o sistema:
# 2x + y + 3z = 4
# -1x + 3y + 2z = 3
# 3x + y - 3z = 2

A = np.array([[2, 1, 3], [-1, 3, 2], [3, 1, -3]])
b = np.array([4, 3, 2])
Ai = np.linalg.inv(A)
r = Ai @ b
print(r)


def cofat(m):
    n = len(m)
    cof = np.zeros((n, n))
    for col in range(n):
        for lin in range(n):
            d_ij = np.delete(m, lin, 0)
            d_ij = np.delete(d_ij, col, 1)
            det = np.linalg.det(d_ij)
            cof[lin][col] = (-1)**(lin+col)*det
    return cof


def adjuta(m):
    return cofat(m).transpose()


def inv_cofat(m):
    return (1/np.linalg.det(m)) * adjuta(m)


A = np.array([[2, 1, 3], [-1, 3, 2], [3, 1, -3]])
Ai1 = np.linalg.inv(A)
Ai2 = inv_cofat(A)
print("Ai com linalg:\n", Ai1, "\nAi com inv_cofat:\n", Ai2)

