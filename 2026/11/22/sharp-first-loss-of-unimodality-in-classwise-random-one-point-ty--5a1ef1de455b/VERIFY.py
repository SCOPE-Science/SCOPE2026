#!/usr/bin/env python3
"""Exact finite corroboration for the class-neighborhood type polynomial.

All arithmetic is integer. The all-size theorem is proved in RESULT.md;
this program does not claim to certify an infinite assertion by enumeration.
"""
from functools import lru_cache
from math import comb

@lru_cache(None)
def partitions(n, minimum=1):
    if n == 0:
        return ((),)
    return tuple((size,) + tail
                 for size in range(minimum, n + 1)
                 for tail in partitions(n - size, size))


def formula(profile):
    n = sum(profile)
    return tuple([len(profile) + 1] + [
        sum(comb(a, j) for a in profile if a >= j)
        for j in range(1, max(profile, default=0) + 1)])


def direct(profile):
    """Enumerate possible finite-extension diagrams, not binomial coefficients."""
    indices = []
    at = 0
    for length in profile:
        indices.append(tuple(range(at, at + length)))
        at += length
    n = at
    counts = [0] * (max(profile, default=0) + 1)
    observed = set()
    # The new E-class can be fresh or identical to one represented old class.
    for class_index in range(-1, len(indices)):
        for mask in range(1 << n):
            # Every edge endpoint must share the new vertex's E-class.
            if class_index == -1:
                valid = mask == 0
            else:
                eligible = set(indices[class_index])
                valid = all(((mask >> i) & 1) == 0 or i in eligible
                            for i in range(n))
            if not valid:
                continue
            key = (class_index, mask)
            assert key not in observed
            observed.add(key)
            counts[mask.bit_count()] += 1
    return tuple(counts)


def unimodal(sequence):
    descending = False
    for a, b in zip(sequence, sequence[1:]):
        if b < a:
            descending = True
        elif b > a and descending:
            return False
    return True


def run():
    examined = 0
    exceptions = []
    for n in range(1, 17):
        bad = []
        for profile in partitions(n):
            c = formula(profile)
            examined += 1
            if n <= 8:
                direct_counts = direct(profile)
                assert c == direct_counts, (profile, c, direct_counts)
            if not unimodal(c):
                bad.append(profile)
            for j in range(3, len(c) - 1):
                if c[j+1] > c[j]:
                    assert c[j] > c[j-1], (n, profile, j, c)
        assert bad == ([] if n < 16 else [(1,) * 10 + (6,)]), (n, bad)
        exceptions.extend((n, p) for p in bad)
    assert examined == 914, examined
    for n in range(16, 101):
        profile = (1,) * (n - 6) + (6,)
        c = formula(profile)
        assert c[1] == n and c[2] == 15 and c[3] == 20
        assert not unimodal(c)
    assert formula((1,) * 10 + (6,)) == (12, 16, 15, 20, 15, 6, 1)
    print('PARTITIONS_CHECKED=914')
    print('DIRECT_EXTENSION_MAX_N=8')
    print('FIRST_NONUNIMODAL_N=16')
    print('UNIQUE_PROFILE_16=(1^10,6)')
    print('WITNESS_COEFFICIENTS=(12,16,15,20,15,6,1)')
    print('PERSISTENCE_TESTED_N=16..100')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
