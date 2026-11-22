#!/usr/bin/env python3
"""Supplementary finite checks for the Poisson-disk expectation formulas.

The analytical proof is in RESULT.md; numerical quadrature is not a proof.
"""
import cmath
import math

N = 8192
unit = [cmath.exp(2j * math.pi * j / N) for j in range(N)]
parameters = [0j, 0.3 + 0.25j, -0.25 + 0.5j, 0.7 + 0j, 0.15 - 0.8j]
checks = 0

def poisson(z):
    return [(1 - abs(z)**2) / abs(1 - z.conjugate() * v)**2 for v in unit]

weights = {z: poisson(z) for z in parameters}
for z, h in weights.items():
    assert min(h) > 0
    checks += 1
    assert abs(sum(h)/N - 1) < 1e-11
    checks += 1
    lo, hi = (1 - abs(z))/(1 + abs(z)), (1 + abs(z))/(1 - abs(z))
    assert min(h) >= lo - 1e-12 and max(h) <= hi + 1e-12
    checks += 1
    for m in range(-6, 7):
        moment = sum(h[j]*unit[j]**m for j in range(N))/N
        expected = z**m if m>=0 else z.conjugate()**(-m)
        assert abs(moment-expected) < 3e-11, (z,m,moment,expected)
        checks += 1
    for k in range(8):
        assert abs(z**(k+1)-z*z**k) < 1e-12
        checks += 1
for z in parameters:
    hz = weights[z]
    for w in parameters:
        hw = weights[w]
        integral = sum(hz[j]*math.log(hz[j]/hw[j]) for j in range(N))/N
        formula = math.log(abs(1-w.conjugate()*z)**2 / ((1-abs(z)**2)*(1-abs(w)**2)))
        assert abs(integral-formula) < 3e-11, (z,w,integral,formula)
        checks += 1
        assert formula >= -1e-12
        checks += 1
        swapped = math.log(abs(1-z.conjugate()*w)**2 / ((1-abs(w)**2)*(1-abs(z)**2)))
        assert abs(swapped-formula) < 1e-12
        checks += 1
print('POISSON_DISK_CHECK_OK', checks)
