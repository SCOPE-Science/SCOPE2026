#!/usr/bin/env python3
"""Exact finite corroboration of the triple Frobenius equality classification."""
import heapq
from math import gcd

def frobenius(a, b, c):
    d = [10 ** 30] * c
    d[0] = 0
    queue = [(0, 0)]
    while queue:
        value, residue = heapq.heappop(queue)
        if value != d[residue]:
            continue
        for generator in (a, b):
            next_residue = (residue + generator) % c
            next_value = value + generator
            if next_value < d[next_residue]:
                d[next_residue] = next_value
                heapq.heappush(queue, (next_value, next_residue))
    assert all(value < 10 ** 30 for value in d)
    return max(d) - c

number, equalities = 0, 0
for c in range(3, 121):
    k = (c + 1) // 2
    for b in range(2, c):
        for a in range(1, b):
            if gcd(gcd(a, b), c) != 1:
                continue
            actual = frobenius(a, b, c)
            ceiling = b * k - c - 1
            predicted = (c % 2 == 0) and (
                (a, b) == (1, 2) or (a, b) == (c // 2, c // 2 + 1)
            )
            assert actual <= ceiling, (a, b, c, actual, ceiling)
            assert (actual == ceiling) == predicted, (a, b, c, actual, ceiling)
            number += 1
            equalities += predicted
print('EXACT_APERY_EXHAUSTIVE_OK triples=', number,
      'equality_cases=', equalities, 'max_c=120')

checked = 0
for k in range(2, 2001):
    for c in (2 * k - 1, 2 * k):
        for a in range(1, c - 1):
            b = a + 1
            if b >= c:
                continue
            bound = b * ((c + 1) // 2) - c - 1
            nonrep = (bound < 0) or (bound // a < bound % a)
            expected = c % 2 == 0 and (a == 1 or a == k)
            assert nonrep == expected, (a, b, c, bound)
            checked += 1
print('TWO_COIN_INTERVAL_CRITERION_OK cases=', checked,
      'largest_k=2000')
print('VERIFY_OK finite_checks_only=yes independent_audit=no')
