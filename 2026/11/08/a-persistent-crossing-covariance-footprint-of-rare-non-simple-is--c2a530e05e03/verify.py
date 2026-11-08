#!/usr/bin/env python3
"""Exact finite checks for isolation–crossing dependence in uniform chord diagrams.
No external packages required. Finite checks supplement, but do not replace, the proof.
"""
from fractions import Fraction
from collections import Counter
from functools import lru_cache
from math import comb

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    first=vertices[0]
    return tuple(((first, partner),)+tail
                 for partner in vertices[1:]
                 for tail in matchings(tuple(v for v in vertices[1:] if v!=partner)))

def crosses(ab,cd):
    a,b=ab; c,d=cd
    return (a<c<b<d) or (c<a<d<b)

def stats(matching):
    degrees=[0]*len(matching)
    for i in range(len(matching)):
        for j in range(i+1,len(matching)):
            if crosses(matching[i],matching[j]):
                degrees[i]+=1; degrees[j]+=1
    return sum(degrees)//2, sum(d==0 for d in degrees)

def odd_double_factorial(j):
    assert j>=0
    k=1
    for t in range(1,2*j,2): k*=t
    return k

def q(n,a):
    b=n-1-a
    return Fraction(odd_double_factorial(a)*odd_double_factorial(b),odd_double_factorial(n))

def predicted_cov(n):
    return -Fraction(n,3)*sum((q(n,a)*(n-1+a*(n-1-a)) for a in range(n)),Fraction())

def empirical(n):
    allm=matchings(tuple(range(2*n)))
    N=len(allm)
    xs,ys=zip(*(stats(m) for m in allm))
    EX=Fraction(sum(xs),N); EI=Fraction(sum(ys),N)
    cov=Fraction(sum(a*b for a,b in zip(xs,ys)),N)-EX*EI
    ss=[sum(min(b-a, 2*n-(b-a))==1 for a,b in m) for m in allm]
    ES=Fraction(sum(ss),N)
    covsimple=Fraction(sum(x*s for x,s in zip(xs,ss)),N)-EX*ES
    covrare=Fraction(sum(x*(y-s) for x,y,s in zip(xs,ys,ss)),N)-EX*(EI-ES)
    varx=Fraction(sum(a*a for a in xs),N)-EX*EX
    return cov,varx,EI,N,covsimple,covrare

checks=0
for n in range(2,8):
    cov,varx,EI,N,covsimple,covrare=empirical(n)
    assert N==odd_double_factorial(n); checks+=1
    assert cov==predicted_cov(n); checks+=1
    assert varx==Fraction(n*(n-1)*(n+3),45); checks+=1
    assert EI==n*sum((q(n,a) for a in range(n)),Fraction()); checks+=1
    assert cov<0;checks+=1
    assert covsimple==-Fraction(2*n*(n-1),3*(2*n-1)); checks+=1
    assert covrare==cov-covsimple; checks+=1
    assert covrare== -Fraction(n,3)*sum((q(n,a)*(n-1+a*(n-1-a)) for a in range(1,n-1)),Fraction()); checks+=1
    assert covrare<0 if n>=3 else covrare==0;checks+=1
    print('n=',n,'pairings=',N,'covariance=',cov,'variance_crossings=',varx)

# Conditioned on one isolated chord, the crossing count is the convolution
# of independent uniform diagrams on its two complementary arcs.
for n in range(2,6):
    matches=matchings(tuple(range(2*n)))
    for a in range(n):
        b=n-1-a
        fixed=(0,2*a+1)
        observed=Counter()
        for m in matches:
            if fixed in m:
                index=m.index(fixed)
                deg=sum(crosses(fixed,c) for c in m if c!=fixed)
                if deg==0: observed[stats(m)[0]]+=1
        expected=Counter()
        left=matchings(tuple(range(2*a)))
        right=matchings(tuple(range(2*b)))
        for ml in left:
            for mr in right:
                expected[stats(ml)[0]+stats(mr)[0]]+=1
        assert observed==expected, (n,a,observed,expected)
        checks+=1

# Orthogonal finite checks: exact q-ratio and simple-chord factorial moments.
for n in range(2,50):
    for a in range(n-1):
        assert q(n,a+1)/q(n,a)==Fraction(2*a+1,2*n-2*a-3)
        checks+=1
    mean_simple=Fraction(2*n,2*n-1)
    second_factorial=Fraction(2*n,2*n-1)
    assert mean_simple==second_factorial; checks+=1

# Numerical evaluations of the exact rational identity illustrate the
# three-term asymptotic but are NOT the proof of the infinite statement.
for n in (20,40,80,160,320,640):
    c=predicted_cov(n)
    cS=-Fraction(2*n*(n-1),3*(2*n-1))
    cR=c-cS
    approxR=-Fraction(1,3)-Fraction(11,12*n)
    assert abs(cR-approxR)*n*n<10;checks+=1
    approx=-Fraction(n,3)-Fraction(1,6)-Fraction(5,6*n)
    assert abs(c-approx)*n*n<10
    checks+=1

print('PASS:',checks,'exact assertions; finite tests are not infinite proofs')
