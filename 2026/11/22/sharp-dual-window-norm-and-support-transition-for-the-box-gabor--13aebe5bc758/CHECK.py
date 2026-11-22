#!/usr/bin/env python3
"""Exact rational-fiber diagnostics for the box-window Gabor dual formula.

These finite tests supplement, but do not replace, the analytic argument.
Run with: python3 CHECK.py
"""
from fractions import Fraction as F
from math import gcd


def fiber(beta, x, weight):
    delta = 1 / beta - 1
    assert F(1, 3) < delta < F(1, 2)
    h = {k: F(0) for k in range(-6, 7)}
    if x < delta - 1:
        h[1] = beta
    elif x < -delta:
        u = weight * beta
        h[-1], h[0], h[1], h[2] = -u, u, beta - u, u - beta
    else:
        h[0] = beta
    return h


def cells(beta):
    delta = 1 / beta - 1
    ends = {-F(1), F(0), delta - 1, -delta}
    for n in range(-5, 6):
        for k in range(-6, 7):
            for sign in (-1, 1):
                v = F(sign) - F(n) / beta - F(k)
                if -1 < v < 0:
                    ends.add(v)
    cuts = sorted(ends)
    return [(a + b) / 2 for a, b in zip(cuts, cuts[1:])]


def verify(beta):
    delta = 1 / beta - 1
    lmiddle = 1 - 2 * delta
    assert lmiddle > 0
    # Integral of the fiberwise absolute sum is exact by the three intervals.
    L1 = beta * (2 * delta + 2 * lmiddle)
    assert L1 == 4 * beta - 2
    support_min = 2 * delta + 2 * lmiddle
    assert support_min == 4 - 2 / beta
    count = 0
    for x in cells(beta):
        for weight in (F(0), F(1, 3), F(2, 3), F(1)):
            h = fiber(beta, x, weight)
            expected = beta * (2 if delta - 1 < x < -delta else 1)
            assert sum(abs(v) for v in h.values()) == expected
            for n in range(-5, 6):
                lhs = sum(v for k, v in h.items()
                          if -1 < x + k + F(n) / beta < 1)
                assert lhs == (beta if n == 0 else 0), (beta, x, n, weight, lhs)
                count += 1
    return count


def main():
    cases, constraints = 0, 0
    for q in range(5, 49):
        for p in range(1, q):
            if 3 * p <= 2 * q or 4 * p >= 3 * q or gcd(p, q) != 1:
                continue
            beta = F(p, q)
            constraints += verify(beta)
            cases += 1
    assert cases >= 30
    print('PASS:', cases, 'rational parameters;', constraints,
          'exact correlation identities and fiber costs')


if __name__ == '__main__':
    main()
