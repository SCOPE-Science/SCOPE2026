#!/usr/bin/env python3
"""Independent finite checks of mutual-inverse adjacency inertia for isotone maps."""
from itertools import combinations, combinations_with_replacement
from math import comb
from fractions import Fraction
import sympy as sp
import numpy as np

def op(x,y):
    return tuple(y[x[i]] for i in range(len(x)))

def inv(x,y):
    return op(op(x,y),x)==x and op(op(y,x),y)==y

def rank(x):return len(set(x))

def data(n,r):
    maps=[x for x in combinations_with_replacement(range(n),n) if rank(x)==r]
    cuts=list(combinations(range(1,n),r-1))
    img=list(combinations(range(n),r))
    ker=[]
    for cc in cuts:
        intervals=[tuple(range(a,b)) for a,b in zip((0,)+cc,cc+(n,))]
        ker.append(intervals)
    R=np.array([[int(all(b in block for b,block in zip(B,A))) for B in img] for A in ker],dtype=np.int64)
    assert len(maps)==len(cuts)*len(img)
    key=lambda x: (tuple(i+1 for i in range(n-1) if x[i]!=x[i+1]),tuple(sorted(set(x))))
    idx={(c,B):i for i,(c,B) in enumerate((c,b) for c in cuts for b in img)}
    assert len(idx)==len(maps)
    A=np.zeros((len(maps),len(maps)),dtype=np.int64)
    for i,x in enumerate(maps):
        for j,y in enumerate(maps):
            A[i,j]=int(inv(x,y))
    # index maps via (kernel cut positions, image)
    ordering=[idx[key(x)] for x in maps]
    # create prediction without invoking semigroup multiplication
    C=np.zeros_like(A)
    for i,x in enumerate(maps):
        ci,bi=key(x); ai=cuts.index(ci); ji=img.index(bi)
        for j,y in enumerate(maps):
            cj,bj=key(y); aj=cuts.index(cj); jj=img.index(bj)
            C[i,j]=R[ai,jj]*R[aj,ji]
    assert np.array_equal(C,A),f'inverse condition mismatch n={n},r={r}'
    assert np.array_equal(A,A.T)
    sig=np.linalg.svd(R,compute_uv=False)
    p,q=R.shape
    assert min(sig)>1e-8
    # Exact full-row-rank certificate: R[:, chosen] is unit lower triangular.
    col_index={b:j for j,b in enumerate(img)}
    chosen=[col_index[tuple(j-1 for j in c)+(n-1,)] for c in cuts]
    triangle=R[:,chosen]
    assert np.array_equal(np.triu(triangle,1),np.zeros_like(triangle))
    assert np.array_equal(np.diag(triangle),np.ones(p,dtype=np.int64))
    # Exact Gram formulas for the boundary Green classes.
    if r==2 and n>=2:
        G=R@R.T
        formula=np.array([[min(i,j)*(n-max(i,j)) for j in range(1,n)] for i in range(1,n)],dtype=np.int64)
        assert np.array_equal(G,formula)
        L=np.diag([2]*(n-1))
        for i in range(n-2):L[i,i+1]=L[i+1,i]=-1
        assert np.array_equal(L@G,n*np.eye(n-1,dtype=np.int64))
        assert int(sp.Matrix(G).det())==n**(n-2)
    if r==n-1 and n>=2:
        G=R@R.T
        desired=np.diag([2]*(n-1))
        for i in range(n-2):desired[i,i+1]=desired[i+1,i]=1
        assert np.array_equal(G,desired)
        assert int(sp.Matrix(G).det())==n
    eig=np.linalg.eigvalsh(A.astype(float))
    inertia=(int(np.sum(eig>1e-7)),int(np.sum(eig< -1e-7)),int(np.sum(abs(eig)<=1e-7)))
    expected=(p*(p+1)//2,p*(p-1)//2,p*(q-p))
    assert inertia==expected,(n,r,inertia,expected)
    predicted=sorted([*([float(s*s) for s in sig]), *([float(sig[i]*sig[j]) for i in range(p) for j in range(i+1,p)]), *([-float(sig[i]*sig[j]) for i in range(p) for j in range(i+1,p)]), *([0.]*(p*(q-p)))])
    assert np.allclose(eig,predicted,atol=1e-8,rtol=1e-8)
    return len(maps),inertia,int(np.trace(A)),int(A.sum())

if __name__=='__main__':
    tests=0; n_maps=0; total_pairs=0
    for n in range(1,7):
        for r in range(1,n+1):
            cnt,inertia,loops,adj=data(n,r)
            print(f'n={n} r={r} elements={cnt} inertia={inertia} loops={loops} directed_inverse_pairs={adj}')
            tests+=1; n_maps+=cnt; total_pairs+=cnt**2
    print(f'VERIFY_OK rank_classes={tests} elements={n_maps} checked_ordered_pairs={total_pairs} inertia_and_full_spectrum=match')
