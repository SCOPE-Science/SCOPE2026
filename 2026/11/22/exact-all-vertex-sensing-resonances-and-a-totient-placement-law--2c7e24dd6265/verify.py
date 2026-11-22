#!/usr/bin/env python3
"""Finite independent checks for the one-defect ring placement theorem.
Standard library only. Integer-scaled exact Krylov ranks and a trigonometric exclusion predicate.
The analytic theorem is proved in RESULT.md; finite checks are not its proof.
"""
from fractions import Fraction
from math import gcd, sin, pi

def exclusion(n, site, w):
    j = min(site, n-1-site)
    if w == 1:
        return True
    if n % 2 and j == n//2:
        return True
    if n % 2 == 0 and gcd(2*j+1,n//2)>1:
        return True
    if j == 0:
        return False
    N = n-2*j-1
    for k in range(1, (N-1)//2+1):
        theta = 2*pi*k/N
        sj = sin(j*theta)
        if abs(sj) < 1e-11:
            continue
        predicted = (1-sin((j+1)*theta)/sj)/2
        if predicted>0 and abs(float(w)-predicted)<1e-10:
            return True
    return False

def krylov_rank(n,site,w):
    w = Fraction(w)
    denominator = w.denominator
    L = [[0]*n for _ in range(n)]
    for i in range(n):
        h=(i+1)%n
        a=(w.numerator if i==n-1 else denominator)
        L[i][i]+=a; L[h][h]+=a; L[i][h]-=a; L[h][i]-=a
    columns=[]
    v=[int(i==site) for i in range(n)]
    for _ in range(n):
        columns.append(v)
        v=[sum(L[i][k]*v[k] for k in range(n)) for i in range(n)]
    A=[[Fraction(columns[c][r]) for c in range(n)] for r in range(n)]
    rank=0
    for c in range(n):
        pivot=next((r for r in range(rank,n) if A[r][c]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        z=A[rank][c]
        for r in range(rank+1,n):
            if A[r][c]:
                mult=A[r][c]/z
                for q in range(c+1,n): A[r][q]-=mult*A[rank][q]
                A[r][c]=Fraction(0)
        rank+=1
        if rank==n:break
    return rank

def verify():
    cases=0
    for n in range(5,16):
        for site in range(n):
            for w in (Fraction(1,2),Fraction(1,3),Fraction(3,4),Fraction(2),Fraction(1)):
                r=krylov_rank(n,site,w)
                if (r<n)!=exclusion(n,site,w):
                    raise AssertionError((n,site,str(w),r))
                if n%2 and w==Fraction(1,2):
                    j=min(site,n-1-site);m=(n-1)//2
                    expected = m if j==m else gcd(m+1,j+1)-1
                    if n-r != expected:raise AssertionError(('nullity',n,j,n-r,expected))
                cases+=1
    # Totient census, analytically predicted; its small instances also checked above.
    for n in range(5,30,2):
        m=(n-1)//2
        count=sum(gcd(j+1,m+1)==1 for j in range(m))*2
        phi=sum(gcd(k,m+1)==1 for k in range(1,m+2))
        assert count == 2*phi
    print('VERIFY_OK',cases,'exact_ranks',13,'totient_checks')
if __name__=='__main__':verify()
