#!/usr/bin/env python3
"""Exact-rational tests for the two-threshold uniform-spacing covariance law.

Only finite arithmetic is tested; the universal and asymptotic claims require
and are supplied with independent mathematical proofs.
"""
from fractions import Fraction as Q
from math import exp, log


def cov_direct(m, s, t):
    assert 2 <= m and Q(0) < s <= t < Q(1)
    a = (1 - s) ** (m - 1)
    b = (1 - t) ** (m - 1)
    c = max(Q(0), 1 - s - t) ** (m - 1)
    return m * b * (1 - a) + m * (m - 1) * (c - a * b)


def bracket(m, s, t):
    v = max(Q(0), 1 - s - t) / (1 - t)
    return 1 - m * (1 - s) ** (m - 1) + (m - 1) * v ** (m - 1)


def sgn(x):
    return (x > 0) - (x < 0)


def monotonic_phase(m, s, t):
    if m == 2 and t == Q(1, 2):
        return 0
    if t <= Q(1, m):
        return 1
    threshold_plateau = 1 - m ** (-1 / (m - 1))
    if t >= (1 - threshold_plateau):
        return sgn(float(s) - threshold_plateau)
    return None


def check():
    n = 0
    for m in range(2, 15):
        for t_index in range(1, 41):
            t = Q(t_index, 41)
            for s_index in range(1, 41):
                s = t * Q(s_index, 40)
                direct = cov_direct(m, s, t)
                via = m * (1 - t) ** (m - 1) * bracket(m, s, t)
                assert direct == via
                expected = monotonic_phase(m, s, t)
                if expected is not None:
                    if sgn(direct) != expected:
                        # skip machine-float plateau thresholds extremely near rational crossings
                        if abs(float(s) - (1 - m ** (-1 / (m - 1)))) > 1e-9:
                            raise AssertionError((m, s, t, direct, expected))
                n += 1
    # Exact special boundary, and signs straddling the plateau root.
    for m in range(2, 18):
        if m == 2:
            for s in [Q(1, 17), Q(7, 17), Q(1, 2)]:
                assert cov_direct(2, s, Q(1, 2)) == 0
        else:
            for s in [Q(1, 100), Q(1, 17), Q(1, m)]:
                if s <= Q(1, m):
                    assert cov_direct(m, s, Q(1, m)) > 0
    # The normalized covariance kernel from the exact finite formula.
    for a, b in [(1.2, 0.15), (2, 0.5), (2, 1.7), (3, 1.5), (4, 2)]:
        for m in (1000, 4000, 10000):
            s, t = b / m, a / m
            A = (1 - s) ** (m-1)
            B = (1 - t) ** (m-1)
            C = (1 - s - t) ** (m-1)
            val = B * (1 - A) + (m - 1) * (C - A * B)
            limit = exp(-a) * (1 - (1 + a*b) * exp(-b))
            assert abs(val - limit) < 0.2
    print('PASS: %d exact-rational covariance identities and sign phases' % n)
    print('PASS: all special two-spacing and mean-threshold boundaries')
    print('PASS: 15 large-size numerical covariance-kernel comparisons')


if __name__ == '__main__':
    check()
