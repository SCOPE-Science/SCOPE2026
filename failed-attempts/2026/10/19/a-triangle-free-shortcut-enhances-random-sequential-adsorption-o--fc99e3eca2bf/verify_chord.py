#!/usr/bin/env python3
"""Exact rational checks for a single-shortcut random-sequential-adsorption theorem.
Uses only the Python standard library. No sampling or numerical inference."""
from functools import lru_cache
from fractions import Fraction
from math import factorial
from itertools import permutations


def greedy_mean(n, edges):
    """Expectation of random-order greedy maximal independent-set size.
    Recursion conditions on the first eligible vertex, an exact identity."""
    mask_close = [1 << i for i in range(n)]
    for x, y in edges:
        mask_close[x] |= 1 << y
        mask_close[y] |= 1 << x

    @lru_cache(maxsize=None)
    def f(mask):
        if mask == 0:
            return Fraction(0)
        total = Fraction(0)
        choices = mask.bit_count()
        rem = mask
        while rem:
            bit = rem & -rem
            rem -= bit
            u = bit.bit_length() - 1
            total += f(mask & ~mask_close[u])
        return 1 + total / choices

    return f((1 << n) - 1)


def path(n):
    return [(i, i+1) for i in range(n-1)]


def cycle(n):
    return path(n) + [(n-1, 0)]


def ttail(k):
    # Dominating finite sum with certified rational remainder:
    # after j=49, the ratio of successive terms is <=1/51.
    s = sum((Fraction(1, factorial(j+1)) for j in range(k, 50)), Fraction(0))
    return s + Fraction(1, factorial(51)) * Fraction(51, 50)


def permutation_mean(n, edges):
    """Second, independent exact method for the smallest examples."""
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b)
        adj[b].add(a)
    count=0
    for perm in permutations(range(n)):
        chosen=set()
        for v in perm:
            if adj[v].isdisjoint(chosen):
                chosen.add(v)
        count+=len(chosen)
    return Fraction(count, factorial(n))


def validate():
    # Motif: four-vertex 0--1--2--3 path, with an extra edge 0--3,
    # flanked by 12 vertices on either side.
    r = 12
    gadget_n = 2*r + 4
    gp = greedy_mean(gadget_n, path(gadget_n))
    gc = greedy_mean(gadget_n, path(gadget_n) + [(r, r+3)])
    improvement = gc-gp
    expected = Fraction(13738981531700639, 304554407185153125)
    assert improvement == expected, (improvement, expected)
    bound = 8*sum((min(10*ttail(r-d+1), 24*ttail(d)) for d in range(r+1)), Fraction(0)) + 12*ttail(r+1)
    assert bound < Fraction(9,1000) and improvement > Fraction(45,1000)
    print('gadget_exact', improvement)
    print('certified_stabilization_error_upper_bound', float(bound))
    print('strict_positive_large_n_lower_bound', float(improvement-bound))
    # Exact first-step recursion for every remaining finite cycle.
    edge_addition = {}
    for n in range(5,29):
        base = greedy_mean(n, cycle(n))
        changed = greedy_mean(n, cycle(n)+[(0,3)])
        edge_addition[n] = changed-base
        if n in (5,7):
            assert changed == base, (n,changed-base)
        elif n >= 6:
            assert changed > base, (n,changed-base)
    for n in (5,6,7):
        assert permutation_mean(n,cycle(n)) == greedy_mean(n,cycle(n))
        assert permutation_mean(n,cycle(n)+[(0,3)]) == greedy_mean(n,cycle(n)+[(0,3)])
    print('permutation_enumeration_sizes', [5,6,7])
    print('positive_finite_sizes' , [n for n in edge_addition if edge_addition[n]>0])
    print('zero_finite_sizes', [n for n in edge_addition if edge_addition[n]==0])
    print('smallest_positive_finite_gap', min(x for x in edge_addition.values() if x>0))
    print('PASS: all n>=6 except n=7 show strict gain; n=5,7 equal')

if __name__ == '__main__':
    validate()
