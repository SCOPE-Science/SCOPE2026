#!/usr/bin/env python3
"""Brute-force test of the stated circular antidictionary, using independent factor enumeration."""
from itertools import product
from random import Random


def proposed(lengths):
    q = len(lengths)
    forbidden = set()
    for i, a in enumerate(lengths):
        forbidden.add((i,) * (a + 1))
        for j in range(q):
            if j != i and j != (i + 1) % q:
                forbidden.add((i, j))
        for t in range(1, a):
            forbidden.add(((i - 1) % q,) + (i,) * t + ((i + 1) % q,))
    return forbidden


def independently_enumerated(lengths):
    q = len(lengths)
    period = tuple(v for v, a in enumerate(lengths) for _ in range(a))
    p = len(period)
    # For a primitive period, all minimal forbidden factors have length <= p.
    factors = set()
    for k in range(1, p + 1):
        doubled = period * 3
        factors.update(doubled[s:s + k] for s in range(p))
    missing = set()
    for prefix in factors:
        if len(prefix) >= p:
            continue
        for letter in range(q):
            v = prefix + (letter,)
            if v not in factors and v[1:] in factors:
                missing.add(v)
    return missing


def run():
    n = 0
    for q in (2, 3, 4, 5):
        for lengths in product(range(1, 4), repeat=q):
            if sum(lengths) > 9:
                continue
            expected = proposed(lengths)
            observed = independently_enumerated(lengths)
            assert observed == expected, (lengths, sorted(observed ^ expected))
            p = sum(lengths)
            assert len(expected) == p + q * (q - 2)
            n += 1
    rng = Random(481007)
    for _ in range(450):
        q = rng.choice((2, 3, 4, 5))
        lengths = tuple(rng.randint(1, 4) for _ in range(q))
        if sum(lengths) > 10:
            continue
        assert independently_enumerated(lengths) == proposed(lengths)
        n += 1
    print('PASS:', n, 'independent full finite antidictionary comparisons')


if __name__ == '__main__':
    run()
