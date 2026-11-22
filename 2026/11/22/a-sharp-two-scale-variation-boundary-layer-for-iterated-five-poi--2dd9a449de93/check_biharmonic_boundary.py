#!/usr/bin/env python3
"""Finite checks of five-tap smoothing and its quartic/Gaussian boundary layer.

Requires Python 3.10+ and NumPy. This is a numerical checker, not an
infinite-dimensional proof of the stated limit theorem.
"""
from fractions import Fraction
import math
import numpy as np


def taps(u):
    return {-2: -u, -1: 4*u, 0: 1-6*u, 1: 4*u, 2: -u}


def convolve(a, b):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            out[i+j] = out.get(i+j, 0) + ai*bj
    return out


def finite_exact(u, exponent):
    p = taps(u)
    v = {0: Fraction(1)}
    for _ in range(exponent):
        v = convolve(v, p)
    assert sum(v.values()) == 1
    return sum(abs(z) for z in v.values())


def spectral_l1(u, exponent):
    # No cyclic aliases: Fourier grid strictly exceeds support diameter 4*exponent.
    n = 1 << (4*exponent+1).bit_length()
    t = 2*np.pi*np.arange(n)/n
    symbol = 1 - 4*u*(1-np.cos(t))**2
    coeffs = np.fft.ifft(symbol**exponent)
    assert max(abs(coeffs.imag)) < 1e-8
    return float(np.abs(coeffs.real).sum())


def run():
    u = Fraction(3,35)
    p = taps(u)
    for power in range(4):
        assert sum(j**power*pj for j,pj in p.items()) == (1 if power == 0 else 0)
    print('EXACT_ZERO_SECOND_MOMENT_AND_POLYNOMIAL_REPRODUCTION_PASS')
    for t in (Fraction(3,35), Fraction(1,8)):
        for r in range(1,7):
            exact=float(finite_exact(t,r))
            numeric=spectral_l1(float(t),r)
            assert abs(exact-numeric) < 3e-10, (t,r,exact,numeric)
    print('EXACT_FINITE_CONVOLUTION_AND_INDEPENDENT_FOURIER_INVERSION_PASS')
    target_h4 = 1.2373 # coarse numerical quadrature benchmark, not a proof
    for lam in (-0.08, 0.0, 0.08):
        target=target_h4+math.exp(16*lam)
        vals=[]
        for r in (1000, 10000, 100000):
            vals.append(spectral_l1(1/8+lam/r,r))
        assert abs(vals[2]-target) < abs(vals[1]-target) < abs(vals[0]-target)
        assert abs(vals[2]-target) < 0.4
        print('NEAR_CRITICAL_FINITE_SCALES',lam,*(f'{x:.8f}' for x in vals),'limit',f'{target:.8f}')
    print('NEAR_CRITICAL_TWO_SCALE_NUMERICAL_TREND_PASS')
    below=[spectral_l1(3/35,r) for r in (1000,10000)]
    assert abs(below[1]-target_h4) < abs(below[0]-target_h4)
    print('FIXED_STABLE_QUARTIC_LIMIT_TREND_PASS')
    print('ALL_FIVE_TAP_BOUNDARY_LAYER_CHECKS_PASS')

if __name__ == '__main__':
    run()
