#!/usr/bin/env python3
"""Standalone checks for one-contrast exponential-kernel integral design.

Requires Python 3.9+ standard library; no network or data files.
Numerical checks supplement rather than certify the infinite-dimensional proof.
"""
import math
import random


def kernel(x, y, ell):
    return math.exp(-abs(x-y)/ell)


def prior_variance(ell):
    return 2*ell*(1-ell*(-math.expm1(-1/ell)))


def m(x, ell):
    return ell*(2-math.exp(-x/ell)-math.exp(-(1-x)/ell))


def gain_direct(u, v, ell, eta):
    cov = m(v, ell)-m(u, ell)
    return cov*cov/(2*(1-math.exp(-(v-u)/ell))+eta)


def gain_boundary(d, ell, eta):
    r = math.exp(-d/ell)
    q = math.exp(-1/ell)
    cov = ell*(-math.expm1(-d/ell))*(-math.expm1(-(1-d)/ell))
    return cov*cov/(2*(1-r)+eta)


def optimal_gap(ell, eta):
    assert ell > 0 and eta >= 0
    q = math.exp(-1/ell)
    low, high = math.sqrt(q), 1.0
    def residual(r):
        return 1/(1-r)-1/(2*(1-r)+eta)-q/(r*(r-q))
    for _ in range(95):
        mid=(low+high)/2
        if residual(mid)>0:
            high=mid
        else:
            low=mid
    return -ell*math.log((low+high)/2)


def simpson(fun, n=1000):
    assert n % 2==0
    h=1/n
    ans=fun(0)+fun(1)
    for j in range(1,n):
        ans += (4 if j%2 else 2)*fun(j*h)
    return ans*h/3


def d_kappa(k):
    return (1-2*k+math.sqrt(1+8*k+4*k*k))/6


def run():
    checks=0
    for ell in (0.2, 0.5, 1.0, 2.0, 5.0):
        for eta in (0.0, 0.01, 0.1, 1.0, 10.0):
            d=optimal_gap(ell,eta)
            assert 0<d<0.5, (ell,eta,d)
            checks+=1
            assert abs(gain_direct(0,d,ell,eta)-gain_boundary(d,ell,eta)) < 2e-14
            checks+=1
            # No uniformly spaced two-point grid design improves upon the exact optimum.
            winner = gain_boundary(d,ell,eta)
            for j in range(40):
                for k in range(j+1,41):
                    u, v = j/40, k/40
                    assert gain_direct(u,v,ell,eta) <= winner + 2e-13, (ell,eta,u,v)
                    checks+=1
            # Optimal gap strictly increases with measurement noise.
            if eta==0:
                q=math.exp(-1/ell)
                r=(math.sqrt(q*q+8*q)-q)/2
                assert abs(d+ell*math.log(r))<2e-12
                checks+=1
        ds=[optimal_gap(ell,eta) for eta in (0,0.01,0.1,1,10,100)]
        assert all(a<b for a,b in zip(ds,ds[1:]))
        checks+=1
        for eta in (10000.0, 100000.0):
            d=optimal_gap(ell,eta)
            coefficient=ell*(-math.expm1(-1/(2*ell)))**2/2
            assert abs((0.5-d)*eta/coefficient - 1)<0.003
            checks+=1
    # Independently check kernel-integral covariance by numerical integration.
    rng=random.Random(20261118)
    for _ in range(80):
        ell=rng.uniform(0.25,2.0)
        u=rng.uniform(0.0,0.9)
        v=rng.uniform(u+0.01,1.0)
        numeric=simpson(lambda s: kernel(s,v,ell)-kernel(s,u,ell),1000)
        exact=m(v,ell)-m(u,ell)
        assert abs(numeric-exact)<2e-6,(ell,u,v,numeric,exact)
        checks+=1
    for k in (0,0.1,1,10):
        for ell in (100., 1000., 10000.):
            d=optimal_gap(ell,k/ell)
            assert abs(d-d_kappa(k))<0.005,(ell,k,d)
            checks+=1
    assert abs(prior_variance(1)-2/math.e)<1e-14
    checks+=1
    for ell in (.2,1,5):
        assert gain_direct(0,1,ell,.5)<1e-28
        checks+=1
    print('PASS',checks,'supplementary exact-formula, optimality-grid, integral and scaling checks')

if __name__=='__main__':
    run()
