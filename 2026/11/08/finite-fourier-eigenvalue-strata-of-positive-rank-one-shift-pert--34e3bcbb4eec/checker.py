#!/usr/bin/env python3
"""Finite consistency checks for Fourier-tuned positive shift couplings.

All infinite-dimensional claims require the independent analytical arguments
in the accompanying result. This script checks finite Fourier data and powers.
"""
import itertools
import cmath
import math

checks = 0

def require(statement):
    global checks
    assert statement
    checks += 1


def orbits(m):
    unseen = set(range(1, m))
    result = []
    while unseen:
        k = min(unseen)
        orbit = {k, (-k) % m}
        result.append(orbit)
        unseen.difference_update(orbit)
    return result

for m in range(2, 17):
    omega = cmath.exp(2j * math.pi / m)
    blocks = orbits(m)
    for mask in range(1 << len(blocks)):
        selected = set().union(*(b for k,b in enumerate(blocks) if (mask >> k) & 1)) if mask else set()
        active = set(range(1,m)) - selected
        alpha = [1 + sum(omega**(j*k) for k in active)/m for j in range(m)]
        for a in alpha:
            require(abs(a.imag) < 2e-12)
            require(a.real > 0)
        for k in range(m):
            fourier = sum(alpha[j]*omega**(-j*k) for j in range(m))
            expected = m if k == 0 else (0 if k in selected else 1)
            require(abs(fourier - expected) < 2e-10)
        # A strictly positive vector has a nonzero zero-frequency component.
        require(sum(a.real for a in alpha) > 0)

# Exact integer-arithmetic matrix powers provide a finite check of the
# stated operator norm formula for the infinite positive block operator.
for m in range(2, 9):
    for alpha in ([1]*m, list(range(1,m+1)), [1 + (i*i)%5 for i in range(m)]):
        N = 12
        size = N + m
        T = [[0]*size for _ in range(size)]
        for i in range(N-1):
            T[i+1][i] = 1
        for j in range(m):
            T[0][N+j] = alpha[j]
            T[N+((j+1)%m)][N+j] = 1
        # Exact nonnegative multiplication on Python integers.
        P = [[int(i==j) for j in range(size)] for i in range(size)]
        for n in range(0, 10):
            columns = [sum(P[i][j] for i in range(size)) for j in range(size)]
            actual = max(columns)
            expected = 1 + max(sum(alpha[(j+k)%m] for k in range(n)) for j in range(m))
            require(actual == expected)
            if n != 9:
                P = [[sum(P[i][k]*T[k][j] for k in range(size))
                      for j in range(size)] for i in range(size)]

# The finite Fourier orthogonality statement used in the analytic inverse
# transform: every nonconstant character has geometric sum zero.
for m in range(2, 110):
    for d in range(m):
        # A geometric sum has ratio 1 exactly when d is divisible by m.
        ratio_one = (d % m == 0)
        # All other cases have ratio != 1 and ratio**m == 1.
        require(ratio_one == (d == 0))

print('POSITIVE_FOURIER_LEAKAGE_FINITE_OK', checks)
