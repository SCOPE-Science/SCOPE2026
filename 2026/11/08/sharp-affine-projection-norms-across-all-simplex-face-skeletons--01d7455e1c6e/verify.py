#!/usr/bin/env python3
"""Exact arithmetic checks for affine face-balanced simplex-skeleton projection.
Finite checks supplement the proof in RESULT.md; they do not replace universal arguments.
"""
from fractions import Fraction as F
from math import comb


def parameters(m,r):
    assert m>=2 and 1<=r<=m
    delta=F(2*m-r-1,m*(m-1)*(r+1))
    alpha=1/delta
    h=F(r-1,(m-1)*(r+1))
    q=1-h
    I=F((m-1)*(r+1),2*m-r-1)*q**r
    return delta,alpha,h,q,I


def integral_vertex_positive(m,r):
    delta,A,h,q,I=parameters(m,r)
    # Compute independently by exact expansion of the conditional beta density.
    if r==1:
        # One uniformly sampled vertex, kernel at v_i equals m or 0.
        return F(1)
    B=1-A/m
    # P(vertex i is contained in sampled face)=r/m.
    # Conditional Beta(1,r-1) density: (r-1)(1-t)^(r-2)
    # Integrate (A*t+B) for t=h..1 by expanding (1-t)^(r-2)
    val=F(0)
    for j in range(r-1):
        coeff=F(r-1)*F(comb(r-2,j))*(-1)**j
        val += coeff*( A*(F(1)-h**(j+2))/F(j+2) + B*(F(1)-h**(j+1))/F(j+1) )
    return F(r,m)*val


def check():
    cases=0
    for m in range(2,17):
        for r in range(1,m+1):
            delta,alpha,h,q,I=parameters(m,r)
            diag=F(2,m*(r+1))
            off=F(r-1,m*(m-1)*(r+1))
            assert diag-off==delta
            # Verify Gram inverse entrywise, including constant eigenvector.
            G=[[diag if i==j else off for j in range(m)] for i in range(m)]
            inverse=[[ (F(1) if i==j else F(0))/delta - F(1,m)/delta + F(1) for j in range(m)] for i in range(m)]
            for i in range(m):
                for j in range(m):
                    assert sum(G[i][k]*inverse[k][j] for k in range(m))==(1 if i==j else 0)
            assert I==integral_vertex_positive(m,r)
            assert 2*I-1==2*F((m-1)*(r+1),2*m-r-1)*q**r-1
            assert 2*I-1<=r
            if r>=2: assert 2*I-1<r
            if r==m:
                assert I==F(m)*(F(m,m+1))**(m-1)
            if r==1: assert 2*I-1==1
            cases+=1
    print('EXACT_SKELETON_GRAM_AND_BETA_MOMENTS_OK',cases,'PAIRS')
    for r in range(2,12):
        previous=F(-1)
        for m in range(r,81):
            L=2*parameters(m,r)[4]-1
            assert L>previous
            previous=L
    print('EXACT_FIXED_FACE_RANK_MONOTONICITY_SAMPLED_OK')
    for r in range(1,13):
        m=5000
        value=float(2*parameters(m,r)[4]-1)
        assert abs(value-r)<0.06
    print('ASYMPTOTIC_FIXED_RANK_DIAGNOSTICS_OK')
    print('ALL_SIMPLEX_SKELETON_CHECKS_PASSED')

if __name__=='__main__':
    check()
