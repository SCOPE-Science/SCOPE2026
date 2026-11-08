#!/usr/bin/env python3
"""Exact finite checks for greedy matchings with low-degree forbidden edges.

Run with Python 3: python check.py
The proof's asymptotic statement does not follow from finite enumeration.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import prod
from random import Random

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

def law(N, missing):
    bad = {tuple(sorted(e)) for e in missing}
    degree = [0] * N
    for i, j in bad:
        check(0 <= i < j < N)
        degree[i] += 1
        degree[j] += 1
    check(max(degree, default=0) <= 2)
    check(N >= 4 and N % 2 == 0)

    @lru_cache(None)
    def rec(mask):
        remain = [i for i in range(N) if mask >> i & 1]
        if len(remain) == 2:
            return {tuple(remain): Fraction(1)}
        available = [(u, v) for u, v in combinations(remain, 2) if (u, v) not in bad]
        check(bool(available))
        result = {}
        for u, v in available:
            for pair, prob in rec(mask ^ (1 << u) ^ (1 << v)).items():
                result[pair] = result.get(pair, Fraction(0)) + prob / len(available)
        return result

    output = rec((1 << N) - 1)
    check(sum(output.values()) == 1)
    return output

def priority_law(N, missing):
    """Independent exhaustive edge-priority implementation for very small N."""
    forbidden = {tuple(sorted(e)) for e in missing}
    edges = [e for e in combinations(range(N), 2) if e not in forbidden]
    outcome = {}
    for ordering in permutations(edges):
        remaining = set(range(N))
        for u, v in ordering:
            if u in remaining and v in remaining:
                remaining.remove(u)
                remaining.remove(v)
        check(len(remaining) in (0, 2))
        if len(remaining) == 2:
            pair = tuple(sorted(remaining))
            outcome[pair] = outcome.get(pair, 0) + 1
    total = prod(range(1, len(edges) + 1))
    return {pair: Fraction(ct, total) for pair, ct in outcome.items()}

def examples(N):
    out = [
        ('one missing', [(0, 1)]),
        ('deleted matching', [(2*j, 2*j+1) for j in range(N//2)]),
        ('deleted path', [(j, j+1) for j in range(N-1)]),
        ('deleted Hamilton cycle', [(j, (j+1) % N) for j in range(N)]),
        ('disjoint deleted triangles', [(3*j+t, 3*j+(t+1) % 3) for j in range(N//3) for t in range(3)]),
    ]
    if N >= 8:
        out += [('two deleted quadrilaterals',
                 [(4*j+t, 4*j+(t+1) % 4) for j in range(2) for t in range(4)])]
    return out

rng = Random(20210423)
for N in (4, 6, 8, 10, 12):
    tests = examples(N)
    for rep in range(5):
        forbidden = []
        degree = [0]*N
        candidates = list(combinations(range(N), 2))
        rng.shuffle(candidates)
        for u, v in candidates:
            if degree[u] < 2 and degree[v] < 2 and rng.randrange(3) == 0:
                forbidden.append((u, v))
                degree[u] += 1
                degree[v] += 1
        tests.append(('seeded degree-2', forbidden))
    for name, H in tests:
        out = law(N, H)
        q = Fraction(3, (N-1)*(N+1))
        for e in H:
            check(out.get(tuple(sorted(e)), Fraction(0)) >= 0)
        failed = sum((out.get(tuple(sorted(e)), Fraction(0)) for e in H), Fraction(0))
        check(0 <= failed <= 1)
        if name == 'one missing':
            check(failed == q)
            check(out[(0, 1)] == q)
        if N == 4 and name in ('one missing', 'deleted matching', 'deleted path'):
            priority = priority_law(N, H)
            for pair in H:
                pair = tuple(sorted(pair))
                check(out.get(pair, Fraction(0)) == priority.get(pair, Fraction(0)))
            check(sum(priority.values()) == failed)
        if N >= 8 and name in ('deleted Hamilton cycle', 'deleted path'):
            print(f'N={N}, {name}: exact failure={failed}, leading={len(H)*q}')

for N in range(4, 102, 2):
    product = prod((Fraction(s-3, s+1) for s in range(4, N+1, 2)), start=Fraction(1))
    check(product == Fraction(3, (N-1)*(N+1)))

print(f'VERIFY_OK {checks} exact assertions')
