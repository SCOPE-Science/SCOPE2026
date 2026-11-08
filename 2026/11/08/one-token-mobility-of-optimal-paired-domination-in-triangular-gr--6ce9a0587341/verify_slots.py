#!/usr/bin/env python3
"""Independent labelled-slot traversal of one-token paired-domination mobility.

A state consists of an unordered collection of centered triples plus a single
uncovered ground vertex. The four elementary exchanges per triple are derived
from swapping center with a leaf or uncovered vertex with a leaf.
"""
from collections import Counter, deque
from math import factorial


def canon(triples, hole):
    return (tuple(sorted((c, *sorted((a, b))) for c, a, b in triples)), hole)


def neighbors(state):
    triples, hole = state
    for i, (c, a, b) in enumerate(triples):
        for leaf, other in ((a, b), (b, a)):
            changed = list(triples)
            changed[i] = (leaf, c, other)
            yield canon(changed, hole)
            changed = list(triples)
            changed[i] = (c, hole, other)
            yield canon(changed, leaf)


def run(m):
    start = canon([(3*i, 3*i+1, 3*i+2) for i in range(m)], 3*m)
    seen = {start: 0}; queue = deque([start]); hist = Counter({0: 1})
    edge_stubs = 0
    while queue:
        s = queue.popleft(); d = seen[s]
        other = set(neighbors(s))
        assert len(other) == 4 * m
        edge_stubs += len(other)
        for t in other:
            if t not in seen:
                seen[t] = d+1; hist[d+1] += 1; queue.append(t)
    n = 3*m+1
    expected = factorial(n) // (2**m * factorial(m))
    assert len(seen) == expected
    assert edge_stubs == 4*m*expected
    assert sum(hist.values()) == expected
    print(f'm={m}: states={expected}, degree={4*m}, edges={edge_stubs//2}, '
          f'eccentricity={max(hist)}, layers={sorted(hist.items())}: PASS')

if __name__ == '__main__':
    for m in (1, 2, 3):run(m)
