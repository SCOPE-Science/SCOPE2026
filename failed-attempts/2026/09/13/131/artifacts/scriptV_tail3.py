"""Script V: diagnose tail: gradient threshold too weak because smin(Df)=0.148 is the
STABLE direction (contraction). The right splitting: decompose j into stable/unstable
parts. For j with large UNSTABLE component, gradient k-Df^T j: Df^T EXPANDS unstable
covectors (Df^{-T} contracts them): |Df^T j_u| >= lambda_w|j_u| ~ 1.13|j_u| (certified)
-- still weakish. For j with large STABLE component: Df^T CONTRACTS stable covectors
(|Df^T j_s| <= 0.221|j_s|) -- gradient k-Df^T j need not be large at all: RESONANCE
j_s = Df^T... this is exactly why anisotropic spaces are needed and why naive Fourier
Galerkin CANNOT certify the gap: near-resonant stable modes decay slowly.
Correct certificate route: anisotropic Banach space (Gouzel-Liverani) where the tail
is controlled by the LY inequality, not by Fourier decay. Quantify the obstruction:
find explicit (j,k) pairs with small gradient (near-resonances) -- these are the modes
a correct proof must handle via the stable foliation, and they explain Script V failure."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
w,P=np.linalg.eigh(Amat)
es=P[:,0]
# Df(0,0)=A: gradient at origin g = k - A j (A symmetric). Near-resonance: k = round(A j) defect.
best=[]
for j1 in range(-6,7):
    for j2 in range(-6,7):
        for j3 in range(-6,7):
            if max(abs(j1),abs(j2),abs(j3))>6 or (j1==0 and j2==0 and j3==0): continue
            Aj=Amat@np.array([j1,j2,j3])
            k=np.round(Aj).astype(int)
            if max(abs(k))>6: continue
            defect=np.linalg.norm(Aj-k)
            best.append((defect,tuple([j1,j2,j3]),tuple(k)))
best.sort()
print("top near-resonances (j -> k=round(Aj), defect):")
for d,j,k in best[:12]: print(f"  j={j} Aj={np.round(Amat@np.array(j),3)} k={k} defect={d:.4f}")
print("stable eigvec es =",np.round(es,4),"(modes along es are contracted by Df^T: gradient stays small)")
