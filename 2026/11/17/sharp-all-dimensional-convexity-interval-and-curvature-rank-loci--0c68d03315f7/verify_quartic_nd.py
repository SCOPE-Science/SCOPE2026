#!/usr/bin/env python3
"""Exact extremal configurations and independent numerical curvature checks.

The stochastic tests are corroborative, not a substitute for the proof.
Requires Python 3 and NumPy.  No network calls.
"""
from fractions import Fraction as F
from math import sqrt
import random
import numpy as np

def thresholds(d):
    return -F(2*(d+2), 3*(3*d+4)), F(d+2, 3*(d+3))

def gram_Q(u, v, d):
    return 12*sum((a*b)**2 for a,b in zip(u,v))-3*sum(a**4 for a in u)-3/(d+2)

for d in range(3,201):
    neg,pos=thresholds(d)
    c=F(3,d+2)
    axis_q=-3-c
    face_q=F(9,2)-c
    assert 1+pos*axis_q==0 and 1+neg*face_q==0
    assert pos>0 and neg<0
    # exact face-diagonal one-tangent zero eigenvalue; the other d-2 tangents positive
    remaining_q=-F(3,2)-c
    assert 1+neg*remaining_q>0
    # exact spherical moment normalization and volume quadratic coefficient
    var=F(24*(d-1),(d+2)**2*(d+4)*(d+6))
    coeff=-F(3*d*(d+3),2)*var
    assert coeff==-F(36*d*(d-1)*(d+3),(d+2)**2*(d+4)*(d+6))
    if d==3:
        assert (neg,pos)==(-F(10,39),F(5,18))
        assert coeff==-F(144,175)

rng=np.random.default_rng(20261109)
n=0
maxdiff=0
for d in (3,4,5,6,8,12,20,50):
    neg,pos=thresholds(d)
    lower,upper=-3-3/(d+2),4.5-3/(d+2)
    for _ in range(3000):
        u=rng.standard_normal(d)
        u/=np.linalg.norm(u)
        v=rng.standard_normal(d)
        v-=np.dot(u,v)*u
        v/=np.linalg.norm(v)
        a=float(gram_Q(u,v,d))
        assert lower-1.e-11<=a<=upper+1.e-11,(d,a,lower,upper)
        assert 1+float(pos)*a>=-1.e-11
        assert 1+float(neg)*a>=-1.e-11
        n+=1
print('QUARTIC_ND_SUPPORT_PASS exact_dimensions=198 random_tangent_pairs=%d d3_volume_consistency=1'%n)
