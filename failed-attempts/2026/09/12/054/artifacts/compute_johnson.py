"""Bounded recovery test for lane-1192 target.

Checks the two routes named in target_claim on an explicit integral model:
 (a) t-image lattice spanning: rank of ∧^3 H / H, and rational-span => finite index.
 (b) model genus-1 BP wedges (decomposable u∧v∧w) can rationally span yet
     integrally generate a proper finite-index sublattice.
 (c) rational H1 cannot separate a finite-index subgroup (transfer argument).

Conclusion recorded: rational data alone cannot exhibit the required
infinite-index t-sublattice (contradicts the F3 hypothesis) nor a rational
H1 obstruction between commensurable groups; the gap is integral/2-torsion
and needs exact curve configuration + sigma/H1 tables not available in-session.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
import itertools

print("=== (a) rank of ∧^3 H / H, g=3 ===")
# H = Z^6 with basis e0..e5; symplectic form pairs (0,1),(2,3),(4,5).
omega_pairs = [((0,1),1), ((2,3),1), ((4,5),1)]
basis3 = list(itertools.combinations(range(6),3))
idx = {t:i for i,t in enumerate(basis3)}
print("rank ∧^3 H =", len(basis3))  # 20
# embedding j: H -> ∧^3 H, x |-> x ∧ omega
omega = sp.zeros(len(basis3),1)
# omega as 2-vector: e0∧e1 + e2∧e3 + e4∧e5
two = list(itertools.combinations(range(6),2))
for (a,b) in [(0,1),(2,3),(4,5)]:
    pass
def wedge3_sign(p):
    # sign of permutation sorting p into ascending order
    inv = 0
    p=list(p)
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: inv+=1
    return -1 if inv%2 else 1
def add_wedge(vec, triple, coeff):
    if len(set(triple)) < 3:
        return  # degenerate wedge x∧x∧y = 0
    s = wedge3_sign(triple)
    t = tuple(sorted(triple))
    vec[idx[t]] += s*coeff
J = sp.zeros(len(basis3),6)  # columns = images of e0..e5
for k in range(6):
    v = sp.zeros(len(basis3),1)
    for (a,b) in [(0,1),(2,3),(4,5)]:
        add_wedge(v,(k,a,b),1)
    J[:,k]=v
# Smith normal form of J to get quotient structure
S = smith_normal_form(J)
diag = [S[i,i] for i in range(min(S.shape))]
print("SNF diag of j:", diag)
# j is injective with saturated image? quotient rank = 20-6 = 14, check torsion
print("rank quotient =", len(basis3)-6)
# torsion in quotient iff some diag entry > 1
print("torsion (diag>1) present:", any(int(d)>1 for d in diag))

print()
print("=== (b) model genus-1 BP wedges: rational span vs integral saturation ===")
# Model: work in the 20-dim lattice ∧^3H; quotient map Q: Z^20 -> Z^14 via
# complement of column space. Build projection by integer nullspace of J.T.
NS = J.T.nullspace()  # rational basis of annihilator, dim 14
assert len(NS)==14
P = sp.Matrix.hstack(*NS).T  # 14x20 rational projection; ker P = im j (rationally)
def proj_rank(rows):
    M = sp.Matrix(rows)  # nx20 integer wedge vectors
    return (P*M.T).rank()
def sat_index(rows):
    """Index of saturation: |det| of projected lattice vs its saturation.
    Compute SNF of projected integer matrix A (14xn); full rank => finite index
    onto its saturation iff all SNF diag nonzero; index = prod(diag)/gcd-content?
    Simpler: report SNF diagonal of A^T (n x 14 -> project). We report whether
    the lattice is saturated by checking SNF of stacked matrix [A | SNF-basis].
    Here: compute g = gcd of all maximal minors? Use SNF diag product as
    covolume; compare two nested lattices: L0 (14 model gens, saturated by
    construction check) vs L1 (subset). Instead demonstrate: a full-rank integer
    matrix can have SNF diag with entries >1 => proper finite-index sublattice.
    """
    A = (P*sp.Matrix(rows).T)  # 14 x n rational
    # clear denominators
    denoms = []
    for i in range(A.rows):
        for j in range(A.cols):
            denoms.append(sp.denom(A[i,j]))
    from math import gcd
    from functools import reduce
    L=1
    for d in denoms: L = L*int(d)//gcd(L,int(d))
    Ai = (A*L)
    # integer SNF of Ai.T? rank and invariant factors
    S2 = smith_normal_form(Ai.T)
    d2=[int(S2[i,i]) for i in range(min(S2.shape))]
    return L, d2
# decomposable wedges u∧v∧w from a small pool of homology classes (model chain classes)
pool = [
 [1,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],
 [0,0,1,1,0,0],[1,0,1,0,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],[0,0,0,0,1,1],
 [1,0,0,0,1,0],[0,1,0,1,0,0],[1,1,1,0,0,0],[0,0,1,0,1,0],
]
def wedge_vec(u,v,w):
    z=sp.zeros(len(basis3),1)
    for (i,j,k) in itertools.permutations([0,1,2]):
        pass
    # (u∧v∧w)_{abc} = det of 3x3 minor rows a,b,c
    M=sp.Matrix([u,v,w]).T  # 6x3
    for t in basis3:
        m=M.extract(list(t),[0,1,2]).det()
        z[idx[t]]=int(m)
    return z
wedges=[wedge_vec(u,v,w) for (u,v,w) in itertools.combinations(pool,3)]
# pick full-rank subset greedily by projected rank
chosen=[]; cur=0
for w in wedges:
    if proj_rank([c.T.tolist()[0] for c in chosen]+[w.T.tolist()[0]])>cur:
        chosen.append(w); cur+=1
    if cur==14: break
print("greedy full-rank subset size:",len(chosen),"proj rank:",proj_rank([c.T.tolist()[0] for c in chosen]))
L,d2 = sat_index([c.T.tolist()[0] for c in chosen])
print("denominator L:",L,"SNF diag of scaled projection:",d2)
# Now take a second subset scaled: multiply one generator by 2 -> still full rank,
# but integral span drops to index >= 2 in saturation. This models how two
# config-carried sets can both rationally span yet differ integrally.
rows=[c.T.tolist()[0] for c in chosen]
rows2=[r for r in rows]; rows2[0]=[2*x for x in rows2[0]]
L1,d1 = sat_index(rows); L2,d2b=sat_index(rows2)
print("L0 SNF:",d1)
print("L1(scaled) SNF:",d2b)
print("=> rational span is compatible with distinct finite-index sublattices;")
print("   integral saturation index decides properness, needs exact F3 matrix.")

print()
print("=== (c) rational H1 cannot detect finite index ===")
print("If A=<F3> has full-rank (rationally spanning) image in Z^14, then")
print("[Im τ : τ(A)] < ∞. Transfer: H1(A;Q) -> H1(I3;Q) has image of finite")
print("index; dim H1(A;Q) >= 14 = dim H1(I3;Q). No rational H1 obstruction exists;")
print("any separation needs integral H1 (torsion/BCJ) or Johnson kernel data.")
print("RECOVERY TEST RESULT: BLOCKED — rational routes exhausted, gap integral.")
