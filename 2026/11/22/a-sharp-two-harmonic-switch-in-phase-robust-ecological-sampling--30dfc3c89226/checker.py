#!/usr/bin/env python3
"""Reproducibility checks for a two-harmonic ecological sampling design.

Only standard-library mathematics is used. Numerical grids are supplementary:
the continuous global bound and uniqueness come from the accompanying proof.
"""
from fractions import Fraction as Q
from math import acos, cos, exp, pi, sqrt
import random


def phase_min(r, q):
    """Exact minimization over x=cos(phase) for fixed r and q=cos(gap/2)."""
    z = 2*q*q-1
    if z <= 0 or r*q >= 4*z:
        return 2*q*q-r*q-1
    return -z-r*r*q*q/(8*z)


def proposed_value(r):
    return max(-1., -r/2.-r*r/16.)


def proposed_gap(r):
    threshold=4*(sqrt(2)-1)
    return acos(r/4) if r < threshold else pi


def exact_certificate(r):
    """All arithmetic rational: verifies optimal phase and threshold polynomial."""
    r=Q(r)
    assert 0 < r < 4
    z=r/4
    q2=(1+z)/2
    x2=q2  # adversarial cos(phase) is minus cos(gap/2)
    harmonic=-r*q2+z*(2*x2-1)
    asserted=-r/2-r*r/16
    assert harmonic==asserted
    assert 0<q2<1
    assert (r*r+8*r-16<0)==(asserted>-1)
    return asserted


def run():
    for r in [Q(1, 8), Q(1, 2), Q(1), Q(3, 2), Q(7, 4), Q(2), Q(7, 2)]:
        print('exact',str(r),str(exact_certificate(r)))

    critical=4*(sqrt(2)-1)
    assert abs((critical*critical+8*critical-16))<2e-14
    assert abs((-critical/2-critical*critical/16)+1)<2e-14

    for r in [.001,.03,.1,.5,1,1.5,critical-1e-5,critical,critical+1e-5,1.8,2,3,4,10,100]:
        v=proposed_value(r)
        gap=proposed_gap(r)
        assert abs(phase_min(r,cos(gap/2))-v)<5e-12
        if abs(r-critical)<1e-12:
            other=acos(r/4)
            assert abs(phase_min(r,cos(other/2))-v)<5e-12
        # Strong finite challenge: 4,001 feasible gaps, each with exact phase minimum.
        for i in range(4001):
            q=cos((i/4000)*(pi/2))
            assert phase_min(r,q) <= v+2e-11, (r,i,phase_min(r,q),v)

    rng=random.Random(140824)
    for _ in range(16000):
        r=10**rng.uniform(-2,2)
        theta=rng.random()*pi/2
        q=cos(theta)
        m=phase_min(r,q)
        # Directly evaluate many independently sampled source phases.
        x=2*rng.random()-1
        f=r*q*x+(2*q*q-1)*(2*x*x-1)
        assert f >= m-4e-11
        assert m <= proposed_value(r)+4e-11

    a,b,c=Q(21,10),Q(1),Q(1)
    assert a>b+c
    assert exact_certificate(b/c)==Q(-9,16)
    best=1-exp(-float(2*a+2*c*Q(-9,16)))
    half=1-exp(-float(2*a-2*c))
    assert best>half
    assert abs(best-0.9538103716183199)<2e-14
    a,b,c=Q(31,10),Q(2),Q(1)
    assert a>b+c
    high=1-exp(-float(2*a-2*c))
    assert abs(high-0.9850044231795223)<2e-14
    print('PASS: rational identities, transition boundary, 60,015 grid checks, 16,000 stochastic challenges, examples')


if __name__=='__main__':
    run()
