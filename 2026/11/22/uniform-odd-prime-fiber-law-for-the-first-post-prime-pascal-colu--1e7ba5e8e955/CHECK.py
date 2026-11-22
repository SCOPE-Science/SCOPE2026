#!/usr/bin/env python3
"""Independent exact fiber checks for the first Pascal column after an odd prime."""
from collections import Counter
from fractions import Fraction
from math import comb


def binom_rat(x, k):
    z = Fraction(1)
    for i in range(k):
        z *= (x - i) / (i + 1)
    return z


def rational_mod(z, m):
    return z.numerator * pow(z.denominator, -1, m) % m


def predicted(p, h, y, a):
    mod = p**h
    if (y - a) % p:
        return p - 1
    ph = p**(h-1)
    z = ((y-a) % mod) // p
    num_roots = sum((r*r-z)%ph == 0 for r in range(ph))
    return p-1 + p*num_roots


def test(p, h):
    mod = p**h
    period = p**(h+1)
    alpha = binom_rat(Fraction(p,2),p+1)
    assert alpha.denominator%p != 0
    a = rational_mod(alpha,mod)
    hist = Counter(comb(n,p+1)%mod for n in range(period))
    for y in range(mod):
        assert hist[y] == predicted(p,h,y,a), (p,h,y,hist[y],predicted(p,h,y,a))
    assert sum(hist.values()) == period
    assert comb(1+p**h,p+1)%mod !=0
    print('PASS p=%d h=%d period=%d, %d output fibers' % (p,h,period,mod))

if __name__ == '__main__':
    for p in (3,5,7,11):
        for h in (1,2,3):
            test(p,h)
