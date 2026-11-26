#!/usr/bin/env python3
"""Independent coefficient-convolution and numerical checks for a four-tap moment inequality."""
from collections import defaultdict
from fractions import Fraction as Q
import cmath
import math

# Exact Laurent polynomials in two commuting unit-modulus indeterminates u, v.
def mul(a, b):
    result = defaultdict(int)
    for (i,j), c in a.items():
        for (k,l), d in b.items():
            result[(i+k, j+l)] += c*d
    return {k:v for k,v in result.items() if v}

poly = [ {(0,0):1}, {(0,0):1}, {(1,0):1}, {(0,1):1} ]
coeff = [ {} for _ in range(10) ]
coeff[0] = {(0,0):1}
cur = [ {(0,0):1} ]
for power in range(3):
    nextc = [defaultdict(int) for _ in range(len(cur)+3)]
    for k, c in enumerate(cur):
        for j, d in enumerate(poly):
            for ij,val in mul(c,d).items():
                nextc[k+j][ij] += val
    cur = [{k:v for k,v in dc.items() if v} for dc in nextc]
assert len(cur)==10
moment = defaultdict(int)
for c in cur:
    conj = {(-i,-j):v for (i,j),v in c.items()}
    for ij,v in mul(c,conj).items():
        moment[ij]+=v
expected = {(0,0):256}
for i,j,c in [(1,0,42),(1,-1,72),(2,-1,42),(0,1,3),(3,-2,3)]:
    expected[(i,j)] = c
    expected[(-i,-j)] = c
assert dict(moment)==expected
print('PASS: independent exact Laurent-coefficient sixth-moment identity')

# Exact algebra Q(sqrt(111)): represent a+b*sqrt(111).
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sc(a,c):return c*a[0],c*a[1]
def times(a,b):return a[0]*b[0]+111*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
one=(Q(1),Q(0)); zero=(Q(0),Q(0))
t=(Q(2),-Q(1,6))  # (12-sqrt(111))/6
t2=times(t,t);t3=times(t2,t)
stationary=add(add(sc(t2,Q(12)),sc(t,-Q(48))),(Q(11),Q(0)))
assert stationary==zero
minimum=add(add(add(sc(one,Q(112)),sc(t2,Q(288))),sc(t,-Q(132))),sc(t3,-Q(48)))
assert minimum==(Q(616),-Q(148,3))
assert 0<float(t[0]+t[1]*math.sqrt(111))<1
print('PASS: exact algebraic stationary root and exact sharp sixth-power constant')

uval=math.acos((math.sqrt(111)-12)/6)
opt=1+0j,1+0j,cmath.exp(1j*uval),cmath.exp(3j*uval)
def trig(phi,psi):
    return (256+84*math.cos(phi)+144*math.cos(phi-psi)+84*math.cos(2*phi-psi)
            +6*math.cos(psi)+6*math.cos(3*phi-2*psi))
def direct(phi,psi):
    u=cmath.exp(1j*phi);v=cmath.exp(1j*psi)
    c=[1+0j,1+0j,u,v]
    d=[0j]*10
    for i in range(4):
      for j in range(4):
       for k in range(4):d[i+j+k]+=c[i]*c[j]*c[k]
    return sum(abs(x)**2 for x in d)
for k in range(50):
    phi = (k*0.7142)% (2*math.pi)
    psi = (k*1.1198)%(2*math.pi)
    assert abs(direct(phi,psi)-trig(phi,psi))<3e-11
assert abs(direct(uval,3*uval)-(616-148*math.sqrt(111)/3))<1e-10
assert abs(direct(-uval,-3*uval)-(616-148*math.sqrt(111)/3))<1e-10
print('PASS: 50 independent complex-convolution phase comparisons and both extremizers')

# Independent circle quadrature (not used to establish global optimality).
for phi,psi in [(uval,3*uval),(-uval,-3*uval),(0.2,0.7),(2.1,5.0)]:
    N=256
    total=0.0
    for j in range(N):
        z=cmath.exp(2j*math.pi*j/N)
        P=1+z+cmath.exp(1j*phi)*z*z+cmath.exp(1j*psi)*z*z*z
        total += abs(P)**6/N
    assert abs(total-trig(phi,psi))<2e-11
print('PASS: four independent 256-point Fourier quadratures')
print('minimum sixth power: {:.14f}'.format(616-148*math.sqrt(111)/3))
print('optimal cosine: {:.14f}'.format((math.sqrt(111)-12)/6))
print('No finite numerical test is used as a proof of global minimality.')
