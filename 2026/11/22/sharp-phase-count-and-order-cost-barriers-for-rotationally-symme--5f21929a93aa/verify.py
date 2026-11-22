#!/usr/bin/env python3
"""Exact arithmetic checks for sharp phase-count and order-cost laws.
Standard library only; finite verification supports but does not replace proof.
"""
from fractions import Fraction as Q
from math import comb, factorial, pi, sqrt, isclose
import cmath

checks=0
def check(cond, name):
    global checks
    checks+=1
    if not cond: raise AssertionError(name)

def add(a,b):
    c=a.copy()
    for k,v in b.items(): c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}
def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items(): c[i+j]=c.get(i+j,0)+x*y
    return {k:v for k,v in c.items() if v}
def hermite(p):
    if p==0:return {0:1}
    h0,h1={0:1},{1:1}
    for n in range(1,p):
        h0,h1=h1,add({k+1:v for k,v in h1.items()},{k:-n*v for k,v in h0.items()})
    return h1
def mom(k):
    if k%2:return 0
    a=1
    for j in range(1,k,2):a*=j
    return a

def c_direct(p,m):
    a=mul(mul(hermite(p),hermite(p)),{2*m:1})
    return Q(sum(v*mom(k) for k,v in a.items()),factorial(m)**2)

def c_closed(p,m):
    return Q(factorial(2*m),factorial(m)**2)*sum((Q(factorial(p-j)*comb(p,j)**2,2**(m-j)*factorial(m-j)) for j in range(m+1)),Q(0))

def var_closed(p):
    return Q(comb(2*p,p))*sum((Q(comb(p,k)**2,2**k) for k in range(p+1)),Q(0))-1

for p in range(1,17):
    hp=hermite(p)
    check(sum(v*mom(k+p) for k,v in hp.items())==factorial(p),f'Hermite Stein expectation p={p}')
    check(c_direct(p,p)-1==var_closed(p),f'variance p={p}')
    for m in range(p):
        check(c_direct(p,m)==c_closed(p,m),f'product formula p,m={p,m}')
        check(sum(v*mom(k+m) for k,v in hp.items())==0,f'orthogonality p,m={p,m}')
    check(var_closed(p)>0,f'variance positive p={p}')

for p in range(2,16):
    for n in range(1,p):
        m=1+(p-1)%n
        check(1<=m<p and (p-m)%n==0,f'least residual p,n={p,n}')
        check(c_closed(p,m)>0,f'positive diverging coefficient p,n={p,n}')
        # each Fourier root filter annihilates all in-range exponents but the same residue
        for exponent in range(1,p+1):
            val=sum(cmath.exp(2j*pi*j*(exponent-p)/n) for j in range(n))/n
            check(abs(val-(1 if (exponent-p)%n==0 else 0))<1e-10,f'phase filter {p,n,exponent}')

# The p-1 phase witness has the particularly simple moment (2p+1)p!.
for p in range(2,20):
    check(c_closed(p,1)==(2*p+1)*factorial(p),f'sharp adjacent phase coefficient p={p}')

# Legendre integral identity and growing-order asymptotic, independent numerical evidence.
# Legendre recurrence at x=3, using integers only.
P0,P1=1,3
for p in range(1,51):
    if p==1:P=P1
    else:
        P2=Q((2*p-1)*3*P1-(p-1)*P0,p)
        P0,P1=P1,P2;P=P2
    check(Q(comb(2*p,p)*P,2**p)-1==var_closed(p),f'Legendre identity p={p}')
root=6+4*sqrt(2)
constant=(1+sqrt(2))/(pi*2**1.25)
for p,lower in [(15,.97),(30,.98),(100,.99)]:
    v=float(var_closed(p))
    ratio=v/(constant*root**p/p)
    check(lower<ratio<1.01,f'asymptotic approximate p={p} ratio={ratio}')
print('VERIFY_OK',checks)
