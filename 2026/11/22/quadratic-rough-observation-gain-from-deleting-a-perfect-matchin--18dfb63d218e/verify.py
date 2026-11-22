#!/usr/bin/env python3
"""Independent finite checks for closed-neighborhood rough pairs on crown graphs.

Only the standard library is required. Bounds are explicitly finite; the
all-order assertions follow from the separate mathematical proof.
"""
from collections import Counter
from itertools import product


def rough_fibers(n, delete_matching=True):
    """Directly compute both approximations using reflexive neighbor masks."""
    sz = 2 * n
    full = (1 << sz) - 1
    neighborhoods = []
    for i in range(sz):
        row = 1 << i
        if i < n:
            for j in range(n):
                if not delete_matching or i != j:
                    row |= 1 << (j + n)
        else:
            for j in range(n):
                if not delete_matching or (i - n) != j:
                    row |= 1 << j
        neighborhoods.append(row)
    fibers = Counter()
    closures = set()
    simultaneous_nonfull = set()
    for subset in range(1 << sz):
        upper = lower = 0
        for i, hood in enumerate(neighborhoods):
            if subset & hood:
                upper |= 1 << i
            if (subset & hood) == hood:
                lower |= 1 << i
        pair = (lower, upper)
        fibers[pair] += 1
        closures.add(upper)
        if upper != full and lower != 0:
            simultaneous_nonfull.add(pair)
    return fibers, closures, simultaneous_nonfull


def expected_nonfull_closures(n):
    allbits = (1 << n) - 1
    out = {(0, 0)}
    for i in range(n):
        bit = 1 << i
        out.add((bit, allbits ^ bit))
        out.add((allbits ^ bit, bit))
    for subset in range(1 << n):
        if 2 <= subset.bit_count() <= n - 1:
            out.add((subset, allbits))
            out.add((allbits, subset))
    for i in range(n):
        for j in range(n):
            if i != j:
                out.add((allbits ^ (1 << j), allbits ^ (1 << i)))
    return {a | (b << n) for a, b in out}


def verify():
    tests = 0
    crown_total = 0
    for n in range(1, 10):
        fibers, closures, both = rough_fibers(n)
        assert sum(fibers.values()) == 4**n
        assert len(fibers) == (4 if n == 1 else 9 if n == 2 else
                               4 * 2**n + 2 * n*n - 5)
        if n >= 3:
            allmask = (1 << (2*n)) - 1
            expected = expected_nonfull_closures(n)
            assert closures - {allmask} == expected
            assert len(closures) - 1 == 2**(n+1) + n*n - n - 3
            assert len(both) == 2*n
            assert all(size == 1 for pair, size in fibers.items()
                       if pair in both)
            d = 2**(n-1) - n
            central = 4**n - (2*n+4)*2**n + 2*n*n + 4*n + 6
            assert fibers[(0, allmask)] == central
            expected_size_dist = Counter({central: 1})
            expected_size_dist[d] += 4*n
            expected_size_dist[1] += len(fibers) - 1 - 4*n
            assert Counter(fibers.values()) == expected_size_dist
        tests += 1
        crown_total += 4**n
        if 2 <= n <= 7:
            base, _, _ = rough_fibers(n, delete_matching=False)
            assert len(base) == 4 * 2**n - 5
            if n >= 3:
                assert len(fibers) - len(base) == 2*n*n
            tests += 1
    print(f"VERIFY_OK family_cases={tests} crown_subsets={crown_total}")


if __name__ == '__main__':
    verify()
