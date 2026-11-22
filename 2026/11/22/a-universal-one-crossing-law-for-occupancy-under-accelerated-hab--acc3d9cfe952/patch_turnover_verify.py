"""Numerical diagnostics for a three-state dynamic habitat model.

Scientific proof is analytic; these finite checks are consistency tests.
Requires Python 3, NumPy, and SciPy.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def occupancy_formula(p, c, e, s, t):
    rate = c + e + (1-p)*s
    z = rate-s
    mixed = t*math.exp(-rate*t) if abs(z)<1.e-11 else (math.exp(-s*t)-math.exp(-rate*t))/z
    return c*p*((-math.expm1(-rate*t))/rate - mixed)


def occupancy_matrix(p,c,e,s,t):
    a=p*s; b=(1-p)*s
    Q=np.array([[-a,b,b],[a,-b-c,e],[0,c,-b-e]])
    return float(expm(Q*t)[2,0])


def crossing(p,c,e,s1,s2):
    def delta(t): return occupancy_formula(p,c,e,s2,t)-occupancy_formula(p,c,e,s1,t)
    left=1.e-3/max(s1,s2,c+e)
    while delta(left)<=0:
        left*=2
        assert left<1
    right=1/max(s1,s2,c+e)
    while delta(right)>=0:
        right*=2
        assert right<1.e8
    return brentq(delta,left,right,xtol=2.e-13)


def run():
    rng=np.random.default_rng(20261119)
    n=0
    for j in range(400):
        p=rng.uniform(.02,.98); c=10**rng.uniform(-1,1); e=10**rng.uniform(-2,1)
        s1=10**rng.uniform(-1,1); s2=s1*rng.uniform(1.3,6)
        x=crossing(p,c,e,s1,s2)
        for t in [x*.03,x*.3,x*.7,x*.95,x*1.05,x*1.4,x*3]:
            d=occupancy_formula(p,c,e,s2,t)-occupancy_formula(p,c,e,s1,t)
            assert (d>0)==(t<x)
            assert abs(d) > 1e-14
            z1=occupancy_matrix(p,c,e,s1,t)
            z2=occupancy_matrix(p,c,e,s2,t)
            assert abs(z1-occupancy_formula(p,c,e,s1,t))<5e-11
            assert abs(z2-occupancy_formula(p,c,e,s2,t))<5e-11
            n+=3
        assert c*p/(c+e+(1-p)*s2)<c*p/(c+e+(1-p)*s1)
        n+=1
    # Exact resonant case lambda_s=s, i.e. c+e=p*s, including extinction-free case.
    for p,c,e,s in [(0.4,1.0,0.2,3.0),(0.75,1.5,0.0,2.0),(0.3,0.7,0.2,3.0)]:
        assert abs(c+e-p*s)<1.e-12
        for t in [0.01,0.2,1,5]:
            assert abs(occupancy_formula(p,c,e,s,t)-occupancy_matrix(p,c,e,s,t))<5.e-11
            n+=1
    p,c,e,s1,s2=.4,1.8,.2,.5,4.
    x=crossing(p,c,e,s1,s2)
    d=lambda t: occupancy_formula(p,c,e,s2,t)-occupancy_formula(p,c,e,s1,t)
    print('sample',p,c,e,s1,s2,'crossing',format(x,'.12f'),'before',d(.5*x),'after',d(2*x))
    print('CHECKS_PASS',n)


if __name__=='__main__': run()
