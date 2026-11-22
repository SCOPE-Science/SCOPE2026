#!/usr/bin/env python3
"""Independent numerical diagnostics for radial kernel comparison; not an infinite proof.
Requires Python 3.10+ and SciPy 1.9+.
"""
import math
from scipy.special import gammainc
from scipy.optimize import brentq


def cdf_e(d, r):
    return float(gammainc(d, r))


def cdf_g(d, r):
    return float(gammainc(d / 2, r*r/(2*(d+1))))


def diff(d, r):
    return cdf_e(d,r)-cdf_g(d,r)


def density_crossings(d):
    h0 = math.lgamma(d)-(d/2-1)*math.log(2)-(d/2)*math.log(d+1)-math.lgamma(d/2)
    disc = (d+1)*(d+1)+2*(d+1)*h0
    return (d+1-math.sqrt(disc), d+1+math.sqrt(disc), h0)


def run():
    checked=0
    for d in range(3,501):
        a,b,h0=density_crossings(d)
        assert h0 < 0 and a > 0 and b > a and a < d+1 < b
        checked += 5
        # Radial probabilities are computed from independent gamma and chi-square CDF formulas.
        assert diff(d,a)>0 and diff(d,b)<0
        checked +=2
        root=brentq(lambda r:diff(d,r),a,b,xtol=1e-10)
        assert a < root < b and abs(diff(d,root))<2e-11
        checked +=2
        for fac in (.05,.1,.25,.5,.75,.95):
            assert diff(d,root*fac)>-4e-14
            checked+=1
        for offset in (.01,.1,.5,1.,2.,4.,8.):
            assert diff(d,root+offset) < 5e-13
            checked+=1
        if d in (3,10,100,500):
            print(f'd={d:4d}: density crosses ({a:.8f},{b:.8f}); unique disk crossover {root:.12f}, offset {root-d:.12f}')
    limit=(4+3*math.sqrt(2))/6
    for d in (100,200,500,1000,2000,4000):
        a,b,_=density_crossings(d)
        root=brentq(lambda r:diff(d,r),a,b,xtol=2e-9)
        assert abs(root-d-limit)<0.1
        checked+=1
    # Direct planar closed form, used only as a familiar boundary check (not novelty).
    root2=brentq(lambda r:math.exp(-r*r/6)-(1+r)*math.exp(-r),2.,5.)
    assert abs(root2-3.376853931208936)<1e-10
    checked+=1
    print('asymptotic offset',f'{limit:.15f}','planar boundary',f'{root2:.12f}')
    print('DIAGNOSTIC ASSERTIONS PASSED',checked)

if __name__=='__main__':
    run()
