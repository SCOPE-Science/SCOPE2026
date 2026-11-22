#!/usr/bin/env python3
"""Deterministic Gaussian cubature checks of the finite-temperature Gibbs wall profile.

These are finite consistency tests, not a substitute for the analytic monotonicity proof.
"""
import itertools
import numpy as np
from numpy.polynomial.hermite import hermgauss


def profile(n, sigma=1.0, order=11):
    z, w = hermgauss(order)
    z = np.sqrt(2.0) * sigma * z
    w = w / np.sqrt(np.pi)
    out = np.zeros(n, dtype=float)
    total = 0.0
    for labels in itertools.product(range(order), repeat=n-1):
        increments = z[list(labels)]
        s = np.r_[0.0, np.cumsum(increments)]
        p = np.exp(s - np.max(s))
        p /= p.sum()
        weight = np.prod(w[list(labels)])
        out += weight * p
        total += weight
    assert abs(total-1.0) < 1e-11
    return out


def validate():
    tests=0
    for n in (3, 4, 5, 6):
        for sigma in (0.15, 0.7, 1.5):
            q = profile(n, sigma, order=9)
            assert np.allclose(q,q[::-1],atol=1e-10,rtol=0), (n,sigma,q)
            assert np.all(np.diff(q[:(n+1)//2]) < -1e-9), (n,sigma,q)
            assert abs(sum(q)-1.0)<1e-10
            print(f'n={n} sigma={sigma:g} q={q} PASS')
            tests+=3
    print(f'{tests} cubature checks PASS; numerical integration is not an infinite proof')

if __name__=='__main__':
    validate()
