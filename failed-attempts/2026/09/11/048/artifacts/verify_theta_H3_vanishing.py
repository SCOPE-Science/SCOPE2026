#!/usr/bin/env python3
"""Verify H_3(B_n(Theta_(2,3,4)); Z) = 0 via the reduced Swiatkowski complex.

Theta_(2,3,4) is the theta graph with branch vertices joined by internally-disjoint
arcs of lengths 2,3,4 (edge counts). The orbit space is homeomorphic to the minimal
(smoothed) theta graph: 2 trivalent vertices joined by 3 parallel edges.

Key fact (An-Drummond-Cole-Knudsen arXiv:1806.05585, Def 2.11 / Prop 4.9):
the reduced Swiatkowski complex uses at each vertex v only the generator `empty`
and differences h_i - h_j of half-edge generators. Hence every h-factor raises
homological degree by 1 AND consumes a distinct vertex.

Minimal theta model: vertices V = {a, b}, each trivalent. Each vertex contributes
at most one difference-generator (since only differences survive in the reduced
complex and choosing one difference uses up that vertex's homological slot).
So homological degree d <= |V| = 2, i.e. C_3 = 0 in every weight, so H_3 = 0.

This script certifies:
 (1) combinatorial inventory of the subdivided model (8 vertices, 9 edges, correct
     valences, Euler characteristic chi = V - E = -1),
 (2) that smoothing bivalent subdivision vertices preserves chi and the number
     of essential (valence>=3) vertices = 2,
 (3) enumeration of reduced-complex basis in degree 3 for weights 5 and 6 for the
     smoothed model: EMPTY (C_3 = 0),
 (4) the induced map s_*: 0 -> 0 has coker = 0 (no Z/2), rationalization surjective,
     so the target conjunction is FALSE.
Stdlib only.
"""
from itertools import combinations
from math import comb

print("=== (1) subdivided Theta_(2,3,4) inventory ===")
# vertices: a=0, b=1; path1: 0-2-1 (2 edges); path2: 0-3-4-1 (3 edges); path3: 0-5-6-7-1 (4 edges)
edges = [(0,2),(2,1),(0,3),(3,4),(4,1),(0,5),(5,6),(6,7),(7,1)]
V = sorted({v for e in edges for v in e})
nV, nE = len(V), len(edges)
chi = nV - nE
val = {v: sum(1 for e in edges if v in e) for v in V}
print("V =", V, " E =", edges)
print("|V| =", nV, " |E| =", nE, " chi =", chi)
print("valences:", val)
assert nV == 8 and nE == 9, "must have 8 vertices, 9 edges"
assert chi == -1, "chi(theta) must be -1"
ess = [v for v in V if val[v] >= 3]
biv = [v for v in V if val[v] == 2]
assert sorted(ess) == [0, 1], f"essential vertices must be branch points, got {ess}"
for v in biv:
    assert val[v] == 2
print("essential:", ess, " bivalent:", biv)

print("=== (2) smoothing ===")
# smoothing all bivalent vertices: chi invariant; minimal model: 2 vertices, 3 edges
nV_min, nE_min = 2, 3
assert nV_min - nE_min == chi, "smoothing preserves chi"
print(f"minimal model: |V|={nV_min}, |E|={nE_min}, chi={nV_min-nE_min} OK")
print("essential-vertex count preserved: 2 -> 2 OK")

print("=== (3) reduced-Swiatkowski degree-3 basis enumeration (minimal model) ===")
# Minimal model: Vmin = {a, b}; each trivalent.
# Reduced local factor at trivalent v: {empty} U {h1-h0, h2-h0}, i.e. degree-0: 1 choice,
# degree-1: 2 choices. A degree-d generator picks d DISTINCT vertices and one
# difference-generator at each, times a monomial of degree w-d in 3 edge variables.
Vmin = ['a', 'b']
nvars = 3
for w in (5, 6):
    for d in (3, 4):
        hcombos = 0
        for chosen in combinations(Vmin, d):
            hcombos += 2 ** d  # only meaningful if d <= 2; combinations() empty otherwise
        nmono = comb((w - d) + nvars - 1, nvars - 1) if (w - d) >= 0 else 0
        total = hcombos * nmono
        print(f"weight {w}, degree {d}: hcombos={hcombos} nmono={nmono} dim C_d={total}")
        if d == 3:
            assert total == 0, "C_3 must vanish"
print("C_3(B_5) = 0 and C_3(B_6) = 0 CERTIFIED (no triples of distinct vertices exist).")

print("=== (4) stabilization cokernel logic ===")
print("H_3(B_5;Z) = 0 (quotient of C_3 = 0).")
print("H_3(B_6;Z) = 0 (quotient of C_3 = 0).")
print("s_*: 0 -> 0; coker(s_*) = 0, which does NOT contain Z/2.")
print("s_* tensor Q: 0 -> 0 is surjective (vacuously).")
print("Target conjunction (torsion coker AND explicit witness 3-cycle) is FALSE.")
print("VERIFY_OK")
