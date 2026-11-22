#!/usr/bin/env python3
"""Independent geometric verification of the Heawood powerful-alliance classification."""
from itertools import combinations
from collections import deque, Counter

POINTS = frozenset(range(7))
LINES = tuple(frozenset(((i+j) % 7 for j in (0,1,3))) for i in range(7))
assert len(set(LINES)) == 7
assert all(len(p) == 3 for p in LINES)
assert all(sum(p in line for line in LINES) == 3 for p in POINTS)

def collinear(triple):
    return any(triple <= line for line in LINES)

TRIANGLES = frozenset(frozenset(t) for t in combinations(POINTS, 3) if not collinear(frozenset(t)))
assert len(TRIANGLES) == 28

def side_lines(triangle):
    return frozenset(i for i, line in enumerate(LINES) if len(line & triangle) == 2)

def powerful(pts, line_ids):
    # For each selected vertex, at least one selected neighbor;
    # for each unselected vertex, at least two selected neighbors.
    for p in POINTS:
        selected_neigh = sum(p in LINES[l] for l in line_ids)
        if selected_neigh < (1 if p in pts else 2):
            return False
    for i, line in enumerate(LINES):
        selected_neigh = len(line & pts)
        if selected_neigh < (1 if i in line_ids else 2):
            return False
    return True

# Derive all optimal sets from ordered edges of the Coxeter graph.
assert all(len(side_lines(t)) == 3 for t in TRIANGLES)
edge_pairs = {(p, q) for p in TRIANGLES for q in TRIANGLES if not (p & q)}
assert len(edge_pairs) == 84
states = set()
for p, q in edge_pairs:
    lines_in_complement = side_lines(q)
    assert powerful(POINTS-p, frozenset(range(7))-lines_in_complement)
    states.add((POINTS-p, frozenset(range(7))-lines_in_complement))
assert len(states) == 84

# Independent complete direct scan of all 2^14 placements.
all_counts = Counter()
valid8 = set()
for bits in range(1 << 14):
    pts = frozenset(i for i in range(7) if bits & (1 << i))
    selected_lines = frozenset(i for i in range(7) if bits & (1 << (7+i)))
    if powerful(pts, selected_lines):
        n = len(pts) + len(selected_lines)
        all_counts[n] += 1
        if n == 8: valid8.add((pts, selected_lines))
assert all_counts == Counter({8:84,9:350,10:511,11:308,12:91,13:14,14:1})
assert states == valid8
assert all(len(p) == len(l) == 4 for p,l in states)

# The graph on optimal placements under one token jump.
placements = sorted(edge_pairs, key=lambda a: (tuple(sorted(a[0])),tuple(sorted(a[1]))))
jumps = {}
for pq in placements:
    p, q = pq
    jumps[pq] = {uv for uv in placements if uv != pq and (uv[0] == p or uv[1] == q)}
assert all(len(jumps[u]) == 4 for u in jumps)
assert sum(len(v) for v in jumps.values())//2 == 168
# Check actual symmetric-difference definition of one token jump and no token slides.
for a in placements:
    sa = (POINTS-a[0], frozenset(range(7))-side_lines(a[1]))
    for b in placements:
        sb = (POINTS-b[0], frozenset(range(7))-side_lines(b[1]))
        changed_p = len(sa[0]^sb[0]); changed_l = len(sa[1]^sb[1])
        if a != b:
            assert (b in jumps[a]) == ((changed_p + changed_l) == 2)
        assert not (changed_p == 1 and changed_l == 1)

profiles = Counter()
for start in placements:
    dist = {start: 0}
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for y in jumps[x]:
            if y not in dist:
                dist[y] = dist[x]+1
                queue.append(y)
    assert len(dist) == 84
    profiles[tuple(Counter(dist.values())[i] for i in range(max(dist.values())+1))] += 1
assert profiles == Counter({(1,4,8,16,28,22,4,1):84})
print('geometry checker PASS: triangle count=28, ordered disjoint pairs=84, exact powerful-alliance polynomial',dict(sorted(all_counts.items())))
print('one-jump graph=84 vertices, 168 edges, connected, diameter=7, uniform distance layers=(1,4,8,16,28,22,4,1); no slides')
