#!/usr/bin/env python3
"""Exact finite checks of the shared-sample Heun first-moment identity.
Analytic convergence and the diffusion coupling are proved separately.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext

checks = 0
for n in range(2, 251):
    h = Q(1, n)
    a = Q(0)
    b = Q(2)
    def heun_multiplier(k1, k2):
        return 1 - h*(k1+k2)/2 + h*h*k1*k2/2
    r00 = heun_multiplier(a, a)
    r22 = heun_multiplier(b, b)
    assert r00 == 1
    assert r22 == 1-2*h+2*h*h
    assert 0 < r22 <= 1
    shared = (r00+r22)/2
    fresh = sum((heun_multiplier(u,v) for u in (a,b) for v in (a,b)), Q(0))/4
    assert shared == 1-h+h*h
    assert fresh == 1-h+h*h/2
    assert shared-fresh == h*h/2
    checks += 5

with localcontext() as ctx:
    ctx.prec = 75
    e_minus_1 = (-Decimal(1)).exp()
    target = e_minus_1/2
    previous = None
    for n in (100, 200, 400, 800, 1600, 3200):
        h = Decimal(1)/Decimal(n)
        exact_mean = (Decimal(1)-h+h*h)**n
        scaled = Decimal(n)*(exact_mean-e_minus_1)
        assert abs(scaled-target) < Decimal(2)/Decimal(n)
        if previous is not None:
            assert abs(scaled-target) < abs(previous-target)
        previous = scaled
        checks += 2
print(f'PASS: {checks} exact/precision assertions; scaled bias approaches exp(-1)/2.')
