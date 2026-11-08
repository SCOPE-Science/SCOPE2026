#!/usr/bin/env python3
"""Checks for the five-tone Gaussian STFT zero-transition theorem.
Run: python3 CHECK.py (Python standard library only).
The all-parameter proof is in RESULT.md; finite evaluations are consistency tests.
"""
import cmath
import math
from fractions import Fraction

TAU=2*math.pi
C1=math.log(2)/2
C2=math.log(1+math.sqrt(5))/2

def amplitude(a,z):
    return 1+2*math.exp(-a)*cmath.cosh(z)+2*math.exp(-4*a)*cmath.cosh(2*z)

def spectral_roots(a):
    u=math.exp(a)
    disc=u**6-4*u**4+8
    ys=[(-u**3+cmath.sqrt(disc))/2,(-u**3-cmath.sqrt(disc))/2]
    roots=[]
    for y in ys:
        w=cmath.acosh(y/2)
        roots.extend([w,-w])
    return ys,roots

def stft_closed(t,xi,sigma,Omega):
    alpha=(sigma*Omega)**2/2
    z=sigma*sigma*Omega*xi+1j*Omega*t
    return math.sqrt(TAU)*sigma*cmath.exp(-1j*xi*t)*math.exp(-(sigma*xi)**2/2)*amplitude(alpha,z)

def stft_integral(t,xi,sigma,Omega):
    # Composite midpoint integration, fast tail; independent of closed formula.
    N=24000
    start=t-12*sigma
    h=24*sigma/N
    sm=0j
    for j in range(N):
        s=start+(j+.5)*h
        f=sum(cmath.exp(1j*k*Omega*s) for k in range(-2,3))
        sm+=f*math.exp(-.5*((s-t)/sigma)**2)*cmath.exp(-1j*xi*s)
    return sm*h

# Exact algebra, expanded by hand from the coefficients; no CAS needed.
def prod_polys(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r
assert prod_polys([-2,1],[-4,-2,1])==[8,0,-4,1]
assert Fraction(3,2)**4-2*Fraction(3,2)**3+2==Fraction(5,16)
assert 1+math.sqrt(5)>2

# Direct transform checks, covering constructive and destructive interference.
for t,xi,sigma,Omega in [(.3,.7,1.0,.9),(.9,-1.1,.8,1.3),(2.0,.2,1.4,.65)]:
    observed=stft_integral(t,xi,sigma,Omega)
    predicted=stft_closed(t,xi,sigma,Omega)
    assert abs(observed-predicted)<3e-10,(observed,predicted)

# All zeros are roots of the auxiliary quartic, with exactly four roots per cell.
for a in [.05,.2,.32,.4,.50,.55,.65,.75,1.1,1.5]:
    ys,zs=spectral_roots(a)
    assert len(zs)==4
    for z in zs:
        assert abs(amplitude(a,z))<1e-8,(a,z,amplitude(a,z))
        u=math.exp(a); w=cmath.exp(z)
        quartic=math.exp(-4*a)*(w**4+1)+math.exp(-a)*(w**3+w)+w*w
        assert abs(quartic)<1e-8,(a,z,quartic)
    if a<C1:
        assert all(abs(y.imag)<1e-11 and -2<y.real<2 for y in ys)
        assert all(abs(z.real)<1e-11 for z in zs)
    elif a<C2:
        assert all(abs(y.imag)>1e-7 for y in ys)
        assert all(abs(z.real)>1e-7 for z in zs)
        assert all(.001<abs(z.imag)<math.pi-.001 for z in zs)
    else:
        assert all(abs(y.imag)<1e-11 and y.real<-2 for y in ys)
        assert all(abs(z.real)>1e-7 and abs(abs(z.imag)-math.pi)<1e-11 for z in zs)

# Two precisely stated critical parameters: two geometrically distinct double roots.
for a in [C1,C2]:
    u=math.exp(a)
    disc=u**6-4*u**4+8
    assert abs(disc)<1e-11
    y=-u**3/2
    z=cmath.acosh(y/2)
    assert abs(amplitude(a,z))<1e-10
    assert abs(2*math.exp(-a)*cmath.sinh(z)+4*math.exp(-4*a)*cmath.sinh(2*z))<1e-10
    second=2*math.exp(-a)*cmath.cosh(z)+8*math.exp(-4*a)*cmath.cosh(2*z)
    assert abs(second)>1e-8
    if a==C1:
        assert abs(z.real)<1e-10 and abs(z.imag-3*math.pi/4)<1e-10
    else:
        assert z.real>0 and abs(z.imag-math.pi)<1e-10

# Nonvanishing at ±2: the only possible multiplicity stems from discriminant zero.
for a in [0,.1,.3,C1,.4,C2,.75,1.5,3]:
    u=math.exp(a)
    assert u**4-2*u**3+2>=5/16-1e-12
    assert u**4+2*u**3+2>0

print('ALL_FIVE_TONE_CHECKS_PASSED')
