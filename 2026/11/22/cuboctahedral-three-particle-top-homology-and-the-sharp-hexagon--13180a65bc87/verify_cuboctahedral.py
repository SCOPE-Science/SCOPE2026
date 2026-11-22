#!/usr/bin/env python3
"""Exact integral certificate for three unordered particles on L(Q_3).
Only Python's standard library is required. No precomputed matrices are loaded.
"""
from itertools import combinations, product
from collections import Counter
from hashlib import sha256
import json

# The twelve vertices of the cuboctahedral graph are cube edges.
cube_edges = [(a, b) for a in range(8) for b in range(a + 1, 8)
              if (a ^ b).bit_count() == 1]
assert len(cube_edges) == 12
G_edges = sorted((i, j) for i in range(12) for j in range(i + 1, 12)
                 if set(cube_edges[i]) & set(cube_edges[j]))
assert len(G_edges) == 24
G_index = {e: i for i, e in enumerate(G_edges)}
neighbors = [set() for _ in range(12)]
incident = [[] for _ in range(12)]
for e, (u, v) in enumerate(G_edges):
    neighbors[u].add(v)
    neighbors[v].add(u)
    incident[u].append(e)
    incident[v].append(e)
for arr in incident:
    arr.sort()
    assert len(arr) == 4

# Weight three, degree three part of the fully reduced Swiatkowski chain complex.
# h(v,k) means half-edge k minus the reference half-edge 0 at vertex v.
C3 = [((u, a), (v, b), (w, c))
      for u, v, w in combinations(range(12), 3)
      for a, b, c in product(range(1, 4), repeat=3)]
C3_index = {b: i for i, b in enumerate(C3)}
assert len(C3) == 5940
# C2 has 66 * 3^2 * 24 = 14256 basis elements. Use only nonzero rows.
rows = {}

def row_number(key):
    if key not in rows:
        rows[key] = len(rows)
    return rows[key]

def boundary_of_C3(triple):
    result = {}
    for j, (v, a) in enumerate(triple):
        pair = tuple(triple[i] for i in range(3) if i != j)
        for edge, s in ((incident[v][a], 1), (incident[v][0], -1)):
            r = row_number((pair, edge))
            result[r] = result.get(r, 0) + (-1)**j * s
    return {r: x for r, x in result.items() if x}

# Gaussian elimination with only unit integer pivots. Every operation is
# an invertible integral row/column operation, so the nonpivot C3 columns
# are global unimodular coordinates on the integer degree-three kernel.
pivots = {}
free_columns = []
peak_abs = 0
for j, triple in enumerate(C3):
    col = boundary_of_C3(triple)
    while col:
        row = min(col)
        old = pivots.get(row)
        if old is None:
            assert abs(col[row]) == 1, ('non-unit-pivot', j, row, col[row])
            pivots[row] = col
            break
        multiplier = col[row] * old[row]  # old[row] = +/- 1
        for r, x in old.items():
            new = col.get(r, 0) - multiplier * x
            if new:
                col[r] = new
            else:
                col.pop(r, None)
    else:
        free_columns.append(j)
    if col:
        peak_abs = max(peak_abs, max(abs(z) for z in col.values()))
assert len(pivots) == 5916 and len(free_columns) == 24
assert len(rows) == 14040

# Enumerate all undirected simple graph cycles exactly once: smallest
# vertex first, and lexicographically minimal choice of orientation.
cycles = set()
for start in range(12):
    def expand(path):
        for next_vertex in sorted(neighbors[path[-1]]):
            if next_vertex == start and len(path) >= 3:
                t = tuple(path)
                cycles.add(min(t, t[:1] + t[:0:-1]))
            elif next_vertex > start and next_vertex not in path:
                expand(path + [next_vertex])
    expand([start])
cycles = sorted(cycles, key=lambda x: (len(x), x))
assert len(cycles) == 1422
cycle_lengths = Counter(map(len, cycles))
cycle_masks = [sum(1 << v for v in c) for c in cycles]

def cycle_one_chain(c):
    result = []
    for i, v in enumerate(c):
        old, new = c[i - 1], c[(i + 1) % len(c)]
        incoming = G_index[tuple(sorted((old, v)))]
        outgoing = G_index[tuple(sorted((v, new)))]
        for a in range(1, 4):
            coefficient = (incident[v][a] == outgoing) - (incident[v][a] == incoming)
            if coefficient:
                result.append(((v, a), coefficient))
    return result

cycle_chains = [cycle_one_chain(c) for c in cycles]

def torus_chain(i, j, k):
    result = {}
    for (a, ca), (b, cb), (c, cc) in product(cycle_chains[i],
                                                cycle_chains[j],
                                                cycle_chains[k]):
        inversions = (a[0] > b[0]) + (a[0] > c[0]) + (b[0] > c[0])
        triple = tuple(sorted((a, b, c)))
        idx = C3_index[triple]
        result[idx] = result.get(idx, 0) + (-1)**inversions * ca * cb * cc
    return {idx: z for idx, z in result.items() if z}

names = []
torus_vectors = []
types = Counter()
free_index = {v: i for i, v in enumerate(free_columns)}
for i in range(len(cycles)):
    for j in range(i + 1, len(cycles)):
        if cycle_masks[i] & cycle_masks[j]:
            continue
        for k in range(j + 1, len(cycles)):
            if cycle_masks[k] & (cycle_masks[i] | cycle_masks[j]):
                continue
            chain = torus_chain(i, j, k)
            # Independent signed check, not merely a rank calculation.
            boundary = {}
            for col, coefficient in chain.items():
                for r, x in boundary_of_C3(C3[col]).items():
                    boundary[r] = boundary.get(r, 0) + coefficient * x
            assert not any(boundary.values()), (i, j, k)
            names.append((i, j, k))
            types[tuple(sorted((len(cycles[i]), len(cycles[j]),
                                len(cycles[k]))))] += 1
            torus_vectors.append([chain.get(f, 0) for f in free_columns])
assert len(names) == 60
assert types == {(3, 3, 3): 8, (3, 3, 4): 12, (3, 3, 5): 24,
                 (3, 3, 6): 16}

# Integer determinant by fraction-free Bareiss elimination, with exact
# divisions and row swaps. All the selected cycles are independently
# checked closed by the boundary computation above.
def determinant(matrix):
    A = [list(row) for row in matrix]
    n = len(A)
    assert all(len(row) == n for row in A)
    sign = 1
    previous = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((p for p in range(k + 1, n) if A[p][k]), None)
            if p is None:
                return 0
            A[k], A[p] = A[p], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = A[i][j] * pivot - A[i][k] * A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
            A[i][k] = 0
        previous = pivot
    return sign * A[n - 1][n - 1]

# Rank over Q, with standard-library fractions; tiny 24 x <=60 matrices.
def rational_rank(rows):
    from fractions import Fraction
    if not rows:
        return 0
    A = [[Fraction(v) for v in row] for row in rows]
    nr, nc = len(A), len(A[0])
    r = 0
    for col in range(nc):
        pr = next((i for i in range(r, nr) if A[i][col]), None)
        if pr is None:
            continue
        A[pr], A[r] = A[r], A[pr]
        fac = A[r][col]
        A[r] = [z/fac for z in A[r]]
        for i in range(r + 1, nr):
            fac = A[i][col]
            if fac:
                A[i] = [x - fac*y for x, y in zip(A[i], A[r])]
        r += 1
        if r == nr:
            break
    return r

# Greedy F_2 independent choice of tori (deterministic cycle-order).
chosen = []
piv = {}
for index, vector in enumerate(torus_vectors):
    mask = sum((v & 1) << a for a, v in enumerate(vector))
    while mask:
        b = (mask & -mask).bit_length() - 1
        if b not in piv:
            piv[b] = mask
            chosen.append(index)
            break
        mask ^= piv[b]
assert len(chosen) == 24
basis_matrix = [[torus_vectors[i][r] for i in chosen] for r in range(24)]
det_basis = determinant(basis_matrix)
assert abs(det_basis) == 1, det_basis

short_indices = [j for j, cycle_indices in enumerate(names)
                 if max(len(cycles[x]) for x in cycle_indices) <= 5]
assert len(short_indices) == 44
short_rank = rational_rank([torus_vectors[i] for i in short_indices])
assert short_rank == 20
# The full rank-20 short-cycle span is saturated, since the 20 earlier
# triangle/square classes are a primitive integral direct summand:
first20 = [i for i, cycs in enumerate(names)
           if max(len(cycles[x]) for x in cycs) <= 4]
assert len(first20) == 20
# A 20x20 unit minor in their 24x20 coordinate matrix, found exhaustively.
# Integer Smith computation is not required for the sharp rank cutoff,
# but the minor certifies that the 20-dimensional short lattice is primitive.
from itertools import combinations as choose
minor = next((determinant([[torus_vectors[j][r] for j in first20]
                           for r in row_ids])
              for row_ids in choose(range(24), 20)
              if abs(determinant([[torus_vectors[j][r] for j in first20]
                                  for r in row_ids])) == 1), None)
assert minor is not None

results = {
    'graph': 'line graph of three-cube (cuboctahedral graph)',
    'graph_vertices': 12, 'graph_edges': 24,
    'C3_rank': len(C3), 'C2_rank': 14256,
    'C2_nonzero_rows': len(rows), 'unit_pivots': len(pivots),
    'free_coordinates': free_columns,
    'H3_integral_rank': len(free_columns),
    'simple_graph_cycles': len(cycles),
    'disjoint_triples': len(names),
    'torus_types': {','.join(map(str, k)): v for k, v in sorted(types.items())},
    'rank_cycles_length_at_most_five': short_rank,
    'rank_cycles_length_at_most_four': rational_rank([torus_vectors[i] for i in first20]),
    'basis_torus_indices_zero_based': chosen,
    'basis_cycle_indices_zero_based': [names[i] for i in chosen],
    'basis_determinant': det_basis,
    'primitive_20_minor': minor,
    'status': 'CUBOCTAHEDRAL_THREE_POINT_H3_TORUS_THRESHOLD_OK'
}
print(json.dumps(results, sort_keys=True, separators=(',', ':')))
