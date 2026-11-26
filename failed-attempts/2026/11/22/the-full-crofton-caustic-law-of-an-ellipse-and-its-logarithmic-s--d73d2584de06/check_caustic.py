#!/usr/bin/env python3
"""Independent numerical checks for a Crofton caustic law of planar ellipses.

Requires numpy and scipy. Exact claims are proved in RESULT.md; this is diagnostic.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk, ellipe


def perimeter(a, b):
    return 4.0 * a * ellipe(1.0 - b * b / (a * a))


def density(z, a, b):
    """Density away from its integrable singularity at z=b*b."""
    c2 = a * a - b * b
    p = perimeter(a, b)
    if not 0 < z < a * a or z == b * b:
        raise ValueError("z must be regular and in the open support")
    if z < b * b:
        return 2.0 * ellipk(c2 / (a * a - z)) / (p * math.sqrt(a * a - z))
    return 2.0 * ellipk((a * a - z) / c2) / (p * math.sqrt(c2))


def geometry_cdf(z, a, b):
    """CDF using only the boundary-speed and uniform-momentum identity."""
    if z <= 0:
        return 0.0
    if z >= a * a:
        return 1.0
    c2 = a * a - b * b
    def integrand(t):
        s2 = b * b + c2 * math.sin(t)**2
        return math.sqrt(s2) - math.sqrt(max(0.0, s2 - z))
    hints = [math.asin(math.sqrt((z - b * b) / c2))] if z > b * b else None
    return 4.0 * quad(integrand, 0.0, math.pi / 2, points=hints,
                      epsabs=2e-11, limit=250)[0] / perimeter(a, b)


def density_cdf(z, a, b):
    if z <= 0:
        return 0.0
    if z >= a * a:
        return 1.0
    mid = b * b
    if z <= mid:
        return quad(lambda v: density(v, a, b), 0, z,
                    epsabs=3e-10, limit=250)[0]
    return (quad(lambda v: density(v, a, b), 0, mid,
                 epsabs=3e-10, limit=250)[0] +
            quad(lambda v: density(v, a, b), mid, z,
                 epsabs=3e-10, limit=250)[0])


def analytic_checks():
    count = 0
    for a, b in [(2.0, 1.0), (1.01, 1.0), (10.0, .8), (3.0, 2.5)]:
        p = perimeter(a, b)
        c = math.sqrt(a * a - b * b)
        assert abs(1 - geometry_cdf(b * b, a, b) - 4 * c / p) < 3e-10
        count += 1
        for z in [.1*b*b, .8*b*b, .999*b*b, 1.001*b*b,
                  .5*(a*a+b*b), .999*a*a]:
            if z >= a*a:
                continue
            assert abs(geometry_cdf(z, a, b) - density_cdf(z, a, b)) < 3e-8
            count += 1
        for gap in [1e-4*c*c, 1e-6*c*c]:
            if gap < a*a - b*b:
                leading = math.log(16*c*c/gap)/(p*c)
                assert abs(density(b*b+gap, a, b) - leading) < 6e-4
                count += 1
        assert abs(density(a*a - 1e-6*(a*a-b*b), a, b) - math.pi/(p*c)) < 2e-5
        count += 1
    print('Analytic vs independent quadrature checks:', count)


def sampling_checks():
    a, b = 2.3, 1.1
    n = 250_000
    rng = np.random.default_rng(8675309)
    # Independent arclength-uniform impacts, by speed-weighted rejection.
    t = rng.uniform(0, 2*math.pi, 1_000_000)
    speed = np.sqrt(b*b + (a*a-b*b)*np.sin(t)**2)
    accepted = t[rng.random(len(t)) < speed/a][:n]
    assert len(accepted) == n
    u = rng.uniform(-1.0, 1.0, n)
    z_boundary = (b*b + (a*a-b*b)*np.sin(accepted)**2)*(1-u*u)
    # Independent invariant-line sampling: angle density proportional to h.
    theta = rng.uniform(0, math.pi, 1_000_000)
    h = np.sqrt(a*a*np.cos(theta)**2 + b*b*np.sin(theta)**2)
    theta = theta[rng.random(len(theta)) < h/a][:n]
    assert len(theta) == n
    h = np.sqrt(a*a*np.cos(theta)**2 + b*b*np.sin(theta)**2)
    offset = rng.uniform(-1.0, 1.0, n)*h
    z_crofton = h*h - offset*offset
    for z in [.15, .5, 1., b*b, 1.8, 3., 5.]:
        exact = geometry_cdf(z, a, b)
        err_boundary = abs(float(np.mean(z_boundary <= z)) - exact)
        err_lines = abs(float(np.mean(z_crofton <= z)) - exact)
        assert err_boundary < .006 and err_lines < .006
    print('Independent Crofton and boundary samples:', n, '+', n, '(seven CDF points)')


if __name__ == '__main__':
    analytic_checks()
    sampling_checks()
    print('All checks passed')
