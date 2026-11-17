#!/usr/bin/env python3
"""Supplementary finite diagnostic for three-site unitary-dilation radii.

Runs with Python standard library only; does not replace the mathematical proof.
"""
import math

def radius(a, b, rho):
    l = (a*a+b*b+math.hypot(a*a-b*b, 2*(rho-1)*a*b))/2
    return math.sqrt(l)/rho

def minors(a, b, rho, t):
    u = 1/(t*t)
    det = rho**3-rho*(a*a+b*b)*u+(2-rho)*a*a*b*b*u*u
    return [rho, rho*rho-a*a*u, rho*rho-b*b*u,
            rho*rho-a*a*b*b*u*u, det]

checks=0
for a in [0., .1, .3, 1., 2., 6.]:
    for b in [0., .2, .9, 1., 4.]:
        if a==0 and b==0:
            continue
        for rho in [.1,.3,.8,1.,1.1,1.5,2.,2.2,5.,10.]:
            t=radius(a,b,rho)
            for scale in [1., 1.0001]:
                q=minors(a,b,rho,t*scale)
                assert min(q)>-1e-7,(a,b,rho,scale,q)
                checks+=1
            q=minors(a,b,rho,t*.999)
            assert min(q)<-1e-7,(a,b,rho,q)
            checks+=1
for rho in [.1, .9, 1., 1.9, 2., 2.1, 5.]:
    vals=[]
    for k in range(101):
        theta=math.pi*k/200
        vals.append(radius(math.cos(theta),math.sin(theta),rho))
    if rho<2:
        assert abs(min(vals)-vals[50])<1e-12
        assert abs(max(vals)-vals[0])<1e-12
    if rho>2:
        assert abs(max(vals)-vals[50])<1e-12
        assert abs(min(vals)-vals[0])<1e-12
    if rho==2:
        assert max(vals)-min(vals)<1e-12
print('FINITE_DIAGNOSTICS_PASS',checks)
