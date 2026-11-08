#!/usr/bin/env python3
"""Reproduce finite numerical checks for the sharp circular-cone phase theorem.

Requires only Python standard library. All universal conclusions rely on the
analytic monotonicity proof, not on this finite check.
"""
import math

pi=math.pi

def R(x):
    return pi*pi*math.sin(x)**3/(8*math.cos(x)*(x-math.sin(x)*math.cos(x)))

def conic_volumes(alpha):
    s,c=math.sin(alpha),math.cos(alpha)
    beta=pi/2-alpha
    return [
        (beta-math.sin(beta)*math.cos(beta))/pi,
        c*c/2,
        2*s*c/pi,
        s*s/2,
        (alpha-s*c)/pi,
    ]

def check():
    assert 16/pi**2>1.5
    assert 16/pi**2<2.25
    assert 3*pi*pi/16>4/3
    assert 3*pi*pi/16<2
    left,right=0.20,1.0
    assert R(left)<2<R(right)
    for _ in range(70):
        mid=(left+right)/2
        if R(mid)<2:left=mid
        else:right=mid
    beta=(left+right)/2
    alpha_star=pi/2-beta
    assert abs(R(beta)-2)<1e-13
    assert 0.98461917882<alpha_star<0.98461917884
    n=0
    for i in range(1,182):
        alpha=(i/182)*pi/2
        v=conic_volumes(alpha)
        assert min(v)>0
        assert abs(sum(v)-1)<2e-14
        ratios=[v[k]**2/(v[k-1]*v[k+1]) for k in (1,2,3)]
        assert abs(ratios[0]-R(pi/2-alpha))<1e-8
        assert abs(ratios[1]-16/pi**2)<1e-12
        assert abs(ratios[2]-R(alpha))<1e-8
        assert ratios[1]>1.5 and ratios[2]>4/3
        assert ratios[1]<2.25
        if alpha<alpha_star-1e-12: assert ratios[0]>2
        if alpha>alpha_star+1e-12: assert ratios[0]<2
        n+=1
    assert R(pi/2-pi/3)<2   # Fu-Wang's published example
    for eps in (0.001, 0.01,0.1):
        assert R(beta-eps)<2<R(beta+eps)
    print('PASS: %d apertures, conic-volume identities, Poisson and binomial inequalities; alpha*=%.15f radians' %(n,alpha_star))

if __name__=='__main__':check()
