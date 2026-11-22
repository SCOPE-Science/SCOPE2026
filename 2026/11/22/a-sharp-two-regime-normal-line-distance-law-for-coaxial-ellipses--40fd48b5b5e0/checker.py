#!/usr/bin/env python3
"""Independent numerical checks of the exact coaxial-ellipse normal-line formula.

The universal proof is analytical; these finite checks are regression tests, not
proofs for untested real semiaxes.
"""
import math
import random
from fractions import Fraction


def algebraic_distance(a, b, c, d):
    assert a >= b > 0 and c >= d > 0
    A, C = a*a-b*b, c*c-d*d
    p, q = b-d, a-c
    q0, q1 = A*d-C*b, A*c-C*a
    if q0*q1 >= 0:
        return 2*abs(q-p), None
    assert A > 0 and C > 0 and A != C
    u = (C*C*b*b-A*A*d*d)/(A*C*(A-C))
    assert 0 < u < 1
    z = math.copysign(math.sqrt((A-C)*(C*b*b-A*d*d)/(A*C)), A-C)
    return 2*(abs(z-p)+abs(q-z)), u


def quadrature(a, b, c, d, n=8192):
    """Trapezoidal integration of half absolute normal-line offset derivative."""
    A, C = a*a-b*b, c*c-d*d
    step = 2*math.pi/n
    total = 0.0
    for j in range(n):
        th = (j+0.5)*step
        x, y = math.cos(th), math.sin(th)
        v1 = math.sqrt(a*a*x*x+b*b*y*y)
        v2 = math.sqrt(c*c*x*x+d*d*y*y)
        deriv = -x*y*(A/v1-C/v2)
        total += abs(deriv)
    return 0.5*step*total


def run():
    # Exact rational stationary angle for the nested, equally gapped ellipses.
    A, C, b, d = Fraction(5), Fraction(3), Fraction(2), Fraction(1)
    u = (C*C*b*b-A*A*d*d)/(A*C*(A-C))
    z2 = (A-C)*(C*b*b-A*d*d)/(A*C)
    assert u == Fraction(11, 30)
    assert z2 == Fraction(14, 15)
    assert A*d-C*b < 0 < A*2-C*3
    v, u_float = algebraic_distance(3, 2, 2, 1)
    assert abs(u_float-float(u)) < 1e-14
    assert abs(v-4*(1-math.sqrt(14/15))) < 1e-13
    assert abs(v-quadrature(3, 2, 2, 1)) < 2e-6
    count = 1
    deterministic = [
        (1, 1, 2, 2), (3, 2, 1, 1), (3, 1, 2, 2),
        (4, 1, 3, 2), (5, 4, 3, 2),
        (2, 1, 1, .5), (4, 2, 2, 1), (4, 3, 3, 2),
        (4, 1, 4, 1), (2, 2, 2, 1), (3, 2, 3, 2),
    ]
    for a,b,c,d in deterministic:
        exact,_ = algebraic_distance(a,b,c,d)
        num = quadrature(a,b,c,d)
        assert abs(exact-num) < 3e-6, (a,b,c,d,exact,num)
        count += 1
    rng=random.Random(2023)
    both = 0
    for _ in range(240):
        b=rng.uniform(.35,4.5);a=b+rng.uniform(.001,3.6)
        d=rng.uniform(.35,4.5);c=d+rng.uniform(.001,3.6)
        exact,critical=algebraic_distance(a,b,c,d)
        num=quadrature(a,b,c,d,4096)
        assert abs(exact-num)<8e-6,(a,b,c,d,exact,num)
        assert exact+1e-11 >= 2*abs((a-b)-(c-d))
        if critical is not None:
            both+=1
            assert exact > 2*abs((a-b)-(c-d))
        count+=1
    assert both>10, both
    print('PASS: exact rational identities and', count,
          'numerical parameter configurations;', both,
          'strict interior-switch cases in random sample')


if __name__=='__main__':
    run()
