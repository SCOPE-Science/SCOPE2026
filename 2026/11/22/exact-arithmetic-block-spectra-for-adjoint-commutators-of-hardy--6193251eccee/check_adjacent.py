#!/usr/bin/env python3
"""Finite-block checks for Hardy weighted-composition cross-adjoint commutators.

All analytical conclusions in RESULT.md are proved independently; this script checks
integer overlap identities, finite block spectra, and limiting-moment diagnostics.
"""
import math
import numpy as np
import sympy as sp


def matrices(m):
    n = m + 1
    h = np.zeros((n, m), dtype=np.int64)
    for r in range(m):
        h[r, r] = m - r
        h[r+1, r] = r + 1
    b = (h.astype(float)-1.0)/math.sqrt(m*n)
    return h,b


def direct_column(m, ell, r):
    n = m + 1
    k = m*ell+r
    # First term V_m^* V_n e_k:
    a = {}
    for v in range(n*k,n*(k+1)):
        q=v//m
        a[q]=a.get(q,0)+1
    # Second term V_n V_m^* e_k:
    for v in range(n*ell,n*(ell+1)):
        a[v]=a.get(v,0)-1
    return a


def check():
    count=0
    # General unequal bases: exact overlap blocks and gcd-controlled unit singular levels.
    for m in range(2,22):
        for n in range(2,22):
            hh=np.array([[max(0,min(n*(r+1),m*(s+1))-max(n*r,m*s)) for r in range(m)] for s in range(n)],dtype=float)
            bb=(hh-1)/math.sqrt(m*n)
            assert np.max(np.abs(hh.sum(axis=0)-n))<1e-13
            assert np.max(np.abs(hh.sum(axis=1)-m))<1e-13
            rank=np.linalg.matrix_rank(bb,tol=1e-8)
            assert rank==min(m,n)-1,(m,n,rank)
            sv=np.linalg.svd(bb,compute_uv=False)
            d=math.gcd(m,n)
            assert np.count_nonzero(np.abs(sv-1)<1e-9)==d-1,(m,n,sv)
            for ell in [0,2]:
                for r in range(m):
                    k=m*ell+r
                    a={}
                    for idx in range(n*k,n*(k+1)):
                        row=idx//m
                        a[row]=a.get(row,0)+1
                    for idx in range(n*ell,n*(ell+1)):
                        a[idx]=a.get(idx,0)-1
                    for s0 in range(n):
                        assert a.get(n*ell+s0,0)==round(hh[s0,r])-1
                    assert set(a).issubset(set(range(n*ell,n*(ell+1))))
            count+=1
    for m in range(2,41):
        n=m+1
        h,b=matrices(m)
        assert np.all(np.sum(h,axis=0)==n)
        assert np.all(np.sum(h,axis=1)==m)
        assert np.allclose(b @ np.ones(m),0)
        for ell in (0,1,3,7):
            for r in range(m):
                col=direct_column(m,ell,r)
                for s in range(n):
                    assert col.get(n*ell+s,0)==h[s,r]-1
                assert set(col).issubset(set(range(n*ell,n*(ell+1))))
                count+=1
        target=np.array([0]+[1-j*(j+1)/(m*n) for j in range(1,m)])
        found=np.linalg.eigvalsh(b.T@b)
        assert np.max(np.abs(np.sort(found)-np.sort(target)))<5e-14
        count+=1
        # exact jacobi-form of the Gram complement
        c=np.array([(r+1)*(m-r-1) for r in range(m-1)],dtype=np.int64)
        lap=np.diag(np.r_[0,c]+np.r_[c,0])
        for r in range(m-1):
            lap[r,r+1]=-c[r]
            lap[r+1,r]=-c[r]
        assert np.array_equal(m*n*np.eye(m,dtype=np.int64)-h.T@h,lap)
        count+=1
    for m in range(2,13):
        h=np.array(matrices(m)[0],dtype=object)
        hh=sp.Matrix(h.tolist())
        jj=sp.ones(m+1,m)
        gram=(hh-jj).T*(hh-jj)
        target=[0]+[m*(m+1)-j*(j+1) for j in range(1,m)]
        assert sorted([int(ev) for ev,mult in gram.eigenvals().items() for _ in range(mult)])==sorted(target)
        count+=1
    # Continuous one-cell density / moments, not a finite-size proof.
    for p in [0.5,1,2,3,5]:
        analytic=math.sqrt(math.pi)*math.gamma(p/2+1)/(2*math.gamma(p/2+1.5))
        for m in [256,1024]:
            moment=sum((1-j*(j+1)/(m*(m+1)))**(p/2) for j in range(1,m))/(m-1)
            assert abs(moment-analytic)<0.02
            count+=1
    print(f'PASS: {count} integer/block/spectrum/moment assertions')


if __name__=='__main__':
    check()
