#!/usr/bin/env python3
"""Exact verifier for the ordinary 3-cut complex of the Heawood graph.
Uses only the Python standard library.
"""
from itertools import combinations
from collections import defaultdict, deque
import hashlib, json

N = 14
ALL = (1 << N) - 1

# Vertices 0,...,6 are Fano points and 7,...,13 are Fano lines.
# Point i is incident with line j iff i-j mod 7 lies in {0,1,3}.
adj = [set() for _ in range(N)]
for i in range(7):
    for j in range(7):
        if (i - j) % 7 in {0, 1, 3}:
            a, b = i, 7 + j
            adj[a].add(b)
            adj[b].add(a)

assert all(len(a) == 3 for a in adj)
assert sum(map(len, adj)) // 2 == 21


def induced_connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        u = stack.pop()
        for v in adj[u] & vertices:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen == vertices

triples = []
disconnected = []
connected = []
for t in combinations(range(N), 3):
    triples.append(t)
    (connected if induced_connected(t) else disconnected).append(t)
assert len(triples) == 364
assert len(connected) == 42
assert len(disconnected) == 322

# Each connected triple in a triangle-free cubic graph is an induced P3.
# Confirm the graph is triangle-free and these are exactly center-plus-two-neighbor triples.
triangle_count = 0
for t in combinations(range(N), 3):
    e = sum((v in adj[u]) for u, v in combinations(t, 2))
    if e == 3:
        triangle_count += 1
assert triangle_count == 0
p3 = set()
for c in range(N):
    for a, b in combinations(sorted(adj[c]), 2):
        p3.add(tuple(sorted((a, c, b))))
assert len(p3) == 42 and p3 == set(connected)

# A face sigma of Delta_3(H) iff its complement contains a disconnected triple.
disc_masks = []
for t in disconnected:
    m = sum(1 << v for v in t)
    disc_masks.append(m)

def is_face(mask):
    comp = ALL ^ mask
    return any((d & comp) == d for d in disc_masks)

faces = [m for m in range(1, 1 << N) if is_face(m)]
face_set = set(faces)
fvec = defaultdict(int)
for m in faces:
    fvec[m.bit_count() - 1] += 1
expected_f = [14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 322]
assert [fvec[i] for i in range(11)] == expected_f
assert len(faces) == 16235

# Facets must be exactly complements of disconnected triples.
facets = {ALL ^ d for d in disc_masks}
assert len(facets) == 322
assert all(f in face_set for f in facets)
for f in facets:
    assert f.bit_count() == 11
    for v in range(N):
        if not (f >> v) & 1:
            assert (f | (1 << v)) not in face_set

# Sequential element matching: at vertex v, pair all still-unmatched
# sigma with sigma U {v} when both are faces.
unmatched = set(faces)
pairs = []
for v in range(N):
    bit = 1 << v
    lows = sorted(m for m in unmatched if not (m & bit) and (m | bit) in unmatched)
    for low in lows:
        high = low | bit
        if low in unmatched and high in unmatched:
            pairs.append((low, high, v))
            unmatched.remove(low)
            unmatched.remove(high)

critical = sorted(unmatched)
crit_by_dim = defaultdict(list)
for m in critical:
    crit_by_dim[m.bit_count() - 1].append(m)
assert len(pairs) == 8099
assert len(critical) == 37
assert {d: len(v) for d, v in crit_by_dim.items()} == {0: 1, 10: 36}

# Validate every pair is a cover relation and no face appears twice.
used = set()
matched_edge = set()
for low, high, v in pairs:
    assert low in face_set and high in face_set
    assert low != high and (low | (1 << v)) == high and not (low & (1 << v))
    assert low.bit_count() + 1 == high.bit_count()
    assert low not in used and high not in used
    used.add(low); used.add(high)
    matched_edge.add((low, high))
assert used.isdisjoint(critical)
assert len(used) + len(critical) == len(faces)

# Full Hasse-orientation acyclicity check.
# Unmatched cover relations point high -> low; matched covers point low -> high.
out = {m: [] for m in faces}
indeg = {m: 0 for m in faces}
cover_count = 0
for high in faces:
    if high.bit_count() <= 1:
        continue
    bits = [v for v in range(N) if (high >> v) & 1]
    for v in bits:
        low = high ^ (1 << v)
        if low == 0 or low not in face_set:
            continue
        cover_count += 1
        if (low, high) in matched_edge:
            a, b = low, high
        else:
            a, b = high, low
        out[a].append(b)
        indeg[b] += 1

queue = deque(sorted(m for m in faces if indeg[m] == 0))
seen = 0
while queue:
    x = queue.popleft()
    seen += 1
    for y in out[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)
assert seen == len(faces), (seen, len(faces))

# Independent F_2 chain ranks from the original simplicial complex.
by_dim = {d: sorted(m for m in faces if m.bit_count() == d + 1) for d in range(11)}

def gf2_rank(cols):
    pivots = {}
    rank = 0
    for x in cols:
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                rank += 1
                break
    return rank

ranks = {}
for d in range(1, 11):
    rows = {m:i for i,m in enumerate(by_dim[d-1])}
    cols = []
    for simplex in by_dim[d]:
        col = 0
        for v in range(N):
            if (simplex >> v) & 1:
                face = simplex ^ (1 << v)
                col ^= 1 << rows[face]
        cols.append(col)
    ranks[d] = gf2_rank(cols)

expected_ranks = {1:13,2:78,3:286,4:715,5:1287,6:1716,7:1716,8:1287,9:715,10:286}
assert ranks == expected_ranks
betti = []
for d in range(11):
    cdim = len(by_dim[d])
    rd = ranks.get(d, 0)
    rnext = ranks.get(d+1, 0)
    b = cdim - rd - rnext
    if d == 0:
        b -= 1  # reduced H_0
    betti.append(b)
assert betti == [0,0,0,0,0,0,0,0,0,0,36]

pair_bytes = b"".join(f"{a}:{b}:{v}\n".encode() for a,b,v in pairs)
crit_bytes = b"".join(f"{m}\n".encode() for m in critical)
summary = {
    "vertices": N,
    "edges": 21,
    "connected_triples": len(connected),
    "disconnected_triples": len(disconnected),
    "facets": len(facets),
    "nonempty_faces": len(faces),
    "f_vector": expected_f,
    "matching_pairs": len(pairs),
    "critical_by_dimension": {str(d): len(v) for d,v in sorted(crit_by_dim.items())},
    "hasse_cover_relations": cover_count,
    "acyclic_oriented_hasse": True,
    "boundary_ranks_mod2": {str(k):v for k,v in sorted(ranks.items())},
    "reduced_betti_mod2": betti,
    "matching_sha256": hashlib.sha256(pair_bytes).hexdigest(),
    "critical_sha256": hashlib.sha256(crit_bytes).hexdigest(),
}
print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
print("VERIFY_OK")
