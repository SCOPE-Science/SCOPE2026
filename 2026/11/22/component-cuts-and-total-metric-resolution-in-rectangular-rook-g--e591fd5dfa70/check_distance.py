#!/usr/bin/env python3
"""Exact direct-distance census for total resolving sets of a 4 by 4 rook graph."""
from itertools import combinations
from collections import Counter, deque

N = 4
vertices = [(i, j) for i in range(N) for j in range(N)]


def distance(u, v):
    return int(u[0] != v[0]) + int(u[1] != v[1])


pairs = []
for i, j in combinations(range(16), 2):
    a, b = vertices[i], vertices[j]
    outside_witness_mask = 0
    weighted = []
    for k, w in enumerate(vertices):
        difference = abs(distance(w, a) - distance(w, b))
        weighted.append(difference)
        if k != i and k != j and difference:
            outside_witness_mask |= 1 << k
    pairs.append((outside_witness_mask, weighted))

polynomial = Counter()
bases = set()
for mask in range(1 << 16):
    if all(mask & witness for witness, _ in pairs):
        k = mask.bit_count()
        polynomial[k] += 1
        if k == 6:
            bases.add(mask)

assert sorted(polynomial.items()) == [
    (6, 2016), (7, 6912), (8, 10872), (9, 10960),
    (10, 7960), (11, 4368), (12, 1820), (13, 560),
    (14, 120), (15, 16), (16, 1)
]
assert len(bases) == 2016

weak_two_only = both = total_only = neither = 0
for chosen in combinations(range(16), 6):
    mask = sum(1 << i for i in chosen)
    total = mask in bases
    weak_two = all(sum(weights[i] for i in chosen) >= 2 for _, weights in pairs)
    if weak_two and total:
        both += 1
    elif weak_two:
        weak_two_only += 1
    elif total:
        total_only += 1
    else:
        neither += 1
assert (weak_two_only, both, total_only, neither) == (1168, 864, 1152, 4824)

maps = []
for k in range(3):
    maps.append([4 * (i + (1 if i == k else -1 if i == k + 1 else 0)) + j
                 for i, j in vertices])
    maps.append([4 * i + (j + (1 if j == k else -1 if j == k + 1 else 0))
                 for i, j in vertices])
maps.append([4 * j + i for i, j in vertices])


def move(mask, mapping):
    out = 0
    for k in range(16):
        if mask & (1 << k):
            out |= 1 << mapping[k]
    return out

remaining = set(bases)
orbit_sizes = []
while remaining:
    seed = min(remaining)
    visited = {seed}
    queue = deque([seed])
    while queue:
        v = queue.popleft()
        for mapping in maps:
            nxt = move(v, mapping)
            assert nxt in bases
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    remaining -= visited
    orbit_sizes.append(len(visited))
assert sorted(orbit_sizes) == [96, 192, 576, 576, 576]
print('DIRECT_DISTANCE_CHECK_OK')
print('all_set_count=', sum(polynomial.values()))
print('basis_count=', len(bases))
print('orbit_sizes=', sorted(orbit_sizes))
print('weak_two_vs_total=', (weak_two_only, both, total_only, neither))
