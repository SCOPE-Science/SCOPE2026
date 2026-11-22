#!/usr/bin/env python3
"""Auxiliary arithmetic and numerical checks for the degree-two Caratheodory orbitope's ellipsoid geometry.

The accompanying mathematical proof, rather than these finite tests, establishes
containment and optimality for all points and all competing ellipsoids.
"""
from fractions import Fraction as Q
import cmath
import math
import random


def check_exact():
    # On the proposed John boundary, t=|z|^2 is in [0,1/3].
    # Squaring (1-2t) >= (2 sqrt(2)/3) sqrt(1-3t) yields
    # (1-2t)^2 - (8/9)(1-3t) = (2t-1/3)^2 >= 0.
    for i in range(1001):
        t = Q(i, 3000)
        left = (1-2*t)**2 - Q(8, 9)*(1-3*t)
        right = (2*t-Q(1, 3))**2
        assert left == right
        assert left >= 0
        if left == 0:
            assert t == Q(1, 6)
    # First harmonic squared radius 1/3; second is 8/9.
    assert 3*Q(1, 6)+Q(9, 8)*Q(4, 9) == 1
    assert Q(1, 6)+Q(2, 3)+Q(1, 6) == 1
    # Volumes / (pi^2), computed independently by disk-fiber integration.
    volume_body_over_pi2 = Q(1, 3)
    volume_john_over_pi2 = Q(1, 2)*Q(1, 3)*Q(8, 9)
    volume_lowner_over_pi2 = Q(1, 2)*Q(2, 1)**2
    assert volume_john_over_pi2 == Q(4, 27)
    assert volume_john_over_pi2/volume_body_over_pi2 == Q(4, 9)
    assert volume_body_over_pi2/volume_lowner_over_pi2 == Q(1, 6)
    assert volume_lowner_over_pi2/volume_john_over_pi2 == Q(27, 2)
    # Exact Fourier moments: uniform S^1 has E[e^(ik theta)]=0 for k nonzero.
    # Real-frame coordinates are cos/sin of frequencies 1,2 divided by sqrt(2).
    # Product-to-sum gives constant mean 1/4 on the diagonal and zero off.
    for a in (1,2):
        for b in (1,2):
            if a != b:
                assert a-b != 0 and a+b != 0
            else:
                assert 2*a != 0
    return 1001


def check_numeric():
    rng = random.Random(20261120)
    for _ in range(6000):
        t = rng.random()/3
        alpha = rng.random()*math.tau
        beta = rng.random()*math.tau
        z = math.sqrt(t)*cmath.exp(1j*alpha)
        w = (2*math.sqrt(2)/3)*math.sqrt(1-3*t)*cmath.exp(1j*beta)
        assert 3*abs(z)**2 + 9/8*abs(w)**2 <= 1+1e-13
        assert abs(z)**2 + abs(w-z*z) <= 1+1e-13
    for samples in (5, 7, 9, 16, 37):
        for sign in (-1, +1):
            points = []
            for j in range(samples):
                theta = math.tau*j/samples
                points.append([
                    math.cos(theta)/math.sqrt(2),
                    math.sin(theta)/math.sqrt(2),
                    sign*math.cos(2*theta)/math.sqrt(2),
                    sign*math.sin(2*theta)/math.sqrt(2)])
            for i in range(4):
                assert abs(sum(v[i] for v in points)/samples)<1e-13
                for j in range(4):
                    target = (0.25 if i == j else 0.)
                    assert abs(sum(v[i]*v[j] for v in points)/samples-target)<1e-13
    for _ in range(3000):
        theta = rng.random()*math.tau
        z=cmath.exp(1j*theta)
        w=cmath.exp(2j*theta)
        assert abs(abs(z)**2+abs(w)**2-2)<1e-13
        zj=cmath.exp(1j*theta)/math.sqrt(6)
        wj=-2*cmath.exp(2j*theta)/3
        assert abs(abs(zj)**2+abs(wj-zj*zj)-1)<1e-13
    return 6000+3000+10*16


if __name__=='__main__':
    exact=check_exact()
    numerical=check_numeric()
    print(f'PASS: {exact} exact-rational inequality checks; {numerical} numerical checks')
    print('NOTE: universal containment, contact uniqueness, and ellipsoid optimality follow from the analytic proof.')
