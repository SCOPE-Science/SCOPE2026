#!/usr/bin/env python3
"""Independent finite certificate check for the antipodal Q4 Rips quotient.
Run: python verify.py (next to matching.json). Standard library only.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

N = 16

def anti(mask):
    return sum(1 << (v ^ 15) for v in range(N) if mask & (1 << v))

def representative(mask):
    return min(mask, anti(mask))

def dimension(mask):
    return mask.bit_count() - 1

def vertices(mask):
    return [v for v in range(N) if mask & (1 << v)]

def admissible(mask):
    vs = vertices(mask)
    return all((u ^ v).bit_count() <= 2 for i, u in enumerate(vs)
               for v in vs[i + 1:])

# Direct enumeration of every possible nonempty subset, not a precomputed table.
faces = {mask for mask in range(1, 1 << N) if mask.bit_count() <= 5
         and admissible(mask)}
even_vertices = {v for v in range(N) if v.bit_count() % 2 == 0}
even_faces = {f for f in faces if set(vertices(f)) <= even_vertices}
orbits = {representative(f) for f in faces}
A = {representative(f) for f in even_faces}
R = orbits - A
assert Counter(dimension(f) for f in faces) == {0: 16, 1: 80, 2: 160, 3: 120, 4: 16}
assert Counter(dimension(f) for f in orbits) == {0: 8, 1: 40, 2: 80, 3: 60, 4: 8}
assert Counter(dimension(f) for f in A) == {0: 4, 1: 12, 2: 16, 3: 8}
assert Counter(dimension(f) for f in R) == {0: 4, 1: 28, 2: 64, 3: 52, 4: 8}
assert all(anti(f) != f for f in faces)
assert all(all((u ^ v).bit_count() == 2 for v in even_vertices
                   if v != u and v != (u ^ 15)) for u in even_vertices)
assert all((u ^ (u ^ 15)).bit_count() == 4 for u in even_vertices)

# CW orbit-incidence check: each facet of each cell yields a different orbit.
cover_edges = set()
for top in orbits:
    if dimension(top) == 0:
        continue
    boundary = [representative(top ^ (1 << v)) for v in vertices(top)]
    assert len(boundary) == len(set(boundary))
    for bot in boundary:
        assert bot in orbits
        cover_edges.add((bot, top))
print("ACTUAL COVER EDGES",len(cover_edges))
assert all(b in A for (b, t) in cover_edges if t in A)

payload = json.loads((Path(__file__).resolve().parent / 'matching.json').read_text(encoding='utf-8'))
pairs = [(int(x, 16), int(y, 16)) for x, y in payload['matching_pairs']]
assert len(pairs) == len(set(pairs)) == 76
matched = set()
for bot, top in pairs:
    assert bot in R and top in R
    assert (bot, top) in cover_edges
    assert bot not in matched and top not in matched
    matched.update((bot, top))
critical = R - matched
assert len(critical) == 4 and all(dimension(f) == 3 for f in critical)
assert sorted(critical) == sorted(int(x, 16) for x in payload['critical_cells'])
assert Counter(dimension(a) for a, _ in pairs) == {0: 4, 1: 24, 2: 40, 3: 8}

# Reconstruct the entire directed Hasse graph, including the even-parity subcomplex.
# Nonmatching incidence: higher -> lower; matching incidence: lower -> higher.
out = {v: set() for v in orbits}
matched_edges = set(pairs)
for bot, top in cover_edges:
    if (bot, top) in matched_edges:
        out[bot].add(top)
    else:
        out[top].add(bot)
indegree = {v: 0 for v in orbits}
for v in out:
    for w in out[v]:
        indegree[w] += 1
stack = [v for v in orbits if indegree[v] == 0]
processed = 0
while stack:
    v = stack.pop()
    processed += 1
    for w in out[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            stack.append(w)
assert processed == len(orbits), 'Gradient cycle detected'

# Independent finite-field cellular homology check.
# The orbit quotient is regular because its cell face orbits are distinct.
by_dim = [sorted(f for f in orbits if dimension(f) == d) for d in range(5)]

def incidence(bottom, top):
    ordered = vertices(top)
    for j, v in enumerate(ordered):
        f = top ^ (1 << v)
        if representative(f) != bottom:
            continue
        if f == bottom:
            return (-1) ** j
        trans = [x ^ 15 for x in vertices(f)]
        inv = sum(trans[i] > trans[jj]
                  for i in range(len(trans)) for jj in range(i + 1, len(trans)))
        return (-1) ** (j + inv)
    return 0

def rank_mod_p(rows, cols, p):
    pivots = {}
    for top in cols:
        col = {i: incidence(bot, top) % p for i, bot in enumerate(rows)
               if (bot, top) in cover_edges}
        col = {i: c for i, c in col.items() if c}
        while col:
            i = max(col)
            if i not in pivots:
                fac = pow(col[i], -1, p)
                pivots[i] = {j: (x * fac) % p for j, x in col.items()}
                break
            fac = col[i]
            for j, x in pivots[i].items():
                y = (col.get(j, 0) - fac * x) % p
                if y:
                    col[j] = y
                else:
                    col.pop(j, None)
    return len(pivots)

for p, required in ((2, (7, 32, 47, 8)), (3, (7, 33, 47, 8))):
    ranks = tuple(rank_mod_p(by_dim[d - 1], by_dim[d], p) for d in range(1, 5))
    assert ranks == required, (p, ranks)
    print(f'boundary ranks modulo {p}: {ranks}')
print('full faces = 392; orbit cells = 196; even-parity orbit cells = 40')
print('orbit Hasse incidences =', len(cover_edges))
print('relative matched pairs = 76; critical relative cells = four dimension-three cells')
print('acyclic directed Hasse graph verified on all 196 orbit cells')
print('ALL_VERIFY_OK')
