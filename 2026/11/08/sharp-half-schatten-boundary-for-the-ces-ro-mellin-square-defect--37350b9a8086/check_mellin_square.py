#!/usr/bin/env python3
"""Finite checks for the sharp Cesaro--Mellin square defect (not an infinite proof)."""
import math
from fractions import Fraction

GAMMA = 0.577215664901532860606512090082402431
count = 0

def check(condition, label):
    global count
    assert condition, label
    count += 1

for size in range(1, 111):
    hs = [Fraction(0)]
    for a in range(1, size + 1):
        hs.append(hs[-1] + Fraction(1, a))
    for a in range(1, size + 1):
        for b in range(1, a + 1):
            directly = sum((Fraction(1, a * ell) for ell in range(b, a + 1)), Fraction(0))
            via_harmonics = (hs[a] - hs[b-1]) / a
            check(directly == via_harmonics, ("square", a, b))
            direct_defect = float(directly) - math.log(a / b) / a
            h = float(hs[a]) - math.log(a) - GAMMA
            g = GAMMA + math.log(b) - float(hs[b-1])
            reconstructed = (h + g) / a
            check(abs(direct_defect - reconstructed) < 3e-14, ("defect", a, b))
    check(via_harmonics == Fraction(1, size * size), ("diagonal", size))
    h = float(hs[size]) - math.log(size) - GAMMA
    g = 1.0 / size - h
    check(0.0 < h < 1.0 / size and 0.0 < g < 1.0 / size, ("positive", size))
    if size > 1:
        k = size * math.log(size / (size - 1)) - 1
        check(0.0 < k <= 1.0 / (size - 1) + 1e-13, ("lower", size))

# Verify the finite inverse identity, with a small numerical matrix multiplication.
try:
    import numpy as np
except ImportError:
    np = None
if np is not None:
    for n in (1, 2, 3, 4, 8, 16, 32, 64, 128):
        a = np.arange(n, 2*n, dtype=float)
        H = np.cumsum(1.0 / np.arange(1, 2*n, dtype=float))
        h = np.array([H[int(t)-1] - math.log(t) - GAMMA for t in a])
        g = 1.0 / a - h
        E = np.tri(n) * ((h[:, None] + g[None, :]) / a[:, None])
        delta = np.eye(n) - np.eye(n, k=-1)
        K = np.zeros((n, n))
        for i in range(1, n):
            K[i, :i] = a[i] * (h[i-1] - h[i])
        target = np.diag(1.0 / a) @ (np.eye(n) - K)
        obtained = delta @ np.diag(a) @ E
        check(np.max(np.abs(obtained-target)) < 1e-10, ("inverse_identity", n))
        smin = np.linalg.svd(E, compute_uv=False)[-1]
        check(smin >= 1.0 / (8.0 * math.e * n * n) * (1-1e-6), ("finite_lower", n))

print(f"MELLIN_SQUARE_DEFECT_FINITE_OK {count}")
