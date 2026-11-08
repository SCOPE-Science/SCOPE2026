"""Numerical cross-check of high-radius Hermite ambiguity design.

Requires numpy and scipy. This samples finitely many orders/radii; it is
not a substitute for the analytic proof of the asymptotic theorem.
"""
import math
import numpy as np
from numpy.polynomial import Polynomial
from scipy.optimize import brentq


def laguerre(k):
    return Polynomial([(-1)**i * math.comb(k, i) / math.factorial(i)
                       for i in range(k + 1)])


def exact_finite_min(m, n, tmax, weight):
    lower, upper = laguerre(m), laguerre(n)
    poly = weight * lower * lower + (1 - weight) * upper * upper
    stationary = (poly.deriv() - poly).roots()
    points = [0., tmax]
    for z in stationary:
        if abs(z.imag) < 2e-7 and 0 < z.real < tmax:
            points.append(float(z.real))
    values = [math.exp(-t) * poly(t) for t in points]
    j = int(np.argmin(values))
    return float(values[j]), float(points[j])


def compact_min(m, n, radius, weight):
    return exact_finite_min(m, n, radius, weight)[0]


def solve_case(m, n, tmax):
    r0 = 4*n + 5
    assert tmax > r0
    upper, lower = laguerre(n), laguerre(m)
    roots = sorted(float(z.real) for z in upper.roots())
    assert all(abs(z.imag) < 1e-9 for z in upper.roots())
    c = min(math.exp(-r) * lower(r)**2 for r in roots)
    b = math.exp(-tmax) * upper(tmax)**2
    a = math.exp(-tmax) * lower(tmax)**2
    assert 0 < a < b
    def gap(w):
        return compact_min(m, n, r0, w) - (b*(1-w) + a*w)
    w = brentq(gap, 0., min(0.4, 6*b/c), xtol=2e-17)
    floor, at = exact_finite_min(m, n, tmax, w)
    outer = b*(1-w) + a*w
    assert abs(floor - outer) < max(1e-14, outer*1e-7)
    assert abs(w/(b/c) - 1) < .035
    assert abs((b-floor)/(b*b/c) - 1) < .15
    return c, b, w, floor, at


def main():
    cases = [(0, 1, 20.), (1, 2, 20.), (1, 2, 25.), (2, 3, 28.)]
    for m,n,T in cases:
        c,b,w,v,_ = solve_case(m,n,T)
        print(f'orders=({m},{n}) T={T:g} weight_ratio={w/(b/c):.8f} '
              f'deficit_ratio={(b-v)/(b*b/c):.8f}')
    rsmall = 2 - math.sqrt(2)
    rlarge = 2 + math.sqrt(2)
    csmall = math.exp(-rsmall)*(1-rsmall)**2
    clarge = math.exp(-rlarge)*(1-rlarge)**2
    assert csmall < clarge
    assert abs(csmall-0.0955091130284885) < 1e-12
    print('HERMITE_DISK_WEIGHT_PASS adjacent_orders=3 numerical_radii=4 root_competition=verified')

if __name__ == '__main__':
    main()
