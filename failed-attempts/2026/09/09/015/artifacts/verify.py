"""Certify STAB(C5) facet description. Exact rationals, stdlib only."""
from fractions import Fraction
import itertools

n = 5
edges = [(i, (i+1) % 5) for i in range(5)]
stables = []
for mask in range(1 << n):
    S = [i for i in range(n) if mask >> i & 1]
    if all(not (u in S and v in S) for u, v in edges):
        stables.append(tuple(1 if i in S else 0 for i in range(n)))
assert len(stables) == 11
ST = [[Fraction(v) for v in s] for s in stables]

# Proposed facets: (a, b): a.x <= b
facets = []
for i in range(5):
    a = [0]*5; a[i] = -1
    facets.append((f"x{i}>=0", a, 0))
for i in range(5):
    a = [0]*5; a[i] = 1; a[(i+1) % 5] = 1
    facets.append((f"edge{i}{(i+1)%5}", a, 1))
facets.append(("odd-hole", [1]*5, 2))

def dot(a, x): return sum(Fraction(a[j])*x[j] for j in range(5))

# 1. validity over stable sets + over conv (LP check on vertices suffices)
for name, a, b in facets:
    assert all(dot(a, x) <= b for x in ST), name
print("validity: OK (11 stable sets satisfy all 11 constraints)")

# 2. facet dimension: 5 affinely independent tight vertices each
def aff_rank(pts):
    # affine rank = rank of differences; gaussian elim
    d = [ [pts[i][j]-pts[0][j] for j in range(5)] for i in range(1, len(pts))]
    r = 0
    M = [row[:] for row in d]
    for c in range(5):
        piv = next((rr for rr in range(r, len(M)) if M[rr][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for rr in range(len(M)):
            if rr != r and M[rr][c] != 0:
                f = M[rr][c]/M[r][c]
                for k in range(c, 5): M[rr][k] -= f*M[r][k]
        r += 1
    return r
for name, a, b in facets:
    T = [x for x in ST if dot(a, x) == b]
    assert aff_rank(T) == 4, (name, len(T))
    print(f"facet-dim {name}: OK tight={len(T)} affrank=4")

# 3. completeness: every vertex of Q is integral stable set (Qverts enumerated in qverts.py: 11 verts, all 0/1)
# re-verify: Q verts file check + check no other basic point feasible (redo quick)
cons = [ (f[1], f[2]) for f in facets ]
def solve5(rows, rhs):
    M = [[Fraction(rows[i][j]) for j in range(5)]+[Fraction(rhs[i])] for i in range(5)]
    for col in range(5):
        piv = next((r for r in range(col,5) if M[r][col]!=0), None)
        if piv is None: return None
        M[col],M[piv]=M[piv],M[col]
        for r in range(5):
            if r!=col and M[r][col]!=0:
                f=M[r][col]/M[col][col]
                for k in range(col,6): M[r][k]-=f*M[col][k]
    return [M[i][5]/M[i][i] for i in range(5)]
pts=set()
for combo in itertools.combinations(range(11),5):
    x=solve5([cons[k][0] for k in combo],[cons[k][1] for k in combo])
    if x is None: continue
    if all(dot(cons[k][0],x)<=cons[k][1] for k in range(11)): pts.add(tuple(x))
assert len(pts)==11 and all(all(v in (0,1) for v in p) for p in pts)
print("completeness: Q has exactly 11 vertices, all integral stable sets -> H-desc = STAB(C5)")

# 4. irredundancy witnesses
W = {
 "odd-hole": [Fraction(1,2)]*5,
 "edge01": [Fraction(1),Fraction(1),Fraction(0),Fraction(0),Fraction(0)],
 "edge12": [Fraction(0),Fraction(1),Fraction(1),Fraction(0),Fraction(0)],
 "edge23": [Fraction(0),Fraction(0),Fraction(1),Fraction(1),Fraction(0)],
 "edge34": [Fraction(0),Fraction(0),Fraction(0),Fraction(1),Fraction(1)],
 "edge40": [Fraction(1),Fraction(0),Fraction(0),Fraction(0),Fraction(1)],
 "x0>=0": [Fraction(-1,2),Fraction(1),Fraction(0),Fraction(0),Fraction(0)],
 "x1>=0": [Fraction(0),Fraction(-1,2),Fraction(1),Fraction(0),Fraction(0)],
 "x2>=0": [Fraction(0),Fraction(0),Fraction(-1,2),Fraction(1),Fraction(0)],
 "x3>=0": [Fraction(0),Fraction(0),Fraction(0),Fraction(-1,2),Fraction(1)],
 "x4>=0": [Fraction(1),Fraction(0),Fraction(0),Fraction(0),Fraction(-1,2)],
}
names = [f[0] for f in facets]
for i,(name,a,b) in enumerate(facets):
    w = W[name]
    assert dot(a,w) > b, name
    assert all(dot(facets[j][1],w) <= facets[j][2] for j in range(11) if j != i), name
print("irredundancy: OK (11 witnesses, each violates exactly its facet)")

# 5. gap: max 1.x over edge-relaxation = 5/2 at (1/2)^5 vs alpha=2
half=[Fraction(1,2)]*5
assert sum(half)==Fraction(5,2)
assert max(sum(s) for s in stables)==2
viol = sum(half)-2
print(f"gap: LP=5/2 INT=2 abs_gap=1/2 rel=5/4 odd-hole_violation={viol}")
print("VERIFY_OK")
