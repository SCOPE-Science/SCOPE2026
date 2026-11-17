#!/usr/bin/env python3
"""Exact finite diagnostics for cyclic two-site gray-level opening.

The unrestricted theorem is proved analytically in RESULT.md; these tests
check the local selector multiplicity mechanism and exact witnesses.
"""
from itertools import permutations
from fractions import Fraction
from random import Random


def opening(x):
    n = len(x)
    return [min(x[i], max(x[(i-1) % n], x[(i+1) % n]))
            for i in range(n)]


def centered_square_times_n(x):
    n = len(x)
    return n * sum(v*v for v in x) - sum(x)**2


def selector_for_permutation(p):
    n = len(p)
    a = []
    for i in range(n):
        left, right = (i-1) % n, (i+1) % n
        if p[i] > p[left] and p[i] > p[right]:
            a.append(left if p[left] > p[right] else right)
        else:
            a.append(i)
    return a


counts_by_n = {}
for n in range(3, 9):
    patterns = set()
    for p in permutations(range(n)):
        patterns.add(tuple(selector_for_permutation(p)))
    two_triples = False
    for a in patterns:
        multiplicities = [a.count(j) for j in range(n)]
        assert max(multiplicities) <= 3
        if multiplicities.count(3) >= 2:
            two_triples = True
    assert two_triples == (n == 8), (n, two_triples)
    counts_by_n[n] = len(patterns)
print('EXHAUSTIVE_LOCAL_SELECTOR_PATTERNS', counts_by_n)

for n in range(8, 61):
    x = [Fraction(0) for _ in range(n)]
    for i in (1, 3, 5, 7):
        x[i] = Fraction(3)
    for i in (2, 6):
        x[i] = Fraction(1)
    y = x.copy()
    e = Fraction(1, 4)
    y[2] += e
    y[6] -= e
    h = [v-u for u, v in zip(x, y)]
    d = [v-u for u, v in zip(opening(x), opening(y))]
    assert centered_square_times_n(d) == 3*centered_square_times_n(h)
    assert [i for i, val in enumerate(d) if val == e] == [1,2,3]
    assert [i for i, val in enumerate(d) if val == -e] == [5,6,7]
print('EXACT_SHARP_TWO_INPUT_WITNESSES_N_8_TO_60_PASSED')

rng = Random(97128)
tests = 0
for n in range(2, 31):
    for k in range(500):
        x = [Fraction(rng.randint(-12, 12), rng.randint(1, 7)) for _ in range(n)]
        y = [Fraction(rng.randint(-12, 12), rng.randint(1, 7)) for _ in range(n)]
        h = [v-u for u, v in zip(x, y)]
        d = [v-u for u, v in zip(opening(x), opening(y))]
        assert centered_square_times_n(d) <= 3*centered_square_times_n(h)
        tests += 1
print('EXACT_RATIONAL_TWO_INPUT_CHECKS_PASSED', tests)

for a in (Fraction(-3), Fraction(0), Fraction(5, 2)):
    for b in (Fraction(-7), Fraction(2), Fraction(9, 4)):
        assert len(set(opening([a,b]))) == 1
print('TWO_SITE_CONSTANT_OUTPUT_PASSED')
print('ALL_CYCLIC_OPENING_HILBERT_CHECKS_PASSED')
