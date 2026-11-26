#!/usr/bin/env python3
"""Standalone exhaustive finite checks for crown-graph induced-forest enumerators.

No packages or network connection required. Run: python3 verify.py
Every subset is checked against its induced graph, rather than the theorem's
structural classification. The analytic formulas are universal proofs only
when combined with the argument in RESULT.md; this is a finite test.
"""
from collections import Counter
from math import comb


def expected(n):
    forest = Counter()
    for k in range(n + 1):
        forest[k] += 2 * comb(n, k)
    forest[0] -= 1
    for b in range(1, n + 1):
        forest[b + 1] += n * comb(n, b)
    for a in range(2, n + 1):
        forest[a + 1] += n * comb(n, a)
    forest[4] += comb(n, 2) * (2 * n - 3)
    forest[5] += n * (n - 1) * (n - 2)
    maximal = Counter()
    maximal[5] += n * (n - 1) * (n - 2)
    if n >= 4:
        maximal[n + 1] += 2 * n
    return +forest, +maximal


def enumerate_by_graph(n):
    N = 2 * n
    edges = [(i, n + j) for i in range(n) for j in range(n) if i != j]
    forests = set()

    def is_forest(bits):
        parent = list(range(N))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        for u, v in edges:
            if bits & (1 << u) and bits & (1 << v):
                ru, rv = root(u), root(v)
                if ru == rv:
                    return False
                parent[ru] = rv
        return True

    for bits in range(1 << N):
        if is_forest(bits):
            forests.add(bits)

    profile = Counter(bits.bit_count() for bits in forests)
    maxima = Counter(
        bits.bit_count()
        for bits in forests
        if all(bits | (1 << v) not in forests for v in range(N) if not bits & (1 << v))
    )
    return +profile, +maxima


def check():
    totals = 0
    for n in range(3, 9):
        measured = enumerate_by_graph(n)
        predicted = expected(n)
        assert measured == predicted, (n, measured, predicted)
        totals += 1 << (2 * n)
        print(f'n={n}: all {1 << (2*n)} subsets; induced forests={sum(measured[0].values())}; '
              f'maximal profile={dict(sorted(measured[1].items()))}; OK')
    print(f'ALL_CHECKS_PASSED: {totals} subsets inspected, n=3,...,8')


if __name__ == '__main__':
    check()
