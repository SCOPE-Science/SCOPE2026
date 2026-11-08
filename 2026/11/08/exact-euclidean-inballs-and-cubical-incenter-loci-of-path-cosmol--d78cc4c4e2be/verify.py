"""Reproducibility checks for intrinsic inballs of path cosmological polytopes.

Run: python3 verify.py
Requires NumPy and SciPy. Finite computations are not an all-dimensional proof.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog


def data(n):
    assert n >= 4
    D = 2*n-1
    def normal(a,b):
        v = np.zeros(D)
        v[a-1:b] = 1
        if a > 1: v[n+a-2] = 1
        if b < n: v[n+b-1] = 1
        return v
    I = [(a,b) for a in range(1,n+1) for b in range(a,n+1)]
    U = np.stack([normal(a,b) for a,b in I])
    cc = np.sqrt(np.sum(U,axis=1)*(D-np.sum(U,axis=1))/D)
    c = lambda q: math.sqrt(q*(D-q)/D)
    r = 2/(2*c(2)+2*c(3)+(n-3)*c(4))
    x=np.zeros(n)
    y=np.zeros(n-1)
    x[0]=x[-1]=r*c(2)/2
    x[1]=x[-2]=r*(c(4)-c(2))/2
    if n>4: x[2:-2]=r*(c(4)-c(3))
    y[0]=y[-1]=r*c(2)/2
    y[1:-1]=r*(c(3)-c(4)/2)
    return I,U,cc,r,np.r_[x,y],r*(2*c(4)-c(3)-c(5))


def vertices(n):
    D=2*n-1
    out=[]
    for i in range(n-1):
        for sx,sy,sz in [(1,1,-1),(1,-1,1),(-1,1,1)]:
            v=np.zeros(D)
            v[i]=sx;v[i+1]=sy;v[n+i]=sz
            out.append(v)
    return np.array(out)


count_lp=0
count_corners=0
count_facets=0
for n in range(4,16):
    I,U,c,r,center,k=data(n)
    assert k>0
    assert abs(sum(center)-1)<1e-10
    assert np.min(U@center-r*c)>-1e-10
    F=[(1,1),(n,n)]+[(i,i+1) for i in range(1,n)]
    selected=np.stack([U[I.index(t)] for t in F])
    assert np.all(selected.sum(axis=0)==2), (n,selected.sum(axis=0))
    for mask in itertools.product([0,1],repeat=n-4) if n<=10 else [[0]*(n-4),[1]*(n-4)]:
        sigma=np.zeros(n+2)
        for i,bit in enumerate(mask,start=3):sigma[i]=bit*k
        z=center.copy()
        for i in range(1,n+1):z[i-1]-=(sigma[i-1]+sigma[i+1])/2
        for i in range(1,n):z[n+i-1]+=(sigma[i]+sigma[i+1])/2
        assert abs(sum(z)-1)<1e-9
        assert np.min(U@z-r*c)>-1e-9,(n,np.min(U@z-r*c))
        count_corners+=1
    if n<=11:
        # Eliminate last coordinate via the sum-one equation; norm of each projected normal
        # is used to formulate the exact intrinsic Chebyshev LP.
        cvec=np.zeros(2*n-1)
        cvec[-1]=-1
        A=np.c_[ -U[:,:-1]+U[:,-1,None], c]
        b=U[:,-1]
        res=linprog(cvec,A_ub=A,b_ub=b,A_eq=None,bounds=[(None,None)]*(2*n-2)+[(0,None)],method='highs')
        assert res.success, (n,res.message)
        assert abs(res.x[-1]-r)<1e-8, (n,res.x[-1],r)
        count_lp+=1
    if n<=8:
        V=vertices(n)
        assert np.linalg.matrix_rank(V[1:]-V[:1])==2*n-2
        assert np.min(U@V.T)>=-1e-12
        for a,b in I:
            h=U[I.index((a,b))]
            Z=V[np.abs(V@h)<1e-12]
            assert np.linalg.matrix_rank(Z[1:]-Z[:1])==2*n-3,(n,a,b)
            count_facets+=1
print('PATH_COSMOLOGICAL_INBALL_VERIFICATION_PASSED',count_lp,count_corners,count_facets)
