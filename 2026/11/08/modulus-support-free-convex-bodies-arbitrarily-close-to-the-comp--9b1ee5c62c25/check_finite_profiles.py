"""Exact-rational spot checks for the moment matrix in the accompanying proof.

Finite arithmetic is not a proof of the infinite-dimensional theorem.
"""
from fractions import Fraction
from itertools import product

checks = 0
for n in range(1, 31):
    t = Fraction(1, 2 ** (n + 1))
    row = t / (1 - t)
    assert row <= Fraction(1, 3)
    checks += 1
    for cutoff in (1, 2, 3, 5, 10, 20):
        partial = sum((t ** k for k in range(1, cutoff + 1)), Fraction(0))
        assert row - partial == t ** (cutoff + 1) / (1 - t)
        checks += 1

# Each nonzero finite profile has a first nonzero coefficient whose moment
# dominates all later coefficients at sufficiently large exponents.
for a in product((-1, 0, 1), repeat=4):
    if not any(a):
        continue
    n0 = next(i + 1 for i, v in enumerate(a) if v)
    t0 = Fraction(1, 2 ** (n0 + 1))
    for k in (10, 40, 160):
        b = sum((v * Fraction(1, 2 ** ((i + 2) * k)) for i, v in enumerate(a)), Fraction(0))
        ratio = b / (t0 ** k)
        error = sum((abs(a[i]) * (Fraction(1, 2 ** (i + 2)) / t0) ** k
                     for i in range(n0, len(a))), Fraction(0))
        assert abs(ratio - a[n0 - 1]) <= error
        checks += 1
print('MOMENT_KERNEL_RATIONAL_CHECK_OK', checks)
