#!/usr/bin/env python3
"""Exact arithmetic checks for the five-tap cyclic least-squares smoother.

Run using Python 3 standard library:
    python3 check_sg_gini.py
The unrestricted claims rest on the proof in RESULT.md. This program
exhausts every binary cut in the four finite base dimensions.
"""
from fractions import Fraction
from itertools import combinations

WEIGHTS = (-3, 12, 17, 12, -3)
OFFSETS = (-2, -1, 0, 1, 2)
EXPECTED = {
    5: (110, 180),
    6: (157, 256, 303),
    7: (204, 338, 414),
    8: (251, 420, 531, 560),
}
EXPECTED_NORMS = {5: Fraction(6, 7), 6: Fraction(101, 105),
                  7: Fraction(69, 70), 8: Fraction(251, 245)}

def unscaled_filter(x):
    n = len(x)
    return tuple(sum(w * x[(i + j) % n] for j, w in zip(OFFSETS, WEIGHTS))
                 for i in range(n))

def gini(x):
    return sum(abs(a - b) for i, a in enumerate(x) for b in x[i+1:])

assert sum(WEIGHTS) == 35
assert sum(j*w for j,w in zip(OFFSETS, WEIGHTS)) == 0
assert sum(j*j*w for j,w in zip(OFFSETS, WEIGHTS)) == 0
print('FIVE_TAP_QUADRATIC_REPRODUCTION_PASSED')

cut_count = 0
for n, expected in EXPECTED.items():
    maxima = [0] * (n // 2)
    full = (1 << n) - 1
    count = 0
    for mask in range(1, full):
        count += 1
        k = mask.bit_count()
        x = tuple((mask >> i) & 1 for i in range(n))
        assert gini(x) == k * (n-k)
        f = gini(unscaled_filter(x))
        idx = min(k, n-k) - 1
        maxima[idx] = max(maxima[idx], f)
    assert count == (1 << n) - 2
    assert tuple(maxima) == expected, (n, maxima)
    norm = max(Fraction(f, 35 * k * (n-k))
               for k, f in enumerate(maxima, 1))
    assert norm == EXPECTED_NORMS[n]
    for k, f in enumerate(maxima, 1):
        y = unscaled_filter(tuple(int(i < k) for i in range(n)))
        assert gini(y) == f, (n, k, f, gini(y))
    cut_count += count
    print(f'EXHAUSTIVE_N={n}_CUTS={count}_NORM={norm}_PASSED')
assert cut_count == 472
print('EXACT_ALL_472_BINARY_CUTS_AND_SHARPNESS_PASSED')

for n in range(5, 101):
    x = (1,) + (0,) * (n-1)
    f = gini(unscaled_filter(x))
    assert f == 47*n - 125, (n, f)
    ratio = Fraction(f, 35*(n-1))
    assert (ratio > 1) == (n >= 8)
    assert ratio <= Fraction(47, 35)
print('EXPLICIT_SINGLETON_ALL_N_GE_5_IDENTITY_CHECKED_5_TO_100')

# Non-exhaustive independent corroboration for nonbinary data, not proof.
for n in range(5, 16):
    for k in range(1, 48):
        x = tuple(((13*k+19*i+7*i*k + 11*i*i)%29)-14 for i in range(n))
        gx = gini(x)
        gy = gini(unscaled_filter(x))
        assert gy <= 47*gx
        if n <= 7:
            assert Fraction(gy, 35) <= EXPECTED_NORMS[n]*gx
print('INTEGER_SIGNAL_SANITY_CHECKS_PASSED_517')
print('ALL_SAVITZKY_GOLAY_CYCLIC_GINI_CHECKS_PASSED')
