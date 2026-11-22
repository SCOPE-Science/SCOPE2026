#!/usr/bin/env python3
"""Independent finite-grid checks for local-averaging commutator formulas.

Requires Python 3, numpy and scipy. The analytic proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.special import beta


def singular_pair_tests():
    rng = np.random.default_rng(2305)
    cases = 0
    for m in (3, 5, 9, 13):
        for _ in range(8):
            f = rng.normal(size=m) + 1j * rng.normal(size=m)
            p = np.ones((m, m), dtype=np.complex128) / m
            c = p @ np.diag(f) - np.diag(f) @ p
            sv = np.linalg.svd(c, compute_uv=False)
            sigma = np.sqrt(np.mean(np.abs(f - np.mean(f))**2))
            assert np.allclose(sv[:2], [sigma, sigma], atol=3e-13, rtol=3e-13)
            assert np.linalg.norm(sv[2:]) < 3e-13
            cases += 1
    return cases


def sawtooth_mass(n, p, steps=4096):
    h = 1.0 / n
    theta = (np.arange(steps, dtype=float) + 0.5) / steps
    cross = (h*h/12.0 + (1.0-h)*theta*(1.0-theta))**(p/2.0)
    return 2.0*((n-1)*(h/math.sqrt(12.0))**p + np.mean(cross))


def sawtooth_tests():
    cases = 0
    for n in (40, 100, 320, 1024, 4096):
        actual = sawtooth_mass(n, 2.0)
        assert abs(actual - (1.0/3.0 - 1.0/(6.0*n))) < 1e-7
        cases += 1
    for p in (0.5, 1.0, 2.0, 3.0):
        n = 8192
        v = sawtooth_mass(n, p)
        observed = (1.0/n)**(1-p)*v if p < 1 else v
        target = (2.0*12**(-p/2.0) if p < 1 else
                  (1.0/math.sqrt(3)+math.pi/4 if p == 1 else
                   2.0*float(beta(1+p/2, 1+p/2))))
        assert abs(observed-target) < (0.03 if p < 1 else 0.001)
        cases += 1
    return cases


def smooth_symbol_tests():
    cases = 0
    for n in (64, 128, 256):
        samples = 80
        h = 1/n
        vals = []
        for k in range(n):
            xs = (k + (np.arange(samples, dtype=float)+0.5)/samples)*h
            v = np.sin(2*math.pi*xs)
            vals.append(np.std(v))
        mass = 2.0*sum(vals)
        assert abs(mass-4.0/math.sqrt(3.0)) < 0.005
        cases += 1
    return cases


if __name__ == '__main__':
    count = singular_pair_tests()+sawtooth_tests()+smooth_symbol_tests()
    print(f'PASS: {count} finite-grid tests; no claim of infinite-dimensional certification')
