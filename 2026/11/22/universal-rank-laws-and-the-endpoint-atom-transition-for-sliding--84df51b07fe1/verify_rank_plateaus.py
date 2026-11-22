#!/usr/bin/env python3
"""Exact finite permutation and rational verification for moving order-statistic plateaus.

The infinite-dimensional statements require the separate analytic proof and are
not certified by this finite checker.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def s_formula(w, r, ell):
    assert 1 <= r <= w and 1 <= ell <= w
    n = w + ell - 1
    terms = []
    for k in range(r):
        h = r - 1 - k
        if k <= ell - 1 and h <= w - ell:
            terms.append(Fraction((w - ell + 1) * comb(ell - 1, k)
                                  * comb(w - ell, h)
                                  * factorial(r - 1 + k)
                                  * factorial(n - r - k), factorial(n)))
    return sum(terms, Fraction(0))


def p_formula(w, r):
    return Fraction(2 * r * (w - r + 1), w * (w + 1))


def tail(w, r, ell):
    return (s_formula(w, r, ell) -
            (s_formula(w, r, ell + 1) if ell < w else Fraction(0))) / p_formula(w, r)


def kth(seq, offset, w, r):
    return sorted(seq[offset:offset + w])[-r]


def exhaustive_s(w, r, ell):
    n = w + ell - 1
    count = 0
    for seq in permutations(range(n)):
        x = kth(seq, 0, w, r)
        count += all(kth(seq, t, w, r) == x for t in range(1, ell))
    return Fraction(count, factorial(n))


def exhaustive_start(w, r, ell):
    n = w + ell
    entries = survivors = 0
    for seq in permutations(range(n)):
        x = kth(seq, 1, w, r)
        if kth(seq, 0, w, r) != x:
            entries += 1
            survivors += all(kth(seq, t, w, r) == x for t in range(2, ell + 1))
    return Fraction(survivors, entries)


def main():
    checks = 0
    for w in range(2, 5):
        for r in range(1, w + 1):
            for ell in range(1, w + 1):
                assert exhaustive_s(w, r, ell) == s_formula(w, r, ell), (w, r, ell)
                checks += 1
    for w in range(2, 5):
        for r in range(1, w + 1):
            for ell in range(1, w + 1):
                assert exhaustive_start(w, r, ell) == tail(w, r, ell), (w, r, ell)
                checks += 1
    for w in range(2, 26):
        for r in range(1, w + 1):
            assert s_formula(w, r, 1) == 1
            assert 1 - s_formula(w, r, 2) == p_formula(w, r)
            assert s_formula(w, r, w) == Fraction(comb(w-1,r-1)
                    * factorial(2*r-2) * factorial(2*w-2*r), factorial(2*w-1))
            checks += 3
            t = [tail(w, r, j) for j in range(1, w + 1)]
            assert t[0] == 1 and all(t[i] > t[i + 1] for i in range(w - 1))
            assert sum(t) == 1 / p_formula(w, r)
            checks += 2
    print(f'PASS: {checks} exact assertions including exhaustive ordered-rank samples, widths 2..4 (equality and Palm entrance).')

if __name__ == '__main__':
    main()
