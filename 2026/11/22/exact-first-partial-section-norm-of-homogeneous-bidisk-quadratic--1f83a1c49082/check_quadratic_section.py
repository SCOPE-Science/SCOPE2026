#!/usr/bin/env python3
"""Exact two-point certificate and supplementary diagnostics for quadratic-section norms.

Pure Python standard library. The mathematical argument uses the displayed
interpolation certificate; finite samples are consistency checks only.
"""
from fractions import Fraction as F
import math
import cmath
import random

# Represent u+v*i*sqrt(3), with rational u,v.
def add(x,y):
    return (x[0]+y[0], x[1]+y[1])
def mul(x,y):
    return (x[0]*y[0]-3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def power(x,n):
    ans=(F(1),F(0))
    for _ in range(n):ans=mul(ans,x)
    return ans

def exact_certificate():
    z_plus=(F(1,2), F(1,2))
    z_minus=(F(1,2), F(-1,2))
    ell_plus=(F(1,2), F(-1,6))
    ell_minus=(F(1,2), F(1,6))
    for k,expected in ((0,F(1)),(1,F(1)),(2,F(0))):
        moment=add(mul(ell_plus,power(z_plus,k)),mul(ell_minus,power(z_minus,k)))
        assert moment==(expected,F(0)), (k,moment)
    # Squared modulus at z=e^{it}, s=cos(t), for P=1/2+z-z^2/4:
    # |P|^2 = 27/16 - (s-1/2)^2/2, the exact maximum is 27/16.
    a,b,c=F(1,2),F(1),F(-1,4)
    constant = a*a+b*b+c*c-2*a*c
    linear = 2*b*(a+c)
    quad=4*a*c
    assert (constant,linear,quad)==(F(25,16),F(1,2),F(-1,2))
    peak=constant+linear*F(1,2)+quad*F(1,4)
    assert peak==F(27,16)
    # The exact squared ratio of the partial-section norm to the full norm.
    assert (a+b)**2/peak==F(4,3)
    # At equality, dual phase forces c=(a-b)/2; stationarity then forces b=2a.
    for a_int in range(1,10):
        for b_int in range(1,10):
            a,b=F(a_int),F(b_int)
            c=(a-b)/2
            derivative=b*(a+c)+2*a*c
            assert derivative==(a+b)*(2*a-b)/2


def numerical_diagnostics():
    rng=random.Random(20261121)
    samples=360
    grid=3600
    nodes=[cmath.exp(2j*math.pi*k/grid) for k in range(grid)]
    threshold=2/math.sqrt(3)
    for j in range(samples):
        a=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        b=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        c=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        if not (abs(a)+abs(b)>1e-15):continue
        sample_max=max(abs(a+b*z+c*z*z) for z in nodes)
        # A lower-bound sample; for random triples equality has probability zero.
        assert (abs(a)+abs(b))/sample_max < threshold+1e-7,(j,a,b,c)
    for phi in range(0,360,15):
        t=math.pi*phi/180
        zeta=cmath.exp(1j*t)
        a=0.5*complex(math.cos(t/2),math.sin(t/2))
        b=zeta*complex(math.cos(t/2),math.sin(t/2))
        c=-0.25*zeta*zeta*complex(math.cos(t/2),math.sin(t/2))
        sampled_max=max(abs(a+b*z+c*z*z) for z in nodes)
        assert abs((abs(a)+abs(b))/sampled_max-threshold)<5e-7
    return samples+24

if __name__=='__main__':
    exact_certificate()
    count=numerical_diagnostics()
    print('QUADRATIC_BIDISK_SECTION_EXACT_CERTIFICATE_OK',count)
