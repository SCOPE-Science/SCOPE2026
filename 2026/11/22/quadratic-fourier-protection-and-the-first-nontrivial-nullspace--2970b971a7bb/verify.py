#!/usr/bin/env python3
"""Exact integer checks for the Walsh spectrum of staircase-board rook placements.

Usage: python3 verify.py
The two independent descriptions are set-partition consecutive arcs and
nonattacking rook placements on cells (i,j) with i < j.
"""
from collections import Counter
from itertools import combinations
from functools import lru_cache


def cells(n):
    return [(i, j) for j in range(n) for i in range(j)]


def arc_masks_from_partitions(n):
    edges = cells(n)
    idx = {e: i for i, e in enumerate(edges)}
    word = [0] * n
    masks = []

    def generate(j, max_label):
        if j == n:
            blocks = {}
            for v, b in enumerate(word):
                blocks.setdefault(b, []).append(v)
            mask = 0
            for block in blocks.values():
                for a, b in zip(block, block[1:]):
                    mask |= 1 << idx[a, b]
            masks.append(mask)
            return
        for k in range(max_label + 2):
            word[j] = k
            generate(j + 1, max(max_label, k))

    generate(1, 0)
    assert len(set(masks)) == len(masks)
    return masks


def fwht(a):
    a = a[:]
    step = 1
    while step < len(a):
        for off in range(0, len(a), 2 * step):
            for j in range(off, off + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return a


def rook_dp(n, freq):
    ix = {e: k for k, e in enumerate(cells(n))}

    @lru_cache(maxsize=None)
    def f(j, used_rows):
        if j == n:
            return 1
        acc = f(j + 1, used_rows)
        for i in range(j):
            if not (used_rows >> i) & 1:
                sign = -1 if (freq >> ix[i, j]) & 1 else 1
                acc += sign * f(j + 1, used_rows | (1 << i))
        return acc

    return f(0, 0)


def check():
    bell = {2: 2, 3: 5, 4: 15, 5: 52, 6: 203}
    mins = {3: {0: 5, 1: 1, 2: -1},
            4: {0: 15, 1: 5, 2: -1},
            5: {0: 52, 1: 22, 2: 2},
            6: {0: 203, 1: 99, 2: 25}}
    zero_degrees = {3: 10, 4: 12, 5: 42, 6: 48, 7: 33, 8: 14, 9: 3}
    total = 0
    for n in range(2, 7):
        m = n * (n - 1) // 2
        v = [0] * (1 << m)
        for mask in arc_masks_from_partitions(n):
            v[mask] = 1
        assert sum(v) == bell[n]
        a = fwht(v)
        total += len(a)
        assert a[0] == bell[n]
        for d in range(min(2, m) + 1):
            vals = [a[sum(1 << i for i in c)]
                    for c in combinations(range(m), d)]
            if n >= 3:
                assert min(vals) == mins[n][d]
                assert all(z != 0 for z in vals)
        if n in (3, 4, 6):
            assert all(t != 0 for t in a)
        if n == 2:
            assert len([v for v in a if v == 0]) == 1
        if n == 5:
            distribution = Counter(s.bit_count() for s, x in enumerate(a) if x == 0)
            assert distribution == zero_degrees
            assert sum(distribution.values()) == 162
            assert len(a) - 162 == 862
            witness = 0
            e = cells(n)
            for cell in [(0, 2), (1, 2), (0, 3)]:
                witness |= 1 << e.index(cell)
            assert a[witness] == 0
            # Independent exact DP checks every frequency at this decisive order.
            for s, expected in enumerate(a):
                assert rook_dp(n, s) == expected, (n, s)
                total += 1
        if n == 6:
            # Independent DP checks every character of degree <= 2.
            for d in range(3):
                for c in combinations(range(m), d):
                    s = sum(1 << i for i in c)
                    assert rook_dp(n, s) == a[s]
                    total += 1
    print("PASS: exact partition-arc and rook-DP comparisons;", total, "coefficient checks")
    print("n=5: 52 partitions; 1024 characters; 162 zero multipliers; rank 862")
    print("n=5 zero character multiplicities by degree:", sorted(zero_degrees.items()))
    print("degree <= 2: zero-free for n = 3,4,5,6; analytic proof covers all n >= 7")

if __name__ == '__main__':
    check()
