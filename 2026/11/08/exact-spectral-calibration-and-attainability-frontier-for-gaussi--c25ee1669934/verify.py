#!/usr/bin/env python3
"""Deterministic numerical sanity checks for the spectral Gaussian posterior-KL theorem.

All assertions are finite checks; the analytic proof establishes the general claim.
"""
import math
import cmath
import random


def scalars(a, b, sigma):
    rho = a / b
    h = (sigma / b) ** 2
    L = (1 - rho) ** 2 + h
    return rho, h, L


def z_opt(a, b, sigma):
    rho, _, L = scalars(a, b, sigma)
    if rho <= 0:
        return 0.0
    disc = math.sqrt((2 * L - 1) ** 2 + 8 * L * rho)
    # Stable positive-root identity, including near cancellation.
    return (4 * rho) / (disc + 2 * L - 1)


def poly(z, rho, L):
    return L * z * z + (2 * L - 1) * z - 2 * rho


def reduced(z, rho, h):
    return 0.5 * (-math.log1p(z) + ((1 + (1 - rho) * z) ** 2 + h * z * z) / (1 + z))


def kl(a, b, sigma, z):
    # Independent Gaussian mean/covariance calculation.
    true_cov = sigma**2 / (sigma**2 + a**2)
    true_gain = a / (sigma**2 + a**2)
    model_cov = 1 / (1 + z)
    model_gain = (z / b) / (1 + z)
    yy = a * a + sigma * sigma
    return 0.5 * (
        true_cov / model_cov - 1
        + math.log(model_cov / true_cov)
        + (model_gain - true_gain)**2 * yy / model_cov
    )


def close(x, y, tol=5e-8):
    return abs(x - y) <= tol * (1 + abs(x) + abs(y))


def main():
    rng = random.Random(261038434)
    cases = [
        (-4, 0.1, 0.01), (0, 1, 1), (1, 1, 2), (2, 1, 1),
        (0.01, 10, 0.005), (10, 0.01, 1), (1, 1, 0.01),
    ]
    cases += [(rng.uniform(-5, 5), 10**rng.uniform(-1, 1),
               10**rng.uniform(-1, 1)) for _ in range(2000)]
    for a, b, sigma in cases:
        rho, h, L = scalars(a, b, sigma)
        z = z_opt(a, b, sigma)
        zeea = 1/L
        assert z >= 0 and math.isfinite(z)
        if a > 0:
            assert z > 0
            assert close(poly(z, rho, L), 0, tol=2e-7)
        else:
            assert z == 0
            assert poly(1e-8, rho, L) > 0
        sign = (a > b) - (a < b)
        measured = (z > zeea * (1 + 5e-9)) - (z < zeea * (1 - 5e-9))
        assert measured == sign, (a, b, sigma, z, zeea)
        assert kl(a, b, sigma, z) <= kl(a, b, sigma, zeea) + 1e-8
        assert kl(a, b, sigma, z) <= kl(a, b, sigma, 0) + 1e-8
        for probe in (0.001, 0.03, 0.25, 1, 4):
            # Complex-step differentiation avoids subtractive cancellation.
            zz = probe + 1e-14j
            jc = 0.5 * (-cmath.log(1+zz) + ((1+(1-rho)*zz)**2+h*zz*zz)/(1+zz))
            numerical = jc.imag / 1e-14
            analytic = poly(probe, rho, L) / (2*(1+probe)**2)
            assert close(numerical, analytic, tol=2e-8), (a,b,sigma,probe)
            # The direct KL and the reduced log-normalizer differ by a constant only.
            assert close(reduced(probe, rho, h) - reduced(0, rho, h),
                         kl(a, b, sigma, probe) - kl(a, b, sigma, 0))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
