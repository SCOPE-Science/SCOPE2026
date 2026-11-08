#!/usr/bin/env python3
"""Finite arithmetic checks for an exact nilpotent weighted-shift residual formula.

Run with Python 3 (standard library). These diagnostics do not replace
proof of the universal minimax theorem or its asymptotic expansion.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from random import Random
from math import log

getcontext().prec = 65
assertions = 0

def check(p):
    global assertions
    assert p
    assertions += 1


def recurrence(n):
    a = [Decimal(0)]
    for _ in range(n):
        t = a[-1]
        a.append((t + (t*t + 4).sqrt()) / 2)
    return a

# An independent rational matrix multiplication checks the diagonal formula.
def mm(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def adj(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a))]

for n in range(1, 11):
    for seed in range(7):
        rng = Random(1337 + 17*n + seed)
        weights = [Fraction(rng.randrange(-5, 6), 1+rng.randrange(1, 8))
                   for _ in range(n)]
        A = [[Fraction(0) for _ in range(n+1)] for _ in range(n+1)]
        for j, w in enumerate(weights):
            A[j+1][j] = w
        AA = mm(adj(A), A)
        A2 = mm(A, A)
        defect = [[p-q for p,q in zip(x,y)] for x,y in
                  zip(mm(AA,AA),mm(adj(A2),A2))]
        xx = [w*w for w in weights] + [Fraction(0)]
        for i in range(n+1):
            for j in range(n+1):
                expected = xx[i]*(xx[i]-xx[i+1]) if i == j and i < n else 0
                check(defect[i][j] == expected)

for n in range(1, 151):
    r = recurrence(n)
    inv = 1 / (r[n]*r[n])
    xs = [r[n-j]/r[n] for j in range(n)] + [Decimal(0)]
    check(xs[0] == Decimal(1))
    check(all(Decimal(0) < xs[j] <= 1 for j in range(n)))
    for j in range(n):
        check(abs(xs[j]*(xs[j]-xs[j+1]) - inv) < Decimal('1e-56'))
    check(abs(sum((Decimal(2)-1/(r[k]*r[k])) for k in range(1,n+1))
              - r[n]*r[n]) < Decimal('1e-55'))
    # Monotone inverse-envelope inequality for all later weights, a proof step.
    for j in range(n):
        bound = (xs[j+1] + (xs[j+1]*xs[j+1] + 4*inv).sqrt()) / 2
        check(abs(bound-xs[j]) < Decimal('1e-56'))

rng = Random(20261012)
for n in range(1, 21):
    inv = 1 / (recurrence(n)[n]**2)
    for _ in range(120):
        x = [Decimal(1)] + [Decimal(rng.randrange(1000001))/1000000
                             for j in range(n-1)] + [Decimal(0)]
        residual = max(abs(x[j]*(x[j]-x[j+1])) for j in range(n))
        check(residual >= inv - Decimal('1e-58'))

# Confirm expected logarithmic correction rather than treating finite values
# as proof of an asymptotic formula.
for n in [200, 2000, 20000]:
    x = 0.0
    for k in range(n):
        x = (x + (x*x+4)**.5)/2
    check(abs((x*x-2*n)+0.5*log(n)) < 2.0)

print(f'EMBRY_DEFECT_CHECK_OK {assertions} assertions')
