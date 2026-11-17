#!/usr/bin/env python3
"""Finite quadrature checks for the two-site Ornstein--Uhlenbeck resetting theorem.

The infinite-domain monotonicity and exact critical density are proved in RESULT.md;
this numerical script is a reproducible diagnostic, not a substitute for proof.
Standard library only. Run: python3 verify_modes.py
"""
import math


def p_stationary(x, kappa, diff, b, rate, steps=11000):
    """Independent exponential-age integral, transformed with age = z*z."""
    upper = math.sqrt(43.0 / rate)
    dz = upper / steps
    total = 0.0
    for j in range(steps):
        z = (j + 0.5) * dz
        t = z * z
        decay = math.exp(-kappa*t)
        var = -diff / kappa * math.expm1(-2.0*kappa*t)
        norm = 1.0 / math.sqrt(2.0*math.pi*var)
        g1 = math.exp(-(x-b*decay)**2/(2.0*var))
        g2 = math.exp(-(x+b*decay)**2/(2.0*var))
        total += 2.0*z*rate*math.exp(-rate*t)*0.5*(g1+g2)*norm
    return total*dz


def critical_height(kappa, diff, b):
    a = kappa / (2.0*diff)
    # Exponent times erfc; tested only in a well-conditioned finite range.
    return 0.5*math.sqrt(math.pi*a)*math.exp(a*b*b)*math.erfc(math.sqrt(a)*b)


def check():
    assertions = 0
    for kappa, diff, b in [(1., 1., .1), (1., 1., 2.), (.5, 2., 4.)]:
        for ratio in [0.35, 0.8, 1., 1.4, 3.]:
            rate = kappa*ratio
            grid = [i*b/12 for i in range(13)]
            values = [p_stationary(x,kappa,diff,b,rate) for x in grid]
            assert min(values) > 0
            assertions += 1
            if ratio < 1:
                for a,c in zip(values,values[1:]):
                    assert a > c + 1e-6 * max(1,a)
                    assertions += 1
            elif ratio > 1:
                for a,c in zip(values,values[1:]):
                    assert c > a + 1e-6 * max(1,c)
                    assertions += 1
            else:
                h = critical_height(kappa,diff,b)
                for val in values:
                    assert abs(val-h) < 2.5e-6
                    assertions += 1
                aa = kappa/(2.0*diff)
                F = math.sqrt(math.pi)/(2*math.sqrt(aa))*math.erfc(math.sqrt(aa)*b)
                outer_one_side = h/F * (math.exp(-aa*b*b)/(2*aa)-b*F)
                assert abs(2*b*h + 2*outer_one_side-1.0) < 2e-12
                assertions += 1
            tail = [p_stationary(b+i*0.2*max(b,1),kappa,diff,b,rate) for i in range(1,8)]
            for a,c in zip(tail,tail[1:]):
                assert a > c
                assertions += 1
    print('PASS:', assertions, 'finite quadrature assertions across 15 parameter configurations')

if __name__=='__main__':
    check()
