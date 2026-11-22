#!/usr/bin/env python3
"""Numerical diagnostics for a geometric width formula.

Dependencies: Python 3, NumPy, SciPy. All assertions are deterministic.
These diagnostics do not replace the analytic proofs in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

PI = math.pi
ROOT3 = math.sqrt(3.0)
MIN_WIDTH = ROOT3 / 2
RNG = np.random.default_rng(291137)


def formula_width(u):
    u = np.asarray(u, dtype=float)
    assert abs(np.linalg.norm(u) - 1) < 1e-12
    t = min(1.0, 3*ROOT3 * abs(float(np.prod(u))))
    return math.cos(math.asin(t) / 3)


def eigen_width(u):
    u1, u2, u3 = u
    A = np.array([[0, u3/2, u2/2],
                  [u3/2, 0, u1/2],
                  [u2/2, u1/2, 0]], dtype=float)
    spectrum = np.linalg.eigvalsh(A)
    return spectrum[-1] - spectrum[0]


def q_of_width(w):
    return math.sqrt(max(0, 1-w*w))*(4*w*w-1)/(3*ROOT3)


def cdf_width(w):
    if w < MIN_WIDTH:
        return 0.
    if w >= 1:
        return 1.
    q = q_of_width(w)
    z0 = 1/ROOT3
    a = lambda z: z*(1-z*z)/2
    lo = brentq(lambda z: a(z)-q, 0., z0, xtol=1e-15)
    hi = brentq(lambda z: a(z)-q, z0, 1., xtol=1e-15)
    return quad(lambda z: (2/PI) * math.acos(min(1., q/a(z))),
                lo, hi, epsabs=3e-13, epsrel=5e-12,
                limit=120)[0]


def upper_tail(eps):
    return 1. - cdf_width(1.-eps)


def upper_two_term(eps):
    return (math.sqrt(6)/PI)*math.sqrt(eps)*(math.log(1/eps)+2+math.log(3/2))


def main():
    checks = 0
    normals = RNG.normal(size=(2500, 3))
    normals /= np.linalg.norm(normals, axis=1)[:, None]
    for u in normals:
        assert abs(formula_width(u)-eigen_width(u)) < 5e-13
        checks += 1
    # The vector (1,1,1)/sqrt(3) minimizes width; coordinate axes maximize it.
    for u in [np.array([1.,0,0]), np.array([0,1.,0]), np.array([0,0,1.])]:
        assert abs(eigen_width(u)-1.) < 1e-13
        checks += 1
    for u in [np.array([a,b,c],float)/ROOT3 for a in [-1,1]
              for b in [-1,1] for c in [-1,1]]:
        assert abs(eigen_width(u)-MIN_WIDTH) < 1e-13
        checks += 1
    # The one-dimensional CDF is nondecreasing and lies in [0,1].
    grid = np.linspace(MIN_WIDTH+1e-5, 1.-1e-5, 51)
    values = np.array([cdf_width(w) for w in grid])
    assert np.all(np.diff(values) > 0)
    assert np.all((0 < values) & (values < 1))
    checks += len(grid)+2
    # Independent sampling of the spherical parameterization checks normalization.
    n = 2**19
    z = RNG.uniform(0., 1., n)
    phi = RNG.uniform(0., 2*PI, n)
    coords = np.column_stack((np.sqrt(1-z*z)*np.cos(phi),
                              np.sqrt(1-z*z)*np.sin(phi), z))
    sample_widths = np.array([formula_width(v) for v in coords])
    for w in [.88,.9,.93,.96,.98]:
        empirical = np.mean(sample_widths <= w)
        exact = cdf_width(w)
        assert abs(empirical-exact) < 0.004
        checks += 1
    # Tails: actual quadrature, not simulated rare-event frequencies.
    for eps, tol in [(0.01, .05), (0.005,.025),(.002,.011),(.001,.006)]:
        ratio = cdf_width(MIN_WIDTH+eps)/(12*eps**2)
        assert 1. < ratio < 1.+tol
        checks += 1
    for eps,tol in [(1e-2,.03),(2e-3,.006),(5e-4,.003),(1e-4,.002)]:
        ratio = upper_tail(eps)/upper_two_term(eps)
        assert 1.-tol < ratio < 1.
        checks += 1
    print('PASS', checks, 'deterministic numerical assertions')
    print('minimum-tail ratio at eps=0.001:',
          cdf_width(MIN_WIDTH+.001)/(12*.001**2))
    for eps in [1e-2,2e-3,1e-4]:
        print('upper tail',eps,upper_tail(eps),
              'two-term ratio',upper_tail(eps)/upper_two_term(eps))


if __name__ == '__main__':
    main()
