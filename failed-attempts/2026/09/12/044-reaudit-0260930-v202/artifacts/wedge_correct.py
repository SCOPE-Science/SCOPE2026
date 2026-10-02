"""CORRECT simplicial multiwedge J_(3,2,1,1,1,1)(octahedron) via MNF edge-replacement.
Wedge at v: MNF' = {F : v not in F} union {(F-{v}) u {n1,n2} : v in F}.
Validates: tetra bdry -> S^3; pentagon -> S^2; then octahedron x3 wedges -> S^5?
"""
from itertools import combinations
import sys
sys.path.insert(0, 'output/artifacts')
from homology_lib import betti_unreduced

def wedge_mnf(MNF, V, v, nxt):
    n1, n2 = nxt, nxt+1
    out = []
    for F in MNF:
        F = set(F)
        if v not in F:
            out.append(set(F))
        else:
            out.append((F - {v}) | {n1, n2})
    Vp = [u for u in V if u != v] + [n1, n2]
    return out, Vp, nxt+2

def faces_from_mnf(MNF, V):
    F = set()
    for r in range(len(V)+1):
        for S in combinations(sorted(V), r):
            St = set(S)
            if not any(set(G).issubset(St) for G in MNF):
                F.add(tuple(sorted(S)))
    return F

def report(name, MNF, V):
    F = faces_from_mnf(MNF, V)
    import collections
    fv = dict(sorted(collections.Counter(len(x)-1 for x in F).items()))
    H = {d: x for d, x in betti_unreduced(F, len(V)).items() if x}
    print(name, "verts:", len(V), "MNF sizes:", sorted(len(m) for m in MNF))
    print("  f-vector:", fv)
    print("  homology (reduced H0):", H)
    return F

# tetra boundary S^2
MNF = [{0,1,2,3}]
M2, V2, nx = wedge_mnf(MNF, [0,1,2,3], 0, 4)
report("wedge(tetra)", MNF if False else M2, V2)

# pentagon S^1
P = [0,1,2,3,4]
E = {(0,1),(1,2),(2,3),(3,4),(4,0)}
MP = []
for i in range(5):
    for j in range(i+1, 5):
        if (i,j) not in E and (j,i) not in E:
            MP.append({i,j})
print("pentagon MNF:", MP)
M3, V3, nx = wedge_mnf(MP, P, 0, 5)
report("wedge(pentagon)", M3, V3)

# octahedron: antipodal pairs
MO = [{0,1},{2,3},{4,5}]
F0 = faces_from_mnf(MO, list(range(6)))
print("octahedron check:", {d: x for d, x in betti_unreduced(F0, 6).items() if x})
W1, V, nx = wedge_mnf(MO, list(range(6)), 0, 6)
report("W1 (wedge oct@0)", W1, V)
# copies of 0 are {6,7}; wedge 6
W2, V, nx = wedge_mnf(W1, V, 6, 8)
report("W2 (wedge @6)", W2, V)
# copies of 6 are {8,9}; vertex 1 still original; wedge 1
W3, V, nx = wedge_mnf(W2, V, 1, 10)
report("W3 = J(oct)", W3, V)
print("W3 MNF:", [sorted(m) for m in W3])
print("W3 verts:", sorted(V))
