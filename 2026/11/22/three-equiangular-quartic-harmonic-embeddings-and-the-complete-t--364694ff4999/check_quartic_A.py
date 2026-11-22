#!/usr/bin/env python3
"""Exact standalone tests for quartic harmonic sampling on simplex root directions.
All arithmetic is rational. This script verifies finite instances; the accompanying
analytic proof establishes the universal assertions.
"""
from fractions import Fraction as F
from itertools import combinations

def zonal_rec(n,t):
    # The unit sphere in the (n-1)-dimensional zero-sum hyperplane.
    p0,p1=F(1),t
    for ell in range(1,4):
        p0,p1=p1,((2*ell+n-3)*t*p1-ell*p0)/(ell+n-3)
    return p1

def zonal_harmonic(n,t):
    D=n-1
    # Derived by taking the Laplacian of the harmonic projection of (x.y)^4.
    return ((D+2)*(D+4)*t**4-6*(D+2)*t**2+3)/F(D*D-1)

def eigen(n):
    return ((F((n-3)*(n+3),8*n),1),
            (F((n+1)*(n*n-9*n+36),16*n*(n-2)),n-1),
            (F((n+1)*(7*n-3),8*n*(n-2)),n*(n-3)//2))

def root_dot(a,b):
    (i,j),(k,l)=a,b
    return F((i==k)-(i==l)-(j==k)+(j==l),2)

def act(mat,v):
    return [sum((a*b for a,b in zip(row,v)),F(0)) for row in mat]

for n in range(4,26):
    edges=list(combinations(range(n),2))
    N=len(edges)
    a=zonal_rec(n,F(1,2));b=zonal_rec(n,F(0))
    assert a==zonal_harmonic(n,F(1,2))
    assert b==zonal_harmonic(n,F(0))
    for t in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
        assert zonal_rec(n,t)==zonal_harmonic(n,t)
    vals=eigen(n)
    assert sum(mult for v,mult in vals)==N
    assert all(v>0 for v,mult in vals)
    assert N*1==sum(v*mult for v,mult in vals)
    # Direct entry-wise computation through the 4th Gegenbauer recurrence.
    # Evaluate invariant test vectors without relying on a numeric eigensolver.
    if n<=12:
        G=[[zonal_rec(n,root_dot(e,f)) for f in edges] for e in edges]
        # Constant subspace
        u=[F(1)]*N
        assert act(G,u)==[vals[0][0]*x for x in u]
        # Vertex star differences span the standard sector.
        for vertex in range(1,n):
            v=[F((vertex in e)-(0 in e)) for e in edges]
            assert act(G,v)==[vals[1][0]*x for x in v]
        # Edge-space orthogonal complement of constant and star sectors.
        # Four-cycle elements span the two-row sector.
        for i,j,k,l in combinations(range(n),4):
            v=[F((e==(i,j))+(e==(k,l))-(e==(i,k))-(e==(j,l))) for e in edges]
            assert act(G,v)==[vals[2][0]*x for x in v]
    # Exact parity of equiangular property: two available nonzero offdiagonal orbit values.
    equals = abs(a)==abs(b)
    assert equals==(n in (5,15,21)),(n,a,b)
    assert (a==b)==(n==21)
    assert (a==-b)==(n in (5,15))
    if n==21:
        assert a==b==F(1,133)
        assert vals[1][0]==vals[2][0]==F(132,133)
        assert vals[0][0]==F(18,7)
        assert vals[1][1]+vals[2][1]==209
    if n==15:
        assert a==-b==-F(1,65)
    if n==5:
        assert a==-b==-F(1,5)
print('QUARTIC_A_EXACT_CHECK_OK: n=4..25; recurrence, harmonic projection, direct Gram eigenvectors, trace, positivity, equiangular exceptions')
