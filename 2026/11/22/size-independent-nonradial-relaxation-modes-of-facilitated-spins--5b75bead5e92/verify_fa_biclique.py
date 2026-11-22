"""Independent finite-state and Fourier-block checks for FA-1f biclique relaxation modes.
Run: python verify.py (requires numpy and scipy)."""
from math import comb
import numpy as np
from scipy.linalg import eigh

def small_operator(m,q):
    # A vacancy is 1, occupancy is 0; on functions -L has off-diagonal -rate.
    p=1-q
    N=1<<m
    D=np.zeros((N,N))
    for s in range(N):
        for i in range(m):
            rate=p if (s>>i)&1 else q
            D[s,s]+=rate
            D[s,s^(1<<i)]-=rate
    P=np.diag([int(s!=0) for s in range(N)])
    return D+P

def root(m,q):
    p=1-q
    w=np.array([comb(m,k)*p**(m-k)*q**k for k in range(m+1)])
    a,b=0.,1.-1e-14
    for _ in range(85):
        mid=(a+b)/2
        value=np.sum(w/(np.arange(1,m+2)-mid))
        if value>1: b=mid
        else: a=mid
    return (a+b)/2

def symmetrized(T,m,q):
    p=1-q
    wt=np.array([q**s.bit_count()*p**(m-s.bit_count()) for s in range(1<<m)])
    return (np.sqrt(wt)[:,None]*T)/np.sqrt(wt)[None,:]

def check(m,n,q):
    T=small_operator(m,q)
    S=symmetrized(T,m,q)
    assert np.linalg.norm(S-S.T,ord=np.inf)<1e-12
    eigen,U=eigh(S)
    idx=np.argmin(eigen)
    lam=float(eigen[idx]); lam2=root(m,q)
    assert abs(lam-lam2)<1e-10
    # eigenvector on functions: convert symmetric eigenvector using density.
    p=1-q
    wt=np.array([q**s.bit_count()*p**(m-s.bit_count()) for s in range(1<<m)])
    x=U[:,idx]/np.sqrt(wt)
    assert np.linalg.norm(T@x-lam*x,ord=np.inf)<1e-10
    # independent full generator on the nonempty-vacancy class.
    M=m+n; cap=(1<<M)-1
    F=np.zeros(cap)
    for s in range(1,cap+1):
        a=s&((1<<m)-1);b=s>>m
        F[s-1]=x[a]*((b&1)-((b>>1)&1))
    y=np.zeros_like(F)
    for s in range(1,cap+1):
        a=s&((1<<m)-1);b=s>>m
        for i in range(M):
            if (b if i<m else a)==0:continue
            t=s^(1<<i)
            assert t!=0 # facilitated flips never reach all occupied
            rate=(1-q) if (s>>i)&1 else q
            y[s-1]+=rate*(F[s-1]-F[t-1])
    residual=np.max(abs(y-lam*F))
    assert residual<2e-9, (m,n,q,residual)
    # the contrast is a nonstationary mode; verify zero mean under product weight
    pi=np.array([q**s.bit_count()*p**(M-s.bit_count()) for s in range(1,cap+1)])
    assert abs(np.dot(pi,F))<5e-11
    return lam,residual

if __name__=='__main__':
    total=0
    for q in (.1,.25,.5,.75,.9):
        for m,n in ((2,2),(2,3),(2,5),(3,3),(3,4),(4,4),(4,5)):
            lam,res=check(m,n,q)
            total+=1
            print(f'm={m} n={n} q={q:.2f} rate={lam:.12f} residual={res:.2e}')
    print('FA_BICLIQUE_MODE_CHECKS_PASSED',total)
