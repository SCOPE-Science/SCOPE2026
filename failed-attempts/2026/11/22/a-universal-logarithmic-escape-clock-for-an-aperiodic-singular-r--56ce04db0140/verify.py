#!/usr/bin/env python3
"""Exact finite consistency checks for the stated rational recurrence.

These checks supplement an analytic infinite-time proof; finite tests alone
cannot establish its asymptotic and measure-theoretic conclusions.
"""
from fractions import Fraction
from math import log


def original(u):
    assert u != -1
    return -4 + u*(1-u)/(1+u)


def shifted(w):
    assert w != 0
    return -w - Fraction(2, 1)/w


def test_exact():
    trials = [Fraction(p, q) for p in range(-9, 10) for q in range(1, 6)
              if Fraction(p, q) != -1]
    steps = 6
    for u in trials:
        w = u + 1
        for k in range(steps):
            assert original(w-1) + 1 == shifted(w)
            wn = shifted(w)
            assert wn*wn == w*w + 4 + 4/(w*w)
            assert abs(wn) > abs(w)
            assert (wn > 0) != (w > 0)
            w = wn
    return len(trials)*steps


def test_asymptotic():
    # Floating-point diagnostics; the actual theorem is proved analytically.
    for u in [-7.0, -3.0, -0.5, 0.0, 0.2, 2.0, 10.0]:
        t = (u+1)**2
        readings = []
        for n in range(1, 200001):
            t += 4 + 4/t
            if n in (100000, 200000):
                readings.append(t - 4*n - log(n))
        assert abs(readings[-1] - readings[0]) < 0.01
    return 7


if __name__ == '__main__':
    print('Exact rational recurrence comparisons:', test_exact())
    print('Floating-point asymptotic diagnostics:', test_asymptotic())
    print('Checks passed; analytic proof establishes the infinite-time result.')
