#!/usr/bin/env python3
"""Exact independent verification of a prescribed cut statistic in uniform labelled trees.

Requires only Python 3 standard library; all finite checks are exact integers/fractions.
The asymptotic theorem is established in the accompanying written proof, not by enumeration.
"""
from itertools import product
from math import comb
from collections import Counter
from fractions import Fraction
from heapq import heapify, heappop, heappush


def prufer_edges(word, n):
    degrees = [1] * n
    for v in word:
        degrees[v] += 1
    leaves = [i for i, d in enumerate(degrees) if d == 1]
    heapify(leaves)
    out = []
    for v in word:
        u = heappop(leaves)
        out.append((u, v))
        degrees[u] -= 1
        degrees[v] -= 1
        if degrees[v] == 1:
            heappush(leaves, v)
    out.append((heappop(leaves), heappop(leaves)))
    return out


def coeff_pgf(n, a):
    b = n - a
    # z (a+bz)^(a-1) (b+az)^(b-1)
    coef = Counter()
    for i in range(a):
        for j in range(b):
            k = 1 + i + j
            coef[k] += comb(a-1, i)*a**(a-1-i)*b**i * comb(b-1, j)*b**(b-1-j)*a**j
    return coef


def check():
    cases = 0
    sampled = 0
    for n in range(2, 8):
        for a in range(1, n):
            expected = coeff_pgf(n, a)
            assert sum(expected.values()) == n**(n-2)
            actual = Counter()
            for word in product(range(n), repeat=n-2):
                edges = prufer_edges(word, n)
                k = sum((u < a) != (v < a) for u,v in edges)
                actual[k] += 1
                sampled += 1
            assert actual == expected, (n,a,actual,expected)
            e = sum(Fraction(k*v,n**(n-2)) for k,v in expected.items())
            variance = sum(Fraction((k-e)**2 * v,n**(n-2)) for k,v in expected.items())
            b = n - a
            assert e == Fraction(2*a*b,n)
            assert variance == Fraction((n-2)*a*b,n*n)
            cases += 1
    print('OK: %d exact cut-size distributions, %d independently decoded Prüfer trees, exact moments.' % (cases,sampled))


if __name__ == '__main__':
    check()
