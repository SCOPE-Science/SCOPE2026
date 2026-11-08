#!/usr/bin/env python3
"""Exact finite symbolic checks of the stated spectral extremal law.

The proof is analytic; this bounded checker is supporting evidence only.
"""
from math import gcd, comb
from fractions import Fraction
from itertools import islice


def smallest_prime_factor(m):
    for p in range(2,m+1):
        if m%p==0:
            return p


def primitive(word):
    n=len(word)
    return not any(word==word[:d]*(n//d) for d in range(1,n) if n%d==0)


def minimum_normalized_log2_multiplier(word, m):
    # Monomial matrix JF^n: input coordinate j is sent to
    # (j+k) mod m and is multiplied in modulus by 2**exponent[j].
    k=sum(word)
    if not k:
        raise ValueError('all-left word is excluded')
    pos=list(range(m))
    exponents=[0]*m
    for r in word:
        for j in range(m):
            if r: # right branch: cyclic shift, scaling last-to-first
                if pos[j]==m-1:
                    exponents[j]+=1
                pos[j]=(pos[j]+1)%m
            elif pos[j]==0:
                exponents[j]+=1
    assert all(pos[j] == (j+k)%m for j in range(m))
    d=gcd(m,k)
    ell=m//d
    classes=[sum(exponents[j] for j in range(m) if j%d==q) for q in range(d)]
    assert sum(classes)==len(word)
    return Fraction(min(classes),ell*len(word))


def independent_circular_sets(n,p):
    if n<2*p:
        return 0
    return n*comb(n-p-1,p-1)//p


def predicted(m,n):
    p=smallest_prime_factor(m)
    min_exponent = min(Fraction(1,m),Fraction(p,m*n))
    if n>p:
        count=comb(n,p)-independent_circular_sets(n,p)
    elif n==1:
        count=1
    else:
        # Möbius-free enumeration of primitive binary necklaces is intentionally
        # performed directly to avoid reliance on another number-theoretic package.
        count=sum(primitive(tuple((w>>j)&1 for j in range(n))) for w in range(1,1<<n))
    return min_exponent,count


def exact_periodic_point(word,m):
    # Assemble the affine branch composition A*x+b with integer entries.
    a=[[int(i==j) for j in range(m)] for i in range(m)]
    b=[0]*m
    for r in word:
        if r:
            a=[[-2*a[-1][j] for j in range(m)]]+a[:-1]
            b=[1-2*b[-1]]+b[:-1]
        else:
            a=[[2*z for z in a[0]]]+a[1:]
            b=[1+2*b[0]]+b[1:]
    # Exact Gauss-Jordan solve (I-A)x=b.
    aug=[[Fraction(int(i==j)-a[i][j]) for j in range(m)]+[Fraction(b[i])] for i in range(m)]
    for i in range(m):
        row=next(k for k in range(i,m) if aug[k][i])
        aug[i],aug[row]=aug[row],aug[i]
        pivot=aug[i][i]
        aug[i]=[v/pivot for v in aug[i]]
        for k in range(m):
            if k!=i:
                t=aug[k][i]
                aug[k]=[aug[k][j]-t*aug[i][j] for j in range(m+1)]
    x=tuple(aug[i][-1] for i in range(m))
    y=x
    for r in word:
        assert (y[0]>=0)==bool(r),(word,m,x,y)
        y=((1-2*y[-1],)+y[:-1]) if r else ((1+2*y[0],)+y[1:])
        assert -1<=y[0]<=1 and all(0<=t<=1 for t in y[1:])
    assert y==x,(word,m,x,y)
    return x


def main():
    assertions=0
    for m in range(2,13):
        for n in range(1,11):
            exponents=[]
            for mask in range(1,1<<n):
                word=tuple((mask>>j)&1 for j in range(n))
                if primitive(word):
                    exponents.append(minimum_normalized_log2_multiplier(word,m))
            actual=(min(exponents),exponents.count(min(exponents)))
            expected=predicted(m,n)
            assert actual==expected,(m,n,actual,expected)
            assertions+=1
    orbit_checks=0
    for m in range(2,9):
        for n in range(1,9):
            p=smallest_prime_factor(m)
            # Select exact words with a spread of right counts, plus all optimal
            # combinatorial types for small n, without relying on floating point.
            cases=[tuple((mask>>j)&1 for j in range(n))
                   for mask in range(1,1<<n) if primitive(tuple((mask>>j)&1 for j in range(n)))]
            for word in cases if n<=5 else cases[:50]:
                exact_periodic_point(word,m)
                orbit_checks+=1
            if n>p:
                x=exact_periodic_point(tuple([0]*(n-p)+[1]*p),m)
                orbit_checks+=1
    print('PASS: %s exhaustive dimension-period multiplier cases and %s exact-rational physical periodic orbit constructions.'%(assertions,orbit_checks))

if __name__=='__main__':
    main()
