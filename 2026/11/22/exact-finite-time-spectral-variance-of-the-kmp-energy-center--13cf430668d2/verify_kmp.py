#!/usr/bin/env python3
"""Standalone numerical reproduction of finite-time KMP center-variance identities.

Requires Python 3 standard library only. Numerical tests support, but do not
replace, the analytic generator and resolvent proof.
"""
import math
import random

PI=math.pi

def theta_weight(theta):
    lam=4*math.sin(theta)**2
    return 4*math.cos(theta)**2*(lam+2)/(PI*(3*lam*lam-4*lam+4))

def simpson(func,n=8192):
    assert n%2==0
    h=PI/(2*n)
    val=func(0)+func(PI/2)
    for j in range(1,n):
        val+=(4 if j%2 else 2)*func(j*h)
    return val*h/3

def spectral_variance(t):
    def f(theta):
        lam=4*math.sin(theta)**2
        return theta_weight(theta)*(t if lam==0 else -math.expm1(-t*lam)/lam)
    return simpson(f)

def r_of_s(s):
    return 2/(2+s+math.sqrt(s*(s+4)))

def laplace_d(s):
    r=r_of_s(s)
    return r*(2-r)/((1-r)*((1-r)**2+2))

def simulate(t,rng):
    energies={0:1.0}; lo=hi=0; tm=0.; center=0.
    while True:
        count=hi-lo+2
        tm+=rng.expovariate(count)
        if tm>=t:
            return center
        left=rng.randrange(lo-1,hi+1)
        a=energies.get(left,0.)
        b=energies.get(left+1,0.)
        p=rng.random()
        new_right=(1-p)*(a+b)
        energies[left]=p*(a+b)
        energies[left+1]=new_right
        center+=new_right-b
        lo=min(lo,left);hi=max(hi,left+1)

def main():
    assert abs(simpson(theta_weight)-2/3)<2e-12
    assert abs(simpson(lambda z:4*math.sin(z)**2*theta_weight(z))-5/9)<2e-12
    for s in (0.03,0.2,1.,7.,40.):
        exact=laplace_d(s)
        integral=simpson(lambda z:theta_weight(z)/(s+4*math.sin(z)**2))
        assert abs(exact-integral)<2e-12,(s,exact,integral)
    for t in (0.2,1.,10.,100.,1000.):
        val=spectral_variance(t)
        assert val>0
        print('spectral_variance',t,format(val,'.12f'))
    rng=random.Random(20261115)
    for t in (0.4,1.5,4.):
        n=20000
        samples=[simulate(t,rng) for _ in range(n)]
        mean=sum(samples)/n
        empirical=sum((x-mean)**2 for x in samples)/n
        m4=sum((x-mean)**4 for x in samples)/n
        standard_error=math.sqrt(max(m4-empirical*empirical,0)/n)
        target=spectral_variance(t)
        print('simulation',t,'observed',format(empirical,'.9f'),
              'theory',format(target,'.9f'),'stderr',format(standard_error,'.9f'))
        assert abs(empirical-target)<5*standard_error+0.002
    print('PASS: 5 resolvents, 2 spectral sum rules, 3 independent simulations')

if __name__=='__main__':
    main()
