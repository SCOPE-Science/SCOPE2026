#!/usr/bin/env python3
"""Reproduce numerical checks for the acute spherical-triangle cosine moment.
Python >=3.10; standard library only.  The proof in RESULT.md is analytical.
"""
import math
import random

PI = math.pi
P0 = 1/(2*PI)-1/8
I0 = (PI-2)/64


def quadrature(nd=1000, nt=600):
    """Direct midpoint quadrature of the conditional latitude/longitude integral."""
    step = PI/(2*nd)
    p = 0.0
    mom = 0.0
    for i in range(nd):
        d = step*(i+0.5)
        sd = math.sin(d/2)
        sd2 = sd*sd
        dt = d/(2*nt)
        acc = 0.0
        for j in range(nt):
            t = dt*(j+0.5)
            st = math.sin(t)
            ct = math.cos(t)
            num = max(0.0, sd2-st*st)
            den = ct*ct-sd2
            acc += 1 - math.sqrt(num/den)
        a = dt*acc/PI
        w = 0.5*step*math.sin(d)*a
        p += w
        mom += w*math.cos(d)
    return p, mom


def uniform_point(rng):
    z = 2*rng.random()-1
    t = 2*PI*rng.random()
    r = math.sqrt(1-z*z)
    return (r*math.cos(t), r*math.sin(t), z)


def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]


def acute(a,b,c):
    p = dot(a,b)
    q = dot(a,c)
    r = dot(b,c)
    return r-p*q>0 and q-p*r>0 and p-q*r>0


def monte_carlo(n=550000, seed=390847):
    rng = random.Random(seed)
    hits=0
    pair=0.0
    dipole=0.0
    pinned_deriv=0.0
    epsilon=0.7
    north=(0.0,0.0,1.0)
    for _ in range(n):
        x=uniform_point(rng)
        y=uniform_point(rng)
        z=uniform_point(rng)
        if acute(x,y,z):
            hits += 1
            pair += dot(x,y)
            dipole += ((1+epsilon*x[2])*(1+epsilon*y[2])*(1+epsilon*z[2]))
        if acute(north,y,z):
            pinned_deriv += y[2]+z[2]
    return hits/n, pair/n, dipole/n, pinned_deriv/n


def main():
    pq, iq=quadrature()
    assert abs(pq-P0)<1e-5, (pq,P0)
    assert abs(iq-I0)<1e-5, (iq,I0)
    pm, im, pd, derivative=monte_carlo()
    epsilon=.7
    assert abs(pm-P0)<.002, (pm,P0)
    assert abs(im-I0)<.002, (im,I0)
    assert abs(pd-(P0+I0*epsilon**2))<.002, (pd,P0+I0*epsilon**2)
    assert abs(derivative-2*I0)<.003, (derivative,2*I0)
    print('ACUTE_SPHERE_CHECK_OK')
    print('integral_p0',format(pq,'.12f'),'exact',format(P0,'.12f'))
    print('integral_cos_moment',format(iq,'.12f'),'exact',format(I0,'.12f'))
    print('mc',dict(p0=pm,cos_moment=im,dipole_probability=pd,pinned_vmf_slope=derivative))

if __name__ == '__main__':
    main()
