#!/usr/bin/env python3
"""Exact certificate checks for sharp quartic moments in H1 + H2 on S2.

Requires only the Python standard library. Does not replace the general proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, pi, sin, cos, sqrt
import random

def df_odd(i):
    v=1
    for j in range(1, i+1):v *= 2*j-1
    return v

def sphere_monomial(xpow, ypow, zpow):
    if xpow%2 or ypow%2 or zpow%2: return F(0)
    a,b,c=xpow//2, ypow//2, zpow//2
    if a+b+c==0: return F(1)
    return F(df_odd(a)*df_odd(b)*df_odd(c), df_odd(a+b+c+1))

def multiply(p,q):
    o={}
    for a,v in p.items():
        for b,w in q.items():
            k=tuple(x+y for x,y in zip(a,b))
            o[k]=o.get(k,F(0))+v*w
    return {k:v for k,v in o.items() if v}

def integral(p):return sum((v*sphere_monomial(*a) for a,v in p.items()),F(0))

def analytic(v,A):
    v2=sum(x*x for x in v)
    s2=sum(A[i][j]*A[i][j] for i in range(3) for j in range(3))
    av2=sum(sum(A[i][j]*v[j] for j in range(3))**2 for i in range(3))
    p=v2/F(3); q=F(2,15)*s2; S=p+q
    m2=S
    m4=F(9,5)*p*p + F(18,7)*p*q+F(15,7)*q*q+F(16,35)*av2
    low=F(45,28)*S*S+F(48,35)*(p-F(5,8)*S)**2+F(16,35)*av2
    high=F(375,112)*S*S-F(192,35)*(p-F(15,32)*S)**2-F(16,35)*(F(2,3)*v2*s2-av2)
    assert m4==low==high
    return m2,m4

def raw_integrals(v,A):
    f={}
    for i in range(3):f[tuple(1 if j==i else 0 for j in range(3))]=v[i]
    for i in range(3):
        for j in range(3):
            idx=tuple((1 if a==i else 0)+(1 if a==j else 0) for a in range(3))
            f[idx]=f.get(idx,F(0))+A[i][j]
    f={k:x for k,x in f.items() if x}
    f2=multiply(f,f)
    f4=multiply(f2,f2)
    return integral(f2),integral(f4)

rng=random.Random(24017)
for i in range(150):
    a=[F(rng.randint(-9,9),rng.randint(1,6)) for _ in range(3)]
    d,e=[F(rng.randint(-9,9),rng.randint(1,6)) for _ in range(2)]
    h,j,k=[F(rng.randint(-9,9),rng.randint(1,6)) for _ in range(3)]
    A=((d,h,j),(h,e,k),(j,k,-d-e))
    assert raw_integrals(a,A)==analytic(a,A)
print('EXACT_DIRECT_SPHERICAL_MONOMIAL_INTEGRALS_MATCH_INVARIANTS',150)

# Homogeneous deficit polynomial identities, checked by exact rational expansion.
p,q,t=F(5,8),F(3,8),F(0)
assert F(9,5)*p*p+F(18,7)*p*q+F(15,7)*q*q+F(16,35)*t == F(45,28)
p,q=F(15,32),F(17,32)
t=F(2,3)*(3*p)*(F(15,2)*q)
assert F(9,5)*p*p+F(18,7)*p*q+F(15,7)*q*q+F(16,35)*t ==F(375,112)
print('EXACT_BOTH_SHARP_ENDPOINTS_AND_INVARIANT_DEFICITS_OK')

# Independent 2-D surface quadrature (midpoint in z and longitude), for equality witnesses.
def quad(kind,N=400,M=480):
    tot2=tot4=0.
    for i in range(N):
        z=-1+(i+.5)*2/N; r=sqrt(1-z*z)
        for j in range(M):
            a=2*pi*(j+.5)/M; x=r*cos(a);y=r*sin(a)
            if kind=='min':f=x*x-y*y+2/sqrt(3)*z
            else:f=(3*z*z-1)+6/sqrt(17)*z
            tot2+=f*f;tot4+=f**4
    tot2/=N*M;tot4/=N*M
    return tot4/(tot2*tot2)
assert abs(quad('min')-float(F(45,28)))<2e-4
assert abs(quad('max')-float(F(375,112)))<2e-4
print('INDEPENDENT_GRID_QUADRATURE_ENDPOINT_WITNESSES_OK')
print('ALL_MIXED_SPHERICAL_HARMONIC_CHECKS_OK')
