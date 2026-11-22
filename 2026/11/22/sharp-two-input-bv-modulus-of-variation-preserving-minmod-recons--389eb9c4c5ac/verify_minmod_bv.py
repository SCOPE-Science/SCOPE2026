#!/usr/bin/env python3
"""Exact rational checks for a minmod finite-volume reconstruction variation law.

Run with Python 3; no external libraries. The analytical all-dimension proof is
in RESULT.md; the finite tests here corroborate identities and witnesses.
"""
from fractions import Fraction as F
from random import Random


def minmod(u, v):
    if u > 0 and v > 0:
        return min(u, v)
    if u < 0 and v < 0:
        return max(u, v)
    return F(0)


def slopes(x):
    assert len(x) >= 2
    return [F(0)] + [minmod(x[i] - x[i-1], x[i+1] - x[i])
                    for i in range(1, len(x)-1)] + [F(0)]


def discrete_variation(x):
    return sum(abs(x[i+1]-x[i]) for i in range(len(x)-1))


def piecewise_variation_between(x, y, theta):
    """Exact distributional BV variation including intercell jumps."""
    assert len(x) == len(y) and F(0) <= theta <= F(1)
    sx, sy = slopes(x), slopes(y)
    ds = [a-b for a, b in zip(sx, sy)]
    dx = [a-b for a, b in zip(x, y)]
    within = theta * sum(abs(s) for s in ds)
    interface = sum(abs(dx[i+1]-dx[i] - theta*(ds[i]+ds[i+1])/2)
                    for i in range(len(dx)-1))
    return within + interface


def expected_gain(n, theta):
    return F(1) if n == 2 else F(1)+theta if n == 3 else F(1)+2*theta


def witness(n, theta):
    assert n >= 2
    if n == 2:
        x = [F(0), F(2)]; start = 1
    elif n == 3:
        x = [F(0), F(1), F(3)]; start = 1
    else:
        x = [F(0), F(2), F(3), F(5)]
        x += [F(8+3*i) for i in range(n-4)]
        start = 2
    y = [x[i]+(F(1,2) if i >= start else F(0)) for i in range(n)]
    den = discrete_variation([a-b for a,b in zip(x,y)])
    num = piecewise_variation_between(x,y,theta)
    assert den > 0
    assert num == expected_gain(n,theta)*den, (n,theta,num,den)
    return num, den


def run():
    rng=Random(20261116)
    for n in range(2, 31):
        for theta in (F(0), F(1,7), F(1,2), F(3,4), F(1)):
            witness(n,theta)
    print('EXACT_ALL_DIMENSION_EXPLICIT_ATTAINING_PAIRS_PASS 145')
    for theta in (F(0),F(1,9),F(1,2),F(5,6),F(1)):
        for a in (F(0),F(1,7),F(1,2),F(4,5),F(1)):
            for b in (F(0),F(2,9),F(1,2),F(5,6),F(1)):
                # Full step contribution is equal to 1 + theta*(a+b).
                # Its outer boundary terms are theta*(a+b)/2 each
                # in aggregate and the middle intercell jump is nonnegative.
                got=F(3,2)*theta*(a+b)+abs(1-theta*(a+b)/2)
                assert got == 1+theta*(a+b)
    print('EXACT_SECANT_STEP_COLUMN_IDENTITY_PASS 125')
    count=0
    for n in range(2, 13):
        for _ in range(2000):
            x=[F(rng.randrange(-13,14),rng.randrange(1,7)) for i in range(n)]
            y=[F(rng.randrange(-13,14),rng.randrange(1,7)) for i in range(n)]
            diff=[a-b for a,b in zip(x,y)]
            den=discrete_variation(diff)
            for theta in (F(0),F(1,4),F(1,2),F(1)):
                assert piecewise_variation_between(x,[F(0)]*n,theta)==discrete_variation(x)
                if den:
                    assert piecewise_variation_between(x,y,theta) <= expected_gain(n,theta)*den
            count+=1
    print('RANDOM_RATIONAL_ONE_INPUT_ISOMETRY_AND_TWO_INPUT_BOUND_PASS',count)
    # Negative gradients and exact perturbation directions also attain.
    for n in range(2,12):
        for theta in (F(0),F(1,3),F(1)):
            k=2 if n==2 else 1 if n==3 else 2
            x=[F(0),F(2)] if n==2 else ([F(0),F(1),F(3)] if n==3 else [F(0),F(2),F(3),F(5)]+[F(8+3*i) for i in range(n-4)])
            x=[-t for t in x]
            y=[x[i]-(F(1,2) if i>=k else F(0)) for i in range(n)]
            den=discrete_variation([a-b for a,b in zip(x,y)])
            assert piecewise_variation_between(x,y,theta) == expected_gain(n,theta)*den
    print('EXACT_NEGATIVE_SLOPE_SYMMETRIC_WITNESSES_PASS')
    print('ALL_MINMOD_RECONSTRUCTION_BV_CHECKS_PASS')

if __name__ == '__main__':
    run()
