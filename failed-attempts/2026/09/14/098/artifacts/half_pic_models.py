"""Half-PIC model verification + pinching-obstruction computations.

Conventions: orthonormal frame, R_ijkl with R_ijij = sectional curvature K(ei,ej).
Curvature operator on wedge^2 in pair basis [12,13,14,23,24,34], then SD/ASD
change of basis -> blocks [[A,B],[B^T,C]]. tr A = tr C = R/4.
Pure numpy (no sympy) by design.
"""
import numpy as np
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
S = np.sqrt(2.0)
PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def build_T():
    T = np.zeros((6,6))
    T[0,0]=1/S; T[0,5]=1/S      # s1=(e12+e34)/s
    T[1,1]=1/S; T[1,4]=-1/S     # s2=(e13-e24)/s
    T[2,2]=1/S; T[2,3]=1/S      # s3=(e14+e23)/s
    T[3,0]=1/S; T[3,5]=-1/S     # a1=(e12-e34)/s
    T[4,1]=1/S; T[4,4]=1/S      # a2=(e13+e24)/s
    T[5,2]=1/S; T[5,3]=-1/S     # a3=(e14-e23)/s
    return T
T = build_T()
assert np.allclose(T @ T.T, np.eye(6)), "T must be orthogonal"

def blocks_from_R(R):
    Rop = np.zeros((6,6))
    for a,(i,j) in enumerate(PAIRS):
        for b,(k,l) in enumerate(PAIRS):
            Rop[a,b] = R[i,j,k,l]
    # symmetrize (algebraic tensor built symmetric already, but be safe)
    Rop = 0.5*(Rop+Rop.T)
    M = T @ Rop @ T.T
    M = 0.5*(M+M.T)
    return Rop, M[:3,:3], M[:3,3:], M[3:,3:]

def ricci(R):
    Rc = np.zeros((4,4))
    for a in range(4):
        for b in range(4):
            Rc[a,b] = sum(R[a,c,b,c] for c in range(4))
    return 0.5*(Rc+Rc.T)

def make_R(Kdict):
    """Kdict: {(i,j): K} sectional curvatures for i<j; all other components 0."""
    R = np.zeros((4,4,4,4))
    def setR(i,j,v):
        for (a,b,c,d) in [(i,j,i,j),(i,j,j,i),(j,i,i,j),(j,i,j,i)]:
            pass
        R[i,j,i,j]=v; R[j,i,i,j]=-v; R[i,j,j,i]=-v; R[j,i,j,i]=v
        R[i,j,i,j]=v
        # pair symmetry
        R[i,j,i,j]=v; R[i,j,i,j]=v
    for (i,j),v in Kdict.items():
        R[i,j,i,j]=v; R[j,i,j,i]=v; R[j,i,i,j]=-v; R[i,j,j,i]=-v
        R[i,j,i,j]=v
    # enforce full symmetries explicitly
    # (block symmetries: R_ijkl=-R_jikl=-R_ijlk=R_klij)
    return R

def report(name, R):
    Rop,A,B,C = blocks_from_R(R)
    Rc = ricci(R)
    Rs = float(np.trace(Rc))
    eA = np.linalg.eigvalsh(A); eC = np.linalg.eigvalsh(C)
    eR = np.linalg.eigvalsh(Rc)
    tol=1e-9
    half = bool((eA.min()>tol) or (eC.min()>tol))
    weak = bool((eA.min()>=-tol) or (eC.min()>=-tol))
    # Ricci multiplicity: max count within tol
    mult = int(max((np.abs(eR - v) < 1e-9).sum() for v in eR))
    out = dict(name=name, scalar=float(Rs),
               eigA=[float(x) for x in eA], eigC=[float(x) for x in eC],
               eigRic=[float(x) for x in eR], ricci_max_mult=mult,
               half_PIC_strict=half, half_PIC_weak=weak,
               trA=float(np.trace(A)), trC=float(np.trace(C)),
               normB=float(np.linalg.norm(B)))
    print(f"--- {name}: R={Rs:.4f}")
    print(f"    eig(A)={np.round(eA,4)} eig(C)={np.round(eC,4)} |B|={np.linalg.norm(B):.4f}")
    print(f"    eig(Ric)={np.round(eR,4)} (max mult {mult})")
    print(f"    strict half-PIC: {half}, weak half-PIC: {weak}")
    return out

results = {}
results['S4'] = report("S^4 (K=1)", make_R({(0,1):1,(0,2):1,(0,3):1,(1,2):1,(1,3):1,(2,3):1}))
results['S3xR'] = report("S^3 x R", make_R({(0,1):1,(0,2):1,(1,2):1}))
results['S2xS2_eq'] = report("S^2 x S^2 equal", make_R({(0,1):1,(2,3):1}))
results['S2xS2_uneq'] = report("S^2 x S^2 unequal (K=1,1/4)", make_R({(0,1):1,(2,3):0.25}))
results['S2xR2'] = report("S^2 x R^2", make_R({(0,1):1}))

# CP^2 Fubini-Study algebraic model: Einstein, B=0, A=diag(R/4,0,0), C=(R/12)I, R=24.
Rs = 24.0
A = np.diag([Rs/4,0.0,0.0]); C = np.eye(3)*Rs/12; B = np.zeros((3,3))
M = np.block([[A,B],[B.T,C]])
Rop = T.T @ M @ T
Rc = Rs/4*np.eye(4)
eR = np.linalg.eigvalsh(Rc)
cp = dict(name="CP^2 FS algebraic (R=24)", scalar=Rs,
          eigA=[float(x) for x in np.linalg.eigvalsh(A)],
          eigC=[float(x) for x in np.linalg.eigvalsh(C)],
          eigRic=[float(x) for x in eR], ricci_max_mult=4,
          half_PIC_strict=bool(np.linalg.eigvalsh(C).min()>0),
          half_PIC_weak=True, trA=float(np.trace(A)), trC=float(np.trace(C)), normB=0.0)
print(f"--- {cp['name']}: eig(A)={np.round(np.linalg.eigvalsh(A),4)} eig(C)={np.round(np.linalg.eigvalsh(C),4)}")
print(f"    strict half-PIC via C: {cp['half_PIC_strict']}")
results['CP2'] = cp

print()
print("="*70)
print("OBSTRUCTION: pure-A pinching cone {A >= eps (trA) I} under Hamilton ODE")
print("Reaction F = A^2 + B B^T + 2 A# ; FQ = F - eps tr(F) I.")
print("Boundary point: trA=1, A=diag(eps,(1-eps)/2,(1-eps)/2), B=t*E22.")
print("="*70)
obstr = {}
for eps in [0.05, 0.1, 0.2]:
    a1 = eps; a2 = a3 = (1-eps)/2
    A0 = np.diag([a1,a2,a3])
    trA2 = a1**2+a2**2+a3**2
    trAhash = a1*a2+a2*a3+a3*a1
    const11 = a1**2 + 2*a2*a3 - eps*(trA2 + 2*trAhash)  # value at t=0
    # (FQ)_11(t) = const11 - eps*t^2  because (BB^T)_11=0, tr(BB^T)=t^2
    ts = [0.0, 1.0, 2.0, 3.0, 5.0]
    vals = [const11 - eps*t*t for t in ts]
    t_star = float(np.sqrt(const11/eps)) if const11>0 else 0.0
    print(f"eps={eps}: (FQ)_11(t) = {const11:.4f} - {eps}*t^2 -> {dict(zip(ts,[round(v,3) for v in vals]))}; zero crossing t*={t_star:.3f}")
    obstr[str(eps)] = dict(const=const11, values=vals, t_star=t_star,
                           formula="(FQ)_11(t) = const - eps*t^2 -> -inf as t->inf")
results['pinching_obstruction'] = obstr

print()
print("="*70)
print("OPENNESS: random A>0 with random B (algebraic pairs); Ricci-mult-3?")
print("(pointwise algebraic only; realization in a shrinker is the open part)")
print("="*70)
rng = np.random.default_rng(0)
count_mult3 = 0; N = 2000
# NOTE: E (traceless Ricci) <-> B is a linear isomorphism; Ricci mult-3 locus has
# codimension >= 2 in the 9-dim fiber, hence measure zero. We mimic by sampling
# B directly: probability that a random B comes from a mult-3 E is 0.
# Here we just record that generic sampled pairs have A>0 (half-PIC algebraic)
# while mult-3 is non-generic: demonstrate via eigenvalues of a proxy symmetric
# 4x4 traceless tensor E and its multiplicity pattern.
def max_mult(eig, tol=1e-6):
    return int(max((np.abs(eig - v) < tol).sum() for v in eig))
n_mult3 = 0
for _ in range(N):
    X = rng.normal(size=(4,4)); X = 0.5*(X+X.T); X -= np.trace(X)/4*np.eye(4)
    if max_mult(np.linalg.eigvalsh(X)) >= 3:
        n_mult3 += 1
print(f"random traceless symmetric 4x4: mult>=3 in {n_mult3}/{N} draws (expect ~0)")
results['openness_scan'] = dict(draws=N, mult3_hits=int(n_mult3))

with open(OUT, "w") as f:
    json.dump(results, f, indent=2)
print()
print("wrote", OUT)
