"""Exact all-state shortest-sequential-swapping census for the 3-by-3 square grid.

No external modules. Independent from the factoradic/C++ implementation:
uses byte-string states, a dictionary of graph distances, and a BFS queue.
"""
from collections import Counter, deque
from math import factorial

VERTICES = tuple((r, c) for r in range(3) for c in range(3))
EDGES = tuple((u, v) for u in range(9) for v in range(u + 1, 9)
              if sum(abs(VERTICES[u][a] - VERTICES[v][a]) for a in range(2)) == 1)
assert len(EDGES) == 12

def swapped(state, u, v):
    a = bytearray(state)
    a[u], a[v] = a[v], a[u]
    return bytes(a)

identity = bytes(range(9))
q = deque([identity]); distance = {identity: 0}
while q:
    p = q.popleft()
    d = distance[p] + 1
    for u, v in EDGES:
        w = swapped(p, u, v)
        if w not in distance:
            distance[w] = d
            q.append(w)

assert len(distance) == factorial(9)  # exhausts all placements
hist = Counter(distance.values())
assert sum(hist.values()) == factorial(9)
assert hist == Counter(dict(enumerate((1,12,88,470,1978,6658,18081,38936,65246,
                                      83000,76688,48316,18975,4024,382,24,1))))
assert max(distance.values()) == 16
assert {p for p, d in distance.items() if d == 16} == {bytes(range(8,-1,-1))}

def lb(p):
    dist_sum = sum(abs(VERTICES[v][0] - VERTICES[token][0]) +
                   abs(VERTICES[v][1] - VERTICES[token][1])
                   for v, token in enumerate(p))
    return (dist_sum + 1) // 2

gaps = Counter(d-lb(p) for p, d in distance.items())
assert gaps == Counter(dict(enumerate((98647,167522,84339,11850,502,20))))
assert all(d >= lb(p) for p,d in distance.items())
assert 0 not in (d for p,d in distance.items() if p!=identity)
print('grid=3x3 vertices=9 edges=12 states=',len(distance),sep='')
print('diameter=16, radius=16, unique antipode=876543210')
print('distance_counts=',','.join(str(hist[i]) for i in range(17)),sep='')
print('lower_bound_excess_counts=',','.join(str(gaps[i]) for i in range(6)),sep='')
print('max_excess=5, maximizers=20')
