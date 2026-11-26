#!/usr/bin/env python3
"""Exact checks for prime-square gcd-difference circulant Smith factors.

Uses only Python's standard library. Finite checks corroborate, but do not
replace, the universal unimodular-equivalence proof in RESULT.md.
"""
from math import comb, gcd, prod
from itertools import combinations


def proposed(p):
    b = p - 1
    return ([1] + [b] * (p-1) + [p*b] * (p*(p-2))
            + [p*p*b] + [2*p*p*b] * (p-2)
            + [2*p*p*b*(3*p-2)])


def bareiss(A):
    n=len(A)
    if n==0: return 1
    a=[row[:] for row in A]
    sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            i=next((i for i in range(k+1,n) if a[i][k]),None)
            if i is None:return 0
            a[k],a[i]=a[i],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def actual_factors(A):
    n=len(A);dprev=1;out=[]
    ids=range(n)
    for k in range(1,n+1):
        g=0
        for rows in combinations(ids,k):
            for cols in combinations(ids,k):
                m=[[A[i][j] for j in cols] for i in rows]
                g=gcd(g,abs(bareiss(m)))
                if g==dprev and g!=0:break
            if g==dprev and g!=0:break
        assert g and g%dprev==0
        out.append(g//dprev);dprev=g
    return out


def main():
    for p in (2,3):
        n=p*p
        A=[[gcd(abs(i-j),n) for j in range(n)] for i in range(n)]
        assert actual_factors(A)==proposed(p),(p,actual_factors(A),proposed(p))
    for p in (2,3,5,7,11,13,17,19,23,29):
        b=p-1;c=p*b;u=2*p-1;v=p*(3*p-2)
        K=[[c,0,0,0],[0,c,0,0],[u,0,v,0],[1,b,p,2*c]]
        assert actual_factors(K)==[1,b,b*p*p,2*b*p*p*(3*p-2)]
        B=[[c,0],[b,2*c]]
        assert actual_factors(B)==[b,2*b*p*p]
        factors=proposed(p)
        assert len(factors)==p*p
        assert all(factors[i+1]%factors[i]==0 for i in range(p*p-1))
        expected=(p*(p-1))**(p*(p-1))*(2*p*(p-1))**(p-1)*p*(3*p-2)
        assert prod(factors)==expected
    print('VERIFY_OK exhaustive_full_SNF p=2,3; exact_core_SNF 10 primes; factor_chains_and_determinants 10 primes')

if __name__=='__main__':main()
