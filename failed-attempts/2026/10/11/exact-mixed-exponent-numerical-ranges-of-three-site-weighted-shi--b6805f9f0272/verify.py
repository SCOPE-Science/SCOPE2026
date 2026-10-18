"""Reproducible supplementary checks for the three-site weighted shift radius.
Uses only the Python standard library; floating checks are supplementary to the proof.
"""
from fractions import Fraction
from math import isclose
import random


def radius(p, a, b):
    if not (p > 1 and a >= 0 and b >= 0):
        raise ValueError("Require p>1 and nonnegative absolute weights")
    if a == b == 0:
        return 0.0
    q = p / (p - 1)
    h = (p - 1) ** ((p - 1) / p) / p
    lo, hi = 0.0, max(a, b) * 2
    def equation(r):
        return (a / r) ** p + (b / r) ** q - 1
    while equation(hi) > 0:
        hi *= 2
    for _ in range(180):
        mid = (lo + hi) / 2
        if equation(mid) > 0:
            lo = mid
        else:
            hi = mid
    return h * hi


def witness(p, a, b, w):
    if a <= 0 or b <= 0:
        raise ValueError("Nondegenerate case only")
    r = (p - 1) * a / (p * w)
    s = (b / (p * w)) ** (1 / (p - 1))
    norm = (1 + r ** p + s ** p) ** (1 / p)
    x = (r / norm, 1 / norm, s / norm)
    actual = a * x[0] ** (p - 1) * x[1] + b * x[1] ** (p - 1) * x[2]
    return x, actual


def checks():
    for p in (1.25, 1.5, 2, 2.5, 3, 4, 6):
        for a,b in ((1, 1), (2,1), (1,2), (8, 1)):
            w=radius(p,a,b)
            x,actual=witness(p,a,b,w)
            assert isclose(sum(t**p for t in x),1,abs_tol=2e-12)
            assert isclose(actual,w,rel_tol=2e-12,abs_tol=2e-12),(p,a,b,w,actual)
            q=p/(p-1)
            assert isclose(radius(p,a,b),radius(q,b,a),rel_tol=2e-12)
    for p in (1.25,1.5,2,3,4,6):
        for a,b in ((1,1),(2,1),(1,2),(8,1)):
            w=radius(p,a,b)
            assert isclose(radius(p,a,0),((p-1)**((p-1)/p)/p)*a,rel_tol=2e-12)
            rng=random.Random(91717+int(p*1000)+int(a*100)+int(b))
            for _ in range(12000):
                raw=[rng.random()+1e-8 for i in range(3)]
                n=sum(v**p for v in raw)**(1/p)
                u,v,z=[t/n for t in raw]
                val=a*u**(p-1)*v+b*v**(p-1)*z
                assert val <= w+1e-11,(p,a,b,val,w)
    t=Fraction(65,4)
    fa=t**3-t**2-4096
    fb=t**3-16*t**2-1
    assert fa<0<fb,(fa,fb)
    assert isclose(radius(2,1,1),2**(-0.5),rel_tol=1e-12)
    print('THREE_SITE_WEIGHTED_LP_NUMERICAL_RADIUS_CHECKS_OK')
    print('p=4, weights=(8,1) radius=',format(radius(4,8,1),'.12f'))
    print('p=4, weights=(1,8) radius=',format(radius(4,1,8),'.12f'))
    print('Exact rational threshold polynomial signs:',fa,fb)

if __name__ == '__main__':
    checks()
