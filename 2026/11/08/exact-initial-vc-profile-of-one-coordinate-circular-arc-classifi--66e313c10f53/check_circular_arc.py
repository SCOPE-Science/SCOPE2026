#!/usr/bin/env python3
"""Finite verification of cyclic-coordinate arc shattering witnesses.

No external packages, random seeds, network access, or other files needed.
"""
from collections import Counter
from itertools import combinations
from math import comb

CYCLES = {
    3: [(0, 1, 2)],
    4: [(0, 1, 2, 3), (0, 1, 3, 2)],
    5: [(0, 1, 2, 3, 4), (0, 2, 4, 1, 3)],
    6: [(0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4),
        (0, 2, 4, 5, 1, 3), (0, 3, 4, 1, 2, 5)],
    7: [(0, 1, 2, 3, 4, 5, 6), (0, 1, 3, 4, 6, 2, 5),
        (0, 2, 3, 5, 1, 4, 6), (0, 4, 1, 2, 6, 3, 5),
        (0, 3, 6, 1, 5, 2, 4)],
}

def arc_traces(cycle):
    n = len(cycle)
    return {frozenset(cycle[(start + offset) % n] for offset in range(size))
            for start in range(n) for size in range(n + 1)}

def all_subsets(n):
    return {frozenset(s) for k in range(n+1)
            for s in combinations(range(n), k)}


def run():
    total_patterns = 0
    for n, collection in CYCLES.items():
        traces = set()
        counts = Counter()
        for cyc in collection:
            assert tuple(sorted(cyc)) == tuple(range(n)), (n, cyc)
            one = arc_traces(cyc)
            traces.update(one)
            for subset in one: counts[subset] += 1
            for k in range(1, n):
                assert len([t for t in one if len(t) == k]) == n
        assert traces == all_subsets(n), (n, len(traces), 2**n)
        if n == 7:
            assert all(counts[frozenset(s)] == 1
                       for s in combinations(range(7), 3))
            assert all(counts[frozenset(s)] > 0
                       for s in combinations(range(7), 2))
        total_patterns += len(traces)
        print('n', n, 'coordinates', len(collection),
              'traces', len(traces), 'target', 2**n,
              'middle', comb(n, n//2))
    # Counting obstructions for all smaller coordinate budgets.
    for n, k, need, upper in [(4,2,2,1), (6,3,4,3),
                                (7,3,5,4), (8,4,9,8)]:
        assert upper*n < comb(n,k)
        assert (comb(n,k) + n - 1)//n == need
    print('CIRCULAR_ARC_STUMP_PASS', total_patterns,
          'WITNESSES', sum(map(len, CYCLES.values())), 'LOWER_BOUNDS', 4)

if __name__ == '__main__':
    run()
