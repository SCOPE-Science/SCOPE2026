#!/usr/bin/env python3
"""Independent finite checks for disk-compression moment and spectral formulas."""
from fractions import Fraction
from math import sqrt, exp, gamma, e, isclose

checks = 0

def check(x):
    global checks
    assert x
    checks += 1


def exact_moments(n, q):
    """Integrate the actual orthonormal beta moments, using rational arithmetic."""
    m = Fraction(n + 1, n + 2)
    variance = Fraction(n + 1, (n + 2)**2 * (n + 3))
    a00 = q ** (n + 1)
    b_over_sqrt = -(1 - q) * a00
    c11 = Fraction(n + 1, 1) * (
        q ** (n + 3) / (n + 3)
        - 2 * m * q ** (n + 2) / (n + 2)
        + m * m * q ** (n + 1) / (n + 1)
    ) / variance
    return a00, b_over_sqrt, c11


def closed_moments(n, q):
    d = 1 - q
    return q ** (n+1), -d * q ** (n+1), q ** (n+1) * (1 - 2*d + (n+2)**2*d*d)

for n in range(15):
    cutoffs = [Fraction(1, 7), Fraction(1, 5), Fraction(1, 3),
               Fraction(1, 2), Fraction(2, 3), Fraction(4, 5)]
    for q in cutoffs:
        A = exact_moments(n, q)
        B = closed_moments(n, q)
        for x, y in zip(A, B):
            check(x == y)
        for r in cutoffs:
            C = exact_moments(n, r)
            # Offdiagonal commutator divided by sqrt((n+1)(n+3)).
            upper = C[1] * (A[0] - A[2]) + A[1] * (C[2] - C[0])
            expected = (n+2)**2 * (1-q) * (1-r) * (r-q) * (q*r)**(n+1)
            check(upper == expected)


def branch(n, q, r):
    return (sqrt((n+1)*(n+3)) * (n+2)**2
            * (1-q)*(1-r)*abs(r-q)*(q*r)**(n+1))

for a, b in [(1.0, 2.0), (0.5, 3.0), (2.5, 1.0)]:
    for eps in [0.04, 0.015, 0.006]:
        q, r = exp(-a*eps), exp(-b*eps)
        nmax = int(100.0 / (eps*(a+b))) + 1
        modes = [branch(n, q, r) for n in range(nmax)]
        lim_norm = 27*a*b*abs(a-b)/(e**3*(a+b)**3)
        check(isclose(max(modes), lim_norm, rel_tol=0.017))
        for p in [0.5, 1.0, 2.0]:
            left = eps * 2 * sum(s**p for s in modes)
            right = 2*gamma(3*p+1)*(a*b*abs(a-b))**p/(p*(a+b))**(3*p+1)
            check(isclose(left, right, rel_tol=0.017))

# Optimize the analytic boundary norm over rate ratios.
optimal = 3*sqrt(3)/(2*e**3)
for ratio in [0.1, 0.3, 0.6, 1.2, 1.9, 2+sqrt(3), 6.0, 50.0]:
    value = 27*ratio*abs(ratio-1)/(e**3*(ratio+1)**3)
    check(value <= optimal*(1+1e-13))
check(isclose(27*(2+sqrt(3))*(1+sqrt(3)) / (e**3*(3+sqrt(3))**3), optimal, rel_tol=1e-12))
print(f"PASS: {checks} exact-rational and supplementary numerical assertions")
