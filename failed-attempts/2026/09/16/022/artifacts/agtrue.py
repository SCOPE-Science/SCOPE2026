"""Corrected Hess^3 (true derivatives: extra gam! factor) + search."""
import numpy as np
from agcore import M, IDX, monomials, eval_points, catalecticant, hvector
import math

F3 = {e: math.factorial(e[0]) * math.factorial(e[1]) * math.factorial(e[2]) for e in M[3]}


def hess3_true_tensor(c):
    """T[i,j,k] = c_{gam+e_k} * (gam_k+1) * gam!  (TRUE order-6 derivatives)."""
    T = np.zeros((10, 10, 3))
    idx7 = IDX[7]
    for i, a in enumerate(M[3]):
        for j, b in enumerate(M[3]):
            gam = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
            gf = math.factorial(gam[0]) * math.factorial(gam[1]) * math.factorial(gam[2])
            for k in range(3):
                A = list(gam)
                A[k] += 1
                T[i, j, k] = c[idx7[tuple(A)]] * (gam[k] + 1) * gf
    return T


def hess3_true_at(T, y):
    return T[:, :, 0] * y[0] + T[:, :, 1] * y[1] + T[:, :, 2] * y[2]
