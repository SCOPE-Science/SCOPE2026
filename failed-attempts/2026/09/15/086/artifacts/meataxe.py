"""Exact-ish MeatAxe over C via numeric kernels + rational recovery over Q(i).
We work with matrices over complex; compute submodules via simultaneous kernel of (g - eig) using eigenvectors
of a generic element, then saturate under algebra action (spinning). Recurse to get composition factors.
Also compute generalized weight decomposition of X1,X2 (joint, commuting)."""
import numpy as np
from engine import principal_series_mats, Q

def rand_alg_element(M, rng):
    return (rng.standard_normal()+1j*rng.standard_normal())*M["T1"]+ \
           (rng.standard_normal()+1j*rng.standard_normal())*M["T2"]+ \
           (rng.standard_normal()+1j*rng.standard_normal())*M["X1"]+ \
           (rng.standard_normal()+1j*rng.standard_normal())*M["X2"]

def spin_submodule(gens, seed_vecs, tol=1e-8):
    n=gens[0].shape[0]
    B=np.array(seed_vecs, dtype=complex).T  # n x k
    # orthonormalize
    def col_space(B):
        if B.size==0: return np.zeros((n,0))
        U,s,Vh=np.linalg.svd(B,full_matrices=False)
        rk=int(np.sum(s>1e-9))
        return U[:,:rk]
    S=col_space(B)
    while True:
        cols=[S]+[g@S for g in gens]
        M=np.concatenate(cols,axis=1)
        S2=col_space(M)
        if S2.shape[1]==S.shape[1]:
            return S2
        S=S2
        if S.shape[1]==n: return S

def restrict(gens, basis):
    # basis n x d orthonormal; return d x d matrices of restrictions if invariant (least squares)
    R=[]
    for g in gens:
        R.append(np.linalg.lstsq(basis, g@basis, rcond=None)[0])
    return R

def quotient_action(gens, basis):
    # complete basis to full unitary, take lower-right block
    n,d=basis.shape
    Qb,_=np.linalg.qr(np.concatenate([basis, np.eye(n)],axis=1))
    # first d cols span same as basis? QR mixing: instead do full QR of [basis, rand]
    # Simpler: get complement via SVD null of basis^H
    U,s,Vh=np.linalg.svd(basis,full_matrices=True)
    # basis cols orthonormal => complement = U[:,d:]
    C=U[:,d:]
    R=[]
    for g in gens:
        # invariance: g*basis in span basis => quotient matrix C^H g C
        R.append(C.conj().T@g@C)
    return R, C

def is_invariant(gens, basis, tol=1e-6):
    n,d=basis.shape
    P=basis@basis.conj().T
    for g in gens:
        R=g@basis - P@(g@basis)
        if np.linalg.norm(R)>tol: return False
    return True

def find_proper_submodule(gens, rng, tol=1e-6, trials=40):
    n=gens[0].shape[0]
    for _ in range(trials):
        a=rand_alg_element({"T1":gens[0],"T2":gens[1],"X1":gens[2],"X2":gens[3]}, rng)
        w,V=np.linalg.eig(a)
        # cluster eigenvalues
        for j in range(n):
            # eigenspace approx: vectors with |w-wj| small
            idx=[k for k in range(n) if abs(w[k]-w[j])<1e-4]
            S=spin_submodule(gens,[V[:,k] for k in idx])
            d=S.shape[1]
            if 0<d<n:
                return S
        # also try kernels of (g - lambda) for each generator's eigenvalues
        for g in gens:
            w,V=np.linalg.eig(g)
            for j in range(n):
                idx=[k for k in range(n) if abs(w[k]-w[j])<1e-6]
                S=spin_submodule(gens,[V[:,k] for k in idx])
                d=S.shape[1]
                if 0<d<n:
                    return S
    return None

def composition_series(gens, rng, depth=0):
    n=gens[0].shape[0]
    if n==0: return []
    S=find_proper_submodule(gens,rng)
    if S is None:
        return [(n, gens)]  # simple factor dims
    d=S.shape[1]
    subR=restrict(gens,S)
    quoR,C=quotient_action(gens,S)
    return composition_series(subR,rng,depth+1)+composition_series(quoR,rng,depth+1)

def comp_factors_dims(t, seed=0):
    M=principal_series_mats(t)
    gens=[M["T1"],M["T2"],M["X1"],M["X2"]]
    rng=np.random.default_rng(seed)
    facs=composition_series(gens,rng)
    dims=sorted([f[0] for f in facs])
    return dims, facs

def gen_weight_spaces(t, tol=1e-5):
    """Joint generalized eigenspaces of commuting X1,X2: cluster by rounded eigenvalues after triangularization? Use recursive split."""
    M=principal_series_mats(t)
    X1,X2=M["X1"],M["X2"]
    n=12
    # simultaneous triangularization: use generic combo eigvecs
    rng=np.random.default_rng(1)
    C=rng.standard_normal()+1j*rng.standard_normal()
    A=X1+C*X2
    w,V=np.linalg.eig(A)
    # each eigenvector gives weight (x1,x2) = Rayleigh quotients
    weights=[]
    for k in range(n):
        v=V[:,k]
        x1=(v.conj()@X1@v)/(v.conj()@v)
        x2=(v.conj()@X2@v)/(v.conj()@v)
        weights.append((x1,x2))
    return weights

if __name__=="__main__":
    import sys
    tests=[(2.0+0j,3.0+0j),(1j,1.0),(1.0,1j),(1.0,-1.0),(1.0,1.0),(-1.0,-1.0),(1j,1j),(-1.0,1.0),(1.0,0.5),(0.5,1.0)]
    for t in tests:
        try:
            dims,facs=comp_factors_dims(t,seed=0)
            print("t=",t,"factors=",dims,"sum=",sum(dims))
        except Exception as e:
            print("t=",t,"ERR",e)
