#!/usr/bin/env python3
"""Exact finite checks for a mixed isolated-chord/crossing identity."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial


def odd_double_factorial(n):
    v=1
    for j in range(1,n+1,2): v*=j
    return v

@lru_cache(None)
def pairings(endpoints):
    if not endpoints:
        return ((),)
    a=endpoints[0]
    return tuple(((a,b),)+tail
                 for bidx,b in enumerate(endpoints[1:])
                 for tail in pairings(endpoints[1:bidx+1]+endpoints[bidx+2:]))

def crosses(c,d):
    (a,b),(u,v)=c,d
    return (a<u<b<v) or (u<a<v<b)

def statistics(P):
    isolated=0
    crossing=0
    for i,c in enumerate(P):
        deg=0
        for j,d in enumerate(P):
            if j!=i and crosses(c,d):
                deg+=1
                if j>i: crossing+=1
        isolated += deg==0
    return isolated,crossing

def all_polys(n):
    counts=Counter()
    weighted=Counter()
    N=0
    sI=sX=sIX=0
    for P in pairings(tuple(range(2*n))):
        I,X=statistics(P)
        counts[X]+=1
        weighted[X]+=I
        N+=1
        sI+=I;sX+=X;sIX+=I*X
    return counts,weighted, (N,sI,sX,sIX)

def convolution(A,B):
    r=Counter()
    for i,a in A.items():
        for j,b in B.items():r[i+j]+=a*b
    return r

def rat_cov(n):
    den=odd_double_factorial(2*n-1)
    total=Fraction(0)
    for a in range(n):
        b=n-1-a
        p=Fraction(odd_double_factorial(2*a-1)*odd_double_factorial(2*b-1),den)
        total += p*(n-1+a*b)
    return -Fraction(n,3)*total

def main():
    polynomials={0:Counter({0:1})}
    tests=0
    for n in range(1,8):
        C,W,raw=all_polys(n)
        N,si,sx,six=raw
        assert N==odd_double_factorial(2*n-1)
        assert Fraction(sx,N)==Fraction(n*(n-1),6)
        assert Fraction(six,N)-Fraction(si*sx,N*N)==rat_cov(n)
        assert rat_cov(n)<0 if n>=2 else rat_cov(n)==0
        tests+=4
        polynomials[n]=C
        expected=Counter()
        for a in range(n):
            b=n-1-a
            for degree,coeff in convolution(polynomials[a],polynomials[b]).items():
                expected[degree]+=n*coeff
        assert W==expected, (n,W,expected)
        tests+=len(set(W)|set(expected))
        print('n',n,'pairings',N,'cov',rat_cov(n),'weighted polynomial degree',max(W))
    for n in range(2,250):
        assert rat_cov(n)<0
        tests+=1
    print('PASS exact assertions', tests)

if __name__=='__main__':main()
