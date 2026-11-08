#!/usr/bin/env python3
"""Exact finite checks of the fixed-stage coextinction covariance theorem.

Uses only the Python standard library.  No Monte Carlo or external files.
The proof for arbitrary n is in RESULT.md; these are regression/independent checks.
"""
from fractions import Fraction
from math import comb
from itertools import combinations


def contained_probability(n, r, s):
    return Fraction(comb(r, s), comb(n, s)) if s <= r else Fraction(0)


def formula(n, r, a, b, c):
    u = a + b - c
    return (contained_probability(n, r, u)
            - contained_probability(n, r, a) * contained_probability(n, r, b))


def direct(n, r, A, B):
    all_r = list(combinations(range(n), r))
    ca = cb = cab = 0
    A, B = set(A), set(B)
    for sample in all_r:
        sample = set(sample)
        ea, eb = A <= sample, B <= sample
        ca += ea
        cb += eb
        cab += ea and eb
    d = len(all_r)
    return Fraction(cab, d) - Fraction(ca * cb, d*d)


def check():
    formula_count = 0
    phase_count = 0
    brute_count = 0
    # All allowable cardinalities and all stages, up to 12 primary species.
    for n in range(2, 13):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                for c in range(max(0, a+b-n), min(a,b) + 1):
                    u = a+b-c
                    seq = []
                    for r in range(n + 1):
                        v = formula(n,r,a,b,c)
                        formula_count += 1
                        if r == n: assert v == 0
                        if r == n-1: assert v == Fraction(c*n-a*b,n*n)
                        if r < min(a,b): assert v == 0
                        if c == min(a,b):
                            assert v >= 0
                            if u <= r < n: assert v > 0
                        elif c*n <= a*b:
                            assert v <= 0
                            if max(a,b) <= r <= n-2: assert v < 0
                            if r == n-1: assert (v == 0) == (c*n == a*b)
                        else:
                            # Incomparable sets with above-random intersection.
                            if max(a,b) <= r < u: assert v < 0
                            if r == n-1: assert v > 0
                            if max(a,b) <= r < n: seq.append((v>0)-(v<0))
                    if seq:
                        # Signs may move -1 -> 0 -> +1, but never decrease.
                        assert seq == sorted(seq)
                        assert seq[0] == -1 and seq[-1] == 1
                        assert seq.count(0) <= 1
                    phase_count += 1
    # Enumerate all uniformly random removed sets independently of the
    # hypergeometric closed form for a representative sweep of networks.
    for n in range(2, 10):
        for a in range(1, n+1):
            for b in range(1, n+1):
                for c in range(max(0,a+b-n), min(a,b)+1):
                    if (a+b+c+n)%3: continue
                    A=set(range(a))
                    B=set(range(c))|set(range(a,a+b-c))
                    for r in range(n+1):
                        assert formula(n,r,a,b,c) == direct(n,r,A,B)
                        brute_count += 1
    # Distinctness from a covariance integrated across removal ranks.
    n,a,b,c=26,5,5,1
    u=a+b-c
    assert formula(n,n-1,a,b,c) == Fraction(1,676)
    rank_cov=(Fraction(n+1,(a+1)*(b+1))
              *(Fraction(c*(n-u),u+2)-Fraction((a-c)*(b-c),u+1)))
    assert rank_cov == Fraction(-9,220)
    print(f'PASS exact-cardinality stage checks={formula_count}; phase cases={phase_count};')
    print(f'PASS independent subset-enumeration comparisons={brute_count}; distinct rank example=PASS')

if __name__ == '__main__':
    check()
