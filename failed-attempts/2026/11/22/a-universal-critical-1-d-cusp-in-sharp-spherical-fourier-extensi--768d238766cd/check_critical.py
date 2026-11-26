#!/usr/bin/env python3
"""Finite numerical stress test for a critical Bessel-moment asymptotic.

Requires numpy and scipy. This is not a proof or an infinite-tail certificate.
"""
import math
import numpy as np
from scipy.special import jv, gamma
from numpy.polynomial.legendre import leggauss

PERIODS = 700
NODES = 64
z, w = leggauss(NODES)
r = (np.arange(PERIODS)[:, None] + (z[None, :] + 1)/2) * math.pi
weights = w[None, :] * math.pi / 2

def finite_moment(d, q, k):
    nu = d/2 - 1
    integrand = np.abs(jv(nu+k, r))**q * r**(d-1-nu*q)
    return float(np.sum(weights*integrand))

def mean_cos_power(q):
    return float(gamma((q+1)/2)/(math.sqrt(math.pi)*gamma(1+q/2)))

for d in (3, 4, 5):
    qc = 2*d/(d-1)
    beta = (d-1)/2
    A = (2/math.pi)**(qc/2)*mean_cos_power(qc)/beta
    D = finite_moment(d, qc, 0)-finite_moment(d, qc, 1)
    assert D > 0, ('critical finite cutoff nonpositive', d)
    K = (2*math.pi)**d*(d-1)/d*D/A**(1/d)
    print('dimension', d, 'critical', qc, 'D_finite', D, 'predicted_K_finite', K)
    for eps in (.1, .04, .02):
        q = qc+eps
        tail = (2/math.pi)**(q/2)*mean_cos_power(q)*(PERIODS*math.pi)**(-beta*eps)/(beta*eps)
        a=finite_moment(d,q,0)+tail
        b=finite_moment(d,q,1)+tail
        assert a>b>0, ('moment ordering failed', d, q)
        # Use derivative-stable difference of two nearly equal powers.
        ratio=(2*math.pi)**d*(a**(2/q)-b**(2/q))/eps**(1/d)
        print(' epsilon', eps, 'rescaled_gap', ratio, 'ratio_to_K', ratio/K)
        assert 0.75 < ratio/K < 1.08, ('unexpected near-critical behavior',d,eps)
print('finite Bessel-moment stress tests passed; no infinite-proof claim')
