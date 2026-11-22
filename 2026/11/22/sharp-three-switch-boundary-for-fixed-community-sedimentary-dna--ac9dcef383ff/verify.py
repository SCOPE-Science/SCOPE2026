#!/usr/bin/env python3
"""Supplementary arithmetic checks for a two-source marker-preservation theorem.

The analytic proof, not these finite tests, establishes the universal bound.
"""
from fractions import Fraction as F
import math
import random


def poly(u):
    return u**5 - 4*u**4 + 9*u - 4


def g(x, a, b):
    return (b-a)*x/((x+a)*(x+b))


def ratio(t,q,k,d,a,b,K):
    x=q*math.exp(k*t)
    return K*math.exp(-d*t)*(x+a)/(x+b)


def ratio_orig(t,q,k,la,lb,A0,A1,B0,B1):
    x=q*math.exp(k*t)
    p=1.0/(1+x)
    ca=math.exp(-la*t)*(p*A0+(1-p)*A1)
    cb=math.exp(-lb*t)*(p*B0+(1-p)*B1)
    return ca/cb


assert poly(F(1,10)) == F(-310039,100000)
assert poly(F(1,2)) == F(9,32)
assert poly(F(1)) == F(2)
assert poly(F(2)) == F(-18)
assert poly(F(4)) == F(32)

k=4.0; d=1.0; a=1.0; b=9.0; q=1e-4
xc=(a*b)**0.5
crit=k*(math.sqrt(b)-math.sqrt(a))/(math.sqrt(b)+math.sqrt(a))
assert abs(crit-2.0)<1e-14
xm=11.0-4*math.sqrt(7)
xp=11.0+4*math.sqrt(7)
assert 0<q<xm<xc<xp
for x in (xm,xp):
    assert abs(d*(x+a)*(x+b)-k*(b-a)*x)<1e-12
assert k*g(xm*.5,a,b)<d
assert k*g((xm+xp)/2,a,b)>d
assert k*g(xp*2,a,b)<d

for uleft,uright in [(F(1,10),F(1,2)),(F(1),F(2)),(F(2),F(4))]:
    assert poly(uleft)*poly(uright)<0

# Compare two algebraically identical representations for a fixed exact witness.
for j in range(601):
    t=0.02*j
    lhs=ratio(t,q,k,d,a,b,40.0)
    rhs=ratio_orig(t,q,k,2.0,1.0,40.0,40.0,9.0,1.0)
    assert abs(lhs-rhs)<1e-10*max(1.0,lhs,rhs)

# The signed derivatives are controlled by a single-peaked rational kernel.
rg=random.Random(20231117)
for j in range(5000):
    a=10**rg.uniform(-3,3)
    b=a*10**rg.uniform(0.01,3)
    x=10**rg.uniform(-5,5)
    h=max(1e-7*x,1e-12)
    numeric=(g(x+h,a,b)-g(max(1e-15,x-h),a,b))/(x+h-max(1e-15,x-h))
    algebra=(b-a)*(a*b-x*x)/((x+a)**2*(x+b)**2)
    assert math.copysign(1,numeric)==math.copysign(1,algebra) or abs(numeric)<1e-10*max(1,abs(algebra))
    dmax=(math.sqrt(b)-math.sqrt(a))/(math.sqrt(b)+math.sqrt(a))
    assert g(x,a,b)<=dmax*(1+1e-12)

print('PASS: exact rational witness, critical points, 601 model equivalences and 5000 derivative/peak samples')
