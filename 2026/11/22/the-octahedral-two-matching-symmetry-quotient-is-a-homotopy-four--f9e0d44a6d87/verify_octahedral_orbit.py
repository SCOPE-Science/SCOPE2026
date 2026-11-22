#!/usr/bin/env python3
"""Exact integral orbit-chain certificate for the full octahedral two-matching quotient.

Uses the Python standard library only. Enumerates all faces and all flags, not a sample.
"""
import collections
import itertools

N = 6
EDGES = tuple((a, b) for a in range(N) for b in range(a + 1, N)
              if a // 2 != b // 2)
assert len(EDGES) == 12
EINDEX = {e: i for i, e in enumerate(EDGES)}

# The full wreath-product automorphism group C2 wr S3.
VERTEX_PERMS = []
for parts in itertools.permutations(range(3)):
    for flips in itertools.product(range(2), repeat=3):
        VERTEX_PERMS.append(tuple(2 * parts[a // 2] + ((a % 2) ^ flips[a // 2])
                                  for a in range(6)))
assert len(VERTEX_PERMS) == 48 and len(set(VERTEX_PERMS)) == 48
EDGE_PERMS = [tuple(EINDEX[tuple(sorted((p[a], p[b])))] for a, b in EDGES)
              for p in VERTEX_PERMS]
MASK_ACTIONS = []
for permutation in EDGE_PERMS:
    action = [0] * (1 << 12)
    for mask in range(1, 1 << 12):
        lsb = mask & -mask
        action[mask] = action[mask ^ lsb] | (1 << permutation[lsb.bit_length() - 1])
    MASK_ACTIONS.append(action)

FACES = set()
for mask in range(1, 1 << 12):
    degrees = [0] * 6
    for i, (a, b) in enumerate(EDGES):
        if mask & (1 << i):
            degrees[a] += 1
            degrees[b] += 1
    if max(degrees) <= 2:
        FACES.add(mask)
assert len(FACES) == 771
assert tuple(sum(m.bit_count() == j for m in FACES) for j in range(1, 7)) == (12, 66, 196, 297, 180, 20)
for act in MASK_ACTIONS:
    assert {act[m] for m in FACES} == FACES

# Independently certify the covering complex is simply connected by Forman's
# elementary acyclic matching: only one critical vertex and cells in dimensions 3,4.
active_faces = set(FACES)
matched = set()
for e in range(12):
    stage = []
    for low in sorted(active_faces):
        high = low | (1 << e)
        if not (low & (1 << e)) and high in active_faces:
            stage.append((low, high))
    for low, high in stage:
        active_faces.remove(low)
        active_faces.remove(high)
        matched.add((low, high))
assert len(matched) == 377
assert collections.Counter(f.bit_count() - 1 for f in active_faces) == {0: 1, 3: 6, 4: 10}
adj = {f: [] for f in FACES}
indeg = {f: 0 for f in FACES}
for high in FACES:
    for bit in range(12):
        if high & (1 << bit):
            low = high ^ (1 << bit)
            if low not in FACES:
                continue
            src, dst = (low, high) if (low, high) in matched else (high, low)
            adj[src].append(dst)
            indeg[dst] += 1
queue = collections.deque(f for f in FACES if not indeg[f])
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in adj[f]:
        indeg[g] -= 1
        if indeg[g] == 0:
            queue.append(g)
assert visited == len(FACES), 'non-acyclic covering-complex matching'

# Three fixed-point elements generating the entire 48-element group.
GENERATORS = ((1, 0, 2, 3, 4, 5),
              (2, 3, 0, 1, 4, 5),
              (0, 1, 4, 5, 2, 3))
assert all(gen in VERTEX_PERMS for gen in GENERATORS)
assert all(any(tuple(sorted((g[a], g[b]))) == (a, b)
               for a, b in EDGES) for g in GENERATORS)
def compose(p, q):
    return tuple(p[q[i]] for i in range(6))
subgroup = {tuple(range(6))}
while True:
    expanded = subgroup | {compose(p, g) for p in subgroup for g in GENERATORS}
    if expanded == subgroup:
        break
    subgroup = expanded
assert len(subgroup) == 48

# Barycentric orbit cells indexed by orbits of strict nonempty-face flags.
canonical_cache = {}
def canonical(flag):
    old = canonical_cache.get(flag)
    if old is not None:
        return old
    result = min(tuple(action[f] for f in flag) for action in MASK_ACTIONS)
    canonical_cache[flag] = result
    return result

cells = {0: sorted({canonical((f,)) for f in FACES})}
for degree in range(1, 6):
    following = set()
    # Strict flags have strictly increasing face cardinality, so no inversions.
    for flag in cells[degree - 1]:
        for superset in FACES:
            if superset != flag[-1] and (superset & flag[-1]) == flag[-1]:
                following.add(canonical(flag + (superset,)))
    cells[degree] = sorted(following)
assert tuple(len(cells[d]) for d in range(6)) == (35, 316, 1101, 1718, 1200, 300)
assert sum((-1) ** d * len(cells[d]) for d in range(6)) == 2
indexes = {d: {flag: i for i, flag in enumerate(cells[d])} for d in cells}

# Each orbit of a barycentric flag is an oriented quotient simplex, with face
# maps by deletion and coefficients added if distinct deletions identify.
boundary = {}
cofaces = {d: collections.defaultdict(set) for d in range(5)}
for d in range(1, 6):
    for j, flag in enumerate(cells[d]):
        coefficients = collections.Counter()
        for i in range(d + 1):
            lower = flag[:i] + flag[i + 1:]
            coefficients[indexes[d - 1][canonical(lower)]] += (-1) ** i
        boundary[d, j] = {i: c for i, c in coefficients.items() if c}
        for i in boundary[d, j]:
            cofaces[d - 1][i].add(j)
for d in range(2, 6):
    for j in range(len(cells[d])):
        dd = collections.Counter()
        for i, c in boundary[d, j].items():
            for h, b in boundary[d - 1, i].items():
                dd[h] += c * b
        assert not any(dd.values()), (d, j)

# Step I: 1,021 algebraic free-unit cancellations (no matrix fill-in).
remaining = {d: set(range(len(cells[d]))) for d in cells}
stack = [(d, i) for d in range(5) for i, js in cofaces[d].items()
         if len(js) == 1 and abs(boundary[d + 1, next(iter(js))][i]) == 1]
first_cancellations = collections.Counter()
while stack:
    d, i = stack.pop()
    if i not in remaining[d]:
        continue
    js = cofaces[d][i] & remaining[d + 1]
    if len(js) != 1:
        continue
    j = next(iter(js))
    if abs(boundary[d + 1, j].get(i, 0)) != 1:
        continue
    remaining[d].remove(i)
    remaining[d + 1].remove(j)
    first_cancellations[d + 1] += 1
    for h in boundary[d + 1, j]:
        cofaces[d][h].discard(j)
        if len(cofaces[d][h]) == 1:
            k = next(iter(cofaces[d][h]))
            if abs(boundary[d + 1, k].get(h, 0)) == 1:
                stack.append((d, h))
    if d >= 1:
        for h in boundary[d, i]:
            cofaces[d - 1][h].discard(i)
            if len(cofaces[d - 1][h]) == 1:
                k = next(iter(cofaces[d - 1][h]))
                if abs(boundary[d, k].get(h, 0)) == 1:
                    stack.append((d - 1, h))
assert sum(first_cancellations.values()) == 1021
assert tuple(len(remaining[d]) for d in range(6)) == (32, 276, 847, 1037, 436, 0)
for d in range(1, 6):
    for j in remaining[d]:
        assert set(boundary[d, j]).issubset(remaining[d - 1])

# Step II: exact sparse Schur-complement reductions, pivots always +/- 1.
cols = {d: {j: dict(boundary[d, j]) for j in remaining[d]} for d in range(1, 6)}
rows = {d: collections.defaultdict(dict) for d in range(1, 6)}
for d in cols:
    for j, values in cols[d].items():
        for i, value in values.items():
            rows[d][i][j] = value

def delete_row(d, i):
    for j in list(rows[d].get(i, {})):
        del cols[d][j][i]
    rows[d].pop(i, None)

def delete_column(d, j):
    for i in list(cols[d].get(j, {})):
        del rows[d][i][j]
        if not rows[d][i]:
            del rows[d][i]
    cols[d].pop(j, None)

second_cancellations = collections.Counter()
while True:
    best = None
    for d in range(1, 6):
        for j, values in cols[d].items():
            for i, val in values.items():
                if abs(val) == 1:
                    choice = ((len(values) - 1) * (len(rows[d][i]) - 1), d, i, j)
                    if best is None or choice < best:
                        best = choice
    if best is None:
        break
    _, d, i, j = best
    pivot = cols[d][j][i]
    other_columns = list(rows[d][i].items())
    pivot_column = list(cols[d][j].items())
    for k, val in other_columns:
        if k == j:
            continue
        multiplier = val // pivot
        for h, b in pivot_column:
            changed = cols[d][k].get(h, 0) - multiplier * b
            if changed:
                cols[d][k][h] = changed
                rows[d][h][k] = changed
            else:
                cols[d][k].pop(h, None)
                rows[d][h].pop(k, None)
                if not rows[d][h]:
                    rows[d].pop(h, None)
    delete_column(d, j)
    delete_row(d, i)
    remaining[d].remove(j)
    remaining[d - 1].remove(i)
    if d >= 2:
        delete_column(d - 1, i)
    if d <= 4:
        delete_row(d + 1, j)
    second_cancellations[d] += 1

assert second_cancellations == {1: 31, 2: 245, 3: 602, 4: 435}
assert sum(second_cancellations.values()) == 1313
assert tuple(len(remaining[d]) for d in range(6)) == (1, 0, 0, 0, 1, 0)
assert all(not values for d in range(1, 6) for values in cols[d].values())
# Independent direct finite-field Gaussian elimination from the *unreduced* orbit
# boundaries (not from the cancelled matrices), a cross-check of the ranks.
def modular_rank(d, prime):
    pivots = {}
    rank = 0
    for j in range(len(cells[d])):
        vector = {i: (a % prime) for i, a in boundary[d, j].items()
                  if a % prime}
        while vector:
            i = max(vector)
            if i not in pivots:
                factor = pow(vector[i], -1, prime)
                pivots[i] = {k: (v * factor) % prime for k, v in vector.items()}
                rank += 1
                break
            factor = vector[i]
            for k, v in pivots[i].items():
                new = (vector.get(k, 0) - factor * v) % prime
                if new:
                    vector[k] = new
                else:
                    vector.pop(k, None)
    return rank

for prime in (2, 3, 5):
    ranks = [modular_rank(d, prime) for d in range(1, 6)]
    assert ranks == [34, 282, 819, 899, 300]
print('OCTAHEDRAL_TWO_MATCHING_FULL_SYMMETRY_S4_VERIFIED')
print('faces=771 group=48 quotient_cells=(35,316,1101,1718,1200,300)')
print('covering_morse=377 critical=(1 in degree 0,6 in degree 3,10 in degree 4)')
print('orbit_chain_cancellations=1021+1313 remaining=(1,0,0,0,1,0)')
print('direct_mod_2_3_5_boundary_ranks=(34,282,819,899,300)')
