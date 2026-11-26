#!/usr/bin/env python3
"""Exact rational coefficient verification of pair-distance moments in triangles.

All claims checked here concern symbolic polynomials, not random samples.
Requires only Python's standard library.
"""
from fractions import Fraction as F
from math import comb, factorial
from collections import defaultdict

def add(a,b):
    z=defaultdict(F)
    for t,v in a.items(): z[t]+=v
    for t,v in b.items(): z[t]+=v
    return {t:v for t,v in z.items() if v}

def scale(a,s): return {t:v*s for t,v in a.items() if v*s}

def mul(a,b):
    z=defaultdict(F)
    for t,v in a.items():
        for u,w in b.items(): z[tuple(i+j for i,j in zip(t,u))]+=v*w
    return {t:v for t,v in z.items() if v}

def power(a,k):
    out={(0,0,0):F(1)}
    for _ in range(k): out=mul(out,a)
    return out

x={(1,0,0):F(1)}
y={(0,1,0):F(1)}
z={(0,0,1):F(1)}
e1=add(add(x,y),z)
e2=add(add(mul(x,y),mul(x,z)),mul(y,z))
e3=mul(mul(x,y),z)

def Dmoment(p,q):
    acc=F(0)
    for a in range(p+1):
        for b in range(q+1):
            U=F(2*factorial(a)*factorial(b),factorial(a+b+2))
            V=F(2*factorial(p-a)*factorial(q-b),factorial(p+q-a-b+2))
            acc+=(-1)**(p+q-a-b)*comb(p,a)*comb(q,b)*U*V
    return acc

def moment(k):
    out={}
    for i in range(k+1):
        for j in range(k-i+1):
            h=k-i-j
            coeff=F(factorial(k),factorial(i)*factorial(j)*factorial(h))
            term=mul(mul(power(x,i),power(y,j)),power(add(add(x,y),scale(z,-1)),h))
            term=scale(term,coeff*Dmoment(2*i+h,2*j+h))
            out=add(out,term)
    return out

M1=scale(e1,F(1,18))
M2=scale(add(power(e1,2),scale(e2,-2)),F(1,60))
M3=scale(add(add(scale(power(e1,3),23),scale(mul(e1,e2),-62)),scale(e3,20)),F(1,4200))
for k,formula in ((1,M1),(2,M2),(3,M3)):
    assert moment(k)==formula,(k,moment(k),formula)
print('EXACT_SECOND_FOURTH_SIXTH_MOMENTS_PASSED')

# Independently verify inversion on a strict triangle of side-squares 9,16,20.
a,b,c=F(9),F(16),F(20)
s1=a+b+c;s2=a*b+a*c+b*c;s3=a*b*c
m1=s1/18
m2=(s1*s1-2*s2)/60
m3=(23*s1**3-62*s1*s2+20*s3)/4200
R1=18*m1
R2=(R1*R1-60*m2)/2
R3=210*m3-F(23,20)*R1**3+F(31,10)*R1*R2
assert (R1,R2,R3)==(s1,s2,s3)
print('INVERSE_COEFFICIENTS_PASSED')

# For r=1/20, two noncongruent strict triangles share the first two moments,
# with the third separating them by r**3/420.
r=F(1,20)
A=(1+r,1-r/2,1-r/2)
B=(1+r/2,1+r/2,1-r)
def sigma(v):
    p,q,t=v
    return p+q+t,p*q+p*t+q*t,p*q*t
sa,sb=sigma(A),sigma(B)
assert sa[:2]==sb[:2]
assert abs(sa[2]-sb[2])==r**3/2
assert abs(sa[2]-sb[2])/210==r**3/420
assert sorted(A)!=sorted(B)
assert min(A)>F(9,10) and min(B)>F(9,10)
print('TWO_MOMENT_NONIDENTIFIABILITY_AND_CUBIC_CUSP_PASSED')
print('ALL_CHECKS_PASSED')
