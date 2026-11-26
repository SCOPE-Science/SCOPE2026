#!/usr/bin/env python3
"""Exact, self-contained discrete Morse certificate for a graph matching complex.
Run: python verify_homotopy.py
"""
from itertools import combinations

LABELS = tuple(combinations(range(5), 2))
EDGES = tuple((i, j) for i, j in combinations(range(10), 2)
              if set(LABELS[i]).isdisjoint(LABELS[j]))
assert len(EDGES) == 15
FACES = set()
for mask in range(1, 1 << 15):
    chosen = [EDGES[k] for k in range(15) if mask & (1 << k)]
    if len({u for e in chosen for u in e}) == 2 * len(chosen):
        FACES.add(mask)
assert len(FACES) == 331
assert [sum(f.bit_count() == k for f in FACES) for k in range(1, 6)] == [15,75,145,90,6]

ORDER = (0, 9, 2, 11, 13, 4, 7, 6, 3, 14, 10, 12, 8, 5, 1)
unpaired = set(FACES)
matched = []
for v in ORDER:
    for f in sorted(tuple(unpaired)):
        if f not in unpaired or f & (1 << v):
            continue
        g = f | (1 << v)
        if g in unpaired:
            unpaired.remove(f)
            unpaired.remove(g)
            matched.append((f, g))
assert len(matched) == 160
assert len(unpaired) == 11
assert [sum(f.bit_count() == k for f in unpaired) for k in range(1, 6)] == [1,0,5,5,0]

# Verify acyclicity of the explicitly specified matching on the Hasse diagram.
up_pairs = set(matched)
adj = {f: [] for f in FACES}
for hi in FACES:
    for v in range(15):
        if hi & (1 << v):
            lo = hi & ~(1 << v)
            if lo in FACES:
                if (lo, hi) in up_pairs:
                    adj[lo].append(hi)
                else:
                    adj[hi].append(lo)
state = {}
def visit(f):
    if state.get(f, 0) == 1:
        raise AssertionError('closed gradient path')
    if state.get(f, 0) == 2:
        return
    state[f] = 1
    for g in adj[f]:
        visit(g)
    state[f] = 2
for cell in FACES:
    visit(cell)

# Integral algebraic Morse cancellation, using only unit pivots.
boundary = {}
for f in FACES:
    used = [i for i in range(15) if f & (1 << i)]
    boundary[f] = {f ^ (1 << i): (-1) ** j
                   for j, i in enumerate(used) if f ^ (1 << i) != 0}

def squared_zero():
    for c, terms in boundary.items():
        b2 = {}
        for f, coeff in terms.items():
            assert f in boundary
            for y, e in boundary[f].items():
                b2[y] = b2.get(y, 0) + coeff * e
        assert all(x == 0 for x in b2.values())
squared_zero()
for a, b in matched:
    pivot = boundary[b].get(a, 0)
    assert abs(pivot) == 1, (a, b, pivot)
    for c in tuple(boundary):
        if c == a or c == b:
            continue
        coeff = boundary[c].get(a, 0)
        if coeff:
            assert coeff % pivot == 0
            for f, d in boundary[b].items():
                boundary[c][f] = boundary[c].get(f, 0) - coeff // pivot * d
                if boundary[c][f] == 0:
                    del boundary[c][f]
    del boundary[a]
    del boundary[b]
    for chain in boundary.values():
        chain.pop(a, None)
        chain.pop(b, None)
assert set(boundary) == unpaired
squared_zero()
assert all(not terms for terms in boundary.values())
print('PETERSEN_MATCHING_COMPLEX')
print('face_counts=15,75,145,90,6')
print('Morse_pairs=160')
print('critical_cells=1(vertex),5(two-cells),5(three-cells)')
print('gradient_acyclic=True')
print('integral_Morse_boundary=zero')
print('homotopy_type=5*S2_vee_5*S3')
print('VERIFY_HOMOTOPY_OK')
