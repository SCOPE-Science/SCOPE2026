#!/usr/bin/env python3
"""Numerical diagnostics for isotropic width moments of a disk-plus-segment solid.

No external packages required. These finite checks are diagnostic; the global
identities and strict inequalities follow from the accompanying analytic proof.
"""
import math
import random

PI = math.pi


def simpson(f, lo, hi, n=4096):
    assert n > 0 and n % 2 == 0
    h = (hi - lo) / n
    acc = f(lo) + f(hi)
    for j in range(1, n):
        acc += (4 if j % 2 else 2) * f(lo + h*j)
    return acc * h / 3.0


def ellipse(m):
    if m == 1.0:
        return float('inf'), 1.0
    K = simpson(lambda t: 1.0/math.sqrt(1.0-m*math.sin(t)**2), 0, PI/2)
    E = simpson(lambda t: math.sqrt(1.0-m*math.sin(t)**2), 0, PI/2)
    return K,E


def mixed_formula(m):
    if m == 1.0:
        return 4.0/(3.0*PI)
    K,E = ellipse(m)
    return 2.0*(2.0*E-(1.0-m)*K)/(3.0*PI)


def mixed_independent(theta):
    s,c = math.sin(theta),math.cos(theta)
    def integrand(t):
        a = c*t
        b = s*math.sqrt(max(0.0,1.0-t*t))
        if a >= b:
            avg = a
        else:
            avg = 2.0/PI * (math.sqrt(max(0.0,b*b-a*a))
                 + a*math.asin(min(1.0,a/b)))
        return math.sqrt(max(0.0,1.0-t*t))*avg
    return simpson(integrand,0.0,1.0,8192)


def moment_formula(r,ell,theta):
    m = math.sin(theta)**2
    mu = (PI*r + ell)/2.0
    raw2 = (8.0*r*r + ell*ell)/3.0 + 4.0*r*ell*mixed_formula(m)
    return mu,raw2,raw2-mu*mu


def run():
    checks=0
    for theta in [0.0,0.02,0.2,0.47,0.8,1.14,1.37,PI/2]:
        m=math.sin(theta)**2
        f=mixed_formula(m)
        independent=mixed_independent(theta)
        assert abs(f-independent) < 2.1e-6, (theta,f,independent)
        checks+=1
    assert abs(mixed_formula(0)-1/3)<1e-13
    assert abs(mixed_formula(1)-4/(3*PI))<1e-13
    checks+=2
    for r,ell in [(1,1),(0.7,2.3),(3.2,0.27)]:
        v0=moment_formula(r,ell,0)[2]
        v1=moment_formula(r,ell,PI/2)[2]
        assert abs(v1-v0 -4*r*ell*(4/PI-1)/3)<1e-12
        for i in range(20):
            mi=i/20
            mj=(i+1)/20
            vi=moment_formula(r,ell,math.asin(math.sqrt(mi)))[2]
            vj=moment_formula(r,ell,math.asin(math.sqrt(mj)))[2]
            delta=(vj-vi)/(r*ell*(mj-mi))
            assert 1/3-1e-10 <= delta <= 4/(3*PI)+1e-10,(mi,delta)
            checks+=1
        checks+=1
    # Independent direct Cartesian widths from a fixed-seed Haar sphere sample.
    rng=random.Random(872103)
    for r,ell,theta in [(1.3,2.1,0),(1.3,2.1,0.45),(1.3,2.1,1.2)]:
        s,c=math.sin(theta),math.cos(theta)
        N=120000
        sw=sw2=0.0
        for _ in range(N):
            z=rng.uniform(-1,1)
            az=rng.uniform(0,2*PI)
            y=math.sqrt(1-z*z)*math.cos(az)
            width=2*r*math.sqrt(1-z*z)+ell*abs(s*y+c*z)
            sw+=width
            sw2+=width*width
        mu,raw2,_=moment_formula(r,ell,theta)
        assert abs(sw/N-mu)<0.015,(sw/N,mu)
        assert abs(sw2/N-raw2)<0.07,(sw2/N,raw2)
        checks+=2
    print(f'OBLIQUE_CYLINDER_WIDTH_CHECKS_OK {checks}')

if __name__=='__main__':
    run()
