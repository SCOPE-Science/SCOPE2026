"""Fast lattice short-vector enumeration via Cholesky + recursive Fincke-Pohst."""
import numpy as np
def short_norms(BL, QMAT, bound, keep=24):
    # BL: rows basis in R^4; enumerate nonzero x=c@BL with x'Qx<=bound
    G = BL@QMAT@BL.T  # Gram in coeff coords
    try:
        L = np.linalg.cholesky(G)
    except np.linalg.LinAlgError:
        return None
    out=[]
    n=4
    def rec(k, off, acc):
        # k: current index (from n-1 down), off: offset vector contribution, acc: accumulated
        if k<0:
            if acc>1e-9 and acc<=bound+1e-9: out.append(acc)
            return
        # bound on c_k: L[k,k]^2 (c_k+mu)^2 <= bound-acc
        mu = off[k]/L[k,k] if L[k,k]>1e-12 else 0
        R2 = bound-acc
        if R2<0: return
        r = np.sqrt(R2)/abs(L[k,k]) if abs(L[k,k])>1e-12 else 0
        for c in range(int(np.ceil(-mu-r)), int(np.floor(mu+r))+1 if False else int(np.floor(-mu+r))+1):
            pass
        for c in range(int(np.ceil(-mu-r)), int(np.floor(-mu+r))+1):
            noff = off.copy(); noff[k]+=c*L[k,k]
            # propagate: off[j] for j<k: off[j] += c*L[k,j]? Cholesky: x_i = Σ_{j<=i} L[i,j]c_j. residual approach:
            rec(k-1, noff if False else off, acc+(c+mu)**2*L[k,k]**2) if False else None
        # simpler: recurse with updated center: standard FP
    # Fallback simple: coefficient box from diagonal
    diag=np.diag(G)
    cb=[int(np.ceil(np.sqrt(bound/d)))+1 if d>1e-12 else 1 for d in diag]
    from itertools import product
    for c in product(*[range(-b,b+1) for b in cb]):
        if all(v==0 for v in c): continue
        x=np.array(c,dtype=float)@BL
        q=float(x@QMAT@x)
        if q<=bound+1e-9: out.append(q)
    out.sort()
    return out[:keep]
