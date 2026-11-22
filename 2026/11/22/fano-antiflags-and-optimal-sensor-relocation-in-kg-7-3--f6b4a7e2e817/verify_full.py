#!/usr/bin/env python3
"""Exhaustive, reproducible finite verification on the 35-vertex odd graph."""
from itertools import combinations
from collections import Counter, deque

TRIPLES = tuple(combinations(range(7), 3))
MASKS = tuple(sum(1 << x for x in t) for t in TRIPLES)
NEIGHBORS = tuple(sum(1 << j for j, b in enumerate(MASKS) if not (a & b)) for a in MASKS)
ALL = (1 << len(TRIPLES)) - 1

def power_dominates(indices):
    observed = 0
    for v in indices:
        observed |= (1 << v) | NEIGHBORS[v]
    while True:
        forced = 0
        for v in range(35):
            if observed & (1 << v):
                unseen = NEIGHBORS[v] & ~observed
                if unseen and (unseen & (unseen - 1)) == 0:
                    forced |= unseen
        if (forced & ~observed) == 0:
            return observed == ALL
        observed |= forced

def is_fan(indices):
    triples = [set(TRIPLES[i]) for i in indices]
    for c in range(7):
        star = [t for t in triples if c in t]
        if len(star) != 3: continue
        paired = [t - {c} for t in star]
        if any(paired[i] & paired[j] for i in range(3) for j in range(i + 1, 3)):
            continue
        trans = next(t for t in triples if c not in t)
        if all(len(trans & part) == 1 for part in paired):
            return True
    return False

def bfs(adjacency, start):
    dist = [-1] * len(adjacency)
    dist[start] = 0
    queue = deque([start])
    while queue:
        a = queue.popleft()
        for b in adjacency[a]:
            if dist[b] < 0:
                dist[b] = dist[a] + 1
                queue.append(b)
    return dist

def main():
    assert len(TRIPLES) == 35 and all(v.bit_count() == 4 for v in NEIGHBORS)
    for k in range(1, 4):
        assert sum(power_dominates(s) for s in combinations(range(35), k)) == 0
    configurations = [s for s in combinations(range(35), 4) if power_dominates(s)]
    assert len(configurations) == 840
    assert all(is_fan(s) for s in configurations)
    assert sum(is_fan(s) for s in combinations(range(35), 4)) == 840
    index = {s: i for i, s in enumerate(configurations)}
    jump = [set() for _ in configurations]
    slide = [set() for _ in configurations]
    for i, s in enumerate(configurations):
        for old in s:
            remaining = set(s) - {old}
            for new in range(35):
                if new in s: continue
                t = tuple(sorted(remaining | {new}))
                j = index.get(t)
                if j is not None:
                    jump[i].add(j)
                    if NEIGHBORS[old] & (1 << new):
                        slide[i].add(j)
    assert Counter(map(len, jump)) == {13: 840}
    assert Counter(map(len, slide)) == {1: 840}
    assert sum(map(len, jump)) // 2 == 5460
    assert sum(map(len, slide)) // 2 == 420
    assert all(i in slide[next(iter(slide[i]))] for i in range(840))
    jump_distances = Counter()
    for root in range(840):
        dist = bfs(jump, root)
        assert min(dist) == 0 and max(dist) == 6 and -1 not in dist
        for d in dist[root + 1:]: jump_distances[d] += 1
    assert jump_distances == {1: 5460, 2: 16380, 3: 36540, 4: 85680, 5: 134400, 6: 73920}
    assert len(configurations) * (len(configurations) - 1) // 2 == sum(jump_distances.values())
    print('PASS: 35 vertices; no successful 1-, 2-, or 3-sets; precisely 840 successful 4-sets')
    print('PASS: all 840 successful 4-sets are exactly the central-fan/transversal configurations')
    print('PASS: jump 13-regular, 5460 edges, connected, radius=diameter=6')
    print('PASS: slide 420 disjoint edges, every vertex degree 1')
    print('PASS: jump distance distribution (unordered pairs)', sorted(jump_distances.items()))

if __name__ == '__main__': main()
