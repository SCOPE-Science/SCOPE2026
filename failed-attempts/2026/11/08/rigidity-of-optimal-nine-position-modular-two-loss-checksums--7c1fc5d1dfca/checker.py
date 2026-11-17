#!/usr/bin/env python3
"""Exhaustive finite verifier of the affine orbit of optimal 9-column pair checksums.

Uses only Python's standard library. The search enumerates each sorted valid
nine-set containing zero exactly once; pruning is a necessary pair-sum test.
"""
from math import gcd

MODULUS = 56
CARDINALITY = 9
SEED = (0, 2, 4, 18, 19, 25, 28, 31, 36)


def mask_of(values):
    return sum(1 << x for x in values)


def valid(values):
    sums = [(a + b) % MODULUS for i, a in enumerate(values)
            for b in values[i + 1:]]
    return len(sums) == len(set(sums)) == 36


def orbit_of(seed):
    return {
        mask_of(sorted((u * x + v) % MODULUS for x in seed))
        for u in range(MODULUS) if gcd(u, MODULUS) == 1
        for v in range(MODULUS)
    }


def anchored_solutions():
    digits = [0]
    count = 0
    nodes = 0
    all_masks = set()

    def search(next_value, pair_sums):
        nonlocal count, nodes
        nodes += 1
        k = len(digits)
        if k == CARDINALITY:
            count += 1
            all_masks.add(mask_of(digits))
            return
        for value in range(next_value, MODULUS - (CARDINALITY-k) + 1):
            new = [(value + x) % MODULUS for x in digits]
            # Since digits are distinct, these new sums are distinct.
            if any((1 << r) & pair_sums for r in new):
                continue
            digits.append(value)
            new_sum_mask = sum(1 << r for r in new)
            search(value + 1, pair_sums | new_sum_mask)
            digits.pop()

    search(1, 0)
    return count, nodes, all_masks


def verify():
    assert valid(SEED)
    full_orbit = orbit_of(SEED)
    anchored_orbit = {m for m in full_orbit if (m & 1)}
    assert len(full_orbit) == MODULUS * 24 == 1344, len(full_orbit)
    assert len(anchored_orbit) == 216, len(anchored_orbit)
    count, nodes, anchored = anchored_solutions()
    assert len(anchored) == count == 216, count
    assert anchored == anchored_orbit
    # Double count pairs (A,a), a in A: 9 per set,
    # and 56 translations each of the anchored sets.
    total_sets, rem = divmod(count * MODULUS, CARDINALITY)
    assert rem == 0 and total_sets == len(full_orbit) == 1344
    for m in full_orbit:
        elements = [x for x in range(MODULUS) if m >> x & 1]
        assert len(elements) == CARDINALITY and valid(elements)
    print('PASS: anchored valid sets=%s, search nodes=%s, orbit=%s, unique affine class' % (
        count, nodes, total_sets))


if __name__ == '__main__':
    verify()
