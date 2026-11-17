#!/usr/bin/env python3
"""Exact checks of Euclidean John-ellipsoid shields in leaf-corona bipartite graphs.

Mathematical certificates are rational: edge feasibility and positive KKT weights.
Small independent convex optimization is an additional (non-proof) check.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import prod

def examine(p, core_edges):
    r = len(p)
    u = {('c',i): F(1,p[i]+1) for i in range(r)}
    leaves=[]; star_edges=[]
    for i, pi in enumerate(p):
        for t in range(pi):
            key=('l',i,t)
            leaves.append(key)
            u[key]=F(pi,pi+1)
            star_edges.append((('c',i),key))
    lam = {(a,b): F(p[a[1]]+1,p[a[1]]) for a,b in star_edges}
    for a,b in star_edges:
        assert u[a]+u[b]==1
        assert lam[a,b]>0
    for i,j in core_edges:
        assert (i%2)!=(j%2), 'Core graph must be bipartite'
        lhs = u['c',i]+u['c',j]
        assert lhs<=1
        assert (lhs==1)==(p[i]==p[j]==1)
        if lhs<1:
            assert lhs<=F(5,6)
    for v in u:
        mu=sum(weight for (a,b),weight in lam.items() if a==v or b==v)
        assert mu==1/u[v], (v,mu,1/u[v])
    determinant = prod([F(pi**pi,(pi+1)**(pi+1)) for pi in p], start=F(1))
    assert prod(u.values(),start=F(1))==determinant
    return len(star_edges),len(core_edges)

def exact_suite():
    profiles=graphs=inequalities=0
    for r in range(1,6):
        possible=[(i,j) for i,j in combinations(range(r),2) if (i-j)%2]
        for p in product(range(1,4),repeat=r):
            profiles+=1
            for mask in range(1<<len(possible)):
                E=[edge for k,edge in enumerate(possible) if mask & (1<<k)]
                s,c=examine(p,E)
                graphs+=1
                inequalities+=s+c
    return profiles,graphs,inequalities

def independent_numeric():
    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError:
        return 'scipy-unavailable'
    trials=0
    for r in (2,3,4):
        possible=[(i,j) for i,j in combinations(range(r),2) if (i-j)%2]
        for p in list(product((1,2,3),repeat=r))[::max(1,3**r//10)]:
            edges=[]; offset=r
            for i,pi in enumerate(p):
                edges.extend((i,offset+t) for t in range(pi)); offset+=pi
            edges.extend(possible)
            n=offset
            true=np.array([1/(pi+1) for pi in p]+[pi/(pi+1) for pi in p for _ in range(pi)],dtype=float)
            constraints=[{'type':'ineq','fun':lambda x,a=a,b=b:1-x[a]-x[b],
                           'jac':lambda x,a=a,b=b:np.eye(n)[a]*-1-np.eye(n)[b]} for a,b in edges]
            f=lambda x: -sum(np.log(x))
            jac=lambda x: -1/x
            ans=minimize(f,np.full(n,0.20),jac=jac,bounds=[(.000001,1)]*n,
                         method='SLSQP',constraints=constraints,
                         options={'ftol':1e-11,'maxiter':500})
            assert ans.success, (r,p,ans.message)
            assert np.max(np.abs(ans.x-true))<3e-5, (r,p,ans.x,true)
            trials+=1
    return trials

if __name__=='__main__':
    p,g,i=exact_suite()
    t=independent_numeric()
    print(f'LEAF_CORONA_JOHN_PASS profiles={p} bipartite_graphs={g} exact_edge_checks={i} independent_numeric={t}')
