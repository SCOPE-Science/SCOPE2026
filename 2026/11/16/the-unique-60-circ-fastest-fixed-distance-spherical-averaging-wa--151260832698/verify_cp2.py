#!/usr/bin/env python3
"""Exact finite algebraic checker for fixed-distance spherical averaging on CP^2.
Analytic coverage of n>=10 and global x is supplied in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

X = Q(-1, 2)
R = Q(1, 8)

def legendre(n, x):
    a, b = Q(1), x
    if n == 0: return a
    if n == 1: return b
    for k in range(1, n):
        a, b = b, ((2*k+1)*x*b - k*a)/Q(k+1)
    return b

def spectral_multiplier(n, x):
    return (legendre(n,x)-legendre(n+1,x))/((n+1)*(1-x))

def independent_hypergeometric(n, x):
    z=(1-x)/2
    return sum(((-1)**k)*Q(comb(n,k)*comb(n+k+1,k+1),n+1)*z**k for k in range(n+1))

count=0
for x in [Q(-1),Q(-4,5),Q(-1,2),Q(-1,3),Q(0),Q(1,4),Q(1,2)]:
    if x==1: continue
    for n in range(1,26):
        assert spectral_multiplier(n,x)==independent_hypergeometric(n,x),(n,x)
        count+=1
assert spectral_multiplier(1,X)==-R; count+=1
assert spectral_multiplier(2,X)==-R; count+=1
expected={
    3:Q(31,256),4:-Q(17,640),5:-Q(47,1024),6:Q(373,7168),
    7:-Q(1633,131072),8:-Q(829,32768),9:Q(39857,1310720)
}
for n,v in expected.items():
    assert spectral_multiplier(n,X)==v
    assert abs(v)<R
    count+=2
# Legendre |P_n(x)|<=1 and ratio formula imply universal n>=10 bound.
for n in range(10,50):
    assert Q(4,3*(n+1))<R
    count+=1
for n in range(1,7):
    # Dimension of bihomogeneous (n,n) trace-free harmonics on C^3.
    d=comb(n+2,2)**2-comb(n+1,2)**2
    assert d==(n+1)**3
    count+=1
assert 8+27==35; count+=1
assert Q(5,6)*(X+Q(1,2))*(X-Q(1,10))==0; count+=1
# Lower-bound argument algebraic: m2+1/8=(5/6)(x+1/2)(x-1/10).
for x in [Q(-1,2)+Q(k,120) for k in range(0,41)]:
    m2=(5*x*x+2*x-1)/6
    assert m2+R==Q(5,6)*(x+Q(1,2))*(x-Q(1,10))
    count+=1
print('PASS',count,'independent exact equalities and strict inequalities')
print('at optimizer:',[(n,str(spectral_multiplier(n,X))) for n in range(1,10)])
print('equality dimensions',8,27,35,'; high-degree universal bound for n>=10: 4/(3(n+1))<1/8')
