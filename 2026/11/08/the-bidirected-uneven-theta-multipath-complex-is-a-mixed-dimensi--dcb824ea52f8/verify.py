#!/usr/bin/env python3
"""Reproduce the complete simplicial and integral Morse calculation for a bidirected theta graph.

Requires Python 3.9+ standard library only. All calculations are exact integers.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import json

# Vertices 0 and 1 are poles. The paths 0-2-1, 0-3-1, 0-4-5-1
# have lengths 2, 2 and 3. Both arc orientations of every edge are present.
UNDIRECTED = ((0, 2), (2, 1), (0, 3), (3, 1), (0, 4), (4, 5), (5, 1))
ARCS = tuple(arc for a, b in UNDIRECTED for arc in ((a, b), (b, a)))
assert len(ARCS) == 14 and len(set(ARCS)) == 14
N = len(ARCS)


def valid(mask):
    """A multipath is a spanning union of directed, noncyclic vertex-disjoint paths."""
    outgoing, incoming = {}, {}
    for j, (a, b) in enumerate(ARCS):
        if mask >> j & 1:
            if a in outgoing or b in incoming:
                return False
            outgoing[a], incoming[b] = b, a
    for start in outgoing:
        visited, x = set(), start
        while x in outgoing:
            if x in visited:
                return False
            visited.add(x)
            x = outgoing[x]
    return True


faces = tuple(mask for mask in range(1, 1 << N) if valid(mask))
F = set(faces)
assert len(F) == 280
sizes = Counter(m.bit_count() - 1 for m in faces)
assert dict(sorted(sizes.items())) == {0: 14, 1: 64, 2: 114, 3: 76, 4: 12}
for f in faces:
    for j in range(N):
        if f >> j & 1:
            assert (f ^ (1 << j)) in F or f.bit_count() == 1
print('FACE_CENSUS_OK', len(F), dict(sorted(sizes.items())))

# Build every immediate face--coface incidence of the Boolean face poset.
lowers = {f: set() for f in F}
uppers = {f: set() for f in F}
for g in F:
    for j in range(N):
        if g >> j & 1:
            f = g ^ (1 << j)
            if f:
                lowers[g].add(f)
                uppers[f].add(g)
incidences = sum(map(len, lowers.values()))

# Deterministic elementary-matching/critical-cell removal.
# Each paired low face has exactly one remaining immediate coface,
# and this coface is maximal in the remaining subcomplex.
remaining = set(F)
co = {f: set(uppers[f]) for f in F}
free = {f for f in F if len(co[f]) == 1}
matching = []
critical = []
sequence = []
while remaining:
    if free:
        f = max(free, key=lambda a: (a.bit_count(), -a))
        assert len(co[f]) == 1
        g = next(iter(co[f]))
        assert g in remaining and g.bit_count() == f.bit_count() + 1
        assert not co[g], 'upper cell must be maximal at cancellation'
        matching.append((f, g))
        sequence.append(['pair', f, g])
        removed = (f, g)
    else:
        facets = [f for f in remaining if not co[f]]
        assert facets
        g = max(facets, key=lambda a: (a.bit_count(), -a))
        critical.append(g)
        sequence.append(['critical', g])
        removed = (g,)
    for x in removed:
        assert x in remaining
        remaining.remove(x)
        free.discard(x)
    for x in removed:
        for y in lowers[x]:
            if y in remaining:
                co[y].discard(x)
                if len(co[y]) == 1:
                    free.add(y)
                else:
                    free.discard(y)

assert 2 * len(matching) + len(critical) == len(F)
C = Counter(c.bit_count() - 1 for c in critical)
assert dict(sorted(C.items())) == {0: 1, 2: 5, 3: 6}
assert len(matching) == 134
print('MORSE_MATCHING_OK', len(matching), dict(sorted(C.items())))

# Independently verify global acyclicity of the COMPLETE directed Hasse graph:
# unmatched pairs point from coface to face; matched pairs are reversed.
matched = set(matching)
adj = {f: [] for f in F}
indeg = {f: 0 for f in F}
for g in F:
    for f in lowers[g]:
        a, b = (f, g) if (f, g) in matched else (g, f)
        adj[a].append(b)
        indeg[b] += 1
queue = deque(f for f in F if indeg[f] == 0)
seen = 0
while queue:
    f = queue.popleft()
    seen += 1
    for g in adj[f]:
        indeg[g] -= 1
        if indeg[g] == 0:
            queue.append(g)
assert seen == len(F)
print('HASSE_ACYCLIC_OK', seen, incidences)

# Exact signed integral Morse differential by elimination of matched pairs.
# Orient each simplex using increasing directed-arc index.
critical_set = set(critical)
matched_low = dict(matching)
matched_high = {g: f for f, g in matching}
assert len(matched_high) == len(matching)


def oriented_boundary(cell):
    positions = [j for j in range(N) if cell >> j & 1]
    return [(cell ^ (1 << j), (-1) ** pos)
            for pos, j in enumerate(positions)]


@lru_cache(None)
def projection(cell):
    if cell in critical_set:
        return {cell: 1}
    if cell in matched_high:
        return {}
    assert cell in matched_low
    upper = matched_low[cell]
    entries = oriented_boundary(upper)
    pivot = next(coef for lower, coef in entries if lower == cell)
    assert abs(pivot) == 1
    result = {}
    for lower, coef in entries:
        if lower == cell:
            continue
        for target, value in projection(lower).items():
            result[target] = result.get(target, 0) - pivot * coef * value
    return {k: v for k, v in result.items() if v}


def morse_boundary(cell):
    result = {}
    for lower, coef in oriented_boundary(cell):
        for target, value in projection(lower).items():
            result[target] = result.get(target, 0) + coef * value
    return {k: v for k, v in result.items() if v}

for c in critical:
    if c.bit_count() > 1:
        assert morse_boundary(c) == {}, (c, morse_boundary(c))
print('INTEGRAL_MORSE_DIFFERENTIAL_OK', len(critical), 'all_zero')

# Independent mod-2 boundary rank check on full simplicial chain complex.
by_degree = {d: sorted(m for m in F if m.bit_count() == d + 1) for d in C.keys() | {1, 4}}
mod2_ranks = {}
for d in range(1, 5):
    index = {m: i for i, m in enumerate(by_degree[d-1])}
    pivot = {}
    for cell in by_degree[d]:
        v = 0
        for low, _ in oriented_boundary(cell):
            v ^= 1 << index[low]
        while v:
            high = v.bit_length() - 1
            if high not in pivot:
                pivot[high] = v
                break
            v ^= pivot[high]
    mod2_ranks[d] = len(pivot)
mod2_betti = {}
for d in range(5):
    mod2_betti[d] = len(by_degree[d]) - mod2_ranks.get(d, 0) - mod2_ranks.get(d + 1, 0)
assert mod2_betti == {0: 1, 1: 0, 2: 5, 3: 6, 4: 0}
print('RAW_MOD2_HOMOLOGY_OK', mod2_betti)

# Since the Morse CW model has no 1-cells, its 2-skeleton is a wedge of
# five S^2. The zero integral attaching-degree matrix means each 3-cell
# attaches nullhomotopically (pi_2 of a simply connected 2-complex is H_2).
print('HOMOTOPY_OK', 'wedge_5_S2_and_6_S3')
print('ALL_VERIFY_OK')

with open('matching_certificate.json', 'w', encoding='utf-8') as out:
    json.dump({'arcs': ARCS, 'face_vector': [len(by_degree[i]) for i in range(5)],
               'critical': critical, 'pairs': matching}, out,
              ensure_ascii=False, separators=(',', ':'))
    out.write('\n')
