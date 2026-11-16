#!/usr/bin/env python3
"""Independent finite numerical checks for the stated Legendre–Bernstein aliasing theorem.
Requires numpy and scipy; no network access or external files.
These finite tests do not prove the limiting theorem.
"""
import math
import numpy as np
from scipy.special import eval_legendre
from scipy.stats import binom

LIMIT = -math.sqrt(math.pi)/(4*math.sqrt(2))

def weighted_value(n, theta):
    j = np.arange(n+1)
    b = binom.pmf(j, n, theta/math.pi)
    a = eval_legendre(2*n-2, np.cos(math.pi*j/n))
    return float(np.dot(b,a))

def monopole(n, quadrature=450):
    z,w = np.polynomial.legendre.leggauss(quadrature)
    t=(z+1)/2
    j=np.arange(n+1)
    samples=eval_legendre(2*n-2, np.cos(math.pi*j/n))
    bern=binom.pmf(j[None,:],n,t[:,None]) @ samples
    return float((math.pi/4)*np.dot(w,np.sin(math.pi*t)*bern))

def reference(theta):
    return math.cos(1.5*theta+math.pi/4)/math.sqrt(math.pi*math.sin(theta))

def run():
    checks=0
    assert abs(LIMIT+0.3133285343288750628)<1e-14
    checks+=1
    for n in (9,12,20,40,80,160,320):
        val=monopole(n)
        assert math.isfinite(val)
        print(f'n={n:3d}, a_0={val:+.11f}, sqrt(n)*a_0={val*math.sqrt(n):+.11f}')
        if n>=9: assert val < 0
        checks+=2
    for n in (40,80,160,320):
        a=monopole(n)
        assert abs(math.sqrt(n)*a-LIMIT)<0.12
        checks+=1
    for theta in (math.pi/4, math.pi/2, 3*math.pi/4):
        for n in (128,512):
            observed=math.sqrt(n)*weighted_value(n,theta)
            expect=reference(theta)
            print(f'local n={n}, theta={theta/math.pi:.2f}pi: {observed:+.9f} vs {expect:+.9f}')
            assert abs(observed-expect)<0.025
            checks+=1
    for n in (8,20,40):
        # Independent integration of the Bernstein kernel using a second
        # low-order Gaussian rule to detect quadrature sensitivity.
        assert abs(monopole(n,360)-monopole(n,510))<4e-10
        checks+=1
    print(f'PASS: {checks} supplementary tests; leading constant {LIMIT:+.15f}')

if __name__=='__main__':run()
