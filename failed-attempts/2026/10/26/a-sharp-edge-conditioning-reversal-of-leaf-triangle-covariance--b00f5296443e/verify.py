#!/usr/bin/env python3
"""Exact finite checks for triangle-count versus degree-one-count dependence in fixed-edge uniform graphs."""
from fractions import Fraction
from itertools import combinations
from math import comb, exp

def falling(x, k):
    y=1
    for j in range(k):
        y *= x-j
    return y

def moments_formula(n,m):
    M=comb(n,2);d=n-1
    ET=Fraction(comb(n,3)*falling(m,3),falling(M,3)) if m>=3 else Fraction(0)
    if 1<=m<=M-d+1:
        EL=Fraction(n*d*m*falling(M-m,d-1),falling(M,d))
    else:
        EL=Fraction(0)
    if m>=3 and EL:
        Q=Fraction((n+1)*(n*n-n-4),n*(n*n-3*n-2))
        cov=ET*EL*(Q*Fraction(m-3,m)-1)
    else:
        cov=Fraction(0)
    return ET,EL,cov

def brute(n):
    edges=list(combinations(range(n),2));M=len(edges)
    triangles=[tuple(edges.index(e) for e in combinations(triple,2)) for triple in combinations(range(n),3)]
    sums=[[0,0,0,0] for _ in range(M+1)]
    for mask in range(1<<M):
        m=mask.bit_count()
        degrees=[0]*n
        for k,(a,b) in enumerate(edges):
            if mask>>k&1: degrees[a]+=1;degrees[b]+=1
        L=sum(deg==1 for deg in degrees)
        T=sum(all(mask>>k&1 for k in tri) for tri in triangles)
        a=sums[m];a[0]+=1;a[1]+=L;a[2]+=T;a[3]+=L*T
    total=[sum(row[k] for row in sums) for k in range(4)]
    NN,LL,TT,LT=total
    actual_cov_np=Fraction(LT,NN)-Fraction(LL,NN)*Fraction(TT,NN)
    p=Fraction(1,2)
    exp_L=n*(n-1)*p*(1-p)**(n-2)
    exp_T=comb(n,3)*p**3
    assert actual_cov_np == -Fraction(3,n)*exp_L*exp_T,(n,actual_cov_np)
    for m,(N,sumL,sumT,sumLT) in enumerate(sums):
        bT,bL,bcov=moments_formula(n,m)
        actualT=Fraction(sumT,N);actualL=Fraction(sumL,N)
        actualcov=Fraction(sumLT,N)-actualT*actualL
        assert (bT,bL,bcov)==(actualT,actualL,actualcov),(n,m,(bT,bL,bcov),(actualT,actualL,actualcov))
    return len(sums)

def sign(x):return (x>0)-(x<0)

def sign_expected(n,m):
    M=comb(n,2)
    if m<3 or m>M-n+2 or n<=3: return 0
    if n==4: return -1 if m==3 else 1
    return -1 if m<=n else 1

if __name__=='__main__':
    count=0
    for n in range(4,7):
        t=brute(n); count+=t
        print(f'exhaustive n={n}: all {t} edge-count strata OK, {1<<comb(n,2)} labeled graphs')
    checked=0
    for n in range(4,501):
        M=comb(n,2)
        # All low edge counts, transitions and upper boundary, with exact arithmetic.
        ms=sorted(set([0,1,2,3,4,n-1,n,n+1,n+2,M-n+1,M-n+2,M-n+3,M-1,M]))
        for m in ms:
            if not 0<=m<=M:continue
            x=moments_formula(n,m)[2]
            assert sign(x)==sign_expected(n,m),(n,m,x,sign_expected(n,m))
            checked+=1
    print('exact sign checks:',checked)
    for c in (Fraction(1,2),Fraction(3,4),Fraction(5,4),Fraction(2,1)):
        approx=8*float(c)**3*(float(c)-1)*exp(-2*float(c))
        seq=[]
        for n in (200,500,1000):
            m=int(c*n)
            seq.append(float(moments_formula(n,m)[2]))
        assert abs(seq[-1]-approx)<0.04, (c,seq,approx)
        print(f'sparse limit c={c}: finite={seq}, limit={approx:.9f}')
    print('ALL CHECKS PASSED')
