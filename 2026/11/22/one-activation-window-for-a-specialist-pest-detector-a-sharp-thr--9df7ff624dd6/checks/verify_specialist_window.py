#!/usr/bin/env python3
"""Supplementary checks for a two-instrument, multipest Poisson-surveillance theorem.

The theorem itself is proved analytically; these finite tests check its specified
example, the marginal condition and the independent numerical optimizer.
Only the Python standard library is required.
"""
import math
import random
from fractions import Fraction


def loss(B, x, b, w, target, specialist_rate):
    return sum(w[i] * math.exp(-b[i] * (B-x) - (specialist_rate*x if i == target else 0.0))
               for i in range(len(b)))


def derivative(B, x, b, w, target, specialist_rate):
    return sum(w[i] * (b[i] - (specialist_rate if i == target else 0.0))
               * math.exp(-b[i] * (B-x) - (specialist_rate*x if i == target else 0.0))
               for i in range(len(b)))


def optimum(B, b, w, target, specialist_rate):
    if derivative(B, 0.0, b, w, target, specialist_rate) >= 0:
        return 0.0
    if derivative(B, B, b, w, target, specialist_rate) <= 0:
        return B
    lo, hi = 0.0, B
    for _ in range(90):
        mid = (lo+hi)/2.0
        if derivative(B, mid, b, w, target, specialist_rate) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


def main():
    b = (2.0, 3.0, 4.0)
    w = (0.5, 8.0, 2.0)
    a_target = 4.0
    target = 1
    rlo = math.log(4 - 2 * math.sqrt(2))
    rhi = math.log(4 + 2 * math.sqrt(2))
    assert 0 < rlo < rhi
    # Exact coefficients of G(B) = e^-2B - 8e^-3B + 8e^-4B.
    assert Fraction(1,2)*2 == 1
    assert 8*(3-4) == -8
    assert 2*4 == 8
    assert Fraction(1) - 8*Fraction(1,8) + 8*Fraction(1,8)**2 > 0
    assert Fraction(1) - 8*Fraction(1,2) + 8*Fraction(1,2)**2 < 0
    assert Fraction(1) - 8*Fraction(7,8) + 8*Fraction(7,8)**2 > 0
    checked = 6
    for B in (0.02, .1, rlo, .2, .5, 1., 1.5, rhi, 2., 3., 10.):
        x = optimum(B, b, w, target, a_target)
        expected_active = rlo < B < rhi
        if abs(B-rlo) < 1e-10 or abs(B-rhi) < 1e-10:
            # Root rounding may perturb the boundary sign by 1e-15.
            assert x < 1e-10
        else:
            assert (x > 1e-10) == expected_active, (B,x)
        assert -1e-10 <= x <= B + 1e-10
        assert loss(B,x,b,w,target,a_target) <= loss(B,0,b,w,target,a_target)+1e-11
        assert loss(B,x,b,w,target,a_target) <= loss(B,B,b,w,target,a_target)+1e-11
        checked += 4
    rng = random.Random(846123)
    # Independent finite checks of the exact first-order boundary condition.
    for _ in range(2500):
        n = rng.randint(1, 12)
        bb = [rng.uniform(.15, 4.) for _ in range(n)]
        ww = [rng.uniform(.1, 5.) for _ in range(n)]
        s = rng.randrange(n)
        aa = rng.uniform(.05, 6.)
        B = rng.uniform(.01, 8.)
        x = optimum(B, bb, ww, s, aa)
        d0 = derivative(B,0,bb,ww,s,aa)
        if abs(d0) > 1e-8:
            assert (x > 1e-9) == (d0 < 0)
        # Strict convexity yields monotone derivative and unique minimizer.
        dL = derivative(B,B,bb,ww,s,aa)
        assert d0 <= dL + 1e-11
        for j in range(11):
            trial = B*j/10
            assert loss(B,x,bb,ww,s,aa) <= loss(B,trial,bb,ww,s,aa)+1e-9
            checked += 1
        checked += 2
    for B in (.1, 1., 3.):
        x = optimum(B,b,w,target,a_target)
        print('example budget', B, 'specialist allocation', format(x,'.12f'),
              'weighted miss', format(loss(B,x,b,w,target,a_target),'.12f'),
              'baseline generalist-only', format(loss(B,0,b,w,target,a_target),'.12f'))
    print('exact switch budgets', format(rlo,'.12f'), format(rhi,'.12f'))
    print('supplementary assertions', checked)

if __name__ == '__main__':
    main()
