#!/usr/bin/env python3
"""Standalone exact audit of uniform K_{2,n} random minimum-spanning-tree law.

All probabilities use integer permutation counts. Main theorem for arbitrary n
is established analytically in RESULT.md, not by finite enumeration here.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial
from fractions import Fraction


def kruskal_tree(k, n, permutation):
    """Return the canonical edge-index tuple of the unique Kruskal tree."""
    edges = [(left, right) for left in range(k) for right in range(n)]
    parents = list(range(k+n))

    def root(u):
        while parents[u] != u:
            parents[u] = parents[parents[u]]
            u = parents[u]
        return u

    accepted = []
    for t in permutation:
        a,b = edges[t]
        ra,rb = root(a),root(k+b)
        if ra != rb:
            parents[ra] = rb
            accepted.append(t)
            if len(accepted) == k+n-1:
                break
    return tuple(sorted(accepted))


def all_spanning_trees(k,n):
    edges = range(k*n)
    return {tuple(T) for T in combinations(edges,k+n-1)
            if len(kruskal_tree(k,n,T)) == k+n-1}


def brute_distribution(k,n):
    return Counter(kruskal_tree(k,n,order)
                   for order in permutations(range(k*n)))


def K2n_representation(n, tree):
    # Edges in row-major order: indices 0..n-1 incident to hub 0;
    # indices n..2n-1 incident to hub 1.
    common = [i for i in range(n) if i in tree and i+n in tree]
    if len(common) != 1:
        return None
    j=common[0]
    orientation = tuple(0 if i in tree else 1 for i in range(n) if i != j)
    return (j,orientation)


def verify_k2n(n):
    counts=brute_distribution(2,n)
    expected_total=n*2**(n-1)
    expected_per_tree=factorial(2*n)//expected_total
    assert len(counts)==expected_total
    assert set(counts.values())=={expected_per_tree}
    reps={K2n_representation(n,T) for T in counts}
    assert None not in reps and len(reps)==expected_total
    for e in range(2*n):
        numerator=sum(c for T,c in counts.items() if e in T)
        assert Fraction(numerator,factorial(2*n)) == Fraction(n+1,2*n)
    for e,f in combinations(range(2*n),2):
        numerator=sum(c for T,c in counts.items() if e in T and f in T)
        target=Fraction(1,n) if e % n == f % n else Fraction(n+2,4*n)
        assert Fraction(numerator,factorial(2*n))==target
    return len(counts), expected_per_tree


def verify_nearby_boundary():
    # Not part of the infinite theorem; verifies nonuniformity already at K_{3,3}.
    distribution=brute_distribution(3,3)
    assert len(distribution)==81
    assert set(distribution.values())=={4200,4680,4800}
    assert sum(distribution.values())==factorial(9)
    # For example, the edge sets below occur 4200 and 4800 times, respectively.
    assert distribution[(0,1,3,5,7)]==4200
    assert distribution[(0,1,2,3,6)]==4800
    return sorted(set(distribution.values()))


def main():
    for n in (2,3,4):
        number, count=verify_k2n(n)
        print('K_{2,%d}: %d trees, each selected by %d of %d edge orders' %
              (n,number,count,factorial(2*n)))
    print('K_{3,3}: nonuniform order counts',verify_nearby_boundary())
    print('EXACT_CHECKS_PASS')

if __name__=='__main__':
    main()
