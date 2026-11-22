#!/usr/bin/env python3
"""Exact integer checks for the Franel residue spectrum modulo eleven.

No external dependencies. The infinite proof is in RESULT.md; this script
independently checks finite certificates and sample computations.
"""
from math import comb

P = 11
DIGIT = [sum(comb(n, k)**3 for k in range(n+1)) % P for n in range(P)]
assert DIGIT == [1, 2, 10, 1, 5, 8, 4, 9, 6, 8, 1]
POWERS = [pow(2, j, P) for j in range(10)]
assert len(set(POWERS)) == 10
LOG = {v: j for j, v in enumerate(POWERS)}
C = [sum(LOG[z] == j for z in DIGIT) for j in range(10)]
assert C == [3, 1, 1, 2, 1, 1, 1, 0, 0, 1]

# The integer cyclic autocorrelation is the coefficient vector of
# P(x)P(x^(-1)) modulo x^10-1.
Q = [sum(C[i] * C[(i+t) % 10] for i in range(10)) for t in range(10)]
assert Q == [19, 13, 10, 12, 11, 10, 11, 12, 10, 13]

# Monic polynomial reduction in Z[x] against cyclotomic polynomials.
def remainder(coeffs, divisor):
    a = coeffs[:]
    while len(a) >= len(divisor):
        shift = len(a) - len(divisor)
        top = a[-1]
        for j, v in enumerate(divisor):
            a[shift+j] -= top * v
        while a and a[-1] == 0:
            a.pop()
    return a

assert remainder(Q, [-1, 1]) == [121]
assert remainder(Q, [1, 1]) == [1]
assert remainder(Q, [1, 1, 1, 1, 1]) == [5, 0, -2, -2]
assert remainder(Q, [1, -1, 1, -1, 1]) == [11]

# Cyclic convolution computes exact full-block counts for each power.
def multiply(a, b):
    return [sum(a[i] * b[(j-i) % 10] for i in range(10))
            for j in range(10)]

def franel_mod11_digit(n):
    out = 1
    while n:
        out = (out * DIGIT[n % 11]) % 11
        n //= 11
    return out

def franel_exact(n):
    return sum(comb(n, k)**3 for k in range(n+1))

for n in range(160):
    assert franel_exact(n) % 11 == franel_mod11_digit(n)

counts = [1] + [0]*9
Vminus2, Vminus1 = 2, 12  # V_0=2 and V_1=12
for r in range(0, 9):
    if r:
        counts = multiply(counts, C)
    assert sum(counts) == 11**r
    V = 2 if r == 0 else 12 if r == 1 else None
    if r >= 2:
        V = 12*Vminus1 - 31*Vminus2
        Vminus2, Vminus1 = Vminus1, V
    deviation_10 = sum((10*c - 11**r)**2 for c in counts)
    assert deviation_10 == 10 * (4*11**r + 2*V + 1), (r, deviation_10, V)
    if r >= 2:
        assert min(counts) > 0
    if r <= 4:
        direct = [0]*10
        for n in range(11**r):
            direct[LOG[franel_mod11_digit(n)]] += 1
        assert direct == counts
    print(f"r={r} counts={counts} variance_x10={(4*11**r+2*V+1)}")
print('PASS: digit Lucas values, cyclotomic autocorrelation, full-block counts, and variance identities')
