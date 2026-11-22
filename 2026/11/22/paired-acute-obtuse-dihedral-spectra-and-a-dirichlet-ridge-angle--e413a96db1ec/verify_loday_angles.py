#!/usr/bin/env python3
"""Finite checks for Euclidean ridge angles of the canonical Loday associahedron.
This is a reproducibility check, not an infinite-dimensional proof.
"""
from functools import lru_cache
from math import comb
from fractions import Fraction
import numpy as np

@lru_cache(None)
def vertices_for_leaves(m):
    if m == 1:
        return ((),)
    return tuple(a + (l*(m-l),) + b for l in range(1,m)
                 for a in vertices_for_leaves(l)
                 for b in vertices_for_leaves(m-l))

def intervals(n):
    return [(i,j) for i in range(n) for j in range(i,n)
            if j-i+1<n]

def compatible(I,J):
    a,b=I; c,d=J
    nested=(a<=c and d<=b) or (c<=a and b<=d)
    far=(b+1<c) or (d+1<a)
    return nested,far

def cosine_square(n,I,J):
    a,b=I; c,d=J
    k=b-a+1; ell=d-c+1
    common=max(0,min(b,d)-max(a,c)+1)
    val=Fraction(n*common-k*ell,1)
    return Fraction(val*val,k*(n-k)*ell*(n-ell))

def count_expected(n):
    A=n*(n-1)*(n-2)*(n+1)//24
    O=(n-2)*(n-1)*(n*n+9*n+12)//24
    R=(n-2)*(n-1)*(n+2)*(n+3)//12
    return A,O,R

def verify(n):
    V=np.asarray(vertices_for_leaves(n+1),dtype=np.int64)
    assert len(V)==comb(2*n,n)//(n+1)
    assert np.all(V.sum(axis=1)==comb(n+1,2))
    ints=intervals(n)
    tight={I: np.flatnonzero(V[:,I[0]:I[1]+1].sum(axis=1)==comb(I[1]-I[0]+2,2)) for I in ints}
    assert all(len(tight[I])>0 for I in ints)
    A=O=0
    acute=set();obtuse=set()
    for i,I in enumerate(ints):
        for J in ints[i+1:]:
            nested,far=compatible(I,J)
            assert not (nested and far)
            vertices=np.intersect1d(tight[I],tight[J], assume_unique=True)
            if len(vertices):
                affine_rank=np.linalg.matrix_rank((V[vertices[1:]]-V[vertices[0]]).astype(float),tol=1e-8)
            else:
                affine_rank=-1
            is_ridge=(affine_rank==n-3)
            if is_ridge!=(nested or far):
                raise AssertionError((n,I,J,nested,far,is_ridge,affine_rank))
            if nested:
                O+=1
                obtuse.add(cosine_square(n,I,J))
            elif far:
                A+=1
                acute.add(cosine_square(n,I,J))
    assert (A,O,A+O)==count_expected(n)
    assert acute==obtuse
    print('n=',n,'vertices=',len(V),'facets=',len(ints),'acute=',A,'obtuse=',O,
          'angle-magnitude-levels=',len(acute),'PASS',flush=True)

if __name__=='__main__':
    for n in range(3,9):
        verify(n)
    print('LODAY_RIDGE_ANGLE_PASS')
