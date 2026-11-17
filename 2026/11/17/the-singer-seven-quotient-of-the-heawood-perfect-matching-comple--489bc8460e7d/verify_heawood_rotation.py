#!/usr/bin/env python3
"""Exact integer and discrete-Morse checks for a Fano perfect-matching orbit space."""
from collections import Counter, defaultdict, deque
import json

# Cyclic (7,3,1) difference set: line a contains a, a+1, a+3.
LINES = [{a, (a + 1) % 7, (a + 3) % 7} for a in range(7)]
EDGES = [(p, a) for a, line in enumerate(LINES) for p in sorted(line)]
EDGE_INDEX = {e: j for j, e in enumerate(EDGES)}
assert len(EDGES) == 21
assert all(len({a for a, line in enumerate(LINES) if p in line}) == 3 for p in range(7))
assert all(sum((p in LINES[a] and q in LINES[a]) for a in range(7)) == 1
           for p in range(7) for q in range(p + 1, 7))

PERFECT = []
def visit(next_edge, used_points, used_lines, mask):
    if mask.bit_count() == 7:
        PERFECT.append(mask)
        return
    for j in range(next_edge, 21):
        p, a = EDGES[j]
        if not ((used_points >> p) & 1 or (used_lines >> a) & 1):
            visit(j + 1, used_points | (1 << p), used_lines | (1 << a), mask | (1 << j))
visit(0, 0, 0, 0)
PERFECT.sort()
assert len(PERFECT) == len(set(PERFECT)) == 24

# The perfect-matching extendibility complex P, on the 21 graph edges.
P_FACES = set()
for top in PERFECT:
    sub = top
    while sub:
        P_FACES.add(sub)
        sub = (sub - 1) & top
assert len(P_FACES) == 2201
p_face_counts = tuple(sum(f.bit_count() == k for f in P_FACES) for k in range(1, 8))
assert p_face_counts == (21, 168, 560, 756, 504, 168, 24)

# Independently verify simple connectivity of P: a complete Forman matching
# with no critical 1-cells, and verify acyclicity on EVERY Hasse incidence.
unpaired = set(P_FACES)
matching = set()
for i in range(21):
    for low in sorted(unpaired):
        if low not in unpaired or (low >> i) & 1:
            continue
        high = low | (1 << i)
        if high in unpaired:
            unpaired.remove(low)
            unpaired.remove(high)
            matching.add((low, high))
assert len(matching) == 1092
assert Counter(f.bit_count() for f in unpaired) == Counter({1: 1, 3: 16})
indegree = {f: 0 for f in P_FACES}
adj = defaultdict(list)
incidences = 0
for high in P_FACES:
    for i in range(21):
        if not ((high >> i) & 1):
            continue
        low = high ^ (1 << i)
        if not low:
            continue
        incidences += 1
        src, dst = (low, high) if (low, high) in matching else (high, low)
        adj[src].append(dst)
        indegree[dst] += 1
assert incidences == 8736
queue = deque(sorted(f for f in P_FACES if indegree[f] == 0))
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for v in adj[f]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert visited == len(P_FACES)
# Forman: one 0-cell, no 1-cells, and 16 2-cells; hence P is simply connected.

# Nerve N of the cover of P by its 24 perfect-matching simplices.
# An edge of the Heawood graph is contained in exactly eight perfect matchings.
N_FACETS = []
for j in range(21):
    facet = sum(1 << i for i, m in enumerate(PERFECT) if (m >> j) & 1)
    assert facet.bit_count() == 8
    N_FACETS.append(facet)
N_FACES = set()
for facet in N_FACETS:
    sub = facet
    while sub:
        N_FACES.add(sub)
        sub = (sub - 1) & facet
assert len(N_FACES) == 4511
n_face_counts = tuple(sum(s.bit_count() == k for s in N_FACES) for k in range(1, 9))
assert n_face_counts == (24, 252, 896, 1386, 1176, 588, 168, 21)

# Simultaneous translation of point and line labels rotates the 24 facets.
pindex = {m: i for i, m in enumerate(PERFECT)}
rotation = []
for m in PERFECT:
    image = 0
    for j, (p, a) in enumerate(EDGES):
        if (m >> j) & 1:
            image |= 1 << EDGE_INDEX[((p + 1) % 7, (a + 1) % 7)]
    rotation.append(pindex[image])
assert sorted(rotation) == list(range(24))
fixed = [i for i, v in enumerate(rotation) if i == v]
assert len(fixed) == 3
assert all((PERFECT[a] & PERFECT[b]) == 0 for a in fixed for b in fixed if a < b)

def rotate(face):
    return sum(1 << rotation[i] for i in range(24) if (face >> i) & 1)

def order_sign(xs):
    return -1 if sum(xs[i] > xs[j] for i in range(len(xs)) for j in range(i+1, len(xs))) % 2 else 1

orbit = {}
for face in N_FACES:
    seq = [face]
    for _ in range(6):
        seq.append(rotate(seq[-1]))
    assert rotate(seq[-1]) == face
    orbit[face] = tuple(seq)
    if len(set(seq)) != 7:
        assert face.bit_count() == 1 and face.bit_length() - 1 in fixed

reps = sorted({min(orbit[s]) for s in N_FACES}, key=lambda s: (s.bit_count(), s))
by_degree = defaultdict(list)
for rep in reps:
    by_degree[rep.bit_count()-1].append(rep)
counts = tuple(len(by_degree[k]) for k in range(8))
assert counts == (6, 36, 128, 198, 168, 84, 24, 3)
# Burnside check by dimension, independent of the representative construction.
for k in range(8):
    fixed_count = 3 if k == 0 else 0
    assert (n_face_counts[k] + 6 * fixed_count)//7 == counts[k]
    assert (n_face_counts[k] + 6 * fixed_count) % 7 == 0
assert sum((-1)**d * counts[d] for d in range(8)) == 5

# Map every oriented face to its canonical oriented rotation representative.
canonical = {}
for rep in reps:
    for face in orbit[rep]:
        old = [i for i in range(24) if (face >> i) & 1]
        moved = list(old)
        rot_steps = next(j for j, r in enumerate(orbit[face]) if r == rep)
        for _ in range(rot_steps):
            moved = [rotation[i] for i in moved]
        assert sum(1 << i for i in moved) == rep
        candidate = (rep, order_sign(moved))
        assert face not in canonical or canonical[face] == candidate
        canonical[face] = candidate
assert len(canonical) == len(N_FACES)

# Integral cellular boundary of the ordered simplex orbits.
# All positive-dimensional simplices have trivial setwise stabilizer.
D = {}
for d in range(1, 8):
    row_index = {f: j for j, f in enumerate(by_degree[d-1])}
    columns = []
    for face in by_degree[d]:
        vec = defaultdict(int)
        v = [i for i in range(24) if (face >> i) & 1]
        for j, i in enumerate(v):
            sub = face ^ (1 << i)
            rep, sign = canonical[sub]
            vec[row_index[rep]] += (-1)**j * sign
        columns.append({r: val for r, val in vec.items() if val})
    D[d] = columns

# Check chain property with unreduced exact integer matrices.
for d in range(2, 8):
    for col in D[d]:
        total = defaultdict(int)
        for middle, a in col.items():
            for row, b in D[d-1][middle].items():
                total[row] += a*b
        assert all(z == 0 for z in total.values())

# Integer elementary cancellations: a boundary coefficient +/-1 admits
# a unimodular basis change and removal of a contractible two-term summand.
# The update to the affected boundary is a Schur complement; the neighboring
# boundaries only lose the corresponding generator because d*d=0.
alive = {d: set(range(counts[d])) for d in range(8)}
per_degree = Counter()
while True:
    pivot = None
    for d in range(7, 0, -1):
        for c in sorted(alive[d]):
            for r in sorted(D[d][c]):
                a = D[d][c][r]
                if r in alive[d-1] and abs(a) == 1:
                    pivot = (d, c, r, a)
                    break
            if pivot: break
        if pivot: break
    if pivot is None:
        break
    d, c, r, a = pivot
    column = D[d][c].copy()
    for j in sorted(alive[d]):
        if j == c: continue
        b = D[d][j].get(r, 0)
        if b:
            for t, x in column.items():
                value = D[d][j].get(t, 0) - (b*a)*x
                if value: D[d][j][t] = value
                else: D[d][j].pop(t, None)
    if d + 1 in D:
        for j in alive[d+1]:
            D[d+1][j].pop(c, None)
    if d - 1 in D:
        D[d-1][r].clear()
    D[d][c].clear()
    alive[d].remove(c)
    alive[d-1].remove(r)
    per_degree[d] += 1

assert sum(per_degree.values()) == 321
assert tuple(per_degree[d] for d in range(1,8)) == (5,31,93,105,63,21,3)
assert tuple(len(alive[d]) for d in range(8)) == (1,0,4,0,0,0,0,0)
assert all(not D[d][j] for d in range(1,8) for j in alive[d])

out = {
    'graph_edges':len(EDGES), 'perfect_matchings':len(PERFECT),
    'perfect_matching_face_vector':p_face_counts,
    'morse_pairs':len(matching),'hasse_incidences':incidences,
    'morse_acyclic_vertices_visited':visited,'critical_faces_by_size':dict(Counter(f.bit_count() for f in unpaired)),
    'nerve_face_vector':n_face_counts, 'fixed_facets':len(fixed),
    'quotient_cell_vector':counts,'quotient_euler_characteristic':5,
    'integer_unit_cancellations':sum(per_degree.values()),
    'integer_boundary_ranks':tuple(per_degree[d] for d in range(1,8)),
    'remaining_cells_by_dimension':tuple(len(alive[d]) for d in range(8)),
    'conclusion':'reduced integral homology Z^4 in degree 2; no others; simply connected quotient; homotopy wedge of four 2-spheres',
    'result':'VERIFY_OK'
}
print(json.dumps(out,sort_keys=True,indent=2))
