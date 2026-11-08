#!/usr/bin/env python3
"""Finite checks of a complete four-partite global-coalition theorem.
Run with Python 3; no external packages required.
"""
from itertools import combinations_with_replacement

SUPPORTS = tuple(range(1, 15))
PARTNERS = {s: tuple(t for t in SUPPORTS if (s | t) == 15) for s in SUPPORTS}

def predicted(sizes):
    a, b, c, d = sorted(sizes, reverse=True)
    if d == 1:
        return a + 1
    if d == 2:
        return a + b
    if d <= 5:
        return a + b + c - 3
    return a + b + c + d - 8

def support_optimum(sizes):
    # Exhaustively chooses a multiplicity of each of the 14 possible nonfull
    # support types; capacity inequalities give a necessary-and-sufficient
    # realization test because leftover vertices may join an existing block.
    best = 0
    def walk(j, remain, used, count):
        nonlocal best
        if j == 14:
            if used and all(any(t in used for t in PARTNERS[s]) for s in used):
                best = max(best, count)
            return
        s = SUPPORTS[j]
        walk(j + 1, remain, used, count)
        lim = min(remain[i] for i in range(4) if s & (1 << i))
        for t in range(1, lim + 1):
            r2 = tuple(v-t if s & (1 << i) else v
                       for i, v in enumerate(remain))
            walk(j + 1, r2, used | {s}, count + t)
    walk(0, tuple(sizes), frozenset(), 0)
    return best

def original_graph_optimum(sizes):
    n = sum(sizes)
    parts = tuple(i for i, sz in enumerate(sizes) for _ in range(sz))
    neighbors = [sum(1 << j for j in range(n)
                     if i != j and parts[i] != parts[j]) for i in range(n)]
    allv = (1 << n)-1
    def dominates(mask, complement=False):
        for v in range(n):
            if mask & (1 << v):
                continue
            nbh = (allv ^ (1 << v) ^ neighbors[v]) if complement else neighbors[v]
            if not (mask & nbh):
                return False
        return True
    dom = [dominates(mask) and dominates(mask, True) for mask in range(1 << n)]
    assert all(dom[mask] == all(any(mask & (1 << j) for j in range(n) if parts[j] == p)
                                 for p in range(4)) for mask in range(1 << n))
    best = 0
    def rgs_partitions(i, blocks):
        nonlocal best
        if i == n:
            if any(dom[block] for block in blocks):
                return
            if all(any(dom[b | other] for j, other in enumerate(blocks) if k != j)
                   for k, b in enumerate(blocks)):
                best = max(best, len(blocks))
            return
        bit = 1 << i
        for j in range(len(blocks)):
            blocks[j] |= bit
            rgs_partitions(i+1, blocks)
            blocks[j] ^= bit
        blocks.append(bit)
        rgs_partitions(i+1, blocks)
        blocks.pop()
    rgs_partitions(0, [])
    return best

def main():
    profiles = list(combinations_with_replacement(range(1, 6), 4))
    for sizes in profiles:
        actual = support_optimum(sizes)
        assert actual == predicted(sizes), (sizes, actual, predicted(sizes))
    print('EXHAUSTIVE_70_PART_SIZE_PROFILES_1_TO_5_OK')
    extra = [(1,6,6,6), (2,9,9,9), (3,6,9,12),
             (4,6,6,6), (5,6,6,6), (2,6,7,9), (3,4,6,8)]
    for sizes in extra:
        actual = support_optimum(sizes)
        assert actual == predicted(sizes), (sizes, actual, predicted(sizes))
    print('ADDITIONAL_7_UNBALANCED_PROFILES_OK')
    graphs = [(1,1,1,1),(1,1,1,2),(1,1,2,2),(1,2,2,2),
              (2,2,2,2),(1,1,3,3),(1,2,2,3)]
    for sizes in graphs:
        actual = original_graph_optimum(sizes)
        assert actual == predicted(sizes), (sizes, actual, predicted(sizes))
    print('ORIGINAL_GRAPH_DEFINITION_PARTITION_ENUMERATION_OK',len(graphs))
    for m, expected in [(1,2),(2,4),(3,6),(4,9),(5,12),(6,16),(7,20)]:
        assert predicted((m,)*4) == expected
    print('BALANCED_BOUNDARY_COUNTS_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
