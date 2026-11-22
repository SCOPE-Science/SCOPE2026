#!/usr/bin/env python3
"""Exact exhaustive certificate for feedback-set add/delete reconfiguration on the Fano incidence graph.

All tests enumerate complete finite spaces. Python 3 standard library only.
"""
from collections import Counter, deque
from itertools import combinations

LINES = tuple(sorted(tuple(c) for c in combinations(range(1, 8), 3)
                     if c[0] ^ c[1] ^ c[2] == 0))
assert len(LINES) == 7
EDGES = tuple((p - 1, 7 + i) for i, line in enumerate(LINES) for p in line)
assert len(EDGES) == 21
FULL = (1 << 14) - 1


def is_fvs(mask):
    """Complement-of-mask is a forest iff a union-find pass finds no cycle."""
    parent = list(range(14))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in EDGES:
        if (mask >> u) & 1 or (mask >> v) & 1:
            continue
        a, b = root(u), root(v)
        if a == b:
            return False
        parent[a] = b
    return True


def states_and_adjacency(cap):
    states = [m for m in range(1 << 14) if m.bit_count() <= cap and is_fvs(m)]
    where = {m: i for i, m in enumerate(states)}
    neighbors = [[] for _ in states]
    for i, m in enumerate(states):
        if m.bit_count() == cap:
            continue
        for bit in range(14):
            if not ((m >> bit) & 1):
                j = where.get(m | (1 << bit))
                if j is not None:
                    neighbors[i].append(j)
                    neighbors[j].append(i)
    return states, neighbors


def components(graph):
    visited = set()
    parts = []
    for start in range(len(graph)):
        if start in visited:
            continue
        visited.add(start)
        q = [start]
        for u in q:
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        parts.append(q)
    return parts


def bfs(src, graph):
    ds = [-1] * len(graph)
    ds[src] = 0
    q = deque([src])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if ds[v] < 0:
                ds[v] = ds[u] + 1
                q.append(v)
    return ds


def main():
    # Enumerate all 2**14 subsets; no sampling or heuristic search.
    ALL = {m for m in range(1 << 14) if is_fvs(m)}
    bysize = Counter(m.bit_count() for m in ALL)
    assert all(k >= 4 for k in bysize)
    assert (bysize[4], bysize[5], bysize[6]) == (70, 812, 2254)
    a5, g5 = states_and_adjacency(5)
    assert len(a5) == 882
    assert sum(map(len, g5)) // 2 == 700
    sizes5 = Counter(map(len, components(g5)))
    assert sizes5 == {1: 168, 51: 14}, sizes5
    assert sum(len(v) == 0 for v in g5) == 168
    a6, g6 = states_and_adjacency(6)
    assert len(a6) == 3136
    assert sum(map(len, g6)) // 2 == 8008
    assert Counter(map(len, components(g6))) == {3136: 1}
    e = Counter()
    distances = Counter()
    excess = Counter()
    min_pairs = 0
    for i, m in enumerate(a6):
        d = bfs(i, g6)
        assert -1 not in d
        e[(m.bit_count(), max(d))] += 1
        for j in range(i + 1, len(a6)):
            target = a6[j]
            distance = d[j]
            distances[distance] += 1
            diff = distance - (m ^ target).bit_count()
            assert diff >= 0 and diff % 2 == 0
            if diff:
                excess[(*sorted((m.bit_count(), target.bit_count())), diff)] += 1
            if m.bit_count() == target.bit_count() == 4:
                assert distance == (m ^ target).bit_count(), (m, target, distance)
                min_pairs += 1
    assert min_pairs == 2415
    assert e == {(4, 10): 70, (5, 11): 812, (6, 12): 2254}, e
    assert dict(excess) == {
        (4, 6, 2): 1260,
        (5, 5, 2): 546,
        (5, 6, 2): 67956,
        (6, 6, 2): 312704,
        (6, 6, 4): 840,
    }, excess
    assert sum(distances.values()) == len(a6) * (len(a6) - 1) // 2
    assert distances[12] == 25844
    print('VERIFIED full14=16384 FVS4=70 FVS5=812 FVS6=2254')
    print('VERIFIED B5: vertices=882 edges=700 components=14x51+168x1')
    print('VERIFIED B6: vertices=3136 edges=8008 connected=1 radius=10 diameter=12')
    print('VERIFIED eccentricities: size4=10(x70), size5=11(x812), size6=12(x2254)')
    print('VERIFIED minimum-pair distances all 2415 exactly Hamming; deviations=0')
    print('VERIFIED other-pair Hamming excess=', sorted(excess.items()))
    print('VERIFIED distance histogram=', sorted(distances.items()))

if __name__ == '__main__':
    main()
