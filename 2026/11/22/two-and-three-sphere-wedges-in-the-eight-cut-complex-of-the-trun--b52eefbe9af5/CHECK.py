#!/usr/bin/env python3
"""Exact, standalone certificate for the ordinary eight-cut complex of T(K4).

Standard library only. Deterministic enumeration and unit integral elimination.
"""
from itertools import combinations, permutations
from math import comb

V = tuple(permutations(range(4), 2))
assert len(V) == 12
N = len(V)
E = set()
for a, b in combinations(range(N), 2):
    x, y = V[a], V[b]
    if x[0] == y[0] or x == y[::-1]:
        E.add((a, b))
assert len(E) == 18
neighbors = [0] * N
for a, b in E:
    neighbors[a] |= 1 << b
    neighbors[b] |= 1 << a
assert all(m.bit_count() == 3 for m in neighbors)
FULL = (1 << N) - 1

def connected(mask):
    reached = 0
    wave = mask & -mask
    while wave:
        reached |= wave
        links = 0
        while wave:
            bit = wave & -wave
            wave ^= bit
            links |= neighbors[bit.bit_length() - 1]
        wave = (links & mask) & ~reached
    return reached == mask

# The complement of each disconnected induced eight-set is a facet.
facets = []
for eight in combinations(range(N), 8):
    S = sum(1 << a for a in eight)
    if not connected(S):
        facets.append(FULL ^ S)
assert len(facets) == 252 and len(set(facets)) == 252
faces = [set() for _ in range(4)]
for f in facets:
    sub = f
    while sub:
        faces[sub.bit_count() - 1].add(sub)
        sub = (sub - 1) & f
F = [sorted(x) for x in faces]
assert [len(x) for x in F] == [12, 66, 204, 252]

# The full one-skeleton and explicit disk fillings of all absent triangles
# make the two-skeleton simply connected.
assert len(faces[1]) == comb(N, 2)
missing_triangles = []
for triple in combinations(range(N), 3):
    triangle = sum(1 << v for v in triple)
    if triangle in faces[2]:
        continue
    witnesses = [w for w in range(N) if w not in triple and all(
        (triangle ^ (1 << v)) | (1 << w) in faces[2]
        for v in triple)]
    assert witnesses, (triple, 'no simplicial cone disk')
    missing_triangles.append((triple, witnesses[0]))
assert len(missing_triangles) == 16

# Signed boundary matrices as sparse row dictionaries, orientation from
# increasing vertex order. Every entry is an ordinary integer.
def boundary(i):
    lower = {mask: r for r, mask in enumerate(F[i-1])}
    R = {r: {} for r in range(len(F[i-1]))}
    for c, face in enumerate(F[i]):
        verts = [v for v in range(N) if face & (1 << v)]
        for pos, v in enumerate(verts):
            r = lower[face ^ (1 << v)]
            R[r][c] = (-1) ** pos
    return R

D2 = boundary(2)
D3 = boundary(3)
# Check the boundary of every boundary is zero over Z.
D1 = boundary(1)
for col in range(len(F[3])):
    accumulated = {}
    two_faces = {row: R[col] for row, R in D3.items() if col in R}
    for triangle_row, sign in two_faces.items():
        for edge_row, incidences in D2.items():
            if triangle_row in incidences:
                accumulated[edge_row] = accumulated.get(edge_row, 0) + sign * incidences[triangle_row]
    assert all(v == 0 for v in accumulated.values())

# Missing-triangle disk fillings imply that H_1 vanishes integrally:
# the boundaries of present triangles span the full integral cycle
# lattice of the complete one-skeleton, of rank C(11,2)=55.
rank_d2 = comb(N-1, 2)
assert rank_d2 == 55

# Integral unimodular elimination. Each pivot ±1 gives invertible integral
# row and column operations and a direct factor Z --(1)--> Z.
# Remove that pair and repeat on the Schur complement. End residual zero
# proves all nonzero Smith invariant factors are exactly 1.
R = {r: dict(items) for r, items in D3.items()}
C = {j: set() for j in range(len(F[3]))}
for r, items in R.items():
    for c in items:
        C[c].add(r)
pivot_history = []
max_abs_entry = 1
while True:
    candidates = [(len(R[r]) * len(C[c]), r, c)
                  for r in R for c, v in R[r].items() if abs(v) == 1]
    if not candidates:
        break
    _, r, c = min(candidates)
    pivot = R[r][c]
    source = dict(R[r])
    for rr in tuple(C[c]):
        if rr == r:
            continue
        multiplier = R[rr][c] // pivot
        for j, v in source.items():
            new_value = R[rr].get(j, 0) - multiplier * v
            max_abs_entry = max(max_abs_entry, abs(new_value))
            if new_value:
                R[rr][j] = new_value
                C[j].add(rr)
            else:
                R[rr].pop(j, None)
                C[j].discard(rr)
    for j in source:
        C[j].discard(r)
    del R[r]
    del C[c]
    for row in R.values():
        row.pop(c, None)
    pivot_history.append((r, c, pivot))
rank_d3 = len(pivot_history)
assert rank_d3 == 143
assert all(not row for row in R.values())
assert max_abs_entry == 1
assert len(F[2])-rank_d2-rank_d3 == 6
assert len(F[3])-rank_d3 == 109

# A separate binary rank reduction of the original signed matrix.
columns = []
for c in range(len(F[3])):
    bits = sum(1 << r for r, row in D3.items() if c in row)
    columns.append(bits)
GF2 = {}
for bits in columns:
    while bits:
        pivot = bits.bit_length() - 1
        if pivot not in GF2:
            GF2[pivot] = bits
            break
        bits ^= GF2[pivot]
assert len(GF2) == 143

print('PASS: graph 12 vertices, 18 edges; disconnected eight-sets 252')
print('PASS: simplicial f-vector (12, 66, 204, 252)')
print('PASS: complete one-skeleton, 16 absent triangles, 16 explicit filling disks')
print('PASS: signed boundary composition is zero over Z')
print('PASS: boundary ranks d2=55, d3=143; d3 has 143 unit pivots and zero residual')
print('PASS: independent mod-two rank d3=143; maximum intermediate absolute coefficient 1')
print('PASS: simply connected, reduced H2=Z^6, H3=Z^109, no torsion')
print('PASS: homotopy type wedge(6,S2) wedge wedge(109,S3)')
