"""Finite diagnostics for a Gaussian Fock weighted-composition singular-value law.

Requirements: Python 3, numpy, scipy. Execute: python checker.py.
Finite truncations do not prove infinite-dimensional assertions.
"""
import math
import numpy as np
from scipy.special import gammaln


def parameters(a, t):
    X = (1 - a*a)**2 - t*t
    Y = (1 + a*a)**2 - t*t
    assert X > 0 and Y > 0 and 0 < a < 1 and 0 <= t < 1-a*a
    Lambda = 2 / (math.sqrt(X) + math.sqrt(Y))
    q = (math.sqrt(Y) - math.sqrt(X)) / (math.sqrt(Y) + math.sqrt(X))
    return X, Y, Lambda, q


def finite_section(a, t, size=120):
    mat = np.zeros((size, size), dtype=float)
    for n in range(size):
        for k in range((size - 1 - n)//2 + 1):
            j = n + 2*k
            if k == 0:
                mat[j, n] = a**n
            elif t > 0:
                mat[j, n] = math.exp(
                    n*math.log(a) + k*math.log(t/2) - gammaln(k+1)
                    + (gammaln(j+1) - gammaln(n+1))/2
                )
    return mat


def verify():
    tests = 0
    for a, t in [(0.6, 0.22), (0.3, 0.4), (0.8, 0.1),
                 (0.4, 0.2), (0.3, 0.65), (0.5, 0.0)]:
        X, Y, Lambda, q = parameters(a, t)
        M = finite_section(a, t)
        empirical = np.linalg.svd(M, compute_uv=False)
        exact = np.sqrt(Lambda)*q**(np.arange(9)/2)
        assert np.allclose(empirical[:9], exact, rtol=2e-7, atol=2e-10)
        tests += 9
        assert math.isclose(Lambda/(1-q), 1/math.sqrt(X), rel_tol=1e-11)
        assert math.isclose(Lambda**2/(1-q*q), 1/math.sqrt(X*Y), rel_tol=1e-11)
        tests += 2
        b = a*a/(1-t*t)
        d = b*t
        if d == 0:
            v = 0.0
        else:
            # Small quadratic root, evaluated without cancellation.
            H = 1+d*d-b*b
            v = 2*d/(H + math.sqrt(H*H-4*d*d))
        assert math.isclose(v, d + v*b*b/(1-d*v), abs_tol=2e-12)
        assert math.isclose(b/(1-d*v), q, rel_tol=1e-10)
        assert math.isclose(1/math.sqrt((1-t*t)*(1-d*v)), Lambda, rel_tol=1e-10)
        tests += 3
    # Scaling profile is evaluated independently from the finite-section SVD.
    a = 0.55
    edge = 1-a*a
    for delta in [1e-3, 1e-5, 1e-7]:
        _, _, Lambda, q = parameters(a, edge-delta)
        for u in [0.0, 0.2, 0.8, 1.7]:
            n = int(u/math.sqrt(delta))
            observed = math.sqrt(Lambda)*q**(n/2)
            predicted = a**(-0.5)*math.exp(-math.sqrt(2*edge)*u/(2*a))
            tolerance = 0.10 if delta == 1e-3 else 0.012 if delta == 1e-5 else 0.002
            assert abs(observed-predicted) < tolerance
            tests += 1
    print(f"PASS: {tests} finite checks; no infinite-dimensional certification claimed")


if __name__ == "__main__":
    verify()
