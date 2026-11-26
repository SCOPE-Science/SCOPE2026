#!/usr/bin/env python3
from cmath import exp, pi
from math import isclose


def primes_upto(n):
    out = []
    for q in range(2, n + 1):
        if all(q % d for d in range(2, int(q ** 0.5) + 1)):
            out.append(q)
    return out


def pair_counts(p):
    counts = [0] * p
    for a in range(1, p):
        for b in range(a + 1, p):
            counts[(a + b) % p] += 1
    assert counts[0] == (p - 1) // 2
    for t in range(1, p):
        assert counts[t] == (p - 3) // 2


def index_formula(p, c):
    assert p % 2 == 1 and c != 1
    return abs(1 - c) * abs(1 - c ** p) ** ((p - 3) // 2)


def index_one_classification(p, c):
    expected = (c in ({0, 2} if p == 3 else {0}))
    assert (index_formula(p, c) == 1) == expected


def vandermonde_ratio(p, c):
    z = exp(2j * pi / p)
    us = [z ** a + c * z ** (-a) for a in range(1, p)]
    zs = [z ** a for a in range(1, p)]
    ratio = 1 + 0j
    for i in range(p - 1):
        for j in range(i + 1, p - 1):
            ratio *= (us[i] - us[j]) / (zs[i] - zs[j])
    return abs(ratio)


pair_cases = 0
for p in [q for q in primes_upto(97) if q % 2 == 1]:
    pair_counts(p)
    pair_cases += 1

classification_cases = 0
for p in [3, 5, 7, 11, 13, 17, 19]:
    for c in range(-10, 11):
        if c == 1:
            continue
        index_one_classification(p, c)
        classification_cases += 1

numeric_cases = 0
for p in [3, 5, 7, 11]:
    for c in [-2, -1, 0, 2, 3]:
        got = vandermonde_ratio(p, c)
        want = float(index_formula(p, c))
        assert isclose(got, want, rel_tol=2e-9, abs_tol=2e-8), (p, c, got, want)
        numeric_cases += 1

print(f"VERIFY_OK pair_cases={pair_cases} classification_cases={classification_cases} numeric_cases={numeric_cases}")
