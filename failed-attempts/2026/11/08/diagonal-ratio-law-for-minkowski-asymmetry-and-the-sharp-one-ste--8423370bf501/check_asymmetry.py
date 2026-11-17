#!/usr/bin/env python3
"""Exact finite checks for a diagonal-ratio Minkowski asymmetry identity.

The mathematical proof is a facet-support and positive-dependence argument.
This program checks its constructive upper and lower certificates over
rational grids; it does not replace that proof for arbitrary real parameters.
"""
from fractions import Fraction as F


def determinant(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def solve_2x2(A, b):
    d=determinant(A)
    assert d != 0
    return ((b[0]*A[1][1]-A[0][1]*b[1])/d,
            (A[0][0]*b[1]-b[0]*A[1][0])/d)


def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]


def certificates(a, lam):
    assert 0 <= a <= F(1,2) and 0 <= lam <= F(1,2)
    t=2-min(a,lam)/(1-max(a,lam))
    v=((F(0),F(0)),(a,lam),(F(1),F(0)),(a,lam-1))
    normals=((-lam,a),(lam,1-a),(1-lam,a-1),(lam-1,-a))
    support=(F(0),lam,1-lam,F(0))
    minimum=[min(dot(n,p) for p in v) for n in normals]
    assert all(max(dot(n,p) for p in v) == b for n,b in zip(normals,support))
    # Saturate the 2nd and 4th supporting inequalities.
    A=(normals[1],normals[3])
    y=(F(1),F(0)) if a==lam==F(1,2) else solve_2x2(A,(t*support[1]+minimum[1], minimum[3]))
    # Constructive upper bound, for the exact y=(t+1)*Minkowski_center.
    assert all(dot(n,y) <= t*b+m for n,b,m in zip(normals,support,minimum))
    # The three nonnegative weights cancel normals 2, 3 and 4.
    beta=( (1-lam)/(1-a), (1-a-lam)/(1-a), F(1))
    assert all(w>=0 for w in beta)
    assert all(sum(beta[i]*normals[i+1][j] for i in range(3))==0 for j in range(2))
    bsum=sum(beta[i]*support[i+1] for i in range(3))
    msum=sum(beta[i]*minimum[i+1] for i in range(3))
    assert bsum == 1-lam > 0
    assert -msum == t*bsum  # Exact supporting lower certificate.
    # The same center meets all three positive-weight facets as equalities.
    assert all(dot(normals[i],y) == t*support[i]+minimum[i] for i in (1,2,3))
    return t,y


def main():
    count=0
    for n in range(2,51):
        for i in range(n//2+1):
            for j in range(n//2+1):
                certificates(F(i,n),F(j,n))
                count+=1
    print('EXACT_QUADRILATERAL_ASYMMETRY_CERTIFICATES_OK',count)
    for a,lam,expect in [(F(1,2),F(1,2),F(1)),
                         (F(1,3),F(1,4),F(13,8)),
                         (F(1,3),F(1,3),F(3,2)),
                         (F(0),F(1,4),F(2)),
                         (F(1,2),F(1,4),F(3,2))]:
        t,_=certificates(a,lam)
        assert t==expect,(a,lam,t,expect)
    print('BOUNDARY_AND_SHARP_CASES_OK')

if __name__=='__main__':
    main()
