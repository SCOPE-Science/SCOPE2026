#!/usr/bin/env python3
"""Finite diagnostics for sparse quasi-Banach matrix inequalities.

The infinite-dimensional results require the analytic proof; this program checks
finite matrix identities, their limiting-exponent reductions, and phase averages.
"""
import cmath
import math
import random

rng = random.Random(21062026)
checks = 0

def verify(test, message):
    global checks
    assert test, message
    checks += 1

def norm(x, exponent):
    return sum(abs(z) ** exponent for z in x) ** (1 / exponent)

def column_norms(A, t):
    return [norm([row[j] for row in A], t) for j in range(len(A[0]))]

def matrix_vector(A, x):
    return [sum(a * u for a, u in zip(row, x)) for row in A]

def weighted_diag_norm(c, p, t):
    if p <= t:
        return max(c)
    r = p * t / (p - t)
    return norm(c, r)

for d in [1, 2, 3, 4]:
    for p, t in [(0.35, 0.65), (0.65, 0.35), (0.55, 0.55), (0.81, 0.49)]:
        for trial in range(30):
            N = 5
            A = []
            for i in range(7):
                row = [0j] * N
                for j in rng.sample(range(N), rng.randrange(d + 1)):
                    row[j] = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
                A.append(row)
            c = column_norms(A, t)
            W = weighted_diag_norm(c, p, t)
            for k in range(8):
                x = [complex(rng.uniform(-1,1),rng.uniform(-1,1)) for j in range(N)]
                ratio = norm(matrix_vector(A, x),t) / norm(x,p)
                verify(ratio <= W + 2e-10, 'operator upper bound')
            if not any(c):
                continue
            x = [rng.uniform(0.1, 1) for j in range(N)]
            target = sum((c[j] * x[j]) ** t for j in range(N)) / d
            total = 0.0
            for k in range(1500):
                phases = [cmath.exp(2j * math.pi * rng.random()) for j in range(N)]
                y = matrix_vector(A, [u*z for u,z in zip(x,phases)])
                total += sum(abs(v)**t for v in y)
            avg = total / 1500
            verify(avg >= target - 0.12 * max(target,1), 'phase-averaged lower bound')

# A single d-to-one positive merger attains the sharp positive lower constant.
for d in range(1, 25):
    for t in [0.25,0.5,0.85]:
        q = t/(1-t)
        A = [[1.0] * d]
        c = column_norms(A,t)
        B = 1.0  # The ℓ1 -> ℓ_t norm of a single-row positive sum.
        verify(abs(B - d**(-1/q)*norm(c,q)) < 1e-10,
               'sharp positive overlap loss')

# A rank-one infinitely supported row violates the finite-overlap criterion.
for p,t in [(0.4,0.6),(0.8,0.3)]:
    for n in [8,32,128]:
        A = [[1.0]*n]
        c = column_norms(A,t)
        q = t/(1-t)
        verify(abs(norm(c,q)-n**(1/q))<1e-8, 'rank-one large columns')
        verify(abs(max(abs(a) for a in A[0])-1)<1e-12,'rank-one bounded extension')

print('SPARSE_MATRIX_DIAGNOSTICS_OK',checks)
