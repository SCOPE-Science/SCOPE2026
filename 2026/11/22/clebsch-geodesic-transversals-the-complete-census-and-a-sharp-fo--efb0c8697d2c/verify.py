#!/usr/bin/env python3
"""Self-contained exhaustive certificate for Clebsch geodesic transversals."""
from collections import Counter, deque
from itertools import combinations

V = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
assert len(V) == 16
N = len(V)
U = (1 << N) - 1
neighbors = tuple(sum(1 << j for j, y in enumerate(V)
                      if (x ^ y).bit_count() == 4) for x in V)
assert all(a.bit_count() == 5 for a in neighbors)
assert all(((neighbors[i] >> j) & 1) == ((neighbors[j] >> i) & 1)
           for i in range(N) for j in range(N))
# Independently enumerate graph distances and every diameter-two geodesic.
distance = [[99] * N for _ in range(N)]
for root in range(N):
    distance[root][root] = 0
    q = deque([root])
    while q:
        v = q.popleft()
        for w in range(N):
            if (neighbors[v] >> w) & 1 and distance[root][w] == 99:
                distance[root][w] = distance[root][v] + 1
                q.append(w)
assert max(max(row) for row in distance) == 2
geodesics = set()
for a, b in combinations(range(N), 2):
    if distance[a][b] == 2:
        for middle in range(N):
            if distance[a][middle] == distance[middle][b] == 1:
                geodesics.add((1 << a) | (1 << b) | (1 << middle))
assert len(geodesics) == 160
assert all(len([a for a in range(N) if (g >> a) & 1]) == 3 for g in geodesics)

# Two independent predicates: degree-at-most-one, and hitting all geodesics.
def diss(t):
    return all((neighbors[i] & t).bit_count() <= 1
               for i in range(N) if (t >> i) & 1)

def hits(s):
    return all(s & g for g in geodesics)

H = {sum(1 << i for i, x in enumerate(V) if ((x >> c) & 1) == bit)
     for c in range(5) for bit in range(2)}
J = set(neighbors)
assert len(H) == 10 and len(J) == 16 and H.isdisjoint(J)
valid = set()
counts = Counter()
for t in range(1 << N):
    good = diss(t)
    assert good == hits(U ^ t), ("geodesic criterion", t)
    if good:
        valid.add(t)
        counts[N - t.bit_count()] += 1
maximal = {t for t in valid if not any((t | (1 << j)) in valid
                                      for j in range(N) if not ((t >> j) & 1))}
assert maximal == H | J, (len(maximal), len(maximal.symmetric_difference(H | J)))
assert counts == {8: 10, 9: 80, 10: 280, 11: 576, 12: 660,
                  13: 400, 14: 120, 15: 16, 16: 1}, counts
assert {16 - t.bit_count() for t in maximal} == {8, 11}
assert all(t.bit_count() == 8 for t in H)
assert all(t.bit_count() == 5 for t in J)
assert all((a & b).bit_count() in (0, 4) for a,b in combinations(sorted(H),2))

# The budgeted reconfiguration graph has a vertex for each valid S=V\T;
# one operation toggles one vertex of S, equivalently one of T.
expected = {8: (10, Counter({(1,1):10})),
            9: (10, Counter({(9,1):10})),
            10:(10, Counter({(37,1):10})),
            11:(26, Counter({(93,1):10,(1,0):16})),
            12:(1, Counter({(1606,10):1}))}
for budget in range(8,13):
    states = {t for t in valid if N-t.bit_count() <= budget}
    todo = set(states)
    components = Counter()
    while todo:
        start = todo.pop()
        q = deque([start]); size=0; opt=0
        while q:
            t = q.popleft()
            size += 1
            opt += t in H
            for bit in range(N):
                u = t ^ (1 << bit)
                if u in todo:
                    todo.remove(u)
                    q.append(u)
        components[(size,opt)] += 1
    assert (sum(components.values()), components) == expected[budget], (budget,components)

states = {t for t in valid if N-t.bit_count() <= 12}
optima = sorted(H)
pair_distances = Counter()
for k, root in enumerate(optima):
    distance = {root: 0}
    q = deque([root])
    while q:
        t = q.popleft()
        for bit in range(N):
            u = t ^ (1 << bit)
            if u in states and u not in distance:
                distance[u] = distance[t] + 1
                q.append(u)
    for other in optima[k+1:]:
        pair_distances[distance[other]] += 1
assert pair_distances == {8:40,16:5}, pair_distances
print("VERIFY_OK CLEBSCH_GEODESIC_TRANSVERSAL")
print("MAXIMAL_GEODESICS",len(geodesics))
print("POLYNOMIAL",dict(sorted(counts.items())))
print("INCLUSION_MINIMAL", {8:10,11:16})
print("TAR_COMPONENTS",{b:expected[b][0] for b in expected})
print("OPTIMUM_PAIR_DISTANCES",dict(sorted(pair_distances.items())))
