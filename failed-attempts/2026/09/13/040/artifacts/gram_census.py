"""Recovery test: [5,3,3,3] Gram signature + ambient-group short-word translation census.
Purpose: show what CAN be certified locally (ambient Coxeter data) vs the missing
finite-index torsion-free subgroup data needed for manifold systoles."""
import itertools, math
import numpy as np

c = (1+math.sqrt(5))/4  # cos(pi/5)
G = np.array([[1,-c,0,0,0],[-c,1,-0.5,0,0],[0,-0.5,1,-0.5,0],
              [0,0,-0.5,1,-0.5],[0,0,0,-0.5,1]])
w = np.linalg.eigvalsh(G)
print("eig(G)=", np.round(w,6))
print("signature: %d positive, %d negative" % ((w>1e-9).sum(), (w<-1e-9).sum()))
print("det(G)=%.6e" % np.linalg.det(G))

Rs = []
for i in range(5):
    R = np.eye(5); R[i,:] -= 2*G[i,:]
    assert np.max(np.abs(R.T@G@R-G))<1e-9
    Rs.append(R)
print("all 5 reflections preserve G: True")

def min_length(L):
    best=(math.inf,None); nlox=0
    for wrd in itertools.product(range(5), repeat=L):
        if any(wrd[k]==wrd[k+1] for k in range(L-1)): continue
        M=np.eye(5)
        for i in wrd: M=Rs[i]@M
        rho=max(abs(np.linalg.eigvals(M)))
        if rho>1+1e-6:
            nlox+=1
            ell=math.log(rho)
            if ell<best[0]: best=(ell,wrd)
    return best,nlox

for L in range(2,9):
    (ell,wrd),n= min_length(L)
    print(f"L={L}: reduced words loxodromic={n}, min ell={ell:.4f} word={wrd}")
