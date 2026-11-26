"""Exact rational checks for a sharp period-two census in a quadratic gap map.

The analytic root bound uses H'' having at most one positive zero;
these computations only check the explicit sharpness witness.
Run: python3 verify_period2.py (standard library only).
"""
from fractions import Fraction as Q

A = Q(1, 5)      # a
B = Q(1, 10)     # b
C = Q(17, 200)   # c
D = Q(2)


def f_left(x):
    assert Q(0) <= x <= B
    return 1 - (1 - A) * ((B - x) / B) ** 2


def f_right(x):
    assert B < x <= Q(1)
    return C * ((x - B) / (1 - B)) ** 2


def H(t):
    return C * ((1 - B) - (1 - A) * t * t) ** 2 / ((1 - B) ** 2) - B * (1 - t)


def Hprime(t):
    return B - 4 * C * (1 - A) * t * ((1 - B) - (1 - A) * t * t) / (1 - B) ** 2


def multiplier(t):
    x = B * (1 - t)
    y = f_left(x)
    return 4 * C * (1 - A) * t * (y - B) / (B * (1 - B) ** 2)


anchors = [Q(0), Q(1, 4), Q(3, 5), Q(1)]
expected = [Q(-3, 200), Q(53, 64800), Q(-87, 125000), Q(17, 16200)]
assert [H(t) for t in anchors] == expected
assert all(A > B for A, B in [(A, B)])

isolations = []
for i in range(3):
    lo, hi = anchors[i:i + 2]
    start_sign = 1 if H(lo) > 0 else -1
    assert start_sign * H(hi) < 0
    for _ in range(95):
        mid = (lo + hi) / 2
        if start_sign * H(mid) > 0:
            lo = mid
        else:
            hi = mid
    mid = (lo + hi) / 2
    x = B * (1 - mid)
    y = f_left(x)
    assert 0 < x < B < y < 1
    assert abs(f_right(y) - x) < Q(1, 10**25)
    m = multiplier(mid)
    assert m == 1 - Hprime(mid) / B
    assert (Q(0) < m < Q(1)) if i in (0, 2) else (m > Q(1))
    isolations.append((lo, hi, x, y, m))

assert isolations[0][1] < isolations[1][0] < isolations[2][0]
print('EXACT_RATIONAL_THREE_PERIOD_TWO_ORBITS_AND_TWO_SINKS_OK')
for i, (_, _, x, y, m) in enumerate(isolations, 1):
    print(i, 'lower_state≈', float(x), 'upper_state≈', float(y), 'multiplier≈', float(m))
