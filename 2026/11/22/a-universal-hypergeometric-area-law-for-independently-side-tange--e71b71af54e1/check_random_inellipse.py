#!/usr/bin/env python3
"""Standalone finite diagnostics for random side-contact inellipse area."""
import math
import random


def normalized_area(t, w):
    assert 0 < t < 1 and 0 < w < 1
    return math.pi*t*w*math.sqrt((1-t)*(1-w))/(t+w-t*w)**1.5


def moment(s, terms=20000):
    # Beta factors times a positive hypergeometric series at z=1.
    beta=math.gamma(1+s/2)*math.gamma(1+s)/math.gamma(2+3*s/2)
    term=1.0
    total=term
    for k in range(terms):
        term *= (1.5*s+k)*(1+s/2+k)**2 / ((2+1.5*s+k)**2*(k+1))
        total += term
    return math.pi**s*beta*beta*total


def run():
    rng=random.Random(1781)
    for _ in range(20000):
        t=rng.uniform(.0001,.9999)
        w=rng.uniform(.0001,.9999)
        h=t+w-t*w
        cx=t/(2*h)
        cy=w/(2*h)
        bary=(cx,cy,1-cx-cy)
        assert all(0<z<0.5 for z in bary)
        p,q,r=(1-2*z for z in bary)
        assert abs(normalized_area(t,w)**2-math.pi**2*p*q*r)<1e-12
        # Recover ellipse quadratic form with coordinate-side tangencies.
        q11=cx*cx;q22=cy*cy;q12=((1-cx-cy)**2-q11-q22)/2
        assert q11*q22-q12*q12>0
        assert abs(2*math.pi*math.sqrt(q11*q22-q12*q12)-normalized_area(t,w))<1e-12
    # Direct 2D midpoint quadrature, independent of hypergeometric series.
    N=680
    sums=[0.,0.,0.]
    for i in range(N):
        t=(i+.5)/N
        for j in range(N):
            w=(j+.5)/N
            A=normalized_area(t,w)
            sums[0]+=A**.5
            sums[1]+=A
            sums[2]+=A*A
    for s,avg in zip((.5,1,2),(x/(N*N) for x in sums)):
        target=moment(s)
        assert abs(avg-target)<0.00017,(s,avg,target)
    # Unique maximum and Hessian: -D^2 A at t=w=1/2.
    eps=.00005
    v=normalized_area(.5,.5)
    assert abs(v-math.pi/(3*math.sqrt(3)))<1e-14
    hxx=(normalized_area(.5+eps,.5)+normalized_area(.5-eps,.5)-2*v)/eps**2
    hxy=(normalized_area(.5+eps,.5+eps)-normalized_area(.5+eps,.5-eps)-normalized_area(.5-eps,.5+eps)+normalized_area(.5-eps,.5-eps))/(4*eps**2)
    assert abs(hxx+16*math.sqrt(3)*math.pi/27)<2e-6
    assert abs(hxy-8*math.sqrt(3)*math.pi/27)<2e-6
    print('PASS: 20000 ellipse identities, 3 independent 462400-point moment quadratures, Hessian and maximum checks')
    print('mean=',format(moment(1),'.12f'),'second=',format(moment(2),'.12f'), 'maximum=',format(v,'.12f'))

if __name__=='__main__':run()
