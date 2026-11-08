"""Standalone numerical and exact finite checks for a two-mode Fourier sampling tail theorem.

This script tests selected algebraic identities and asymptotic consistency.
The proof of the all-sample-size tail law is analytic, not based on these tests.
Requires Python 3 standard library only.
"""
import cmath
import itertools
import math
from fractions import Fraction as F


def determinant(matrix):
    a = [[F(x) for x in row] for row in matrix]
    n = len(a)
    d = F(1)
    for k in range(n):
        j = next((i for i in range(k, n) if a[i][k]), None)
        assert j is not None
        if j != k:
            a[j], a[k] = a[k], a[j]
            d = -d
        pivot = a[k][k]
        d *= pivot
        for i in range(k + 1, n):
            t = a[i][k] / pivot
            for h in range(k + 1, n):
                a[i][h] -= t * a[k][h]
            a[i][k] = F(0)
    return d


def threshold_constant(m):
    d = m - 1
    return m ** (m / 2) / (math.pi ** (d / 2) * math.gamma(d / 2 + 1))


checks = 0
for m in range(2, 13):
    d = m - 1
    B = [[F(int(i == j)) - F(1, m) for j in range(d)] for i in range(d)]
    assert determinant(B) == F(1, m)
    checks += 1
    vectors = [tuple(range(1, d + 1)), tuple(((-1) ** i) * (i + 2) for i in range(d))]
    for v in vectors:
        w = (0,) + v
        left = sum((w[i] - w[j]) ** 2 for i in range(m) for j in range(i + 1, m))
        right = sum(m * B[i][j] * v[i] * v[j] for i in range(d) for j in range(d))
        assert left == right
        checks += 1

# Explicit exact distribution in the two-sample case, evaluated independently
# against a deterministic angular quadrature.
for t in (1.2, 2.0, 5.0, 10.0, 20.0):
    formula = 4 / math.pi * math.atan(1 / t)
    ngrid = 40000
    count = 0
    for j in range(ngrid):
        theta = 2 * math.pi * (j + 0.5) / ngrid
        modulus = abs(1 + cmath.exp(1j * theta))
        kap = math.sqrt((2 + modulus) / (2 - modulus))
        count += (kap > t)
    assert abs(count / ngrid - formula) < 0.00006
    checks += 1

# Deterministic torus quadrature of the two-dimensional tail domain, m=3.
# Its convergence to a sharp local-ellipsoid asymptotic is not used as proof.
N = 640
for t in (6.0, 12.0):
    n_event = 0
    for i in range(N):
        u = cmath.exp(1j * (2 * math.pi * (i + 0.5) / N))
        for j in range(N):
            v = cmath.exp(1j * (2 * math.pi * (j + 0.5) / N))
            r = abs(1 + u + v)
            if (3 + r) / (3 - r) > t * t:
                n_event += 1
    empirical = n_event / (N * N)
    predicted = threshold_constant(3) / (t * t)
    assert abs(empirical / predicted - 1) < 0.04, (t, empirical, predicted)
    checks += 1

# Local quadratic approximation with phase lift, independent of quadrature.
for m in range(2, 9):
    d = m - 1
    v0 = [(-1) ** j * (j + 1) for j in range(d)]
    Bquad = sum(F(int(i == j)) * v0[i] * v0[j] - F(1, m) * v0[i] * v0[j]
                for i in range(d) for j in range(d))
    for h in (0.001, 0.0002):
        z = 1 + sum(cmath.exp(1j * h * x) for x in v0)
        ratio = (m - abs(z)) / (0.5 * h * h * float(Bquad))
        assert abs(ratio - 1) < 0.001, (m, h, ratio)
        checks += 1

assert abs(threshold_constant(2) - 4 / math.pi) < 1e-14
assert abs(threshold_constant(3) - 3 * math.sqrt(3) / math.pi) < 1e-14
assert abs(threshold_constant(4) - 64 / (3 * math.pi**2)) < 1e-14
checks += 3
print(f"VERIFY_OK: {checks} analytic-identity/numerical-consistency groups; m=2 exact tail; m=3 deterministic torus integrals")
