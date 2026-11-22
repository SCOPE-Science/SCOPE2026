"""Reproducible supplementary checks for a finite-support Foguel coupling theorem.

Requires Python 3, NumPy, SciPy. No experiment certifies the infinite case.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import bmat, csr_matrix, diags
from scipy.sparse.linalg import eigsh


def green0(n):
    k = np.arange(1, n + 1)
    return 2.0 * np.minimum.outer(k, k)


def green(s, n):
    i = np.arange(n)
    return (np.exp(-s * abs(i[:, None] - i[None, :]))
            - np.exp(-s * (i[:, None] + i[None, :] + 2))) / math.sinh(s)


def compressed_norm(g, a):
    L = np.linalg.cholesky(g)
    return np.linalg.norm(L.T @ a @ L, 2)


def jacobi_top(a, t, extent=170):
    n = len(a)
    J = diags([np.full(extent - 1, .5)] * 2, [-1, 1], format="csr")
    T = np.zeros((extent, extent))
    T[:n, :n] = a * (t / 2)
    H = bmat([[J, csr_matrix(T)], [csr_matrix(T.T), J]], format="csr")
    return eigsh(H, k=1, which="LA", return_eigenvectors=False, tol=1e-9)[0]


def run():
    rng = np.random.default_rng(20261119)
    checked = 0
    for n in (1, 2, 3, 4, 7):
        for _ in range(10):
            a = rng.random((n, n))
            a[a < .5] = 0
            if not a.any():
                continue
            critical = 2 / compressed_norm(green0(n), a)
            for f in (.65, 1., 1.3):
                got = jacobi_top(a, critical * f)
                if f <= 1:
                    assert got < 1.0002, (n, f, got)
                else:
                    assert got > 1.000001, (n, f, got)
                checked += 1
    for i, j in ((0, 0), (0, 1), (2, 3), (9, 4)):
        tc = 1 / math.sqrt((i + 1) * (j + 1))
        for t in (1.1 * tc, 1.5 * tc, 4 * tc):
            def t_of_s(s):
                return 2 * math.sinh(s) / math.sqrt(
                    (-math.expm1(-2 * (i + 1) * s))
                    * (-math.expm1(-2 * (j + 1) * s)))
            s = brentq(lambda ss: t_of_s(ss) - t, 1e-9, 10)
            assert abs(t_of_s(s) - t) < 1e-9
            checked += 1
    G = green0(2)
    assert np.allclose(G, [[2, 2], [2, 4]])
    for a, b in ((0., .7), (.3, .2), (.5, .5), (.4142135623730951, .4142135623730951)):
        T = np.array([[0., a], [b, 0.]])
        M = np.linalg.inv(G) - T.T @ G @ T / 4
        formula = 1 - 2*a*a - 2*a*b - 2*b*b + a*a*b*b
        assert abs(np.linalg.det(M) - formula / 4) < 1e-12
        checked += 1
    assert np.linalg.norm(green(.00001, 5) - green0(5)) < .003
    print(f"PASS: {checked} finite numerical comparisons and exact two-way formula checks")


if __name__ == "__main__":
    run()
