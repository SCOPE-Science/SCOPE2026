#!/usr/bin/env python3
"""Exact-rational witnesses for the power-exponential survival-copula criterion.

These tests illustrate and independently check selected identities. They do not
replace the global derivative-and-optimization proof in RESULT.md.
"""
from fractions import Fraction as F


def threshold_integer(a, b):
    assert isinstance(a, int) and isinstance(b, int) and a >= 1 and b >= 1
    m = a + b - 1
    # Interpret 0**0 as 1 in the limiting endpoint expression.
    return F(m ** (2 * m), a ** (2 * a) * b ** (2 * b)
             * (a - 1) ** (a - 1) * (b - 1) ** (b - 1))


def numerator(a, b, phi, x, y, t=None):
    # For the half-integer witness supply exact t=phi*sqrt(x)*y.
    if t is None:
        assert isinstance(a, int) and isinstance(b, int)
        t = phi * x ** a * y ** b
    return (x + a * t) * (y + b * t) - a * b * t


assert threshold_integer(1, 1) == F(1)
assert threshold_integer(1, 3) == F(1, 4)
assert threshold_integer(2, 2) == F(729, 256)
assert threshold_integer(2, 3) == F(1024, 729)

boundary = numerator(2, 2, F(729, 256), F(4, 9), F(4, 9))
assert boundary == 0, boundary

above = numerator(2, 2, F(3), F(4, 9), F(4, 9))
assert above == F(-37232, 4782969), above
assert above < 0

edge = numerator(1, 3, F(1, 3), F(1, 1000), F(2))
assert edge == F(-239, 375000), edge
assert edge < 0

x, y, phi = F(1, 10000), F(1, 2), F(1, 2)
# sqrt(x)=1/100 exactly.
t = phi * F(1, 100) * y
subunit = numerator(F(1, 2), 1, phi, x, y, t=t)
assert subunit == F(-4573, 8000000), subunit
assert subunit < 0

# Finite rational-grid checks for several integer-exponent threshold cases.
# Again: the proof, not this grid, covers every real positive x and y.
for a, b in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 3)]:
    phi = threshold_integer(a, b)
    for nx in range(1, 25):
        for ny in range(1, 25):
            x, y = F(nx, 12), F(ny, 12)
            h = numerator(a, b, phi, x, y)
            assert h >= 0, (a, b, phi, x, y, h)

print('PASS: all exact rational threshold and sign witnesses; grid sanity checks')
