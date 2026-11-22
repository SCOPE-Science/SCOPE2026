#!/usr/bin/env python3
"""Exact finite diagnostics for a three-site, two-width Gaussian RBF matrix.

All exact identities and infinite parameter assertions are proved in RESULT.md;
finite tests here are supporting independent arithmetic checks, not enumeration proofs.
"""
from fractions import Fraction as F


def determinant(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def matrix(x,y):
    return [[F(1),y,x**4],[x,F(1),x],[x**4,y,F(1)]]


def cubic(x):
    return x**3+x**2+x-1


def main():
    checked=0
    for a in range(1,18):
        x=F(a,19)
        for b in range(1,18):
            y=x+(1-x)*F(b,19)
            det=determinant(matrix(x,y))
            formula=(1-x**4)*(1+x**4-2*x*y)
            assert det==formula
            checked+=1
    # Certified rational isolating bracket (strictly increasing cubic).
    left,right=F(543689,1000000),F(543690,1000000)
    assert cubic(left)<0<cubic(right)
    checked+=1
    # Exactly singular rational matrix with nontrivial kernel.
    x,y=F(3,4),F(337,384)
    m=matrix(x,y)
    assert x<y<1 and determinant(m)==0 and 1-x*y>0
    v=(F(1),F(-3,2),F(1))
    assert all(sum(a*b for a,b in zip(row,v))==0 for row in m)
    checked+=5
    # Strictly safe high-localization region: at every tested y below 1.
    for x in (F(1,10),F(1,3),F(1,2)):
        for u in (F(1,3),F(2,3),F(99,100)):
            y=x+(1-x)*u
            assert determinant(matrix(x,y))>0
            checked+=1
    # For 3/4 the singular y is interior, with both determinant signs.
    ystar=F(337,384)
    assert determinant(matrix(F(3,4),(F(3,4)+ystar)/2))>0
    assert determinant(matrix(F(3,4),(F(1)+ystar)/2))<0
    checked+=2
    print(f'PASS: {checked} exact-rational diagnostics; rank-two singular certificate verified.')


if __name__=='__main__':
    main()
