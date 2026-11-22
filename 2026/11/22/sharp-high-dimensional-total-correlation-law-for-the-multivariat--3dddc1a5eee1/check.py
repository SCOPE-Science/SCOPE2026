#!/usr/bin/env python3
"""Numerical cross-checks for a common-exponential-shock copula entropy law.

Requires scipy; the infinite-dimensional conclusion is proved analytically in RESULT.md.
"""
from math import exp, log, isfinite
from scipy.integrate import quad
from scipy.special import digamma


def hb(p):
    if p == 0 or p == 1:
        return 0.0
    return -p * log(p) - (1 - p) * log(1 - p)


def minimum_density(t, theta, d):
    q = 1.0 - theta
    eps = q / d
    return (q / eps) * exp(-t / eps) + theta / (1.0 - eps) * (
        exp(-t) - exp(-t / eps))


def unit_exponential_plus_noise_entropy(eps):
    # Exact closed form for a sum of two independent exponential variables.
    r = eps / (1 - eps)
    return 1 + eps + log(1 - eps) + digamma(2 + r) - digamma(2)


def entropy_and_tc(theta, d):
    q = 1.0 - theta
    eps = q / d

    def integrand(t):
        val = minimum_density(t, theta, d)
        return -val * log(val) if val > 1e-260 else 0.0

    # The first piece resolves an O(1/d) peak, essential for large d.
    h = eps * quad(lambda z: integrand(eps * z), 0, 40,
                   epsabs=1e-10, limit=500)[0]
    h += quad(integrand, 40 * eps, 80, epsabs=1e-10,
              limit=500)[0]
    total_correlation = -d * log(q) + 1 + log(eps) - h
    return h, total_correlation


def verify(theta, d):
    q = 1 - theta
    eps = q / d
    # This is the Laplace-transform algebra proving unit exponential margins.
    for s in (0.0, 0.3, 1.0, 9.0):
        laplace = (q + theta / (1 + s)) / (1 + q * s)
        assert abs(laplace - 1 / (1 + s)) < 1e-13

    mass = quad(lambda z: minimum_density(eps * z, theta, d) * eps,
                0, 40, epsabs=1e-11)[0]
    mass += quad(lambda t: minimum_density(t, theta, d),
                 40 * eps, 80, epsabs=1e-11)[0]
    assert abs(mass - 1) < 2e-9, (theta, d, mass)

    h, tc = entropy_and_tc(theta, d)
    assert isfinite(tc) and tc >= -1e-9
    h_y = unit_exponential_plus_noise_entropy(eps)
    assert 1 - 1e-10 <= h_y <= 1 + log(1 + eps) + 1e-10

    h_j_given_m = (1 - theta) * (1 + log(eps)) + theta * h_y + hb(theta) - h
    assert -3e-9 <= h_j_given_m <= hb(theta) + 3e-9
    approx = -d * log(q) - theta * log(d / q) - hb(theta)
    residual = tc - approx
    # This is an exact entropy-mixture identity, not a numerical asymptotic fit.
    assert abs(residual - (h_j_given_m - theta * (h_y - 1))) < 3e-9
    assert residual >= -theta * log(1 + eps) - 3e-9
    bound_error = q * exp(-d**0.5 / q) + theta / (d**0.5)
    if bound_error <= 0.5:
        assert residual <= hb(bound_error) + 3e-9
    return tc, approx, residual


def main():
    for theta in (0.25, 0.5, 0.75):
        for d in (2, 5, 20, 100, 1000):
            tc, asym, residual = verify(theta, d)
            print(f"theta={theta:.2f} d={d:4d} "
                  f"TC={tc:.12f} asym={asym:.12f} residual={residual:.9f}")
    reference = ((0.5, 2, 0.315467309390),
                 (0.5, 100, 66.013754179575),
                 (0.5, 1000, 688.661456244993))
    for theta, d, target in reference:
        assert abs(verify(theta, d)[0] - target) < 4e-7
    print("All scalar-density, entropy, mixture, and error-bound checks passed.")


if __name__ == '__main__':
    main()
