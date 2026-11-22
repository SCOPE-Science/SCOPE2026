#!/usr/bin/env python3
"""Deterministic numerical and symbolic sanity checks for the 3-point spherical-code endpoint.
Dependencies: Python 3.10+, NumPy >=1.24, SciPy >=1.10.
The proof is analytical; numerical tests do not establish an asymptotic theorem.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, gammaln

THETA_STAR = 2 * math.pi / 3


def endpoint_constant(d):
    assert isinstance(d, int) and d >= 3
    return (2 ** (3 - d) * 3 ** ((5 * d - 2) / 4) * math.gamma(d / 2)
            / (d * (d + 2) * math.pi ** 1.5 * math.gamma((d - 1) / 2)))


def gram_constant(d):
    # Density of (U1.U2, U1.U3, U2.U3) over the positive Gram domain.
    return math.exp(2 * gammaln(d / 2) - 1.5 * math.log(math.pi)
                    - gammaln((d - 1) / 2) - gammaln((d - 2) / 2))


def exact_probability(d, h):
    """Exact 2D beta-integral, numerically quadratured (not Monte Carlo).

    θ=2π/3-h; the domain is rescaled to [-2,1]^2 using the
    exact necessary condition x+y+z>=-3/2.
    """
    assert d >= 3 and 0 < h < 0.2
    q = math.cos(THETA_STAR - h)
    delta = q + .5
    c = math.exp(gammaln(d / 2) - .5 * math.log(math.pi)
                 - gammaln((d - 1) / 2))
    a = (d - 2) / 2

    def value(v, u):
        x = -.5 + delta * u
        y = -.5 + delta * v
        zscale = math.sqrt((1 - x*x) * (1 - y*y))
        t = (q - x*y) / zscale
        if t <= -1:
            return 0.0
        beta_cdf = 1.0 if t >= 1 else float(betainc(a, a, (1 + t) / 2))
        return c*c * ((1 - x*x) * (1 - y*y)) ** ((d - 3)/2) * beta_cdf

    def inner(u):
        return quad(lambda v: value(v, u), -2, 1,
                    epsabs=1e-12, epsrel=3e-6, limit=100)[0]

    return delta*delta*quad(inner, -2, 1,
                            epsabs=1e-12, epsrel=3e-6, limit=100)[0]


def run_checks():
    # Independent cap-lens and Gram-determinant integrations lead to
    # algebraically equivalent normalizations.
    for d in [3, 4, 5, 6, 9]:
        a = (d - 4) / 2
        J = 3 ** ((d+2)/2) * math.gamma((d-2)/2) / math.gamma((d+4)/2)
        gram = (gram_constant(d) * (3/2)**a * J
                * (math.sqrt(3)/2)**((d+2)/2))
        assert math.isclose(gram, endpoint_constant(d), rel_tol=2e-13)
        # T/3 ~ Beta(3,(d-2)/2), its mean is 6/(d+4).
        assert math.isclose(3/(3+(d-2)/2), 6/(d+4), rel_tol=1e-15)

    assert math.isclose(endpoint_constant(3), 3**(9/4)/(10*math.pi), rel_tol=1e-14)
    for d in (3, 4, 5):
        previous_error = float('inf')
        for h in (.10, .05, .025, .0125):
            exact = exact_probability(d, h)
            leading = endpoint_constant(d) * h**((d+2)/2)
            ratio = exact/leading
            error = abs(ratio-1)
            assert exact > 0 and error < previous_error
            previous_error = error
            assert error < (.045 if h == .1 else .03)
            print(f'd={d} h={h:.4f} exact={exact:.12g} ratio={ratio:.9f}')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    run_checks()
