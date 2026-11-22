#!/usr/bin/env python3
"""Exhaustive exact flip metric on proper two-colorings of PG(2,3)."""
from itertools import product
from collections import Counter, deque

def normalize(v):
    a = next(t for t in v if t)
    return tuple((t * (1 if a == 1 else 2)) % 3 for t in v)

points = sorted({normalize(x) for x in product(range(3), repeat=3) if any(x)})
assert len(points) == 13
lines = sorted({sum(1 << i for i, p in enumerate(points)
                    if sum(a*b for a,b in zip(p, q)) % 3 == 0)
                for q in points})
assert len(lines) == 13 and all(x.bit_count() == 4 for x in lines)
assert all(sum((l & (1 << i)) != 0 and (l & (1 << j)) != 0 for l in lines) == 1
           for i in range(13) for j in range(i+1,13))

valid = {x for x in range(1 << 13)
         if all(0 < (x & l) < l for l in lines)}
assert len(valid) == 468
assert Counter(x.bit_count() for x in valid) == {6: 234, 7: 234}
assert all(((1 << 13) - 1) ^ x in valid for x in valid)

neighbors = {x: [x ^ (1 << i) for i in range(13) if (x ^ (1 << i)) in valid]
             for x in valid}
assert all(len(y) == 3 for y in neighbors.values())
assert sum(map(len, neighbors.values())) == 1404

joint = Counter(); detour = Counter(); spheres = set(); antipodes = True
verts = sorted(valid)
for index, start in enumerate(verts):
    distance = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for w in neighbors[u]:
            if w not in distance:
                distance[w] = distance[u] + 1
                queue.append(w)
    assert len(distance) == len(verts)
    shell = tuple(Counter(distance.values())[i] for i in range(14))
    spheres.add(shell)
    assert max(distance.values()) == 13
    assert [t for t in verts if distance[t] == 13] == [start ^ ((1 << 13) - 1)]
    for t in verts[index + 1:]:
        h = (start ^ t).bit_count(); d = distance[t]
        assert d >= h and (d - h) % 2 == 0
        joint[(h, d)] += 1
        detour[d - h] += 1
assert len(spheres) == 1
assert detour == {0: 83070, 2: 26208}, detour
assert sum(joint.values()) == 468 * 467 // 2
expected = {
    (1, 1): 702, (2, 2): 1404, (3, 3): 2808,
    (4, 4): 5616, (4, 6): 2808,
    (5, 5): 11232, (5, 7): 5616,
    (6, 6): 14040, (6, 8): 10296,
    (7, 7): 16848, (7, 9): 7488,
    (8, 8): 16848, (9, 9): 8424,
    (10, 10): 2808, (11, 11): 1404,
    (12, 12): 702, (13, 13): 234
}
assert joint == expected, (joint - expected, expected - joint)
print('PASS: 13 points, 13 lines, projective incidence 2-(13,4,1)')
print('proper_coloring_count=468 sizes_6_7=234,234 edges=702 degree=3')
print('components=1 radius=13 diameter=13 unique_antipode=complement')
print('distance_sphere=' + ','.join(map(str, next(iter(spheres)))))
print('pair_counts Hamming distance shortest distance number:')
for (h,d),n in sorted(joint.items()): print(h,d,n)
print('detour_0=83070 detour_2=26208 detour_other=0')
