#!/usr/bin/env python3
"""Numerical cross-checks for a near-boundary resetting threshold.

Only standard-library arithmetic; not a substitute for the analytic proof.
"""
import math

B = math.pi / 2

def logcosh(z):
    z = abs(z)
    return z + math.log1p(math.exp(-2 * z)) - math.log(2)

def H(k, delta):
    return logcosh(k * B) - logcosh(k * (B - delta)) - math.log1p(k * k)

def root(delta):
    lower = 3.0 / delta
    assert H(lower, delta) < 0
    upper = 2 * lower
    while H(upper, delta) <= 0:
        upper *= 2
    for _ in range(100):
        middle = (lower + upper) / 2
        if H(middle, delta) > 0:
            upper = middle
        else:
            lower = middle
    return (lower + upper) / 2

for d in (1/50, 1/100, 1/200, 1/500, 1/1000):
    k = root(d)
    assert abs(H(k,d)) < 2e-11, (d, H(k,d))
    assert H(k/2,d) < 0 and H(2*k,d) > 0
    L = math.log(1/d)
    y = d*k/2
    leading = L + math.log(L) + math.log(2)
    print('delta=',f'{d:.4g}', 'rstar=',f'{1+k*k:.9f}',
          'scaled=',f'{y:.8f}', 'doublelog_approx=',f'{leading:.8f}',
          'residual=',f'{y-leading:.8f}')
print('finite checks passed')
