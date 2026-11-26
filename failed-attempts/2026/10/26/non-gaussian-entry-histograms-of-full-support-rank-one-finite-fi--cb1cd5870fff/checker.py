#!/usr/bin/env python3
"""Independent exact finite census and Fourier linear-algebra checks.

Run: python rank_one_support_checker.py
Only the Python standard library is required.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from cmath import exp, pi
from math import sqrt


def det(A):
    a=[list(map(float,row)) for row in A]
    n=len(a); d=1.0
    for i in range(n):
        pivot=max(range(i,n),key=lambda j:abs(a[j][i]))
        if abs(a[pivot][i])<1e-11:return 0.0
        if pivot!=i:a[i],a[pivot]=a[pivot],a[i];d=-d
        c=a[i][i];d*=c
        for j in range(i+1,n):
            f=a[j][i]/c
            for k in range(i+1,n):a[j][k]-=f*a[i][k]
    return d


def fourier_check(d):
    t=[((-1)**i)*(i+2)/7 for i in range(d)]
    P=[[float(i==j)-1/d for j in range(d)] for i in range(d)]
    B=[[t[(i+j)%d] for j in range(d)] for i in range(d)]
    PB=[[sum(P[i][k]*B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
    Q=[[sum(PB[i][k]*P[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
    E=[[float(i==j)+sum(Q[i][k]*Q[j][k] for k in range(d))/d**2 for j in range(d)] for i in range(d)]
    direct=det(E)**(-0.5)
    spectral=1.0
    for k in range(1,d):
        ht=sum(t[a]*exp(2j*pi*k*a/d) for a in range(d))
        spectral*=(1+(abs(ht)/d)**2)**(-.5)
    assert abs(direct-spectral)<1e-9,(d,direct,spectral)
    return round(direct,9)


def census(d,m,n):
    total=d**(m+n-1)
    S=[0]*d; P2=[[0]*d for _ in range(d)]
    pairs=Counter(); fourth=Fraction(0,1)
    seen=set()
    for raw in product(range(d), repeat=m+n-1):
        x=(0,)+raw[:m-1];y=raw[m-1:]
        matrix=tuple((x[i]+y[j])%d for i in range(m) for j in range(n))
        assert matrix not in seen
        seen.add(matrix)
        counts=[matrix.count(a) for a in range(d)]
        for a in range(d):
            S[a]+=counts[a]
            for b in range(d):P2[a][b]+=counts[a]*counts[b]
        if m*n>=4:pairs[(matrix[0],matrix[1],matrix[n],matrix[n+1])]+=1
        fourth+=((Fraction(counts[0],1)-Fraction(m*n,d))**4)/((m*n)**2)
    assert len(seen)==total
    for a in range(d):
        assert Fraction(S[a],total)==Fraction(m*n,d)
        for b in range(d):
            actual=Fraction(P2[a][b],total)-Fraction(m*n,d)**2
            expected=Fraction(m*n,d)*(a==b)-Fraction(m*n,d*d)
            assert actual==expected,(d,m,n,a,b,actual,expected)
    for i in range(4):
        for j in range(i+1,4):
            # indexes of the top-left 2x2 cells are 0,1,n,n+1
            c=Counter((p[i],p[j]) for p in pairs.elements())
            for a in range(d):
                for b in range(d):assert c[(a,b)]==total//(d*d)
    return total, float(fourth/total)


def main():
    cases=[(d,m,n) for d in (1,2,3,4,5) for m,n in ((2,2),(2,3),(3,3))]
    count=0
    for d,m,n in cases:
        total,fourth=census(d,m,n);count+=total
        print('d=%d m=%d n=%d distinct=%d scaled_fourth=%.9f'%(d,m,n,total,fourth))
    for d in range(1,7):print('d=%d CF=%.9f'%(d,fourier_check(d)))
    print('ALL_FULL_SUPPORT_RANK_ONE_CHECKS_PASSED cases=%d matrices=%d Fourier_cases=6'%(len(cases),count))

if __name__=='__main__':main()
