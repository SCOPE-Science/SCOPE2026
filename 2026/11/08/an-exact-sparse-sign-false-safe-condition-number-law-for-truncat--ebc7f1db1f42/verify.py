"""Standalone arithmetic checks of the sparse-sign condition-screening example.

The infinite-parameter proof is in RESULT.md. This script checks finite
specializations and the exact sign-pattern census without external packages.
"""
from fractions import Fraction
from itertools import product
from math import comb, sqrt, isclose


def inner(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm(x):
    return sqrt(inner(x, x))


def matvec(A, v):
    return [inner(row, v) for row in A]


def add_scaled_outer(A, x, y, coef):
    n = len(x)
    for i in range(n):
        for j in range(n):
            A[i][j] += coef * x[i] * y[j]


for eps in [0.001, 0.01, 0.09]:
    n = 9
    u = [1.0, -1.0] + [0.0] * (n - 2)
    den = sqrt(2 + eps * eps)
    b1 = [a / den for a in u]
    b2 = [a / den for a in u]
    b1[2] += eps / den
    b2[3] += eps / den
    c = 2 / (2 + eps * eps)
    sig = eps * sqrt(4 + eps * eps) / (2 + eps * eps)
    assert abs(inner(b1, b2)-c) < 1e-12
    q1 = b1
    q2 = [(b2[i] - c * b1[i]) / sig for i in range(n)]
    q3 = [float(i == 4) for i in range(n)]
    assert abs(norm(q1) - 1) < 1e-12
    assert abs(norm(q2) - 1) < 1e-11
    assert abs(inner(q1, q2)) < 1e-11
    assert abs(inner(q3, q2)) < 1e-11
    d = eps * eps / 10
    A = [[float(i == j) for j in range(n)] for i in range(n)]
    add_scaled_outer(A, q1, q1, c - 1)
    add_scaled_outer(A, q1, q2, sig)
    add_scaled_outer(A, q2, q1, sig)
    add_scaled_outer(A, q2, q2, 1/c - 1)
    add_scaled_outer(A, q2, q3, d)
    add_scaled_outer(A, q3, q2, d)
    assert max(abs(v - w) for v, w in zip(matvec(A, b1), b2)) < 1e-11
    Ab2 = matvec(A, b2)
    assert abs(inner(Ab2, q3) - sig * d) < 1e-11
    assert sig * d > 0
    assert eps + 1.1 * eps * eps < 1
    kappa_B = sqrt((1 + c) / (1 - c))
    assert isclose(kappa_B, sqrt(4 + eps*eps) / eps, rel_tol=1e-9)

# Full exact enumeration of the signed columns when s=zeta=8.
zeta, s = 8, 8
signed = list(product((-1, 1), repeat=zeta))
assert len(signed) == comb(s, zeta) * 2**zeta == 256
anchor = signed[0]
nonparallel = 0
max_abs_dot = Fraction(0)
min_noncollision_dist2 = Fraction(99)
for signs in signed:
    rho = Fraction(sum(a*b for a, b in zip(anchor, signs)), zeta)
    if signs not in (anchor, tuple(-a for a in anchor)):
        nonparallel += 1
        max_abs_dot = max(max_abs_dot, abs(rho))
    else:
        assert abs(rho) == 1
    if signs != anchor:
        d2 = Fraction(sum((a-b)**2 for a, b in zip(anchor, signs)), zeta)
        min_noncollision_dist2 = min(min_noncollision_dist2, d2)
assert nonparallel == 254
assert max_abs_dot == Fraction(3,4)
assert min_noncollision_dist2 == Fraction(1,2)
assert sqrt((1+float(max_abs_dot))/(1-float(max_abs_dot))) < 10
assert (sqrt(float(min_noncollision_dist2)) - 0.01) / 0.01 > 10
assert Fraction(nonparallel, len(signed)**2) == Fraction(127,32768)

for s, z in [(8,8), (30,8), (8,4), (16,2)]:
    M = comb(s,z)*2**z
    p = Fraction(M-2, M*M)
    assert p > 0
    assert p == Fraction(1,M) * (1-Fraction(2,M))
    tau = max(10.0, sqrt(2*z-1))
    e = min(.01, sqrt(2/z)/(2*(tau+1)))
    assert e < sqrt(2/z)/(tau+1)
print("VERIFY_OK: SPD Krylov realization, six algebraic identities, 256 sign patterns, four exact probabilities")
