#!/usr/bin/env python3
"""Exact rational checks of the path-Laplacian minimum-ball formulas.

Finite checks supplement the proof of the all-size theorem in RESULT.md.
Requires Python 3.9+ standard library only.
"""
from math import comb
from fractions import Fraction as F


def matrix(n):
    m = [[0] * n for _ in range(n)]
    for k in range(n - 1):
        m[k][k] += 1
        m[k+1][k+1] += 1
        m[k][k+1] -= 1
        m[k+1][k] -= 1
    return m


def sum_sq(x):
    return sum(z*z for z in x)


def verification(n):
    L=matrix(n)
    if n==3:
        weights=[F(7,27),F(13,27),F(7,27)]
        expected_r2=F(98,27)
    else:
        B=comb(n+2,5)
        weights=[F(0)] + [F(comb(i,2)*comb(n-i+1,2),B) for i in range(2,n)] + [F(0)]
        expected_r2=6-F(6,B)
        assert sum(weights)==1
        assert all(weights[i]>0 for i in range(1,n-1))
        # Independent polynomial identity: fourth difference of a quartic.
        m=n-2
        def W(j):
            return j*(j+1)*(m+1-j)*(m+2-j)
        for j in range(1,m+1):
            assert W(j-2)-4*W(j-1)+6*W(j)-4*W(j+1)+W(j+2)==24
        assert sum(W(j) for j in range(1,m+1))==4*B
    assert sum(weights)==1
    center=[sum(L[i][j]*weights[j] for j in range(n)) for i in range(n)]
    ds=[sum_sq([L[k][i]-center[k] for k in range(n)]) for i in range(n)]
    assert sum(weights[i]*ds[i] for i in range(n))==expected_r2
    assert max(ds)==expected_r2
    if n==3:
        assert center==[F(-2,9),F(4,9),F(-2,9)]
        assert len(set(ds))==1
    else:
        B=comb(n+2,5)
        assert ds[0]==ds[-1]==2+F(6*(n-1),B)
        assert all(ds[i]==expected_r2 for i in range(1,n-1))
        assert center==[F(-6*i*i+6*(n+1)*i-(n+1)*(n+2),2*B) for i in range(1,n+1)]
        assert (ds[0]==expected_r2)==(n==4)
        assert (expected_r2-ds[0])==4-F(6*n,B)
        # Exact barycentric optimality: the weighted contact-vertex mean is center.
        assert sum(weights[i]*sum_sq([L[k][i]-center[k] for k in range(n)]) for i in range(n))==expected_r2
    return expected_r2


def main():
    for n in range(3,81):
        verification(n)
    # A second integer recurrence check tests much larger orders without matrices.
    for n in range(4,1001):
        B=comb(n+2,5)
        m=n-2
        def W(j):return j*(j+1)*(m+1-j)*(m+2-j)
        assert sum(W(j) for j in range(1,m+1))==4*B
        for j in range(1,m+1):
            assert W(j-2)-4*W(j-1)+6*W(j)-4*W(j+1)+W(j+2)==24
    print('PATH_LAPLACIAN_BALL_EXACT_PASS rational_profiles=78 integer_profiles=997 recurrence_positions=498500')

if __name__=='__main__':
    main()
