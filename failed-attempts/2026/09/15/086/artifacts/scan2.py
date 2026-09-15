import numpy as np, cmath
from meataxe import comp_factors_dims
# The (6,6) at 8th roots is suspicious: our numeric splitter may fail to split 6-dim factors (need harder trials).
# Retry those with more trials/seeds; also check (1,-1) -> simple? That contradicts "1,2,2" expectation.
# Note: "1,2,2 at t_{1,-1}" might mean weight-space dims, not composition factors. Check.

from engine import principal_series_mats
def jordan_weight_profile(t):
    M=principal_series_mats(t)
    X1,X2=M["X1"],M["X2"]
    rng=np.random.default_rng(0)
    # joint eigenvalues via Schur-ish: diagonalize generic combo, round
    C=0.37+0.23j
    A=X1+C*X2
    w,V=np.linalg.eig(A)
    # recover x1,x2 per vector
    prof=[]
    for k in range(12):
        v=V[:,k]
        x1=(v.conj()@X1@v)/(v.conj()@v); x2=(v.conj()@X2@v)/(v.conj()@v)
        prof.append((x1,x2))
    return prof

for t in [(1.0,-1.0),(1.0,1.0),(cmath.exp(2j*cmath.pi/8),1.0),(1j,1.0)]:
    M=principal_series_mats(t)
    print("t=",t)
    print("  X1 eig:", np.round(np.linalg.eigvals(M["X1"]),3))
    print("  X2 eig:", np.round(np.linalg.eigvals(M["X2"]),3))
    # ranks
    print("  rank X1-1:", np.linalg.matrix_rank(M["X1"]-np.eye(12),tol=1e-6), " rank X1+1:", np.linalg.matrix_rank(M["X1"]+np.eye(12),tol=1e-6))
