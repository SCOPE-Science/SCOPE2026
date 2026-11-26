"""Reproduce spectral-rank and antipodal-survival checks for Möbius ladders."""
import math
import numpy as np
from numpy.linalg import eigh


def adjacency(n):
    assert n>=3
    N=2*n
    a=np.zeros((N,N),dtype=np.int64)
    for i in range(N):
        for j in ((i+1)%N, (i-1)%N, (i+n)%N):
            a[i,j]=1
    assert np.array_equal(a,a.T)
    assert np.all(np.sum(a,axis=1)==3)
    return a


def formula(n):
    if n%6==3: return 2/n
    if n%4==2: return 4/(3*n)
    return 0.0


def spectral(n):
    a=adjacency(n)
    es,u=eigh(a.astype(float))
    N=2*n
    S=0.0
    rank=0
    groups=0
    for i,x in enumerate(es):
        if i and abs(x-es[i-1])<1e-7: continue
        which=np.flatnonzero(abs(es-x)<1e-7)
        p0=u[0,which]
        pn=u[n,which]
        rank+=1
        S+=float(np.dot(pn,pn)-(np.dot(p0,pn)**2)/np.dot(p0,p0))
        groups+=1
    return S,rank


def exact_rank(n):
    import sympy as sp
    a=sp.Matrix(adjacency(n).tolist())
    v=sp.eye(2*n)[:,0]
    cols=[]
    for j in range(2*n):
        cols.append(v)
        v=a*v
    return sp.Matrix.hstack(*cols).rank()


if __name__=='__main__':
    for n in range(3,81):
        s,r=spectral(n)
        expected_rank=n if n%6==3 or n%4==2 else n+1
        assert r==expected_rank,(n,r,expected_rank)
        assert abs(s-formula(n))<1e-9,(n,s,formula(n))
    print('78 floating spectral rank and survival checks: PASS')
    for n in range(3,11):
        r=exact_rank(n)
        expected_rank=n if n%6==3 or n%4==2 else n+1
        assert r==expected_rank,(n,r,expected_rank)
    print('8 exact integer Krylov rank checks: PASS')
    # Verify decay of all bright modes at two distinct trap strengths.
    from numpy.linalg import eigvals
    for n in (3,4,6,9,10):
        a=adjacency(n).astype(complex)
        s=formula(n)
        for gamma in (0.3,1.7):
            k=a.copy();k[0,0]-=1j*gamma
            z=eigvals(k)
            q=sum(abs(w.imag)<1e-8 for w in z)
            # There are N-r dark eigenvalues; all other modes decay.
            r=n if n%6==3 or n%4==2 else n+1
            assert q==2*n-r,(n,gamma,q,2*n-r)
    print('10 independent dissipative-spectrum checks: PASS')
