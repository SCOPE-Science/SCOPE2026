#!/usr/bin/env python3
"""Exact finite simplicial verification for a four-cube geodesic general-position complex."""
from collections import Counter, deque
from itertools import combinations

D = 4
N = 1 << D
PIVOTS = (12, 0, 11, 3, 8, 5, 4, 9, 15, 6, 7, 13, 1, 10, 2, 14)
assert len(PIVOTS) == N and set(PIVOTS) == set(range(N))

def dist(a, b):
    return (a ^ b).bit_count()

def bad_triples():
    return [sum(1 << z for z in t) for t in combinations(range(N), 3)
            if any(dist(a,b) == dist(a,c) + dist(c,b)
                   for a,b,c in ((t[0],t[1],t[2]),(t[0],t[2],t[1]),(t[1],t[2],t[0])))]

BAD = bad_triples()
assert len(BAD) == 400, len(BAD)
FACES = set()
for s in range(1,1<<N):
    if not any(s & triple == triple for triple in BAD):
        FACES.add(s)
assert Counter(s.bit_count()-1 for s in FACES) == {0:16,1:120,2:160,3:120,4:16}
assert len(FACES) == 432

remaining = set(FACES)
pairs = []
for v in PIVOTS:
    bit = 1 << v
    for s in sorted(remaining):
        if not s & bit and (s | bit) in remaining:
            remaining.remove(s)
            remaining.remove(s | bit)
            pairs.append((s,s | bit))
assert len(pairs) == 191
assert Counter(s.bit_count()-1 for s in remaining) == {0:1,1:40,3:9}
assert len(remaining) == 50

# Standard acyclic-matching test: orient unmatched Hasse cover relations
# from higher face to lower, and each matching relation upward.
matched = set(pairs)
adj = {s: [] for s in FACES}
indeg = {s:0 for s in FACES}
for big in FACES:
    t = big
    while t:
        b = t & -t
        t ^= b
        small = big ^ b
        if small not in FACES:
            continue
        if (small,big) in matched:
            a, c = small, big
        else:
            a, c = big, small
        adj[a].append(c)
        indeg[c] += 1
queue = deque(s for s in FACES if indeg[s] == 0)
visited = 0
while queue:
    a=queue.popleft()
    visited+=1
    for c in adj[a]:
        indeg[c]-=1
        if indeg[c] == 0:
            queue.append(c)
assert visited == len(FACES), (visited,len(FACES))
assert 16-120+160-120+16 == 1-40-9
print('PASS: 400 forbidden geodesic triples; f-vector (16,120,160,120,16); 191 pairs; critical (1,40,0,9,0); Hasse DAG 432 vertices; Euler characteristic -48.')
