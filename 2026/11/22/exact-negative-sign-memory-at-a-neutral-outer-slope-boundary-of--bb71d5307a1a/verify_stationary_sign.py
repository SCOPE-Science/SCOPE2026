#!/usr/bin/env python3
"""Exact rational supplementary checks for a four-branch interval map.

Run: python3 verify_stationary_sign.py
Tests are finite consistency checks; the general result uses an analytic proof.
"""
from fractions import Fraction as Q
from math import ceil, log


def map_f(x, m):
    x = Q(x)
    assert -m <= x <= m
    if x <= -1:
        return x + 1
    if x < 0:
        return m * (x + 1)
    if x < 1:
        return m * (x - 1)
    return x - 1


def markov(m):
    # Ordered states: +0,...,+(m-1), -0,...,-(m-1).
    size = 2 * m
    P = [[Q(0) for _ in range(size)] for _ in range(size)]
    for side in range(2):
        for k in range(m):
            i = side * m + k
            if k > 0:
                P[i][side*m + k - 1] = Q(1)
            else:
                for j in range(m):
                    P[i][(1-side)*m+j] = Q(1,m)
    return P


def right_multiply(vec, mat):
    return [sum(x * mat[i][j] for i, x in enumerate(vec)) for j in range(len(vec))]


def finite_check():
    total = 0
    for m in range(2, 31):
        P = markov(m)
        pi = [Q(m-k,m*(m+1)) for side in range(2) for k in range(m)]
        assert sum(pi) == 1
        assert right_multiply(pi, P) == pi
        bit = [1]*m + [-1]*m
        vec = [pi[i]*bit[i] for i in range(2*m)]
        a = Q(m-1,m)
        exact = []
        for n in range(m+1):
            computed = sum(bit[i] * vec[i] for i in range(2*m))
            claimed = Q(1-7*m+4*n,m+1) + Q(8*m,m+1)*a**n
            assert computed == claimed, (m,n,computed,claimed)
            exact.append(computed)
            vec = right_multiply(vec, P)
            total += 1
        minval = min(exact)
        minimizers = [n for n,c in enumerate(exact) if c == minval]
        assert minimizers == ([1,2] if m == 2 else [ceil(log(Q(1,2))/log(float(a)))])
        assert minval < 0
        # Independent direct map interiors, with no fixed points.
        for x in [Q(2*k+1,2) for k in range(-m,m)]:
            y = map_f(x,m)
            assert -m <= y <= m and x != y
    print('PASS:', total, 'exact (m,lag) correlation checks, m=2..30;')
    print('PASS: stationary Markov balance, minimum-lag, and branch checks')


if __name__ == '__main__':
    finite_check()
