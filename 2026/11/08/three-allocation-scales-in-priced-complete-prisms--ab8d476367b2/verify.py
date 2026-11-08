#!/usr/bin/env python3
"""Reproducible exact arithmetic and numerical smoke tests for the stated two-layer resistance theorem.
Only Python standard library is required; numerical checks support, not replace, the proof.
"""
from fractions import Fraction as F
from math import sqrt


def inverse(A):
    n=len(A)
    a=[list(A[i])+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j]);a[j],a[p]=a[p],a[j]
        v=a[j][j];a[j]=[t/v for t in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j]
                if v: a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]


def laplacian(n,a,b):
    N=2*n
    L=[[F(0) for _ in range(N)] for _ in range(N)]
    def edge(i,j,w):
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    for layer in (0,1):
        for i in range(n):
            for j in range(i+1,n): edge(2*i+layer,2*j+layer,a)
    for i in range(n): edge(2*i,2*i+1,b)
    return L


def kirkhoff_from_matrix(n,a,b):
    N=2*n
    L=laplacian(n,a,b)
    M=[[L[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    inv=inverse(M)
    return N*(sum(inv[i][i] for i in range(N))-1)


def kirkhoff_formula(n,a,b):
    return 2*n*(F(1,2*b)+F(n-1,n*a)+F(n-1,n*a+2*b))


def dF(n,c,r):
    S=F(n-1,n)+F(1,2*r)+F(n-1,n+2*r)
    Sp=-F(1,2*r*r)-F(2*(n-1),(n+2*r)**2)
    return c*S+(n-1+c*r)*Sp


def root(n,c):
    lo=F(1,1000000000);hi=F(n*n*n)
    assert dF(n,c,lo)<0 and dF(n,c,hi)>0
    for _ in range(130):
        mid=(lo+hi)/2
        if dF(n,c,mid)<0:lo=mid
        else:hi=mid
    return float((lo+hi)/2)


def main():
    count=0
    for n in range(4,10):
        for a in (F(1,3),F(1),F(5,2)):
            for b in (F(1,4),F(2,3),F(3,2)):
                A=kirkhoff_from_matrix(n,a,b)
                B=kirkhoff_formula(n,a,b)
                assert A==B,(n,a,b,A,B)
                count+=1
    for n in range(4,13):
        for c in (F(1,4),F(1),F(4),F(13,7)):
            r=root(n,c)
            assert abs(float(dF(n,c,F(r)))) < 1e-8
            # Exact derivative signs on a rational bracket, plus positive weights and budget.
            low=F(r)*F(999,1000); high=F(r)*F(1001,1000)
            assert dF(n,c,low)<0<dF(n,c,high)
            B=F(7)
            a=B/(n*(n-1+c*F(r)))
            b=F(r)*a
            assert a>0 and b>0 and n*(n-1)*a+n*c*b==B
            count+=4
    for c in (F(1,2),F(1),F(2),F(5)):
        n=100000
        r=root(n,c)
        if c<1:
            target=(sqrt(2/float(c)-1)-1)/2
            assert abs(r/n-target) < 0.008
        elif c==1:
            assert abs(r/(n**(2/3)) -0.5) < 0.012
        else:
            target=1/(2*sqrt(float(c)-1))
            assert abs(r/sqrt(n)-target) < 0.01
        count+=1
    print('VERIFY_OK',count)

if __name__=='__main__':main()
