#!/usr/bin/env python3
"""Exact integer checks for the seven-excess Shannon/Simpson threshold.

Only uses the Python standard library. This finite check supports the
partition certificate; the proof of uniformity in species richness is analytic.
"""
from functools import lru_cache
from itertools import combinations
from math import prod

@lru_cache(maxsize=None)
def partitions(total, minimum=1):
    """All nondecreasing positive-part partitions, as tuples."""
    if total == 0:
        return ((),)
    return tuple((a,) + rest
                 for a in range(minimum, total + 1)
                 for rest in partitions(total - a, a))


def majorizes(a, b):
    length = max(len(a), len(b))
    x = sorted(a, reverse=True) + [0] * (length - len(a))
    y = sorted(b, reverse=True) + [0] * (length - len(b))
    assert sum(x) == sum(y)
    sx = sy = 0
    for u, v in zip(x, y):
        sx += u
        sy += v
        if sx < sy:
            return False
    return True


def keys_from_excess(e):
    """Square-sum excess and exact exponential Shannon key."""
    abundances = [z + 1 for z in e]
    return (sum((z * z - 1) for z in abundances),
            prod(z ** z for z in abundances))


def check():
    assert [len(partitions(t)) for t in range(8)] == [1, 1, 2, 3, 5, 7, 11, 15]
    expected = {
        6: {
            ((1, 1, 1, 3), (2, 2, 2)),
            ((1, 1, 4), (3, 3)),
        },
        7: {
            ((1, 1, 1, 1, 3), (1, 2, 2, 2)),
            ((1, 1, 1, 4), (1, 3, 3)),
            ((1, 1, 1, 4), (2, 2, 3)),
            ((1, 1, 5), (3, 4)),
        },
    }
    checks = 0
    for t in range(8):
        incomparables = set()
        opposites = set()
        for a, b in combinations(partitions(t), 2):
            assert sum(a) == sum(b) == t
            comparable = majorizes(a, b) or majorizes(b, a)
            ca, pa = keys_from_excess(a)
            cb, pb = keys_from_excess(b)
            if not comparable:
                incomparables.add((a, b))
                if (ca - cb) * (pa - pb) < 0:
                    opposites.add((a, b))
            checks += 1
        assert incomparables == expected.get(t, set()), (t, incomparables)
        assert opposites == ({((1, 1, 5), (3, 4))} if t == 7 else set())
        checks += 2
    # Cross-check the fixed-richness abundance enumeration independently.
    # No finite list of k alone proves the unbounded-richness assertion.
    for k in range(3, 12):
        for t in range(8):
            profiles = [tuple(sorted([1] * (k-len(e)) + [z+1 for z in e]))
                        for e in partitions(t) if len(e) <= k]
            assert len(profiles) == len(set(profiles))
            incompatible = []
            for a, b in combinations(profiles, 2):
                ca, cb = sum(z*z for z in a), sum(z*z for z in b)
                pa, pb = prod(z**z for z in a), prod(z**z for z in b)
                if (ca-cb)*(pa-pb) < 0:
                    incompatible.append((a, b))
                checks += 1
            expect = []
            if t == 7:
                a = tuple(sorted([1] * (k-3) + [1,4,5]))
                b = tuple(sorted([1] * (k-3) + [2,2,6]))
                expect = [(a,b)] if a < b else [(b,a)]
            assert len(incompatible) == len(expect), (k,t,incompatible)
            assert set(tuple(sorted(z)) for z in incompatible) == set(tuple(sorted(z)) for z in expect)
            checks += 3
    a=(1,4,5)
    b=(2,2,6)
    assert sum(z*z for z in a)==42
    assert sum(z*z for z in b)==44
    assert prod(z**z for z in a)==800000
    assert prod(z**z for z in b)==746496
    checks += 4
    print(f"PASS: {checks} assertions/structural comparisons; partitions t=0..7; k=3..11")

if __name__ == "__main__":
    check()
