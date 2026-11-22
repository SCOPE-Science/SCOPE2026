#!/usr/bin/env python3
"""Exact incidence checks for the sixteen-line F_7 example.
The general rigidity theorem is proved geometrically, not by computation.
"""
from itertools import combinations, product
from collections import Counter

P = 7
LINES = [
    (0,1,2),(0,1,3),(0,1,5),(1,0,0),
    (1,0,1),(1,0,3),(1,1,1),(1,1,6),
    (1,2,3),(1,3,4),(1,4,1),(1,4,5),
    (1,5,1),(1,5,6),(1,6,1),(1,6,2)
]
M = (1,6,6)
LEAVES = {1:(1,2,6),3:(1,3,5),10:(1,5,3),15:(1,1,0)}

def canonical(v):
    for a in v:
        if a % P:
            return tuple(x*pow(a,-1,P)%P for x in v)
    raise ValueError('zero projective vector')

def cross(a,b):
    return canonical((a[1]*b[2]-a[2]*b[1],
                      a[2]*b[0]-a[0]*b[2],
                      a[0]*b[1]-a[1]*b[0]))

def on(line, point):
    return sum(a*b for a,b in zip(line,point))%P == 0

assert len({canonical(L) for L in LINES}) == 16
assert not any(canonical(L) == canonical(M) for L in LINES)
points = {cross(LINES[i],LINES[j]) for i,j in combinations(range(16),2)}
incidence = {p:tuple(i+1 for i,L in enumerate(LINES) if on(L,p)) for p in points}
assert len(points) == 38
assert Counter(len(v) for v in incidence.values()) == {2:16,3:12,4:8,5:2}
counts = [sum(on(L,p) for p in points) for L in LINES]
assert Counter(counts) == {7:14,6:2}
Mpoints = sorted(p for p in points if on(M,p))
assert len(Mpoints) == 8
assert all(len(incidence[p])==2 for p in Mpoints)
for index, expected in LEAVES.items():
    nodes = [p for p in points if len(incidence[p])==2 and index in incidence[p]]
    assert nodes == [canonical(expected)], (index,nodes)
    assert canonical(expected) in Mpoints
assert len({canonical(p) for p in LEAVES.values()}) == 4
# All eight-point secants are defined over F_7: two rational points determine a rational line.
all_lines = {canonical(c) for c in product(range(P),repeat=3) if any(c)}
maximizers = [L for L in all_lines if sum(on(L,p) for p in points) == 8]
assert maximizers == [canonical(M)]
assert max(sum(on(L,p) for p in points) for L in all_lines) == 8
print('PASS: 38 geometric intersections, multiplicities 16/12/8/2, line counts 7^14 6^2.')
print('PASS: 8 double points on M; four distinct single-double-point lines.')
print('PASS: M is the sole geometric 8-secant line; the theorem uses a separate proof for all curves.')
