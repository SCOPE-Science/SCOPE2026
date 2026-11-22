#!/usr/bin/env python3
"""Exact checks of Euclidean diameter-degree formula for open two-row ladder matchings.

No external dependencies; finite checks corroborate the universal combinatorial proof.
"""
from functools import lru_cache
from collections import Counter
from math import comb

@lru_cache(None)
def tilings(n):
    if n == 0:
        return ((),)
    z = [('V',) + t for t in tilings(n - 1)]
    if n >= 2:
        z.extend(('H',) + t for t in tilings(n - 2))
    return tuple(z)

def matching_edges(t, n):
    j = 0
    edges = set()
    for tile in t:
        if tile == 'V':
            edges.add(('r', j))
            j += 1
        else:
            edges.add(('a', j))
            edges.add(('b', j))
            j += 2
    assert j == n and len(edges) == n
    return frozenset(edges)

def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in (0, 1))
                       for j in (0, 1)) for i in (0, 1))

def transfer_degree(t):
    V = ((0, 1), (1, 0))
    H = ((1, 1), (1, 1))
    M = ((1, 0), (0, 1))
    for tile in t:
        M = mul(M, V if tile == 'V' else H)
    return M[0][0]

def predicted_degree(t):
    k = t.count('H')
    if k:
        return 2 ** (k - 1)
    return int(len(t) % 2 == 0)

pair_cases = 0
for n in range(2, 13):
    ts = tilings(n)
    es = [matching_edges(t, n) for t in ts]
    actual = [0] * len(ts)
    diametral = 0
    for i in range(len(ts)):
        for j in range(i + 1, len(ts)):
            pair_cases += 1
            squared_distance = len(es[i] ^ es[j])
            assert squared_distance <= 2 * n
            if squared_distance == 2 * n:
                diametral += 1
                actual[i] += 1
                actual[j] += 1
    assert diametral == (2 ** (n - 1) + (-1) ** n) // 3, (n, diametral)
    assert actual == [predicted_degree(t) for t in ts], n
    assert Counter(t.count('H') for t in ts) == Counter(
        {k: comb(n - k, k) for k in range(n // 2 + 1)})

transfer_cases = 0
for n in range(2, 20):
    ts = tilings(n)
    for t in ts:
        transfer_cases += 1
        assert transfer_degree(t) == predicted_degree(t), (n, t)
    assert sum(predicted_degree(t) for t in ts) == 2 * ((2 ** (n - 1) + (-1) ** n) // 3)
print('LADDER_JACOBSTHAL_DIAMETER_PASS',
      'pair_cases=' + str(pair_cases),
      'transfer_cases=' + str(transfer_cases),
      'complete_n=2..12', 'transfer_n=2..19')
