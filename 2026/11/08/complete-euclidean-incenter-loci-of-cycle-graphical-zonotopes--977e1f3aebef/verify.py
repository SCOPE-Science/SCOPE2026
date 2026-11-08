#!/usr/bin/env python3
"""Reproducibility checks for the Euclidean incenter locus of cycle graphical zonotopes.
Requires only Python standard library; no external proof assistant is used.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations, product
from math import comb
getcontext().prec=70
D=lambda v:Decimal(v)
TOL=D('1e-57')

def inradius(n):
    m=(n*n)//4
    return (D(n)/D(m)).sqrt()

def slack(n,s):
    return D(1)-inradius(n)*(D(s*(n-s))/D(n)).sqrt()

def vertices_of_cube_section(k):
    """Dimension-k cube intersected by the sum-zero hyperplane, normalized to side [-1,1]."""
    if k%2==0:
        return [v for v in product((-1,1),repeat=k) if sum(v)==0]
    out=[]
    for j in range(k):
        for a in product((-1,1),repeat=k-1):
            if sum(a)==0:
                out.append(a[:j]+(0,)+a[j:])
    return out

def assert_interval_point(x,n):
    for s in range(1,n):
        cap=slack(n,s)
        for i in range(n):
            lhs=abs(sum(x[(i+j)%n] for j in range(s)))
            assert lhs<=cap+TOL,(n,s,i,str(lhs),str(cap))

def rank_rat(a):
    a=[[Fraction(z) for z in row] for row in a]
    m=len(a); n=len(a[0]); piv=0
    for j in range(n):
        l=next((l for l in range(piv,m) if a[l][j]!=0),None)
        if l is None: continue
        a[piv],a[l]=a[l],a[piv]
        z=a[piv][j];a[piv]=[v/z for v in a[piv]]
        for l in range(m):
            if l!=piv:
                z=a[l][j]
                if z:a[l]=[q-z*b for q,b in zip(a[l],a[piv])]
        piv+=1
        if piv==m:break
    return piv

def check():
    for n in range(3,22):
        m=(n*n)//4
        assert abs(inradius(n)**2-D(n)/D(m))<TOL
        # All cyclic-interval outer normal lengths and distances are checked.
        for s in range(1,n):
            assert slack(n,s)>=-TOL
            assert abs(slack(n,s))<TOL if s*(n-s)==m else slack(n,s)>0
        k=n//2
        b=D(1)-(D(1)-D(1)/(D(k)*D(k))).sqrt() if n%2==0 else None
        # Matrix of linear equations imposed by the tight supporting facets.
        constraints=[[1]*n]
        for s in range(1,n):
            if s*(n-s)==m:
                for i in range(n):
                    row=[0]*n
                    for j in range(s):row[(i+j)%n]=1
                    constraints.append(row)
        rank=rank_rat(constraints)
        assert n-rank == (k-1 if n%2==0 else 0),(n,rank)
        if n%2: continue
        vs=vertices_of_cube_section(k)
        assert len(vs)==(comb(k,k//2) if k%2==0 else k*comb(k-1,(k-1)//2))
        assert len(vs)==len(set(vs))
        for y in vs:
            x=tuple(D(v)*b for v in y+y)
            assert_interval_point(x,n)
        # The strongest k+1 interval inequality forces each coordinate bound.
        assert abs(slack(n,k+1)-b)<TOL
        # For every angular gap j, convexity ensures j*b <= 1-sqrt(1-j*j/k*k).
        for j in range(1,k):
            bound=D(1)-(D(1)-D(j*j)/D(k*k)).sqrt()
            assert D(j)*b <= bound + TOL,(k,j)
        # A sample point strictly inside incenter polytope (except equality constraints).
        x=tuple(D(v)*b/D(3) for v in vs[0]+vs[0])
        assert_interval_point(x,n)
        print('verified n=',n,'radius=',str(inradius(n))[:17], 'incenter_dimension=',k-1,'vertices=',len(vs))
    print('CYCLE_GRAPHICAL_ZONOTOPE_INCENTER_CHECKS_PASSED')

if __name__=='__main__':check()
