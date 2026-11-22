"""Exact checks for the two-type household reproduction-threshold crossover.

Pure Python 3 standard library; the arbitrary-contrast uniqueness proof is
analytical and is provided in RESULT.md, not inferred from numerical sampling.
"""
from fractions import Fraction
from math import exp, log


def poly16(x):
    return x**16 - 8*x**4 + 16*x - 9


def same_r4(x):
    return 8 - 4*x**4


def mixed_r4(x):
    return Fraction(25, 2) - 8*x - x**16 / 2


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


# Coefficient order is ascending, so this tests the complete exact identity.
q = [-9, -2, 5, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
expected = [-9, 16, 0, 0, -8] + [0] * 11 + [1]
assert mul([1, -2, 1], q) == expected
assert sum(int(v > 0) and not int(q[i - 1] > 0)
           for i, v in enumerate(q) if i) == 1

for x, sigma, same_expected, mixed_expected in [
    (Fraction(3, 4), Fraction(2, 13), Fraction(431, 416),
     Fraction(55791528127, 55834574848)),
    (Fraction(1, 2), Fraction(1, 8), Fraction(31, 32),
     Fraction(1114111, 1048576)),
]:
    assert 2 * (same_r4(x) - mixed_r4(x)) == poly16(x)
    assert sigma * same_r4(x) == same_expected
    assert sigma * mixed_r4(x) == mixed_expected

assert poly16(Fraction(3, 4)) == Fraction(2056312641, 4294967296)
assert poly16(Fraction(1, 2)) == Fraction(-98303, 65536)
assert poly16(Fraction(13, 20)) < 0 < poly16(Fraction(2, 3))
assert Fraction(431, 416) > 1 > Fraction(55791528127, 55834574848)
assert Fraction(31, 32) < 1 < Fraction(1114111, 1048576)

# Non-proof sanity samples across a range of real contrasts.
for r in [1.01, 1.1, 1.5, 2.0, 4.0, 9.0, 20.0]:
    f = lambda t: -(r - 1)**2 - 2*r*exp(-r*t) + exp(-(r*r)*t) + (r*r)*exp(-t)
    assert f(1e-2 / r) > 0 and f(100) < 0

print('PASS: polynomial identity, exact criticality reversals, root bracket, and numerical sanity samples')
