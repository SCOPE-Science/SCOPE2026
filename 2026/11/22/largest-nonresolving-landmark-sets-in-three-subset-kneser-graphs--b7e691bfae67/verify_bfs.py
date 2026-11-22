#!/usr/bin/env python3
"""Exhaustive distance-based verification of worst-case resolving thresholds."""
from collections import Counter, deque
from itertools import combinations
from math import comb
import json


def run(n):
    vertices = tuple(combinations(range(n), 3))
    N = len(vertices)
    masks = tuple(sum(1 << x for x in v) for v in vertices)
    adj = [tuple(j for j, b in enumerate(masks) if i != j and not (a & b))
           for i, a in enumerate(masks)]
    dist = []
    for i in range(N):
        row = [-1] * N
        row[i] = 0
        q = deque([i])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if row[y] < 0:
                    row[y] = row[x] + 1
                    q.append(y)
        assert all(d >= 0 for d in row)
        dist.append(row)
    counts = {r: Counter() for r in (0, 1, 2)}
    witnesses = {}
    minimum = N + 1
    for i, j in combinations(range(N), 2):
        overlap = (masks[i] & masks[j]).bit_count()
        distinguish = sum(dist[i][w] != dist[j][w] for w in range(N))
        counts[overlap][distinguish] += 1
        minimum = min(minimum, distinguish)
        key = tuple(w for w in range(N) if dist[i][w] == dist[j][w])
        witnesses.setdefault(key, []).append((i, j))
    maximum = N - minimum
    best = [k for k in witnesses if len(k) == maximum]
    multiplicities = Counter(len(witnesses[k]) for k in best)
    if n == 7:
        assert (minimum, len(best), multiplicities) == (20, 21, Counter({10: 21}))
    else:
        assert minimum == 2 + 2 * comb(n-4, 2)
        assert len(best) == comb(n,2)*comb(n-2,2)
        assert multiplicities == Counter({1: len(best)})
    return {
        'n': n, 'vertices': N,
        'distinguishing_by_intersection': {str(r): dict(sorted(c.items())) for r, c in counts.items()},
        'minimum_distinguishers': minimum, 'threshold': N-minimum+1,
        'largest_nonresolving_size': maximum, 'largest_nonresolving_sets': len(best),
        'bisector_witness_multiplicities': dict(sorted(multiplicities.items()))
    }


if __name__ == '__main__':
    for n in range(7, 12):
        print(json.dumps(run(n), sort_keys=True, separators=(',', ':')))
