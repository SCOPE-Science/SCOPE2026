#!/usr/bin/env python3
"""Exact standalone certificate for a punctured two-step Fano-incidence neighborhood complex."""
from collections import Counter, deque
from functools import lru_cache

N = 14
vertices = range(N)
points = range(1, 8)
adj = [set() for _ in vertices]
for a in points:
    for b in points:
        if (a & b).bit_count() % 2 == 0:
            u, v = a - 1, 7 + b - 1
            adj[u].add(v)
            adj[v].add(u)
assert sum(len(v) for v in adj) == 42
assert set(map(len, adj)) == {3}

def distances(src):
    out = {src: 0}
    todo = deque([src])
    while todo:
        u = todo.popleft()
        for v in sorted(adj[u]):
            if v not in out:
                out[v] = out[u] + 1
                todo.append(v)
    assert len(out) == N
    assert Counter(out.values()) == {0: 1, 1: 3, 2: 6, 3: 4}
    return out

balls = []
for v in vertices:
    ds = distances(v)
    mask = sum(1 << u for u in vertices if ds[u] in (1, 2))
    assert mask.bit_count() == 9
    balls.append(mask)
assert len(set(balls)) == N

faces = set()
for facet in balls:
    f = facet
    while f:
        faces.add(f)
        f = (f - 1) & facet
assert len(faces) == 4480
fvec = [sum(f.bit_count() == k + 1 for f in faces) for k in range(9)]
assert fvec == [14, 91, 364, 903, 1358, 1106, 504, 126, 14]

# Successively delete free codimension-one pairs, or one maximal critical face.
active = set(faces)
cofaces = {s: set() for s in active}
for s in active:
    for i in vertices:
        t = s | (1 << i)
        if t != s and t in active:
            cofaces[s].add(t)
degree = {s: len(cofaces[s]) for s in active}
free = {s for s in active if degree[s] == 1}
pairs, critical = [], []
while active:
    if free:
        s = min(free)
        free.remove(s)
        if s not in active or degree[s] != 1:
            continue
        t = next(u for u in cofaces[s] if u in active)
        assert t.bit_count() == s.bit_count() + 1
        pairs.append((s, t))
        gone = (s, t)
    else:
        s = max(active, key=lambda u: (u.bit_count(), -u))
        assert not any((s | (1 << i)) in active and (s | (1 << i)) != s for i in vertices)
        critical.append(s)
        gone = (s,)
    for s in gone:
        active.remove(s)
        bits = s
        while bits:
            bit = bits & -bits
            bits -= bit
            low = s ^ bit
            if low in active:
                degree[low] -= 1
                if degree[low] == 1:
                    free.add(low)

crit = Counter(s.bit_count() - 1 for s in critical)
assert len(pairs) == 2224 and crit == {0: 1, 4: 29, 5: 2}
assert 2 * len(pairs) + len(critical) == len(faces)
low_to_high = dict(pairs)
high_to_low = {t: s for s, t in pairs}
assert len(low_to_high) == len(high_to_low) == len(pairs)
assert not (set(low_to_high) & set(high_to_low))

# Confirm acyclicity of the oriented full Hasse diagram, independently of
# the deletion construction.  Matched incidences reverse their orientation.
out = {s: [] for s in faces}
indeg = dict.fromkeys(faces, 0)
cover_count = 0
for high in faces:
    if high.bit_count() == 1:
        continue
    bits = high
    while bits:
        bit = bits & -bits
        bits -= bit
        low = high ^ bit
        if low_to_high.get(low) == high:
            start, end = low, high
        else:
            start, end = high, low
        out[start].append(end)
        indeg[end] += 1
        cover_count += 1
queue = deque(s for s in sorted(faces) if indeg[s] == 0)
removed = 0
while queue:
    s = queue.popleft()
    removed += 1
    for t in out[s]:
        indeg[t] -= 1
        if indeg[t] == 0:
            queue.append(t)
assert removed == len(faces)

# Morse differential from critical five-cells to critical four-cells.
# Formal integral substitution along the acyclic gradient matching.
critical4 = {s for s in critical if s.bit_count() == 5}
critical5 = {s for s in critical if s.bit_count() == 6}
def sign(high, low):
    bit = high ^ low
    assert bit.bit_count() == 1
    return -1 if (high & (bit - 1)).bit_count() % 2 else 1

@lru_cache(None)
def reduce_four(simplex):
    if simplex in critical4:
        return {simplex: 1}
    if simplex in high_to_low:
        return {}
    upper = low_to_high[simplex]
    assert upper.bit_count() == 6
    pivot = sign(upper, simplex)
    result = {}
    bits = upper
    while bits:
        bit = bits & -bits
        bits -= bit
        lower = upper ^ bit
        if lower == simplex:
            continue
        multiplier = -pivot * sign(upper, lower)
        for target, coeff in reduce_four(lower).items():
            result[target] = result.get(target, 0) + multiplier * coeff
    return {s: c for s, c in result.items() if c}

critical_boundaries = {}
for high in sorted(critical5):
    result = {}
    bits = high
    while bits:
        bit = bits & -bits
        bits -= bit
        lower = high ^ bit
        for target, coeff in reduce_four(lower).items():
            result[target] = result.get(target, 0) + sign(high, lower) * coeff
    critical_boundaries[high] = {s: c for s, c in result.items() if c}
assert critical_boundaries == {0x297: {}, 0x1f80: {}}

# Independent combinatorial computation over F_2; the integer Morse
# certificate, not these modular ranks, proves the integral claim.
by_dim = {d: sorted(s for s in faces if s.bit_count() == d + 1) for d in range(9)}
rank = {}
for k in range(1, 9):
    pos = {s: j for j, s in enumerate(by_dim[k - 1])}
    pivots = {}
    for high in by_dim[k]:
        col, bits = 0, high
        while bits:
            bit = bits & -bits
            bits -= bit
            col ^= 1 << pos[high ^ bit]
        while col:
            head = col.bit_length() - 1
            if head in pivots:
                col ^= pivots[head]
            else:
                pivots[head] = col
                break
    rank[k] = len(pivots)
# Boundary ranks give mod-two Betti numbers in positive degrees.
red_betti = {k: len(by_dim[k]) - rank.get(k, 0) - rank.get(k + 1, 0)
             for k in range(1, 9)}
red_betti = {k: v for k, v in red_betti.items() if v}
assert rank[1] == 13 and red_betti == {4: 29, 5: 2}
assert sum((-1)**d * fvec[d] for d in range(9)) == 28
print('HEAWOOD_PUNCTURED_TWO_STEP_NEIGHBORHOOD_PASS')
print('vertices=14 edges=21 distance_distribution=1,3,6,4')
print('distinct_facets=14 vertices_per_facet=9')
print('nonempty_faces=4480 f_vector=' + repr(fvec))
print('matched_pairs=2224 critical_cells=' + repr(dict(sorted(crit.items()))))
print('hasse_cover_relations=' + str(cover_count) + ' acyclic_nodes=' + str(removed))
print('critical_five_masks=' + repr([hex(s) for s in sorted(critical5)]))
print('morse_five_to_four_nonzero_entries=' + str(sum(len(x) for x in critical_boundaries.values())))
print('mod_two_reduced_betti=' + repr(red_betti))
print('euler_characteristic=28')
