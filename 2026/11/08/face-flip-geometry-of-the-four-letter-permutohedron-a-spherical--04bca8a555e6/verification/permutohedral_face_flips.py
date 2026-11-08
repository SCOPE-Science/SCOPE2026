"""Exact permutation-model verification of truncated-octahedron face flips.

Requires only Python 3.10+ standard library. Run:
    python permutohedral_face_flips.py
"""
from collections import Counter, deque
from itertools import permutations
from math import comb

VERTICES = tuple(permutations(range(4)))
POSITION = {p: i for i, p in enumerate(VERTICES)}


def exchange(p, generator):
    p = list(p)
    p[generator], p[generator + 1] = p[generator + 1], p[generator]
    return tuple(p)


EDGES = sorted({tuple(sorted((i, POSITION[exchange(p, k)])))
                for i, p in enumerate(VERTICES) for k in range(3)})
EDGE_ID = {e: k for k, e in enumerate(EDGES)}
INCIDENT = [[] for _ in VERTICES]
for k, (u, v) in enumerate(EDGES):
    INCIDENT[u].append((v, k))
    INCIDENT[v].append((u, k))
assert len(VERTICES) == 24 and len(EDGES) == 36
assert all(len(n) == 3 for n in INCIDENT)


def generated_coset(seed, gens):
    vertices = {seed}
    frontier = [seed]
    for u in frontier:
        for k in gens:
            v = POSITION[exchange(VERTICES[u], k)]
            if v not in vertices:
                vertices.add(v)
                frontier.append(v)
    return frozenset(vertices)


FACES = []
FACE_SIZES = []
for gens in ((0, 2), (0, 1), (1, 2)):
    distinct = {generated_coset(i, gens) for i in range(24)}
    for face in sorted(distinct, key=lambda f: sorted(f)):
        FACES.append(face)
        FACE_SIZES.append(len(face))
FACE_EDGES = []
for face in FACES:
    listed = [k for k, (a, b) in enumerate(EDGES) if a in face and b in face]
    assert len(listed) == len(face)
    assert all(sum((a == u or b == u) for k in listed
                   for a, b in [EDGES[k]]) == 2 for u in face)
    FACE_EDGES.append(sum(1 << k for k in listed))
assert Counter(FACE_SIZES) == {4: 6, 6: 8}
assert all(sum(bool(f & (1 << k)) for f in FACE_EDGES) == 2
           for k in range(len(EDGES)))


def enumerate_matchings():
    matchings = []

    def recurse(vertices_left, edge_mask):
        if vertices_left == 0:
            matchings.append(edge_mask)
            return
        u = (vertices_left & -vertices_left).bit_length() - 1
        for v, e in INCIDENT[u]:
            if vertices_left & (1 << v):
                recurse(vertices_left ^ (1 << u) ^ (1 << v),
                        edge_mask | (1 << e))

    recurse((1 << 24) - 1, 0)
    assert len(matchings) == len(set(matchings))
    return tuple(sorted(matchings))


MATCHINGS = enumerate_matchings()
assert len(MATCHINGS) == 169
INDEX = {m: i for i, m in enumerate(MATCHINGS)}


def make_graph(excluded=None):
    graph = [set() for _ in MATCHINGS]
    for i, m in enumerate(MATCHINGS):
        for f, face_edges in enumerate(FACE_EDGES):
            if f == excluded:
                continue
            neighbor = INDEX.get(m ^ face_edges)
            if neighbor is not None:
                graph[i].add(neighbor)
    assert all(i in graph[j] for i, row in enumerate(graph) for j in row)
    return graph


def distances(graph):
    output = []
    for root in range(len(graph)):
        d = [-1] * len(graph)
        d[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    queue.append(v)
        assert -1 not in d
        output.append(tuple(d))
    return output


def measures(graph, d):
    pairs = Counter(d[i][j] for i in range(len(d))
                    for j in range(i + 1, len(d)))
    eccentricity = Counter(max(row) for row in d)
    return (sum(map(len, graph)) // 2, min(eccentricity),
            max(eccentricity), eccentricity, pairs)


def median_test(d):
    n = len(d)
    intervals = {}
    for a in range(n):
        for b in range(a + 1, n):
            intervals[a, b] = sum(1 << z for z in range(n)
                                  if d[a][z] + d[z][b] == d[a][b])
    count = Counter()
    for a in range(n):
        for b in range(a + 1, n):
            ab = intervals[a, b]
            for c in range(b + 1, n):
                count[(ab & intervals[a, c] & intervals[b, c]).bit_count()] += 1
    assert sum(count.values()) == comb(n, 3)
    return count


ALL = make_graph()
D_ALL = distances(ALL)
edges, rad, diam, ecc, pairs = measures(ALL, D_ALL)
assert (edges, rad, diam) == (460, 7, 9)
assert ecc == {7: 69, 8: 92, 9: 8}
assert pairs == {1: 460, 2: 1324, 3: 2428, 4: 3138,
                 5: 3032, 6: 2436, 7: 1204, 8: 170, 9: 4}
assert Counter(len(row) for row in ALL) == {
    2: 8, 3: 12, 4: 24, 5: 52, 6: 22, 7: 32, 8: 17, 10: 2}
assert median_test(D_ALL) == {0: 79828, 1: 700774, 2: 9642}

# Three canonical perfect matchings use a fixed adjacent-transposition
# generator throughout the 24-vertex Cayley graph.
canonical = []
for k in range(3):
    matching = 0
    for i, p in enumerate(VERTICES):
        j = POSITION[exchange(p, k)]
        matching |= 1 << EDGE_ID[tuple(sorted((i, j)))]
    canonical.append(INDEX[matching])
a, b, c = canonical
assert (D_ALL[a][b], D_ALL[a][c], D_ALL[b][c]) == (4, 6, 4)
assert not any(D_ALL[a][z] + D_ALL[z][b] == D_ALL[a][b]
               and D_ALL[a][z] + D_ALL[z][c] == D_ALL[a][c]
               and D_ALL[b][z] + D_ALL[z][c] == D_ALL[b][c]
               for z in range(len(MATCHINGS)))

for removed in range(14):
    gr = make_graph(removed)
    ds = distances(gr)
    e, r, diameter, eccs, counts = measures(gr, ds)
    if FACE_SIZES[removed] == 4:
        assert (e, r, diameter) == (410, 11, 22)
    else:
        assert (e, r, diameter) == (440, 11, 21)
    # One representative of each symmetry orbit of faces suffices for a
    # direct median test; all faces in an orbit are conjugate in S4.
    if removed in (0, 6):
        assert median_test(ds) == {1: comb(169, 3)}

print('PERMUTATION_MODEL_24_VERTICES_36_EDGES_6_SQUARES_8_HEXAGONS_PASS')
print('MATCHINGS_169_FULL_FLIPS_460_RADIUS_7_DIAMETER_9_PASS')
print('ECCENTRICITIES_69_AT_7_92_AT_8_8_AT_9_PASS')
print('PAIR_DISTANCES_460_1324_2428_3138_3032_2436_1204_170_4_PASS')
print('ALL_FACES_NONMEDIAN_79828_EMPTY_9642_DOUBLE_MEDIANS_PASS')
print('THREE_GENERATOR_MATCHINGS_NO_MEDIAN_PASS')
print('REMOVE_ANY_SQUARE_410_EDGES_RADIUS11_DIAMETER22_PASS')
print('REMOVE_ANY_HEXAGON_440_EDGES_RADIUS11_DIAMETER21_PASS')
print('PUNCTURED_MEDIAN_GRAPHS_PASS')
