"""Reproducible finite diagnostics for dyadic Chebyshev singular-number bound.
The proof is analytic; finite calculations are only supplementary diagnostics.
"""
import math
import numpy as np

M = 16.0 / (7.0 * math.sqrt(3.0))
C_block = 4*M * (2/math.sqrt(3))
C_tail = math.sqrt(3/2)
assert C_block + C_tail < 8.0

checks = 0
max_ratio = 0.0
for N in (5, 10, 20, 40, 80):
    ix = np.arange(1, N+1, dtype=float)
    a = 1.0 / ((ix[:, None] * ix[None, :]) * (ix[:, None]+ix[None, :]-1.0))
    vals = np.linalg.eigvalsh(a)
    assert vals[-1] > 0
    # Finite section spectral stability: trace tail is nonnegative and bounded.
    for k in range(1, min(N, 10)):
        assert vals[-k] >= -1e-13
        assert vals[-k] <= 4 * math.log(2) - math.pi**2/6 + 1e-10
        checks += 1

for J in range(1, 7):
    L = J
    nmax = (1 << J) - 1
    xq, wq = np.polynomial.legendre.leggauss(320)
    xgrid = (xq + 1)/2
    wq = wq/2
    approx = np.zeros((nmax, len(xgrid)), dtype=float)
    actual = np.zeros_like(approx)
    for j in range(J):
        a = 1 << j
        nodes = np.cos((np.arange(L)+0.5)*math.pi/L)
        z = 1.5*a + 0.5*a*nodes
        F = np.array([xgrid**(t-1)/t for t in z])
        coeff = np.polynomial.chebyshev.chebfit(nodes, F, L-1)
        for n in range(a, 2*a):
            t = 2*n/a-3
            approx[n-1] = np.polynomial.chebyshev.chebval(t, coeff)
            actual[n-1] = xgrid**(n-1)/n
    diff = np.sqrt(np.sum((approx-actual)**2 * wq[None, :], axis=1))
    # Gauss quadrature diagnoses the Hilbert-space error, not pointwise error.
    for n in range(1, nmax+1):
        j = n.bit_length()-1
        a = 1 << j
        bound = 4*M * (a**-1.5) * 2**(-L)
        assert diff[n-1] < bound + 1e-10, (J,n,diff[n-1],bound)
        max_ratio = max(max_ratio, diff[n-1]/bound)
        checks += 1

# Exact trace identity through convergent positive series.
for N in (20, 100, 1000):
    s = sum(1.0/(n*n*(2*n-1)) for n in range(1,N+1))
    total = 4*math.log(2)-math.pi**2/6
    assert 0 < total-s <= 1.5/(N*N)
    checks += 1
print(f"PASS: {checks} finite checks; interpolation max bound fraction {max_ratio:.5g}; analytic constant {C_block+C_tail:.8f} < 8")
