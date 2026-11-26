#!/usr/bin/env python3
"""Independent finite tests of a two-prime primitive-set inequality.

No finite check is a proof of the infinite theorem.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, log


def layer(p, q, r, t=1):
    return sum(Fraction(1, (p ** i * q ** (r - 1 - i)) ** t)
               for i in range(r))


def all_grid_antichains(p=2, q=3, M=5):
    total = 0
    for r in range(1, M + 2):
        bound = layer(p, q, r)
        target = tuple((i, r - 1 - i) for i in range(r))
        for aa in combinations(range(M + 1), r):
            for bb0 in combinations(range(M + 1), r):
                bb = tuple(reversed(bb0))
                coords = tuple(zip(aa, bb))
                if coords == ((0, 0),):
                    continue
                weight = sum(Fraction(1, p**a * q**b)
                             for a, b in coords)
                if r == 1:
                    assert weight <= Fraction(1, p)
                else:
                    assert weight <= bound, (r, coords, weight, bound)
                    if weight == bound:
                        assert coords == target, (r, coords)
                total += 1
    return total


def R(p, q, t, d):
    x = p ** (-t)
    y = q ** (-t)
    return (x ** (d + 2) - y ** (d + 2)) / (x ** (d + 1) - y ** (d + 1))


def optimal_rank(p, q, t):
    # Direct positive recurrence avoids cancellation when p and q are close.
    x, y = p ** (-t), q ** (-t)
    w_prev, w_curr = 1., x + y
    d = 1
    while True:
        w_next = (x + y) * w_curr - x * y * w_prev
        if w_next <= w_curr:
            return d
        w_prev, w_curr = w_curr, w_next
        d += 1
        assert d < 2000


def critical_bracket(p, q):
    def f(t):
        x, y = p ** (-t), q ** (-t)
        return x*x + x*y + y*y - x - y
    lo, hi = 0., 2.
    assert f(lo) > 0 and f(hi) < 0
    for _ in range(100):
        mid = (lo + hi)/2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2

if __name__ == '__main__':
    k = all_grid_antichains(2, 3, 5)
    assert k == comb(12, 6) - 2
    for p, q in [(2, 3), (2, 5), (3, 5), (5, 7), (11, 13)]:
        tc = critical_bracket(p, q)
        assert 0 < tc < 0.461
        for t in [0.04, 0.08, 0.1, 0.2, 0.3, 0.4, 0.45, 0.47, 0.5, 0.8, 1., 2.]:
            d = optimal_rank(p, q, t)
            vals = [sum(p ** (-t*a) * q ** (-t*(j-a)) for a in range(j+1)) for j in range(1, max(d+7, 100))]
            assert all(vals[d-1] >= v - 1e-9 for v in vals)
    print('VERIFIED rational_antichains', k, 'grid_side', 6, 'prime_pairs', 5, 'exponent_tests', 12,
          'critical_2_3', f'{critical_bracket(2, 3):.15f}')
