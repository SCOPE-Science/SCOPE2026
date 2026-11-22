#!/usr/bin/env python3
"""Supplementary checks for an exact Bergman Toeplitz hyponormality boundary.

Uses only the Python standard library. Finite checks are not substitutes for the
all-index rational inequality and negative-vector proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def a(n):
    return sqrt((n + 1) / (n + 3)) if n >= 0 else 0.0


def b(n):
    return sqrt(n * (n + 1)) / (n + 2) if n >= 1 else 0.0


def D(n):
    return F(4, (n + 1) * (n + 3)) if n >= 2 else [F(1, 3), F(1, 2)][n]


def E(n):
    return -F((n + 1) * (3 * n + 8), (n + 2) ** 2 * (n + 3) ** 2)


def O(n):
    return 2 * sqrt((n + 1) / (n + 4)) / ((n + 3) * (n + 5)) if n >= 0 else 0.0


def P(n):
    return 13*n**4 + 79*n**3 + 89*n**2 - 175*n - 270


assert P(3) == 3192
assert [F(1, 3) + F(4, 9)*E(0), F(1, 2)+F(4, 9)*E(1),
        D(2)+F(4,9)*E(2)] == [F(19,81), F(35,81), F(11,50)]
assert F(19,81)-F(4,45) == F(59,405)
assert F(35,81)-F(1,18) == F(61,162)
assert F(11,50)-F(4,105) == F(191,1050)

nchecks = 0
for n in range(3, 1203):
    symbolic_bound = (D(n) + F(4,9)*E(n) - F(4, 3*(n+3)*(n+5))
                      - F(4, 3*n*(n+2)))
    exact_polynomial = F(4*P(n), 9*n*(n+1)*(n+2)**2*(n+3)**2*(n+5))
    assert symbolic_bound == exact_polynomial and symbolic_bound > 0
    shifted_coeff = (13*(n-3)**4+235*(n-3)**3+1502*(n-3)**2
                     +3896*(n-3)+3192)
    assert P(n) == shifted_coeff
    nchecks += 2

for n in range(1203):
    assert isclose(a(n)**2-a(n-2)**2, float(D(n)), abs_tol=3e-14)
    assert isclose(b(n)**2-b(n+1)**2, float(E(n)), abs_tol=3e-14)
    assert isclose(a(n)*b(n+3)-a(n+1)*b(n+1), O(n), abs_tol=3e-14)
    critical = float(D(n) + F(4,9)*E(n))
    off = F(2,3)*(O(n)+O(n-3))
    assert critical >= float(off)-1e-13
    nchecks += 4

# Direct operator action against the exact self-commutator quadratic form.
# End-points are treated as projections of the infinite operator, not as
# hard truncations of its adjoint.
for t in (0.0, 1/4, 2/3, 7/10):
    x = [(-1.0)**k/(k+1.0) for k in range(45)]
    T_x = [0.0]*50
    Tstar_x = [0.0]*50
    for n,v in enumerate(x):
        T_x[n+2] += a(n)*v
        if n>=1: T_x[n-1] += t*b(n)*v
        if n>=2: Tstar_x[n-2] += a(n-2)*v
        Tstar_x[n+1] += t*b(n+1)*v
    direct = sum(v*v for v in T_x)-sum(v*v for v in Tstar_x)
    identity = sum((float(D(n))+t*t*float(E(n)))*v*v for n,v in enumerate(x))
    identity += sum(2*t*O(n)*x[n]*x[n+3] for n in range(len(x)-3))
    assert isclose(direct,identity,rel_tol=2e-12,abs_tol=2e-12)
    nchecks += 1

# Explicit finite negative witnesses for ratios beyond the sharp boundary.
for t in (0.68, 0.70, 0.80, 1.00):
    length = 1000 if t<.69 else 90
    N = 20000
    diagonal = sum(float(D(N+3*j)) + t*t*float(E(N+3*j)) for j in range(length)) / length
    off = sum(O(N+3*j) for j in range(length-1))
    quadratic = diagonal - 2*t*off/length
    assert quadratic < 0, (t,quadratic)
    nchecks += 1

print(f"PASS: {nchecks} supplementary identities and positivity/witness tests")
