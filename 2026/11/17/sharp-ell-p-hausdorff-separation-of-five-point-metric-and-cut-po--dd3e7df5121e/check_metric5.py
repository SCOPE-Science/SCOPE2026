#!/usr/bin/env python3
"""Exact witnesses for the Euclidean separation of the five-point metric and cut polytopes.

Only the optional scipy/Qhull census is numerical. The proof of exhaustiveness
uses the published complete vertex classification of MET(5), not Qhull.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter

N=5
EDGES=list(combinations(range(N),2))
IX={e:i for i,e in enumerate(EDGES)}
SUBSETS=[s for s in range(1<<N) if not (s & (1<<(N-1)))]
ONE=(F(1),)*10

def cut(s):
    return tuple(F((s>>i&1)^(s>>j&1)) for i,j in EDGES)

def anticut(s):
    c=cut(s)
    return tuple(F(2,3)-F(1,3)*v for v in c)

def projection(s):
    c=cut(s)
    return tuple(F(3,5)-F(1,5)*v for v in c)

def norm2(v):return sum(x*x for x in v)

def dot(u,v):return sum(a*b for a,b in zip(u,v))

def inequalities():
    constraints=[]
    for i,j,k in combinations(range(N),3):
        triple=[IX[tuple(sorted(e))] for e in ((i,j),(i,k),(j,k))]
        for p in range(3):
            a=[0]*10
            for q in triple:a[q]=-1
            a[triple[p]]=1
            constraints.append((tuple(a),0))
        a=[0]*10
        for q in triple:a[q]=1
        constraints.append((tuple(a),2))
    return constraints

def rank(rows):
    from sympy import Matrix
    return Matrix(rows).rank()

def run():
    cuts=[cut(s) for s in SUBSETS]
    anti=[anticut(s) for s in SUBSETS]
    P=[projection(s) for s in SUBSETS]
    assert len(set(cuts))==16 and len(set(anti))==16
    assert len(set(cuts+anti))==32
    H=inequalities()
    assert len(H)==40
    for v in cuts+anti:
        assert all(dot(a,v)<=b for a,b in H)
        active=[a for a,b in H if dot(a,v)==b]
        assert rank(active)==10,(v,len(active))
    triple_incidence=[[int((i in t) and (j in t)) for i,j in EDGES] for t in combinations(range(N),3)]
    assert rank(triple_incidence)==10
    max_cuts=[c for c in cuts if sum(c)==6]
    assert len(max_cuts)==10
    barycenter=tuple(sum(c[j] for c in max_cuts)/10 for j in range(10))
    assert barycenter==(F(3,5),)*10
    for s in SUBSETS:
        v=anticut(s);p=projection(s)
        assert norm2(tuple(v[i]-p[i] for i in range(10)))==F(2,45)
        # Explicit convex combination of switched maximum-cut vertices.
        switched=[]
        for c in max_cuts:
            d=cut(s)
            switched.append(tuple(1-c[i] if d[i] else c[i] for i in range(10)))
        assert tuple(sum(c[j] for c in switched)/10 for j in range(10))==p
        # Global projection normal certificate, checked at every vertex of CUT5.
        assert all(dot(tuple(v[i]-p[i] for i in range(10)),tuple(c[i]-p[i] for i in range(10)))<=0 for c in cuts)
    residuals=[tuple(v[i]-p[i] for i in range(10)) for v,p in zip(anti,P)]
    assert len(set(residuals))==16 and 0 not in [norm2(r) for r in residuals]
    assert all(norm2(r)==F(2,45) for r in residuals)
    # Optional independent floating point H-to-V conversion and candidate equality.
    census='not_run'
    try:
        import numpy as np
        from scipy.spatial import HalfspaceIntersection
        hs=np.array([list(a)+[-b] for a,b in H],dtype=float)
        x=np.ones(10)/2
        calc=HalfspaceIntersection(hs,x,qhull_options='Qx').intersections
        expected=np.array([[float(t) for t in v] for v in cuts+anti])
        assert len(calc)==32
        assert max(np.min(np.linalg.norm(expected-v,axis=1)) for v in calc)<1e-8
        assert max(np.min(np.linalg.norm(calc-v,axis=1)) for v in expected)<1e-8
        census='32_matched'
    except ImportError:
        census='scipy_not_installed'
    print('MET5_CUT5_EXACT_PASS inequality_count=40 cuts=16 anticuts=16 rank=10 maximum_cut_size=6 projection_squared_distance=2/45 unique_anticut_residuals=16 numerical_vertex_census='+census)

if __name__=='__main__':run()
