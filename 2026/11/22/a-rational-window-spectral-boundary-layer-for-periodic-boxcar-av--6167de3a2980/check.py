#!/usr/bin/env python3
"""Numerical reproducibility checks for the periodic boxcar counting theorem.
All infinite statements are proved separately in RESULT.md.
"""
import math
from fractions import Fraction

def count(alpha, threshold):
    assert 0 < alpha < 1 and threshold > 0
    bound = int(1 / (math.pi * alpha * threshold)) + 1
    return 2 * sum(
        abs(math.sin(math.pi * n * alpha)) > math.pi * alpha * n * threshold
        for n in range(1, bound + 1)
    )

def constant(alpha, denominator=None):
    if denominator is None:
        return 4 / (math.pi * math.pi * alpha)
    z = math.pi / (2 * denominator)
    return 2 / (math.pi * alpha * denominator) / math.tan(z)

def bisect_cos_root(lam):
    lo, hi = 0.0, 1.0
    for _ in range(90):
        mid = (lo + hi) / 2
        if math.cos(2 * lam * mid) > mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def verify():
    # Exact rational-frequency periodicity and node identities.
    for a, b in [(1,2), (1,3), (2,5), (3,7)]:
        f=Fraction(a,b)
        for n in range(1, 100):
            assert ((n*a) % b == 0) == (n % b == 0)
            assert Fraction(n*a,b).denominator == b // math.gcd(n,b)
        coeff=constant(a/b,b)
        assert coeff > 0 and coeff < constant(a/b)
    print('rational periodicity and coefficient inequalities: PASS')

    for a, b in [(1,2), (2,5)]:
        alpha=a/b
        target=constant(alpha,b)
        measured=1e-5*count(alpha,1e-5)
        assert abs(measured-target) < 0.002, (alpha,target,measured)
        print('rational:',alpha,measured,target)

    for alpha in [(math.sqrt(5)-1)/2, math.sqrt(2)-1]:
        target=constant(alpha)
        measured=1e-5*count(alpha,1e-5)
        assert abs(measured-target) < 0.005, (alpha,measured,target)
        print('irrational:',alpha,measured,target)

    # Moving spectral window alpha(t)=1/2+lambda*t, including the branch-off threshold.
    for lam in [0.0, .125, .25, .5]:
        target=2/math.pi*bisect_cos_root(lam)
        measured=1e-5*count(.5+lam*1e-5,1e-5)
        assert abs(target-measured)<0.004,(lam,measured,target)
        print('critical:',lam,measured,target)
    assert bisect_cos_root(.25)<1
    assert 8/(math.pi**2)>2/math.pi
    assert abs(count(.5-0.25e-5,1e-5)-count(.5+0.25e-5,1e-5))<=2
    print('half-window nonmonotone-dip identities: PASS')

if __name__=='__main__':verify()
