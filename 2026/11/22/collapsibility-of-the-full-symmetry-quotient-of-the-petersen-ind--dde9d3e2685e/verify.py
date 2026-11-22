#!/usr/bin/env python3
"""Finite reproducibility check for the Petersen induced-forest orbit-space collapse.
Uses only the Python standard library. Run from a directory containing collapse_pairs.txt.
"""
import itertools
import collections
from functools import lru_cache
from pathlib import Path
import hashlib

V = list(itertools.combinations(range(5), 2))
assert len(V) == 10
IDX = {x: i for i, x in enumerate(V)}
EDGES = [(i, j) for i in range(10) for j in range(i + 1, 10)
         if set(V[i]).isdisjoint(V[j])]
assert len(EDGES) == 15

# Two independent forest predicates: cycle-rank and disjoint-set cycle detection.
def is_forest(m):
    nodes = {j for j in range(10) if m >> j & 1}
    es = [(a, b) for a, b in EDGES if a in nodes and b in nodes]
    adjacency = {u: [] for u in nodes}
    for a, b in es:
        adjacency[a].append(b)
        adjacency[b].append(a)
    unseen = nodes.copy()
    comps = 0
    while unseen:
        comps += 1
        frontier = [unseen.pop()]
        while frontier:
            for u in adjacency[frontier.pop()]:
                if u in unseen:
                    unseen.remove(u)
                    frontier.append(u)
    cycle_rank_zero = len(es) == len(nodes) - comps
    parent = list(range(10))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    union_forest = True
    for a, b in es:
        x, y = root(a), root(b)
        if x == y:
            union_forest = False
            break
        parent[x] = y
    assert cycle_rank_zero == union_forest
    return union_forest

FACESET = {i for i in range(1, 1 << 10) if is_forest(i)}
assert len(FACESET) == 785
assert [sum(m.bit_count() == k for m in FACESET) for k in range(1, 8)] == [10, 45, 120, 210, 240, 140, 20]
assert max(m.bit_count() for m in FACESET) == 7

GROUP = []
for p in itertools.permutations(range(5)):
    GROUP.append(tuple(IDX[tuple(sorted((p[a], p[b])))] for a, b in V))
assert len(GROUP) == 120 and len(set(GROUP)) == 120
for g in GROUP:
    assert all(tuple(sorted((g[a],g[b]))) in set(map(lambda x: tuple(sorted(x)), EDGES)) for a,b in EDGES)
# The five maximum independent stars determine the full graph-automorphism group.
stars = [{IDX[v] for v in V if a in v} for a in range(5)]
assert len({frozenset(s) for s in stars}) == 5
indep4 = []
for s in itertools.combinations(range(10),4):
    if all(not (set(V[a]).isdisjoint(V[b])) for a,b in itertools.combinations(s,2)):
        indep4.append(frozenset(s))
assert set(indep4) == set(map(frozenset,stars))
# Each pair of star sets intersects in one distinct graph vertex.
assert len({next(iter(stars[a] & stars[b])) for a,b in itertools.combinations(range(5),2)}) == 10

@lru_cache(maxsize=None)
def act(m,gi):
    g = GROUP[gi]
    return sum(1 << g[j] for j in range(10) if m >> j & 1)

@lru_cache(maxsize=None)
def rep_and_transporters(m):
    images = [act(m,i) for i in range(120)]
    r = min(images)
    return r, tuple(i for i,v in enumerate(images) if v == r)

@lru_cache(maxsize=None)
def normalize(chain):
    r, ids = rep_and_transporters(chain[-1])
    return min(tuple(act(f,i) for f in chain) for i in ids)

@lru_cache(maxsize=None)
def subchains(m):
    """All strictly increasing nonempty-face chains ending in m."""
    result = [(m,)]
    sub = (m - 1) & m
    while sub:
        for prior in subchains(sub):
            result.append(prior + (m,))
        sub = (sub - 1) & m
    return result

FACE_REPS = sorted({rep_and_transporters(m)[0] for m in FACESET})
assert len(FACE_REPS) == 23
ORBIT_CHAINS = set()
for rep in FACE_REPS:
    for ch in subchains(rep):
        ORBIT_CHAINS.add(normalize(ch))
CELLS = sorted(ORBIT_CHAINS, key=lambda c: (len(c), c))
assert len(CELLS) == 15255
CELLID = {c:i for i,c in enumerate(CELLS)}
DIM = [len(c)-1 for c in CELLS]
counts = [DIM.count(d) for d in range(7)]
assert counts == [23,283,1535,3984,5230,3360,840], counts
assert sum((-1)**d * n for d,n in enumerate(counts)) == 1

BOUNDARY = []
for cell in CELLS:
    row = []
    for k in range(len(cell)):
        shortened = cell[:k] + cell[k+1:]
        if shortened:
            f = CELLID[normalize(shortened)]
            row.append((f, (-1)**k))
    assert len(set(i for i,s in row)) == len(row)
    BOUNDARY.append(row)
# Verify integral chain-complex identities before reducing.
for i,edges in enumerate(BOUNDARY):
    coef = collections.defaultdict(int)
    for j,s in edges:
        for k,t in BOUNDARY[j]:
            coef[k] += s*t
    assert all(c == 0 for c in coef.values()), ('boundary_square',i)

# Collapses of regular barycentric orbit cells. Each chain simplex stabilizer
# fixes its faces, so the orbit-cell attaching maps have degree +/-1.
cofaces = [set() for _ in CELLS]
for upper,faces in enumerate(BOUNDARY):
    for lower,_ in faces:
        assert DIM[lower] + 1 == DIM[upper]
        cofaces[lower].add(upper)

CERT = Path(__file__).resolve().parent / 'collapse_pairs.txt'
if not CERT.is_file():
    raise FileNotFoundError('Required collapse_pairs.txt is absent')
lines = CERT.read_text(encoding='ascii').splitlines()
assert len(lines) == 7627
live = [True]*len(CELLS)
for t,line in enumerate(lines):
    parts = line.split()
    assert len(parts) == 2 and all(p.isdecimal() for p in parts), ('syntax',t)
    low,high = map(int,parts)
    assert 0 <= low < len(CELLS) and 0 <= high < len(CELLS)
    assert live[low] and live[high], ('reused', t, low,high)
    assert DIM[high] == DIM[low] + 1, ('wrong_dimension',t)
    assert cofaces[low] == {high}, ('not_a_free_face',t,low,cofaces[low])
    live[low] = live[high] = False
    for v in (low,high):
        for f,_ in BOUNDARY[v]:
            cofaces[f].discard(v)
remains = [i for i,ok in enumerate(live) if ok]
assert len(remains) == 1 and DIM[remains[0]] == 0, remains
print('PETERSEN_INDUCED_FOREST_S5_QUOTIENT_COLLAPSES_OK')
print('faces=785 group=120 orbit_faces=23 orbit_cells=15255 collapse_pairs=7627 vertices_left=1')
print('orbit_cell_vector=' + repr(counts))
print('certificate_sha256=' + hashlib.sha256(CERT.read_bytes()).hexdigest())
