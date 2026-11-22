#!/usr/bin/env python3
"""Exact finite checks of perfect-matchable Cayley-tree leaf laws.

Only the Python standard library is used. Analytical asymptotics are proved in
RESULT.md, not inferred from the finite enumerations here.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def cayley_edges(code, n):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        u = next(i for i, d in enumerate(degree) if d == 1)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
    u, v = [i for i, d in enumerate(degree) if d == 1]
    edges.append((u, v))
    return edges


def leaf_count(edges, n):
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    return degree.count(1)


def has_perfect_matching(edges, n):
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    cache = {}
    def rec(mask):
        if mask == 0:
            return True
        if mask in cache:
            return cache[mask]
        u = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << u)
        ans = any((rest & (1 << v)) and rec(rest ^ (1 << v))
                  for v in neighbors[u])
        cache[mask] = bool(ans)
        return bool(ans)
    return rec((1 << n) - 1)


def predicted_leaf_probability(m, leaves):
    # Factorial-moment inversion for m possible leaf-pairs.
    if m == 1:
        return Fraction(int(leaves == 2))
    return sum((Fraction(comb(m, k) * (2*m-k)**(m-2), (2*m)**(m-2))
                * comb(k, leaves) * (-1)**(k-leaves))
               for k in range(leaves, m+1))


def predicted_total(m):
    return factorial(2*m) // factorial(m) * (2*m)**(m-2) if m >= 2 else 1


def direct_cayley_enumeration(m):
    n = 2*m
    counts = Counter()
    for code in product(range(n), repeat=n-2):
        edges = cayley_edges(code, n)
        if has_perfect_matching(edges, n):
            counts[leaf_count(edges, n)] += 1
    total = sum(counts.values())
    assert total == predicted_total(m), ('total', m, total)
    for leaves in range(n+1):
        assert Fraction(counts[leaves], total) == predicted_leaf_probability(m, leaves), (m, leaves)
    return total


def quotient_enumeration(m):
    # Fix matching [(0,1),(2,3),...], enumerate each quotient Cayley tree
    # and each of the four endpoint assignments on every quotient edge.
    counts = Counter()
    for code in product(range(m), repeat=m-2):
        quotient = cayley_edges(code, m)
        for choices in product(range(4), repeat=m-1):
            edges = [(2*i, 2*i+1) for i in range(m)]
            for (u, v), c in zip(quotient, choices):
                edges.append((2*u+(c & 1), 2*v+((c >> 1) & 1)))
            counts[leaf_count(edges, 2*m)] += 1
    total = m**(m-2) * 4**(m-1)
    assert sum(counts.values()) == total
    for leaves in range(2*m+1):
        assert Fraction(counts[leaves], total) == predicted_leaf_probability(m, leaves), (m, leaves)
    return total


def moment_identity(m):
    a = Fraction((2*m-1)**(m-2), (2*m)**(m-2))
    b = Fraction((m-1)**(m-2), m**(m-2))
    mean = m*a
    var = m*a*(1-a)+m*(m-1)*(b-a*a)
    mass = [predicted_leaf_probability(m,l) for l in range(m+1)]
    assert sum(mass) == 1 and all(p >= 0 for p in mass)
    assert sum(l*p for l,p in enumerate(mass)) == mean
    assert sum((l-mean)**2*p for l,p in enumerate(mass)) == var
    assert mass[m] == Fraction(1, 2**(m-2))
    assert mass[2] == Fraction(factorial(m), 2*(2*m)**(m-2))
    return mean, var


def run():
    for m in (2,3,4):
        print('direct',m,direct_cayley_enumeration(m))
    for m in (2,3,4,5):
        print('quotient',m,quotient_enumeration(m))
    for m in range(2, 25):
        moment_identity(m)
    print('23 exact moment/distribution checks passed; direct and quotient enumeration checks passed.')

if __name__ == '__main__':
    run()
