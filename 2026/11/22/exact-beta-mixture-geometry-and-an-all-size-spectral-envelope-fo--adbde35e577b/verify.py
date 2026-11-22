#!/usr/bin/env python3
"""Exact finite diagnostics for harmonic-descent occupation probabilities.

The general moment-mixture theorem is proved analytically; finite checks
here test the recurrence, the finite-difference formula, and consequences.
Python 3 standard library only; no network access.
"""
from fractions import Fraction
from math import comb

NMAX = 46
KMAX = 13
H = [Fraction(0)]
for n in range(1, NMAX + 1):
    H.append(H[-1] + Fraction(1, n))

# Route A: Markov chain first-step recursion.
p = [[Fraction(0) for _ in range(NMAX + 1)] for _ in range(NMAX + 1)]
for k in range(2, NMAX + 1):
    p[k][k] = Fraction(1)
    for n in range(k + 1, NMAX + 1):
        p[n][k] = sum((p[j][k] / (n-j) for j in range(k, n)), Fraction(0)) / H[n-1]

count = 0
for k in range(2, KMAX + 1):
    # Route B: exact finite-difference formula, which is independent of recursion.
    for n in range(k, NMAX + 1):
        direct = H[k-1] * comb(n-1, k-1) * sum(
            ((-1)**j * comb(n-k, j) / H[k+j-1]
             for j in range(n-k+1)), Fraction(0))
        assert direct == p[n][k], ("finite-difference identity", k, n)
        count += 1

    # Strict alternating differences for every permissible m and r <= 8.
    for r in range(1, 9):
        for m in range(0, NMAX-k-r+1):
            alt = sum(((-1)**j * comb(r,j) * p[k+m+j][k]
                       for j in range(r+1)), Fraction(0))
            assert alt > 0, ("strict complete monotonicity", k, m, r, alt)
            count += 1

    # Strict two-by-two Hankel positivity / log-convexity.
    for m in range(0,NMAX-k-1):
        lhs = p[k+m][k]*p[k+m+2][k]-p[k+m+1][k]**2
        assert lhs > 0, ("strict log-convexity", k, m)
        count += 1

    # Three-by-three Hankel minors are strictly positive for available indices.
    for m in range(0,min(11,NMAX-k-4)):
        a = [[p[k+m+i+j][k] for j in range(3)] for i in range(3)]
        det = (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
               -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
               +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
        assert det > 0, ("Hankel 3x3", k, m)
        count += 1
print(f"PASS: {count} exact rational assertions; k=2..{KMAX}; n<={NMAX}; r<=8")
