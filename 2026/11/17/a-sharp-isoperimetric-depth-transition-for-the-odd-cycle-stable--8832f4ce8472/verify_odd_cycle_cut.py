#!/usr/bin/env python3
"""Finite arithmetic and independent hull checks for odd-cycle cutting-plane geometry.
Run: python3 verify_odd_cycle_cut.py; optional NumPy/SciPy for hull check.
All exact determinant/facet checks use only Python's standard library.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial, sqrt

def det(A):
    # Fractional Gaussian elimination, exact.
    A=[list(map(F,row)) for row in A]
    n=len(A); ans=F(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        if pivot is None:return F(0)
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];ans=-ans
        d=A[j][j];ans*=d
        for i in range(j+1,n):
            f=A[i][j]/d
            for k in range(j+1,n):A[i][k]-=f*A[j][k]
            A[i][j]=0
    return ans

def gram_sq(columns):
    G=[[sum(a*b for a,b in zip(u,v)) for v in columns] for u in columns]
    return det(G)

def vertices(n):
    return [tuple(map(F,x)) for x in product((0,1),repeat=n)
            if all(x[i]+x[(i+1)%n]<=1 for i in range(n))]

def max_stable_vertices(n):
    return [v for v in vertices(n) if sum(v)==(n-1)//2]

def euler_alt(n):
    # Exact brute count only for n<=8 used in checks.
    return sum(all((p[i]<p[i+1]) if i%2==0 else (p[i]>p[i+1])
                   for i in range(n-1)) for p in permutations(range(n)))

def test(n):
    V=max_stable_vertices(n)
    assert len(V)==n
    h=tuple(F(1,2) for _ in range(n))
    # Label each neighbor by unique unsaturated cycle-edge inequality.
    W={next(i for i in range(n) if v[i]+v[(i+1)%n]==0):v for v in V}
    assert len(W)==n
    ordered=[W[i] for i in range(n)]
    differences=[[v[j]-h[j] for j in range(n)] for v in ordered]
    assert abs(det(differences))==F(1,2)
    # Old simplex facets and the new, equal-volume cut plane.
    old_sq=F(1,2)
    for i in range(n):
        columns=[differences[j] for j in range(n) if j!=i]
        assert gram_sq(columns)==old_sq
    new_columns=[[ordered[i][j]-ordered[0][j] for j in range(n)] for i in range(1,n)]
    assert gram_sq(new_columns)==F(n)
    E=euler_alt(n-1)
    assert E=={3:1,5:5,7:61,9:1385}[n]
    a=(1-sqrt(2/n))/((1+sqrt(2))*E)
    b=1/(n*E)
    sstar=a/b
    assert (0<sstar<1) if n in (3,5) else (sstar>1)
    if n in (3,5,7):
        try:
            import numpy as np
            from scipy.spatial import ConvexHull
        except ImportError:
            print('HULL_SKIPPED: optional scipy/numpy unavailable')
        else:
            raw=vertices(n)
            integ=ConvexHull(np.array(raw,dtype=float))
            frac=ConvexHull(np.array(raw+[h],dtype=float))
            vol=E/(2*factorial(n-1))
            area=n*E*(1+1/sqrt(2))/factorial(n-1)
            dv=1/(2*factorial(n))
            ds=(sqrt(n)-n/sqrt(2))/factorial(n-1)
            assert abs(frac.volume-vol)<1e-8
            assert abs(integ.volume-(vol-dv))<1e-8
            assert abs(frac.area-area)<1e-8
            assert abs(integ.area-(area+ds))<1e-8
    return n,len(vertices(n)),E,sstar

if __name__=='__main__':
    out=[test(n) for n in (3,5,7,9)]
    for row in out:print('n=%d vertices=%d E=%d optimal_cut_depth=%.12g'%row)
    print('ODD_CYCLE_CUT_GEOMETRY_PASS cases=4 exact_simplex_facets=28')
