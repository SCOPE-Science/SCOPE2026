"""Numerical checks of the exact two-erasure Chebyshev--Gauss sampling theorem.
Run: python3 check_dct.py (requires NumPy).
Finite tests supplement, and do not replace, the all-N analytical inequalities.
"""
import itertools
import math
import numpy as np


def data(N, j, k):
    theta = math.pi * (np.arange(N) + 0.5) / N
    U = None
    B = math.sqrt(2/N) * np.array([[(-1)**t*math.sin(2*theta[t]),
                                     (-1)**t*math.sin(theta[t])] for t in [j, k]])
    trace = float(np.sum(B*B))
    delta = float(np.linalg.det(B)**2)
    lam_minus = 2 * delta / (trace + math.sqrt(max(0., trace*trace-4*delta)))
    lam_plus = trace - lam_minus
    return U, lam_minus, lam_plus, delta


checks = 0
for N in range(4, 21):
    rows = {}
    for j, k in itertools.combinations(range(N), 2):
        U, lmin, lmax, delta = data(N, j, k)
        theta = math.pi * (np.arange(N) + 0.5) / N
        U = np.stack([math.sqrt((1 if r == 0 else 2) / N)
                      * np.cos(r * theta) for r in range(N)], axis=1)
        assert np.max(np.abs(U.T @ U - np.eye(N))) < 1e-12
        keep = [i for i in range(N) if i not in (j, k)]
        A = U[np.ix_(keep, range(N-2))]
        evals = np.linalg.eigvalsh(A.T @ A)
        wanted = np.sort(np.array([lmin, lmax]+[1.0]*(N-4)))
        assert np.max(np.abs(evals-wanted)) < 2e-11, (N, j, k, evals, wanted)
        assert abs(float(np.linalg.det(A))**2 - delta) < 2e-11
        assert lmin > 0
        rows[(j,k)] = lmin
        checks += 4
    minima = sorted(rows, key=rows.get)
    assert set(minima[:2]) == {(0,1),(N-2,N-1)}
    assert abs(rows[(0,1)] - rows[(N-2,N-1)]) < 1e-12
    checks += 2

for N in [21, 30, 50, 100, 200]:
    values = {}
    for j,k in itertools.combinations(range(N),2):
        _, lmin, _, _ = data(N,j,k)
        values[(j,k)] = lmin
    assert set(sorted(values,key=values.get)[:2]) == {(0,1),(N-2,N-1)}
    checks += 1

limit = 9*math.pi**6/25
for N in [100, 200, 400]:
    lam = data(N,0,1)[1]
    assert abs(lam*N**7/limit-1) < 0.01
    checks += 1
print('PASS:',checks,'finite checks; sharp asymptotic constant',limit)
