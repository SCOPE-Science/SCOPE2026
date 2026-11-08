#!/usr/bin/env python3
"""Exact certificate for the endpoint-neighbor positivity threshold of TR-BDF2 on paths.
Run using Python 3 standard library only: python verify.py
"""
from fractions import Fraction as Q
from math import comb


def powers(n):
    d = 4*n-3
    a = [0]*(d+1)
    a[0] = 3
    a[2*n] += 4*n-3
    a[2*n-3] += 4*n-3
    a[d] += 3
    b = [0]*(d+1)
    for i in range(2*n):
        for j in (0, 1):
            for k in (0, 2*n-3):
                b[i+j+k] += 1
    return a, b


def bernstein_points(power):
    d = len(power)-1
    return [sum((Q(power[j]*comb(k,j),comb(d,j))
                 for j in range(k+1)), Q(0)) for k in range(d+1)]


def bisect(points):
    layers = [points]
    while len(layers[-1]) > 1:
        old = layers[-1]
        layers.append([(old[i]+old[i+1])/2 for i in range(len(old)-1)])
    return [layer[0] for layer in layers], [layer[-1] for layer in reversed(layers)]


def rational_eval(coeffs,r):
    val=Q(0)
    for c in reversed(coeffs):
        val=val*r+c
    return val


def mat_inverse(A):
    n=len(A)
    X=[[Q(A[i][j]) for j in range(n)]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        ix=next(k for k in range(i,n) if X[k][i]!=0)
        X[i],X[ix]=X[ix],X[i]
        pivot=X[i][i]; X[i]=[q/pivot for q in X[i]]
        for k in range(n):
            if k!=i:
                mult=X[k][i]
                X[k]=[X[k][j]-mult*X[i][j] for j in range(2*n)]
    return [row[n:] for row in X]


def matrix_ratio(n,s):
    A=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        A[i][i]=1+s*(1 if i in (0,n-1) else 2)
        if i+1<n: A[i][i+1]=-s; A[i+1][i]=-s
    R=mat_inverse(A)
    return sum(R[0][k]*R[k][1] for k in range(n))/R[0][1]


def formula_ratio(n,r):
    A,B=powers(n)
    return Q(1,2)+rational_eval(A,r)/(2*rational_eval(B,r))


def main():
    n=32; A,B=powers(n)
    P=[50000*a-8579*b for a,b in zip(A,B)]
    pts=bernstein_points(P)
    assert len(pts)==126
    # All 4 indicated dyadic subdivisions are strictly positive.
    left,right=bisect(pts)
    assert min(left)>0
    left2,right2=bisect(right)
    assert min(left2)>0
    left3,right3=bisect(right2)
    assert min(left3)>0 and min(right3)>0
    bounds=[min(left),min(left2),min(left3),min(right3)]
    print('B32_Certificate=PASS; intervals=4; degree=125; minimum_positive=',float(min(bounds)))

    n=33; A,B=powers(n); r=Q(10,11)
    t=50000*rational_eval(A,r)-8578*rational_eval(B,r)
    assert t<0
    print('P33_Exact_negative=PASS; rational_s=110; ratio=',float(formula_ratio(n,r)))
    # One-sided rational traps for the irrational target.
    assert Q(141421,100000)**2<2
    assert Q(70711,50000)**2>2
    # Thus 58578/100000 < 2-sqrt(2) < 58579/100000.
    for n in (2,3,4,5,8):
        for s in (Q(1,4),Q(1),Q(7,2)):
            # solve r/(1-r)^2=s using exact rational r only when square root rational;
            # instead compare with polynomial recurrence for R_{0,1}.
            if n==2:
                # Explicit path length two: R01=s/(1+2s)
                ratio=Q(2)*(1+s)/(1+2*s)
            else:
                e0,e1=Q(1),1+s
                vals=[e0,e1]
                for k in range(2,n): vals.append((1+2*s)*vals[-1]-s*s*vals[-2])
                D=(1+s)*vals[n-1]-s*s*vals[n-2]
                U=s*vals[n-2]
                # R01 from endpoint Cramer's rule
                R=mat_inverse([[Q(int(i==j))+s*((1 if i in (0,n-1) else 2) if i==j else (-1 if abs(i-j)==1 else 0)) for j in range(n)] for i in range(n)])
                assert R[0][1]==U/D
                ratio=sum(R[0][k]*R[k][1] for k in range(n))/R[0][1]
            assert ratio==matrix_ratio(n,s)
    # Exact comparison of rational generating-function ratio with direct matrix inverse
    # at r=1/2 -> s=2, and at r=2/3 -> s=6.
    for n in (2,3,5,8):
        for r in (Q(1,2),Q(2,3)):
            s=r/(1-r)**2
            assert formula_ratio(n,r)==matrix_ratio(n,s)
    print('Exact_matrix_replay=PASS; ratios_and_continuants=PASS')
    print('VERIFY_OK')

if __name__=='__main__': main()
