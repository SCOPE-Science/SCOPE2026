#!/usr/bin/env python3
"""Exact rational checks for the ordered-path pair-averaging Gini theorem.

Requires only Python 3. No floating point is used in the reported identities.
"""
from fractions import Fraction
from itertools import combinations


def variation(v):
    return sum((abs(v[i] - v[j]) for i in range(len(v))
                for j in range(i + 1, len(v))), Fraction(0))


def sweep(v):
    y = [Fraction(t) for t in v]
    for i in range(len(y) - 1):
        q = (y[i] + y[i + 1]) / 2
        y[i] = q
        y[i + 1] = q
    return y


def predicted(n):
    vals = [(Fraction(2) * (1-Fraction(1, 2**k)) /
             (k * (n-k)), k) for k in range(1, n//2 + 1)]
    best = min(v for v, k in vals)
    return 1-best, [k for v, k in vals if v == best]


def all_cut_norm(n):
    greatest = Fraction(-1)
    for k in range(1, n):
        for S in combinations(range(n), k):
            y = [int(i in S) for i in range(n)]
            r = variation(sweep(y)) / (k*(n-k))
            if r > greatest:
                greatest = r
    return greatest


def check():
    expected = [Fraction(0), Fraction(1,2), Fraction(2,3),
                Fraction(3,4), Fraction(13,16), Fraction(41,48),
                Fraction(53,60), Fraction(29,32), Fraction(369,400),
                Fraction(449,480), Fraction(121,128)]
    witness_count = 0
    for n in range(2, 13):
        formula, bestk = predicted(n)
        exact = all_cut_norm(n)
        assert formula == exact == expected[n-2], (n, formula, exact)
        for k in bestk:
            x = [0] * (n-k) + [1] * k
            assert variation(sweep(x)) == Fraction(k*(n-k)) - 2*(1-Fraction(1, 2**k))
            witness_count += 1
        print('EXACT_BINARY_CUT_N', n, 'NORM', exact, 'OPTIMAL_SUFFIX_LENGTHS', bestk)
    # Purely finite spot checks of the general adjacent-ratio comparison;
    # the proof for arbitrary n is given in the theorem text.
    for n in range(9, 161):
        formula, bestk = predicted(n)
        assert bestk == [n//2]
        assert formula == 1 - Fraction(2) * (1-Fraction(1, 2**(n//2))) / ((n//2)*(n-n//2))
    print('BALANCED_SUFFIX_FORMULA_CHECKED_N9_TO160')
    print('EXACT_WITNESSES_CHECKED', witness_count)
    print('ALL_ORDERED_GOSSIP_GINI_EXACT_CHECKS_PASS')


if __name__ == '__main__':
    check()
