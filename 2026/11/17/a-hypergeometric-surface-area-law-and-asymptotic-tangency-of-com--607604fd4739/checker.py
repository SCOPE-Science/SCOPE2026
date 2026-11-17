#!/usr/bin/env python3
"""Independent finite Euclidean checks of the complete-root-polytope facet formulas.
Uses SciPy/Qhull geometry; no published full-text dependencies.
"""
import itertools, math
from fractions import Fraction
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull


def formula(n,s):
    return math.sqrt(s*(n-s))/(math.factorial(s-1)*math.factorial(n-s-1))


def check(n):
    standard=np.eye(n)
    all_vertices=np.array([standard[i]-standard[j] for i in range(n) for j in range(n) if i!=j])
    B=null_space(np.ones((1,n)))
    hull=ConvexHull(all_vertices@B)
    volume=math.sqrt(n)*math.comb(2*n-2,n-1)/math.factorial(n-1)
    assert math.isclose(hull.volume,volume,rel_tol=2e-8,abs_tol=1e-8), (n,hull.volume,volume)
    observed=[]
    for s in range(1,n):
        for S in itertools.combinations(range(n),s):
            S=set(S)
            P=np.array([standard[i]-standard[j] for i in S for j in range(n) if j not in S]);
            W=P[1:]-P[0]
            dim=np.linalg.matrix_rank(W,tol=1e-9)
            assert dim==n-2, (n,s,dim)
            if dim==1:
                area=float(np.linalg.norm(P[1]-P[0]))
            else:
                _,_,V=np.linalg.svd(W,full_matrices=False)
                area=ConvexHull((P-P[0])@V[:dim].T).volume
            expected=formula(n,s)
            assert math.isclose(area,expected,rel_tol=2e-8,abs_tol=1e-8),(n,S,area,expected)
            observed.append(area)
    assert len(observed)==2**n-2
    total=sum(observed)
    S_exact=sum(math.comb(n,s)*formula(n,s) for s in range(1,n))
    assert math.isclose(total,S_exact,rel_tol=1e-8,abs_tol=1e-8)
    assert math.isclose((n-1)*volume,sum(math.comb(n,s)*math.sqrt(n/(s*(n-s)))*formula(n,s) for s in range(1,n)),rel_tol=1e-10)
    print(f'GEOMETRY_PASS n={n} facets={len(observed)} intrinsic_volume={volume:.11g} surface={total:.11g}')


def test_hypergeom(n):
    total=math.comb(2*n,n)
    pmf=[math.comb(n,s)**2/total for s in range(n+1)]
    h=[(4*s*(n-s)/n**2)**1.5 for s in range(n+1)]
    mu=sum(p*h0 for p,h0 in zip(pmf,h))
    tilted=[p*h0/mu for p,h0 in zip(pmf,h)]
    tv=sum(abs(a-b) for a,b in zip(pmf,tilted))/2
    assert tv<=3/(4*n-5)+1e-12
    assert abs(sum(tilted)-1)<1e-10
    if n>=30:
        # center mass and asymptotic surface expansion
        first=1-3/(4*n)
        assert abs(mu-first)<4/n**2,(n,mu,first)
    print(f'PROBABILITY_PASS n={n} tv={tv:.9g} mu={mu:.9g}')


if __name__=='__main__':
    for n in range(3,7):check(n)
    for n in (3,4,5,7,10,30,70,120):test_hypergeom(n)
    print('ROOT_SURFACE_PASS')
