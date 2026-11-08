"""Standalone finite numerical checks for the cardinal spline Zak asymptotic.

Requires Python 3, numpy, scipy. The universal claim uses analytic proof;
these finite calculations test the normalization and representative ranges.
"""
import math
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import minimize_scalar


def spline(n):
    return BSpline.basis_element(np.arange(n + 1, dtype=float), extrapolate=False)


def direct_zak(n, x, nu, basis=None):
    b = spline(n) if basis is None else basis
    v = np.array([float(b(x + k)) if x + k < n else 0.0
                  for k in range(n)], dtype=float)
    return np.sum(v * np.exp(-2j * np.pi * np.arange(n) * nu))


def poisson_zak(n, x, nu, cap=120):
    ell = np.arange(-cap, cap + 1, dtype=float) + nu
    fh = np.exp(-1j * np.pi * n * ell) * np.sinc(ell) ** n
    return np.sum(fh * np.exp(2j * np.pi * x * ell))


def Q(n, x, nu, basis=None):
    return (abs(direct_zak(n, x, nu, basis)) ** 2
            + abs(direct_zak(n, x, nu + 0.5, basis)) ** 2)


def main():
    checks = 0
    # Order two gives the exact, nonasymptotic half-density symbol.
    for x in np.linspace(0, 1, 19):
        for nu in np.linspace(0, 0.5, 27):
            assert abs(Q(2, x, nu) - 2*((1-x)**2 + x**2)) < 1e-11
            checks += 1
    # Poisson aliasing is compared with independent compact-support evaluation.
    for n in [4, 5, 6, 8, 12, 18]:
        b = spline(n)
        for x in [0.07, 0.27, 0.5, 0.84]:
            assert abs(sum(float(b(x+k)) if x+k < n else 0
                           for k in range(n)) - 1) < 1e-10
            checks += 1
            for nu in [0, 0.08, 0.17, 0.25, 0.34, 0.48]:
                assert abs(direct_zak(n, x, nu, b)
                           - poisson_zak(n, x, nu)) < 2e-7
                checks += 1
    # Independent Walnut/even-index correlation reconstruction of the frame symbol.
    for n in [2, 3, 4, 6, 8]:
        b = spline(n)
        for x in [0.13, 0.47, 0.79]:
            v = np.array([float(b(x+j)) if x+j<n else 0 for j in range(n)])
            for nu in [0.07, 0.25, 0.43]:
                walnut = sum(2*v[j]*v[k]*np.exp(-2j*np.pi*(j-k)*nu)
                             for j in range(n) for k in range(n) if (j-k)%2==0)
                assert abs(walnut.imag) < 1e-10
                assert abs(walnut.real - Q(n,x,nu,b)) < 1e-10
                checks += 1
    # Approximate the global minimum using one-dimensional frequency search
    # across a mesh of x; finer grids for x are unnecessary for the limit.
    c = 2 * math.sqrt(2) / math.pi
    ratios = []
    for n in [6, 8, 10, 12, 16, 20, 24]:
        b = spline(n)
        xgrid = np.linspace(0, 1, 17, endpoint=False)
        minima = []
        for x in xgrid:
            res = minimize_scalar(lambda w: Q(n, x, w, b),
                                  bounds=(0.125, 0.375), method='bounded',
                                  options={'xatol': 3e-10})
            minima.append(float(res.fun))
        measured = min(minima)
        predicted = 2*c**(2*n)
        ratios.append(measured / predicted)
        assert abs(measured / predicted - 1) < 0.05
        assert abs(Q(n, .29, .25, b) / predicted - 1) < .05
        checks += 2
    assert abs(ratios[-1] - 1) < .0001
    checks += 1
    # The partition-of-unity fiber at integer frequency gives the upper bound >=1.
    for n in [2, 3, 4, 8, 16, 24]:
        b = spline(n)
        for x in [0, 0.31, 0.5, 0.91]:
            assert abs(direct_zak(n, x, 0, b) - 1) < 1e-10
            assert Q(n, x, 0, b) >= 1 - 1e-11
            checks += 2
    print('CARDINAL_SPLINE_HIGH_ORDER_CHECKS_PASSED', checks)
    print('high_order_ratio', ratios)


if __name__ == '__main__':
    main()
