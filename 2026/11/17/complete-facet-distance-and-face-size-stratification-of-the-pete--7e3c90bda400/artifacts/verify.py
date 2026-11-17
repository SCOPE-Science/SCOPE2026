"""Exact finite verification of Petersen polar facet-distance spectrum.

Run with Python 3.9+; standard library only. All computations are integral.
"""
from collections import Counter, defaultdict
from itertools import product, combinations, permutations

PAIRS = tuple(combinations(range(5), 2))
N = len(PAIRS)
EDGES = tuple((i, j) for i in range(N) for j in range(i+1, N)
              if set(PAIRS[i]).isdisjoint(PAIRS[j]))
assert N == 10 and len(EDGES) == 15
NEIGHBORS = tuple(tuple(j if i == a else a for a, j in EDGES
                        if i == a or i == j) for i in range(N))


def connected_tight(values):
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in NEIGHBORS[i]:
            if j not in seen and abs(values[i]-values[j]) == 1:
                seen.add(j)
                stack.append(j)
    return len(seen) == N


def feasible(values):
    return all(abs(values[i]-values[j]) <= 1 for i, j in EDGES)


def normalize(values):
    m = min(values)
    return tuple(x-m for x in values)


def shell_integer(values):
    """Return 10 times the centered squared Euclidean norm."""
    return 10*sum(x*x for x in values)-sum(values)**2

# Enumeration I: all 3^10 potential words, normalized by their minimum.
vertices = set()
for values in product(range(3), repeat=N):
    if min(values) == 0 and feasible(values) and connected_tight(values):
        vertices.add(values)
assert len(vertices) == 1410
SHELL_COUNTS = {56:30, 49:180, 45:20, 44:120, 41:300,
                40:150, 36:280, 29:60, 25:120, 24:130, 21:20}
assert dict(Counter(shell_integer(v) for v in vertices)) == SHELL_COUNTS

# Complete joint metric/face-size table, not merely the marginal shell counts.
JOINT = Counter((shell_integer(v), sum(abs(v[i]-v[j]) == 1 for i,j in EDGES))
                for v in vertices)
EXPECTED_JOINT = {
    (56,12):30, (49,11):180, (45,9):20, (44,10):120,
    (41,9):120, (41,11):180, (40,10):120, (40,12):30,
    (36,10):240, (36,12):40, (29,9):60, (25,9):60,
    (25,11):60, (24,10):120, (24,12):10, (21,9):20
}
assert dict(JOINT) == EXPECTED_JOINT
assert sum(v for (k,t),v in JOINT.items() if t == 9) == 280

# Enumeration II: fixed-root potential differences along a fixed spanning tree.
parent = [-1]*N
order = [0]
for i in order:
    for j in NEIGHBORS[i]:
        if j not in order:
            parent[j] = i
            order.append(j)
assert len(order) == N
vertices_from_tree = set()
for steps in product((-1, 0, 1), repeat=N-1):
    v = [0]*N
    for i, delta in zip(order[1:], steps):
        v[i] = v[parent[i]]+delta
    if feasible(v) and connected_tight(v):
        vertices_from_tree.add(normalize(v))
assert vertices_from_tree == vertices

# The full automorphism group is S5 acting on two-subsets, together with negation.
lookup = {pair: i for i, pair in enumerate(PAIRS)}
automorphisms = []
for perm in permutations(range(5)):
    image = tuple(lookup[tuple(sorted((perm[a], perm[b])))] for a, b in PAIRS)
    assert len(set(image)) == N
    assert all(tuple(sorted((image[i], image[j]))) in EDGES for i, j in EDGES)
    automorphisms.append(image)
assert len(automorphisms) == 120

remaining = set(vertices)
orbits = []
while remaining:
    rep = min(remaining)
    orbit = set()
    for sigma in automorphisms:
        y = [0]*N
        for i, j in enumerate(sigma):
            y[j] = rep[i]
        w = normalize(y)
        orbit.add(w)
        orbit.add(tuple(max(w)-t for t in w))
    assert orbit <= remaining
    remaining.difference_update(orbit)
    orbits.append((shell_integer(rep), len(orbit), rep))
assert len(orbits) == 18
EXPECTED_ORBIT_SIZES = {
    56:(30,), 49:(60,120), 45:(20,), 44:(120,),
    41:(60,120,120), 40:(30,120), 36:(40,240),
    29:(60,), 25:(60,60), 24:(10,120), 21:(20,)
}
assert {k:tuple(sorted(size for shell,size,_ in orbits if shell==k))
        for k in SHELL_COUNTS} == EXPECTED_ORBIT_SIZES

# Every explicit table representative and its stated face size and orbit count.
# Pair codes are one-based, e.g. "12" means the two-set {1,2}.
REPS = (
    (56,30,12,"12,13,25,35","15,23"),
    (49,120,11,"12,13,25","15,23"),
    (49,60,11,"12,13,45","14,15"),
    (45,20,9,"12,13,14,25,35,45","15"),
    (44,120,10,"12,13,14,25,35","15"),
    (41,120,11,"12,13,14,25","15"),
    (41,120,9,"12,13,24,35","23"),
    (41,60,11,"12,13,24,34","23"),
    (40,120,10,"12,13","15,23"),
    (40,30,12,"12,13","14,15"),
    (36,240,10,"12,13,24","23"),
    (36,40,12,"12,13,14","15"),
    (29,60,9,"12,13","23"),
    (25,60,11,"12,13,14,15,23",""),
    (25,60,9,"12,13,14,23,25",""),
    (24,120,10,"12,13,14,15,23,24",""),
    (24,10,12,"12,13,14,15",""),
    (21,20,9,"12,13,14,15,23,24,25","")
)

def rep_from_codes(a_codes, b_codes):
    p = [1]*N
    for codes, level in ((a_codes,0),(b_codes,2)):
        for code in codes.split(','):
            if code:
                pair = (int(code[0])-1, int(code[1])-1)
                p[lookup[pair]] = level
    return tuple(p)

seen_orbit_members=set()
for expected_norm, expected_size, expected_face_vertices, zeros, twos in REPS:
    v = rep_from_codes(zeros,twos)
    assert v in vertices and shell_integer(v) == expected_norm
    assert sum(abs(v[i]-v[j]) == 1 for i,j in EDGES) == expected_face_vertices
    candidate_orbit=set()
    for sigma in automorphisms:
        y=[0]*N
        for i,j in enumerate(sigma):
            y[j]=v[i]
        w=normalize(y)
        candidate_orbit.add(w)
        candidate_orbit.add(tuple(max(w)-x for x in w))
    assert len(candidate_orbit)==expected_size
    assert not candidate_orbit.intersection(seen_orbit_members)
    seen_orbit_members.update(candidate_orbit)
assert seen_orbit_members == vertices and len(REPS)==len(orbits)==18

# Count of exact levels and near-insphere gap, no floating point involved.
assert sorted(SHELL_COUNTS, reverse=True)[:2] == [56,49]
assert SHELL_COUNTS[56] == 30 and SHELL_COUNTS[49] == 180
assert 49 * 10 == 490 and 56 * 10 == 560
print('PETERSEN_FACET_SPECTRUM_CHECKS_PASSED words=59049 tree_words=19683 facets=1410 shells=11 symmetry_orbits=18')
for k in sorted(EXPECTED_ORBIT_SIZES, reverse=True):
    print(k, SHELL_COUNTS[k], EXPECTED_ORBIT_SIZES[k])
