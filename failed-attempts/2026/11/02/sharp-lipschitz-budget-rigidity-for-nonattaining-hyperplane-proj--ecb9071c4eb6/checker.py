#!/usr/bin/env python3
"""Independent numerical spot checks for an exact bounded-Lipschitz tradeoff.

Run: python3 checker.py
These finite checks do not establish the analytic theorem.
"""
import math
import random


def critical(alpha):
    return 2.0*(alpha+2.0)/(alpha+1.0)


def envelope(alpha, L, R):
    if R >= L/2.0:
        return L/critical(alpha)
    return R - 2.0**(alpha+1.0)/(alpha+2.0)*R**(alpha+2.0)/L**(alpha+1.0)


def root(alpha, L):
    assert L >= critical(alpha)
    lo,hi=0.0,L/2.0
    for _ in range(110):
        r=(lo+hi)*0.5
        if envelope(alpha,L,r)<1.0:
            lo=r
        else:
            hi=r
    return (lo+hi)/2.0


def quadrature(alpha,L,R,steps=24000):
    # Substitute z=(2u)^(alpha+1):
    # 2c*int_0^(1/2) u^alpha min(Lu,R) du
    # =int_0^1 min((L/2)*z^(1/(alpha+1)),R) dz.
    s=0.0
    for k in range(steps):
        z=(k+0.5)/steps
        s+=min(L*z**(1.0/(alpha+1.0))/2.0,R)
    return s/steps


def norm_approx(alpha,L):
    return 1.0+root(alpha,L)


def check():
    rng=random.Random(20261031)
    tests=0
    for alpha in [-.75,-.5,-.25,0.,.1,.5,1.,2.,4.]:
        Ls=critical(alpha)
        for ratio in [1.,1.000001,1.0001,1.01,1.1,1.3,2.,4.,10.,100.]:
            L=Ls*ratio
            R=root(alpha,L)
            assert R>=1.0-1.e-12 and R<=L/2.0+1.e-11
            assert abs(envelope(alpha,L,R)-1.0)<1.e-11
            assert abs(quadrature(alpha,L,R)-1.0)<2.5e-5
            tests+=4
            for _ in range(50):
                r=rng.random()*L/2.0
                M=envelope(alpha,L,r)
                assert abs(quadrature(alpha,L,r,steps=700)-M)<.004
                tests+=1
            if ratio>1.0000001:
                eps=1e-6*max(1.,R)
                assert envelope(alpha,L,R-eps)<1.0
                tests+=1
    for alpha in [-.5,0.,.25,1.,3.]:
        C=2**(alpha+1.)/(alpha+2.)
        for L in [10**(j/(alpha+1.)) for j in [4.,5.,6.]]:
            L=max(L,critical(alpha)*2)
            R=root(alpha,L)
            leading=C*L**(-(alpha+1.))
            assert abs((R-1.)/leading-1.)<.04
            tests+=1
        L0=critical(alpha)
        R0=L0/2
        for delta in [1e-3,1e-4,1e-5]:
            R=root(alpha,L0+delta)
            predicted=R0-math.sqrt(delta/(alpha+1.))
            assert abs(R-predicted)<2.0*delta
            tests+=1
    print('PASS',tests,'deterministic assertions; finite supplemental checks only')

if __name__=='__main__':
    check()
