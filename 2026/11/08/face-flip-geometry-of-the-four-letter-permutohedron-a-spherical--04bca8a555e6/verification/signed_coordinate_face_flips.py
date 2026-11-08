"""Independent exact verifier using integer coordinates of a truncated octahedron.

Requires only Python 3.10+ standard library. Run:
    python signed_coordinate_face_flips.py
"""
from collections import Counter, deque
from itertools import permutations, product
from math import comb

# The 24 distinct integer points obtained from coordinate permutations
# and independent signs of (0,1,2) are the polyhedron's vertices.
V = sorted({tuple(s[i] * x[i] for i in range(3))
            for x in permutations((0, 1, 2))
            for s in product((-1, 1), repeat=3)})
E = [(i, j) for i in range(len(V)) for j in range(i + 1, len(V))
     if sum((V[i][k] - V[j][k]) ** 2 for k in range(3)) == 2]
assert (len(V), len(E)) == (24, 36)
neighbor = [[] for _ in V]
for edge, (a, b) in enumerate(E):
    neighbor[a].append((b, edge))
    neighbor[b].append((a, edge))
assert all(len(x) == 3 for x in neighbor)

# Six coordinate-supporting planes yield squares; eight sign planes
# yield hexagons. Each support set induces exactly its face cycle.
F = []
for axis in range(3):
    for value in (-2, 2):
        F.append({i for i, x in enumerate(V) if x[axis] == value})
for sign in product((-1, 1), repeat=3):
    F.append({i for i, x in enumerate(V)
              if sum(sign[k] * x[k] for k in range(3)) == 3})
assert [len(s) for s in F] == [4] * 6 + [6] * 8
FE = []
for face in F:
    ids = [k for k, (a, b) in enumerate(E) if a in face and b in face]
    assert len(ids) == len(face)
    assert all(sum(a == u or b == u for e in ids
                   for a, b in [E[e]]) == 2 for u in face)
    FE.append(sum(1 << k for k in ids))
assert all(sum(bool(edges & (1 << k)) for edges in FE) == 2
           for k in range(len(E)))


def enumerate_dimer_configs():
    states = []
    stack = [((1 << len(V)) - 1, 0)]
    while stack:
        uncovered, matching = stack.pop()
        if uncovered == 0:
            states.append(matching)
            continue
        x = (uncovered & -uncovered).bit_length() - 1
        for y, edge in neighbor[x]:
            if uncovered & (1 << y):
                stack.append((uncovered & ~(1 << x) & ~(1 << y),
                              matching | (1 << edge)))
    return sorted(states)


STATES = enumerate_dimer_configs()
assert len(STATES) == len(set(STATES)) == 169
IDS = {state: i for i, state in enumerate(STATES)}


def graph_omit(omit):
    adj = [set() for _ in STATES]
    for i, state in enumerate(STATES):
        for face, edge_mask in enumerate(FE):
            if face == omit:
                continue
            if (state & edge_mask).bit_count() != len(F[face]) // 2:
                continue
            target = state ^ edge_mask
            if target in IDS:
                adj[i].add(IDS[target])
    assert all(i in adj[j] for i, row in enumerate(adj) for j in row)
    return adj


def full_distance_data(adj):
    dist = []
    for i in range(len(adj)):
        d = [-1] * len(adj)
        d[i] = 0
        todo = deque([i])
        while todo:
            x = todo.popleft()
            for y in adj[x]:
                if d[y] == -1:
                    d[y] = d[x] + 1
                    todo.append(y)
        assert min(d) == 0
        dist.append(d)
    return dist


def summary(adj, d):
    histogram = Counter(d[i][j] for i in range(len(d))
                        for j in range(i + 1, len(d)))
    assert sum(histogram.values()) == comb(len(d), 2)
    ecc = Counter(max(row) for row in d)
    return (sum(len(x) for x in adj) // 2,
            min(ecc), max(ecc), ecc, histogram)


whole = graph_omit(-1)
d = full_distance_data(whole)
edge_count, rad, diam, ecc, pair_hist = summary(whole, d)
assert (edge_count, rad, diam) == (460, 7, 9)
assert ecc == {7: 69, 8: 92, 9: 8}
assert pair_hist == {1: 460, 2: 1324, 3: 2428, 4: 3138,
                     5: 3032, 6: 2436, 7: 1204, 8: 170, 9: 4}

# The graph is bipartite, but a connected bipartite graph need not be
# a median graph. Intersect three shortest-path intervals exactly.
intervals = {}
for i in range(len(STATES)):
    for j in range(i + 1, len(STATES)):
        intervals[i, j] = sum(1 << k for k in range(len(STATES))
                              if d[i][k] + d[k][j] == d[i][j])
median_counts = Counter()
for i in range(len(STATES)):
    for j in range(i + 1, len(STATES)):
        ij = intervals[i, j]
        for k in range(j + 1, len(STATES)):
            med = ij & intervals[i, k] & intervals[j, k]
            median_counts[med.bit_count()] += 1
assert median_counts == {0: 79828, 1: 700774, 2: 9642}

# The 14 potential outer-face choices are actually checked individually.
# These values should not be assumed from a numerical sample of faces.
for omission in range(len(F)):
    a = graph_omit(omission)
    data = summary(a, full_distance_data(a))
    if omission < 6:
        assert data[:3] == (410, 11, 22)
    else:
        assert data[:3] == (440, 11, 21)

assert all(d[0][j] % 2 != d[0][i] % 2
           for i, row in enumerate(whole) for j in row)
print('SIGNED_COORDINATES_24_VERTICES_36_EDGES_14_SUPPORT_FACES_PASS')
print('SECOND_MATCHING_ENUMERATION_169_PASS')
print('SECOND_FLIP_CENSUS_460_EDGES_RADIUS7_DIAMETER9_PASS')
print('SECOND_ALL_PAIR_DISTANCE_AND_ECCENTRICITY_HISTOGRAM_PASS')
print('SECOND_ALL_TRIPLES_MEDIAN_INTERSECTION_CENSUS_PASS')
print('SECOND_ALL_14_FACE_DELETIONS_22_OR_21_DIAMETER_PASS')
