#!/usr/bin/env python3
"""Reproducibility checks for exact short-excursion bridge identities."""
from itertools import combinations
from math import comb, factorial
from fractions import Fraction

checks = 0

def eq(a,b,label):
    global checks
    checks += 1
    if a != b:
        raise AssertionError((label, a, b))

def cat(m):
    return comb(2*m,m)//(m+1)

def nonnegative_binom(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0

def hypergeom(n,k,j):
    if n==k:
        return Fraction(int(j==k),1)
    N=2*n-k-1
    return Fraction(nonnegative_binom(k-1,j)*nonnegative_binom(2*(n-k),n-j),comb(N,n))

def cat_power_coeff(m,k):
    if k==0:
        return int(m==0)
    return k*comb(2*m+k,m)//(2*m+k)

# All balanced words of length 2n, n <= 9. No Monte Carlo.
for n in range(1,10):
    count={}
    for plus_positions in combinations(range(2*n),n):
        plus=set(plus_positions)
        height=0; previous=0; K=J=0
        for i in range(2*n):
            height += 1 if i in plus else -1
            if height==0:
                K+=1
                J+=int((i+1)-previous==2)
                previous=i+1
        eq(height,0,'balanced endpoint')
        count[K,J]=count.get((K,J),0)+1
    eq(sum(count.values()),comb(2*n,n),'all bridges')
    for k in range(1,n+1):
        mass=sum(v for (kk,j),v in count.items() if kk==k)
        expected=2**k*cat_power_coeff(n-k,k)
        eq(mass,expected,'marginal return count')
        for j in range(k+1):
            eq(Fraction(count.get((k,j),0),mass),hypergeom(n,k,j), 'conditional mass')

# Independent Catalan-power convolution and all factorial moments.
for n in range(2,31):
    for k in range(1,n+1):
        total=cat_power_coeff(n-k,k)
        # Independent dynamic convolution: C(z)^k at coefficient n-k.
        p=[1]+[0]*(n-k)
        for _ in range(k):
            q=[0]*(n-k+1)
            for i,a in enumerate(p):
                for j in range(n-k-i+1):
                    q[i+j]+=a*cat(j)
            p=q
        eq(p[n-k],total,'Catalan convolution')
        for r in range(k+1):
            if n==k:
                expected=factorial(k)//factorial(k-r)
                actual=expected
            else:
                actual=Fraction(factorial(k),factorial(k-r))*Fraction(cat_power_coeff(n-k,k-r),total)
                if r>=k: expected=0
                else:
                    numerator=1;denominator=1
                    for s in range(r):
                        numerator*= (n-s)*(k-1-s)
                        denominator*= (2*n-k-1-s)
                    expected=Fraction(numerator,denominator)
            eq(actual,expected,'factorial moment')
print('PASS:',checks,'exact assertions')
