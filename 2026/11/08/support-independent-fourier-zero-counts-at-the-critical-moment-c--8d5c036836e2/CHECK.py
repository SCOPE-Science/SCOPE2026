#!/usr/bin/env python3
"""Exact finite-field checks for balanced-phase moment-curve zero counts.

Python 3 standard library only.  Counts distinct coefficient vectors and,
independently, balanced value vectors satisfying the interpolation hyperplane.
This verifies finite instances, not the all-prime theorem.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import factorial


def balanced_blocks(r):
    """Count balanced set partitions by number of blocks via restricted-growth words."""
    counts = Counter()
    n = 2*r
    def rec(words, blocks):
        if len(words) == n:
            if all(sum(i in block for i in range(r)) == sum(i >= r for i in block) for block in blocks):
                counts[len(blocks)] += 1
            return
        i = len(words)
        for j in range(len(blocks)):
            blocks[j].append(i)
            rec(words + [j], blocks)
            blocks[j].pop()
        blocks.append([i])
        rec(words + [len(blocks)-1], blocks)
        blocks.pop()
    rec([], [])
    return counts


def predicted(p, r):
    b = balanced_blocks(r)
    total = 0
    for t, amount in b.items():
        falling = 1
        for j in range(1, t):
            falling *= p-j
        total += amount*falling
    return total


def zero_count_coeff(p, degree, plus, minus):
    nodes = plus + minus
    pp = [[pow(x, k, p) for x in nodes] for k in range(1, degree+1)]
    count = 0
    for a in product(range(p), repeat=degree):
        values = [sum(a[k]*pp[k][i] for k in range(degree)) % p for i in range(len(nodes))]
        count += sorted(values[:len(plus)]) == sorted(values[len(plus):])
    return count


def hyperplane_count(p, plus, minus):
    nodes = plus + minus
    lambdas = []
    for i, x in enumerate(nodes):
        top, bottom = 1, 1
        for j, y in enumerate(nodes):
            if j != i:
                top = top*(-y) % p
                bottom = bottom*(x-y) % p
        lambdas.append(top*pow(bottom, -1, p) % p)
    assert sum(lambdas) % p == 1
    count = 0
    for v in product(range(p), repeat=len(plus)):
        for w in set(permutations(v)):
            values = v+w
            if sum(z*a for z, a in zip(lambdas, values)) % p == 0:
                count += 1
    return count


def run():
    assert [balanced_blocks(r)[t] for r, t in [(2,1),(2,2),(3,1),(3,2),(3,3),
            (4,1),(4,2),(4,3),(4,4)]] == [1,2,1,9,6,1,34,72,24]
    cases = [
        (5, (0,1), (2,3)),
        (7, (0,2), (1,6)),
        (7, (0,1,2), (3,4,5)),
        (7, (0,1,3), (2,4,6)),
        (11, (0,1,2), (3,4,5)),
        (11, (1,2,3), (4,5,6)),
    ]
    for p, plus, minus in cases:
        r = len(plus)
        expected = predicted(p, r)
        observed = zero_count_coeff(p, 2*r-1, plus, minus)
        assert observed == expected, (p,plus,minus,observed,expected)
    for p, plus, minus in [
        (7,(0,1,2),(3,4,5)),
        (7,(0,1,3),(2,4,6)),
        (11,(0,1,2,3),(4,5,6,7)),
        (11,(0,1,3,5),(2,4,6,9)),
    ]:
        observed = hyperplane_count(p, plus, minus)
        assert observed == predicted(p,len(plus)), (p,plus,minus,observed)
    below = []
    for plus, minus in [((0,1,2),(3,4,5)), ((0,1,2),(3,4,6)), ((0,1,3),(2,4,5))]:
        below.append(zero_count_coeff(11,4,plus,minus))
    assert below == [141,51,231], below
    print('CHECK_OK prime_instances=6 hyperplane_instances=4 lower_degree_counts=141,51,231 B4=1,34,72,24')


if __name__ == '__main__':
    run()
