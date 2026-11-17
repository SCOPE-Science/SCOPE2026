#!/usr/bin/env python3
"""Exact finite tests for positional excedance covariances in uniform derangements."""
from itertools import permutations
from fractions import Fraction
from math import factorial, comb

def d(n):
    return sum((-1)**k*comb(n,k)*factorial(n-k) for k in range(n+1))

def H(n,m):
    return sum((-1)**k*comb(m,k)*factorial(n-2-k) for k in range(m+1))

def prob(n,i,j):
    A,B,C=(H(n,n-2),H(n,n-3),H(n,n-4))
    if not (1<=i<j<=n): raise ValueError
    return Fraction((n-j)*(B+(n-i-2)*C), d(n))

def formula(n,i,j):
    C=H(n,n-4)
    delta=Fraction(C,d(n))-Fraction(1,(n-1)**2)
    return -(i-1)*(n-j)*delta

def check():
    total=0
    for n in range(4,10):
        rows=[0]*n
        pair=[[0]*n for _ in range(n)]
        count=0
        for p in permutations(range(1,n+1)):
            if any(p[i]==i+1 for i in range(n)):
                continue
            count+=1
            ones=[i for i in range(n) if p[i]>i+1]
            for i in ones:rows[i]+=1
            for i in ones:
                for j in ones:
                    pair[i][j]+=1
        assert count==d(n)
        for i in range(n):
            assert Fraction(rows[i],count)==Fraction(n-1-i,n-1)
            total+=1
            for j in range(i+1,n):
                empirical=Fraction(pair[i][j],count)
                assert empirical==prob(n,i+1,j+1),(n,i,j,empirical,prob(n,i+1,j+1))
                expected=Fraction(rows[i]*rows[j],count**2)
                assert empirical-expected==formula(n,i+1,j+1),(n,i,j,empirical-expected,formula(n,i+1,j+1))
                total+=2
        print('n=',n,'derangements=',count, 'checked')
    for n in range(4,81):
        D=d(n); A,B,C=H(n,n-2),H(n,n-3),H(n,n-4)
        assert D==(n-1)*(B+(n-3)*C)
        assert D==A+2*(n-2)*B+(n-2)*(n-3)*C
        assert C* (n-1)**2>D
        assert ((n-1)**2*C-D)==(n-1)* (Fraction(n-1,n-3)*d(n-2)+d(n-3))
        total+=4
    print('PASS',total, 'exact assertions')
if __name__=='__main__':check()
