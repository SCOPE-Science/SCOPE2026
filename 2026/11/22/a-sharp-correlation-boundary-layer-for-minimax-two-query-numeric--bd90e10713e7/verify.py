#!/usr/bin/env python3
"""Reproducible supplementary checks for a two-query correlated-noise derivative design.
The exact mathematical proof is in RESULT.md; these tests are not a replacement.
"""
import math
import random


def q(x, rho):
    return (1.0-rho) + rho*(-math.expm1(-2*x)-x*math.exp(-2*x))


def opt(kappa, rho):
    assert kappa > 0 and 0 <= rho <= 1
    lo, hi = 0.0, max(1., 2*kappa**(1/6))
    while hi**6 <= kappa*q(hi,rho):
        hi *= 2
    for _ in range(180):
        mid = (lo+hi)/2
        if mid**6 > kappa*q(mid,rho): hi=mid
        else: lo=mid
    return (lo+hi)/2


def risk(x,kappa,rho):
    # M = ell = 1, sigma^2 = kappa / 9
    return x**4/36 + kappa*(1-rho*math.exp(-2*x))/(18*x*x)


def run():
    rng=random.Random(20261118)
    total=0
    for k in [1e-12, 1e-9, 1e-6, 1e-3, 1., 25.]:
        xs=[]
        for rho in [0., 0.1, 0.5, 0.9, 0.99, 0.999999, 1.]:
            x=opt(k,rho);xs.append(x)
            assert x>0
            assert abs(x**6-k*q(x,rho)) <= 2e-12*max(x**6,k*q(x,rho))
            # Entire log-spaced competitor mesh from x/100 to 100*x
            rx=risk(x,k,rho)
            for j in range(-180,181):
                z=x*math.exp(j/20)
                assert risk(z,k,rho) >= rx*(1-2e-11), (k,rho,z,x,rx)
                total+=1
        assert all(xs[i]>xs[i+1] for i in range(len(xs)-1)), (k,xs)
    # Exact bias for the cubic extremizer: f(t)=a+b*t+c*t^2+M*t^3/6.
    for h in [0.01, .125, 1., 2.]:
        # Use only differences to avoid catastrophic cancellation for tiny h.
        term=(h**3/6-(-h)**3/6)/(2*h)
        assert abs(term-h*h/6)<1e-15
    # Positivity certificates used in the paper.
    for _ in range(5000):
        x=math.exp(rng.uniform(-12,8))
        rho=rng.random()
        qq=q(x,rho)
        xp=rho*(1+2*x)*math.exp(-2*x)
        assert 6*qq-x*xp > 0
        total+=1
    # Boundary-layer law for rho=1-alpha*kappa^(1/5).
    for alpha in [0, .5, 2, 5]:
        z_lo,z_hi=1.,4.
        for _ in range(100):
            mid=(z_lo+z_hi)/2
            if mid**6-mid-alpha>0:z_hi=mid
            else:z_lo=mid
        z=(z_lo+z_hi)/2
        for k in [1e-10,1e-15,1e-20]:
            rho=1-alpha*k**.2
            actual=opt(k,rho)/k**.2
            assert abs(actual-z)<.015, (alpha,k,actual,z)
            total+=1
    print('PASS: checks=', total, 'including root equations, strict sampling order,',
          'global competitor grids, positivity certificates, cubic-bias identity,',
          'and boundary-layer convergence')
    print('example kappa=1e-5:')
    for rho in [0, .9, .999, 1]:
        x=opt(1e-5,rho)
        print('rho=',rho,' optimal h/ell=',format(x,'.12g'),
              ' normalized risk=',format(risk(x,1e-5,rho),'.12g'))

if __name__=='__main__':run()
