#!/usr/bin/env python3
"""Finite oracle check of a cyclic-run common-factor classification.

Only finite tests; the accompanying mathematical proof handles all parameters.
"""
from itertools import product
from random import Random


def proposed(a, b):
    q = len(a)
    mismatch = [i for i in range(q) if a[i] != b[i]]
    if not mismatch:
        return []
    out = []
    for t, left in enumerate(mismatch):
        right = mismatch[(t + 1) % len(mismatch)]
        interior = []
        h = (left + 1) % q
        while h != right:
            interior.extend([h] * a[h])
            h = (h + 1) % q
        out.append(tuple([left] * min(a[left], b[left]) +
                         interior + [right] * min(a[right], b[right])))
    return out


def cyclic_factor_set(a, cap):
    period = tuple(c for j, n in enumerate(a) for c in [j] * n)
    n = len(period)
    sampled = period * (cap // n + 3)
    return {sampled[s:s+l] for s in range(n) for l in range(1, cap + 1)}


def check(a, b):
    assert len(a) == len(b) >= 2
    assert a != b
    fs = proposed(a, b)
    assert len(fs) == sum(x != y for x, y in zip(a, b))
    assert len(set(fs)) == len(fs)
    cap = 1 + max(map(len, fs))
    intersection = cyclic_factor_set(a, cap) & cyclic_factor_set(b, cap)
    assert all(f in intersection for f in fs), (a, b, 'missing candidate')
    assert all(any(len(g) >= len(f) and f in tuple_slice(g) for g in fs)
               for f in intersection), (a, b, 'uncovered factor')
    maximal = {f for f in intersection if not any(
        len(g) > len(f) and f in tuple_slice(g) for g in intersection)}
    assert maximal == set(fs), (a, b, fs, maximal)


def tuple_slice(w):
    """Represent contiguous subwords as a set for the verification oracle."""
    return {w[s:e] for s in range(len(w)) for e in range(s + 1, len(w) + 1)}


def main():
    count = 0
    for q, lengths in [(2, range(1, 6)), (3, range(1, 4)),
                       (4, range(1, 3)), (5, range(1, 3))]:
        profiles = list(product(lengths, repeat=q))
        for a in profiles:
            for b in profiles:
                if a != b:
                    check(a, b)
                    count += 1
    rng = Random(376103)
    for _ in range(150):
        q = rng.randint(2, 9)
        a = tuple(rng.randint(1, 8) for _ in range(q))
        b = tuple(rng.randint(1, 8) for _ in range(q))
        if a == b:
            continue
        check(a, b)
        count += 1
    print(f'PASS {count} independent finite pairs (all maximal factors and whole common language up to L+1)')


if __name__ == '__main__':
    main()
