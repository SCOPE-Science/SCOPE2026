"""Recheck the minimal edge-multiset resolving sets and their full automorphism orbits."""
import itertools
from collections import Counter, deque
from pathlib import Path

vertices = [x for x in range(32) if x.bit_count() in (2, 3)]
assert len(vertices) == 20
index = {v: i for i, v in enumerate(vertices)}
neighbor = [[j for j, v in enumerate(vertices) if (u ^ v).bit_count() == 1]
            for u in vertices]
edge_list = [(a,b) for a in range(20) for b in neighbor[a] if a < b]
assert len(edge_list) == 30

distance = []
for root in range(20):
    d = [-1] * 20
    d[root] = 0
    queue = deque([root])
    while queue:
        a = queue.popleft()
        for b in neighbor[a]:
            if d[b] == -1:
                d[b] = d[a] + 1
                queue.append(b)
    distance.append(d)

masks = [int(line) for line in Path(__file__).with_name('min_masks.txt').read_text().splitlines()]
assert len(masks) == len(set(masks)) == 720
assert all(mask.bit_count() == 8 for mask in masks)
for mask in masks:
    selected = [v for v in range(20) if mask >> v & 1]
    signatures = [tuple(sorted(min(distance[v][a], distance[v][b]) for v in selected))
                  for a, b in edge_list]
    assert len(signatures) == len(set(signatures)) == 30

maps = []
for p in itertools.permutations(range(5)):
    for dual in (False, True):
        mapping = []
        for x in vertices:
            y = sum(1 << p[i] for i in range(5) if x >> i & 1)
            if dual:
                y ^= 31
            mapping.append(index[y])
        maps.append(mapping)
assert len({tuple(m) for m in maps}) == 240

def move(mask, perm):
    return sum(1 << perm[i] for i in range(20) if mask >> i & 1)

seeds = [3534, 5582, 5933]
orbits = [{move(seed, g) for g in maps} for seed in seeds]
assert [len(o) for o in orbits] == [240, 240, 240]
assert all(orbits[i].isdisjoint(orbits[j]) for i in range(3) for j in range(i+1,3))
assert set.union(*orbits) == set(masks)
for seed, required_edges in zip(seeds, [4, 5, 6]):
    selected = [i for i in range(20) if seed >> i & 1]
    induced_edges = sum(a in selected and b in selected for a, b in edge_list)
    assert induced_edges == required_edges

all_hist = Counter(min(distance[v][a],distance[v][b]) for v in range(20)
                   for a,b in edge_list[:1])
assert [all_hist[t] for t in range(5)] == [2,4,8,4,2]
print('ORBIT_CERTIFICATE_OK', 'orbits', [len(o) for o in orbits],
      'selected-edge counts', [4, 5, 6])
