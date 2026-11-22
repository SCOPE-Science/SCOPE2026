"""Numerical diagnostics for the short-distance Cassini cross-lobe theorem.

Requires Python 3.9+ and numpy; this is a reproducibility aid, not a proof.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def finite_lobe_area(q, nodes=1000):
    assert 0 <= q < 0.5
    theta_max = math.acos(2 * q) / 2
    v, w = leggauss(nodes)
    theta = theta_max * v
    return 0.5 * theta_max * np.dot(w, np.sqrt(np.maximum(np.cos(2 * theta)**2 - 4 * q*q, 0)))


def hyperbolic_pair_integral(lam, nodes=700):
    """Deterministic 2D Gauss--Legendre integral for Phi(lam)."""
    assert lam >= 0
    if lam <= 2:
        return 0.0
    v, w = leggauss(nodes)
    s = lam * v
    a = np.sqrt(1 + s**2)
    spacing = s[:, None] - s[None, :]
    budget = np.sqrt(np.maximum(lam*lam - spacing**2, 0)) - a[:, None] - a[None, :]
    weights = w[:, None] * w[None, :]
    return 0.5 * lam**2 * np.sum(weights * np.maximum(budget, 0)**2)


def cone_integral(nodes=500):
    """Numerically integrate the exact cone-sum formula."""
    v, w = leggauss(nodes)
    r = (v + 1)/math.sqrt(2)
    wr = w/math.sqrt(2)
    theta = (v + 1)*math.pi/4
    wt = w*math.pi/4
    radial = np.dot(wr, r**3)
    angular = np.dot(wt, np.sin(theta)*np.cos(theta))
    return radial * angular/4


if __name__ == '__main__':
    assert abs(finite_lobe_area(0) - 0.5) < 1e-11
    assert abs(cone_integral() - 0.125) < 1e-11
    assert hyperbolic_pair_integral(2) == 0
    assert hyperbolic_pair_integral(1.5) == 0
    for lam in (2.05, 2.1, 2.2, 3.0, 5.0, 10.0):
        ph = hyperbolic_pair_integral(lam)
        assert ph > 0
        print('lambda', lam, 'Phi', round(ph, 10),
              'onset ratio', round(ph / (math.pi/(3*math.sqrt(2)) * (lam-2)**3), 6),
              'cone ratio', round(ph / (lam**4/8), 6))
    print('cone coefficient', 4*cone_integral())
    print('lobe areas:', [(q, float(finite_lobe_area(q))) for q in (0, 0.05, 0.1)])
