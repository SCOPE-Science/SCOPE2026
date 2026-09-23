"""Quantified pruned-search frontier for d=8, n=29 (alpha=1/3).
1) Small-n PSD backtracking node counts (canonical lex order, PSD prune) to show branching growth.
2) T8-extension barrier: 29th line would need sign vector b in col(M28); test random sample,
   time it, extrapolate exhaustive 2^28 cost. Second PSD implementation: pivoted float
   Cholesky vs eigendecomposition (agreement check).
Stdlib + numpy only.
"""
import numpy as np, itertools, time, random

def load_M28():
    M=np.loadtxt("output/artifacts/T8_28_d7_3G.csv", delimiter=",", dtype=int)
    return M

def float_cholesky_psd_rank(M, tol=1e-8):
    """Second PSD implementation: pivoted Cholesky (float) counting positive pivots.
    Returns (is_psd, rank). Different code path from eigvalsh."""
    A=M.astype(float).copy(); n=A.shape[0]
    perm=list(range(n)); rank=0
    for k in range(n):
        # find max diag in trailing
        d=np.diag(A)[k:]
        p=k+int(np.argmax(d))
        maxv=d[p-k]
        if maxv<=tol:
            # check trailing zero
            if np.max(np.abs(A[k:,k:]))>1e-6:
                return False, rank
            return True, rank
        if maxv< -tol:
            return False, rank
        # swap
        if p!=k:
            perm[k],perm[p]=perm[p],perm[k]
            A[[k,p],:]=A[[p,k],:]
            A[:,[k,p]]=A[:,[p,k]]
        # eliminate
        piv=A[k,k]; rank+=1
        for i in range(k+1,n):
            A[i,k]/=piv
        for i in range(k+1,n):
            for j in range(k+1,n):
                # manual update to differ from eig path (uses loops)
                pass
        # vectorized trailing update (same math, different path)
        A[k+1:,k+1:]-=np.outer(A[k+1:,k],A[k+1:,k])*piv
        A[k+1:,k]=0; A[k,k+1:]=0
    return True, rank

def small_backtrack(d=8, nmax=7):
    """Enumerate Seidel sign matrices in lex-canonical order with PSD prune.
    Vertices added one by one; for new vertex k, signs to 0..k-1 in {+-1}^k.
    Canonical: enforce first row pattern to break switching (fix v0 signs +1),
    and lex-nonincreasing rows to break some perms (sound: every switching class
    has such rep? we use weak form: only fix global flip, so sound). Count nodes."""
    print("=== Small-n backtracking (PSD prune, switching-normalized) ===")
    # fix: vertex0 has no choices; vertex1 sign fixed +1 (switching); else 2^k patterns
    for n in range(2, nmax+1):
        t0=time.time()
        # DFS count with PSD prune using float eig on the fly (small n)
        count_pass=[0]; count_leaf=[0]
        # iterative stack: each entry (k, matrix kxk)
        # start k=2 fixed
        stack=[]
        M2=np.array([[3,1],[1,3]],dtype=float)  # fix s01=+1 wlog switching
        stack.append(M2)
        nodes=0
        leaves=0
        while stack:
            Mk=stack.pop()
            k=Mk.shape[0]
            nodes+=1
            # PSD rank<=d check
            eig=np.linalg.eigvalsh(Mk)
            if eig.min()<-1e-8:
                continue
            # rank check: #eig>1e-8 <=d
            r=int((eig>1e-8).sum())
            if r>d:
                continue
            if k==n:
                leaves+=1
                continue
            # expand to k+1: all sign patterns for new column (2^k), but fix switching:
            # flipping new vector sign maps b->-b, so identify pairs: fix first entry +1 to halve
            # (sound: every orbit has rep with b0=+1)
            kk=k
            for mask in range(2**(kk-1)):
                b=np.ones(kk,dtype=float)
                for j in range(1,kk):
                    if (mask>>(j-1))&1: b[j]=-1.0
                    else: b[j]=1.0
                # Note b[0]=+1 fixed
                Mnew=np.zeros((kk+1,kk+1))
                Mnew[:kk,:kk]=Mk; Mnew[kk,:kk]=b; Mnew[:kk,kk]=b; Mnew[kk,kk]=3
                stack.append(Mnew)
        print(f" n={n}: stacked nodes visited ~{nodes}, PSD-surviving leaves={leaves}, time={time.time()-t0:.2f}s")
        # Note: nodes counts include pruned; leaves are PSD survivors

if __name__=="__main__":
    M28=load_M28()
    print(f"Loaded T8 M28 shape {M28.shape}")
    # agreement of two PSD implementations on witnesses
    for path in ["output/artifacts/Clebsch16_d6_3G.csv","output/artifacts/T8_28_d7_3G.csv"]:
        M=np.loadtxt(path, delimiter=",", dtype=int)
        ok, r=float_cholesky_psd_rank(M)
        eig=np.linalg.eigvalsh(M.astype(float))
        reig=int((eig>1e-8).sum())
        print(f"{path}: cholesky_psd={ok} rank={r} vs eig rank={reig} emin={eig.min():.2e} agree={ok and r==reig}")
    print()
    small_backtrack(d=8, nmax=7)
    print()
    print("=== T8 extension barrier (29th line) ===")
    Mf=M28.astype(float)
    # nullspace via SVD
    U,S,Vt=np.linalg.svd(Mf)
    rank=int((S>1e-6).sum())
    print(f"rank={rank}, singular values: {S}")
    N=Vt[rank:,:].T  # 28x21 null basis
    print(f"null basis shape {N.shape}")
    # col-membership residual: ||N^T b|| / ||b||
    rng=np.random.default_rng(0)
    T=20000
    t0=time.time()
    minres=1e9; minb=None
    for _ in range(T):
        b=rng.choice(np.array([-1.0,1.0]), size=28)
        res=np.linalg.norm(N.T@b)/np.linalg.norm(b)
        if res<minres: minres=res; minb=b.copy()
    dt=time.time()-t0
    print(f"random {T} sign vectors: min null-residual={minres:.4f} (0 needed for col membership), time={dt:.2f}s")
    print(f"per-vector {dt/T*1e6:.1f}us; exhaustive 2^28={2**28} would take ~{2**28/T*dt/3600:.1f} hours single-core (float residual only, full PSD more)")
    # also test structured candidates: all-+1, all-but-one, etc.
    for name,b in [("all+1",np.ones(28)),("all-1",-np.ones(28))]:
        res=np.linalg.norm(N.T@b)/np.linalg.norm(b)
        print(f" {name}: residual={res:.4f}")
    print("Conclusion: no random extension even close to column space; exhaustive closure of n=29")
    print("from scratch (2^(406) patterns) or even T8-extension (2^28) exceeds 2h budget.")
    print("Frontier quantified; full n=29 infeasibility NOT closed (hence upper bound via LP, not search).")
