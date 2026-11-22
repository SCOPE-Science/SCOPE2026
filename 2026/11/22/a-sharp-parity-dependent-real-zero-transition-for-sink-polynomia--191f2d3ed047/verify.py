"""Exact small-order checks for sink counts on double-star trees.
Run with Python 3.10+; only the standard library is required.
The all-order root classification is proved in RESULT.md, not inferred from these tests.
"""
from itertools import product
from math import comb
from fractions import Fraction


def mul(A, B):
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i + j] += a * b
    return out


def plus(A, B):
    out = [0] * max(len(A), len(B))
    for i, a in enumerate(A):
        out[i] += a
    for j, b in enumerate(B):
        out[j] += b
    return out


def coeffs(b):
    u = [1, 1]
    pa = [comb(2, j) for j in range(3)]
    pb = [comb(b, j) for j in range(b + 1)]
    pab = [comb(b + 2, j) for j in range(b + 3)]
    correction = mul([-1, 1], plus(pa, pb))
    return plus([2 * x for x in pab], correction)


def direct(b):
    edges = [(0, 2), (0, 3)] + [(1, 4 + i) for i in range(b)] + [(0, 1)]
    tally = [0] * (b + 3)
    for bits in product((0, 1), repeat=len(edges)):
        out = [0] * (b + 4)
        for (a, c), bit in zip(edges, bits):
            out[a if bit == 0 else c] += 1
        tally[sum(v == 0 for v in out)] += 1
    return tally


for b in range(2, 11):
    c = coeffs(b)
    tally = direct(b)
    assert c == tally, (b, c, tally)
    assert sum(c) == 2 ** (b + 3)
print('DIRECT_ORIENTATION_CENSUS_PASS b=2..10')

# Exact identity: (3+x)-(1+x)^11(1-3x-2x^2)
# has low-degree part p(x) and strictly positive remaining coefficients.
from math import comb
p = [2, -7, -20, 22, 275]
A = [comb(11, i) for i in range(12)]
L = plus(mul(A, [1, -3, -2]), [-3, -1])
assert [-x for x in L[:5]] == p
assert all(x < 0 for x in L[5:])
# p(x), on x in [0,1/4], has positive Bernstein coefficients.
B = [Fraction(2), Fraction(25, 16), Fraction(11, 12),
     Fraction(19, 128), Fraction(107, 256)]
for i in range(5):
    # The monomial coefficient of y^i in sum_j B_j C(4,j)y^j(1-y)^(4-j).
    derived = sum(B[j] * comb(4, j) * comb(4-j, i-j) * (-1)**(i-j)
                  for j in range(i+1))
    assert derived == Fraction(p[i], 4**i), (i, derived)
assert min(B) > 0
assert sum(Fraction(j*p[j], 4**(j-1)) for j in range(1, 5)) == Fraction(69,16)
assert sum(Fraction(j*(j-1)*p[j], 4**(j-2)) for j in range(2,5)) == Fraction(797,4)
print('POSITIVE_POLYNOMIAL_CERTIFICATE_PASS')

# The positive hump at b=15 is an exact inequality, not a float estimate.
t = Fraction(6,5)
g = -2*t*t + t + 2
assert g == Fraction(8,25)
assert t**13 * g - (t+2) == Fraction(6829302128,30517578125) > 0
# For each odd b=3,...,13, the hump is bounded by the b=13 case.
# For odd b>=15 it persists because g(6/5)>0 and the exponent increases.
print('ODD_THRESHOLD_RATIONAL_WITNESS_PASS')
print('VERIFY_OK')
