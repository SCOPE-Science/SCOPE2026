#!/usr/bin/env python3
"""Exact rational check of two moment-matched return gaps."""
from fractions import Fraction as F

P = ((-1, F(1, 2)), (1, F(1, 2)))
Q = ((-2, F(1, 8)), (0, F(3, 4)), (2, F(1, 8)))


def excess(law, s):
    return sum(p * F(2)**(-s*k) for k, p in law) - 1


def difference(law, x):
    return (excess(law, 2) - x * excess(law, 1)) / x**2


def main():
    for law in (P, Q):
        assert all(p > 0 for _, p in law)
        assert sum(p for _, p in law) == 1
        assert sum(k*p for k, p in law) == 0
        assert sum(k*k*p for k, p in law) == 1
    assert (excess(P, 1), excess(P, 2)) == (F(1, 4), F(9, 8))
    assert (excess(Q, 1), excess(Q, 2)) == (F(9, 32), F(225, 128))
    lower, upper = (excess(law, 2) / excess(law, 1) for law in (P, Q))
    assert (lower, upper) == (F(9, 2), F(25, 4))
    assert max(F(2)**(-k) for law in (P, Q) for k, _ in law) < lower < 5 < upper
    assert difference(P, lower) == 0 < difference(Q, lower)
    assert difference(P, upper) < 0 == difference(Q, upper)
    assert difference(P, F(5)) == -F(1, 200)
    assert difference(Q, F(5)) == F(9, 640)
    print('PASS: moments, gap support, full sign interval thresholds, endpoints and exact witness')


if __name__ == '__main__':
    main()
