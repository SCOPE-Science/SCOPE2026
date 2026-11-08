#!/usr/bin/env python3
"""Finite numerical diagnostics for reset tight-binding purity.

The asymptotic claims are proved analytically in RESULT.md; these finite
computations test the normalization, exact elliptic identity, and finite-torus
spectral formula. All calculations use the displayed physical parameters.
"""
import math
import warnings
import numpy as np
from scipy.integrate import quad, IntegrationWarning
from scipy.special import j0, ellipk


def purity_integral(d, kappa, rate):
    assert d >= 1 and kappa > 0 and rate > 0
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', IntegrationWarning)
        # t=s/r, with the exponential sampled on a bounded effective range.
        v, _ = quad(lambda s: math.exp(-s)*j0(2*kappa*s/rate)**(2*d),
                    0, 45, limit=900, epsabs=1e-11, epsrel=3e-9)
    return v


def purity_elliptic(kappa, rate):
    denominator = math.sqrt(rate*rate+16*kappa*kappa)
    return 2*rate/(math.pi*denominator)*ellipk((4*kappa/denominator)**2)


def purity_finite_cycle(L, kappa, rate):
    q = np.arange(L)
    energy = -2*kappa*np.cos(2*math.pi*q/L)
    gaps = energy[:, None] - energy[None, :]
    return np.mean(rate*rate/(rate*rate+gaps*gaps))


def audit():
    checks=0
    for kappa in (0.6, 1.0, 1.7):
        for rate in (0.7, 1.8, 4.0):
            integral=purity_integral(1,kappa,rate)
            elliptic=purity_elliptic(kappa,rate)
            assert abs(integral-elliptic) < 1e-8, (kappa,rate,integral,elliptic)
            checks+=1
    for rate in (0.4, 0.75, 1.3, 2.5):
        cycle=purity_finite_cycle(137,1.0,rate)
        infinite=purity_elliptic(1.0,rate)
        assert abs(cycle-infinite)< 1e-8, (rate,cycle,infinite)
        checks+=1
    for d in (1,2,3):
        vals=[purity_integral(d, 1.0, r) for r in (0.5,1.0,3.0)]
        assert 0 < vals[0] < vals[1] < vals[2] < 1, (d,vals)
        checks+=3
    for d in (1,2,3,4):
        rate=90.
        numer=purity_integral(d,1.0,rate)
        predicted=1 - 4*d/rate**2+12*d*(4*d-1)/rate**4
        assert abs(numer-predicted)<1e-6,(d,numer,predicted)
        checks+=1
    for rate in (1e-3,2e-4,5e-5):
        exact=purity_elliptic(1,rate)
        asym=rate/(2*math.pi)*math.log(16/rate)
        assert abs(exact/asym-1)<1e-5,(rate,exact,asym)
        checks+=1
    for d in (1,2,3,4,5):
        a=math.comb(2*d,d)/(4**d*math.pi**d)
        theta=np.linspace(0,2*math.pi,100001)
        avg=np.trapezoid(np.cos(theta)**(2*d),theta)/(2*math.pi)
        assert abs(avg-math.comb(2*d,d)/4**d)<1e-10
        assert a>0
        checks+=1
    print(f'PASS: {checks} finite assertions; exact integral/elliptic, torus spectrum, rates, short-time expansion and periodic means.')
    print(f'example: d=1 kappa=1 r=0.7 purity={purity_elliptic(1,0.7):.12f}')
    print(f'example: d=2 kappa=1 r=0.7 purity={purity_integral(2,1,0.7):.12f}')
if __name__=='__main__':
    audit()
