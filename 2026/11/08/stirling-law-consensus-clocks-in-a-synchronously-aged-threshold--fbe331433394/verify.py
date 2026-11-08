#!/usr/bin/env python3
"""Exact finite-time checks for an inverse-age threshold cascade on a path.

Requires only Python 3 standard library. Run: python verify.py
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def stirling_first(nmax):
    a = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    a[0][0] = 1
    for n in range(1, nmax + 1):
        for k in range(1, n + 1):
            a[n][k] = (n - 1) * a[n - 1][k] + a[n - 1][k - 1]
    return a


def state_dist(m, t):
    """Independent Markov update of the adopted prefix; t full rounds."""
    p = [Fraction(0)] * (m + 1)
    p[0] = Fraction(1)
    for u in range(t):
        rate = Fraction(1, u + 2)
        nxt = [Fraction(0)] * (m + 1)
        nxt[m] = p[m]
        for k in range(m):
            nxt[k] += p[k] * (1 - rate)
            nxt[k + 1] += p[k] * rate
        p = nxt
    return p


def count_cycles(p):
    n = len(p)
    seen = set()
    count = 0
    for i in range(n):
        if i not in seen:
            count += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return count


def check():
    total = 0
    c = stirling_first(65)
    for m in range(1, 10):
        for t in range(0, 61):
            p = state_dist(m, t)
            assert sum(p) == 1
            n = t + 1
            for k in range(m):
                assert p[k] == Fraction(c[n][k + 1], factorial(n)), (m, t, k)
                total += 1
            assert p[m] == Fraction(sum(c[n][j] for j in range(m + 1, n + 1)), factorial(n))
            total += 1
            assert sum(p[:-1]) == Fraction(sum(c[n][j] for j in range(1, min(m,n) + 1)),factorial(n))
            total += 1
    for n in range(1, 9):
        counts = [0] * (n + 1)
        for p in permutations(range(n)):
            counts[count_cycles(p)] += 1
        assert counts == c[n][:n + 1], n
        total += n + 1
    assert state_dist(1,1) == [Fraction(1,2),Fraction(1,2)]
    assert state_dist(2,1) == [Fraction(1,2),Fraction(1,2),Fraction(0)]
    assert state_dist(2,2) == [Fraction(1,3),Fraction(1,2),Fraction(1,6)]
    print('VERIFY_OK',total,'exact equalities and independent exhaustive permutation counts')

if __name__ == '__main__':
    check()
