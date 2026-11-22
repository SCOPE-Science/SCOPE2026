"""Finite numerical corroboration for axial heat covariance band thresholds.

Requires Python 3 with NumPy and SciPy. No assertions about infinite theorems
are inferred from finite computations.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def coupling(ell, m=0):
    return math.sqrt(((ell + 1) ** 2 - m ** 2) / ((2 * ell + 1) * (2 * ell + 3)))


def top_band(L, t, m=0):
    off = np.array([2 * coupling(ell, m) * math.cosh(t * (ell + 1))
                    for ell in range(m, L)], dtype=float)
    if not len(off):
        return 0.0
    return float(eigh_tridiagonal(np.zeros(len(off) + 1), off,
                                 select='i', select_range=(len(off), len(off)),
                                 eigvals_only=True)[0])


def geometric_top(q, n=200):
    off = np.array([q ** j for j in range(n)], dtype=float)
    return float(eigh_tridiagonal(np.zeros(n + 1), off,
                                 select='i', select_range=(n, n),
                                 eigvals_only=True)[0])


assert abs(coupling(0) - 1 / math.sqrt(3)) < 1e-14
assert abs(coupling(1) - 2 / math.sqrt(15)) < 1e-14
for t0 in (0.4, 1.0):
    assert abs(1/top_band(1,t0) - math.sqrt(3)/(2*math.cosh(t0))) < 1e-12
    low2 = 1/math.sqrt((4/3)*math.cosh(t0)**2+(16/15)*math.cosh(2*t0)**2)
    assert abs(1/top_band(2,t0)-low2) < 1e-12
for t in (0.25, 0.5, 1.0, 1.5):
    q = math.exp(-t)
    rho = geometric_top(q)
    assert math.sqrt(1 + q * q) < rho < 1 + q
    prev = float('inf')
    for L in (2, 3, 4, 5, 8, 12, 20, 32, 64, 128):
        lam = top_band(L, t)
        eps = 1 / lam
        assert eps < prev
        prev = eps
        if L <= 12:
            assert all(top_band(L, t, m) < lam for m in range(1, L + 1))
        if L >= 32:
            calibrated = eps * rho * math.exp(t * L) / 2
            # Expected relative correction: 1 - 1/(8 L^2) + O(L^-3).
            assert abs(calibrated - (1 - 1 / (8 * L * L))) < 0.02 / L**2
    for ell in (12, 20, 40):
        # A nonzero tilt eventually makes a two-by-two principal form indefinite.
        edge = 2 * coupling(ell) * math.cosh(t * (ell + 1))
        assert edge > 1
print('PASS: zonal dominance, strict finite-band cutoffs, geometric Jacobi edge law, and high-mode obstructions')
