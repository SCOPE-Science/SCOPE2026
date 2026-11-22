#!/usr/bin/env python3
"""Independent reproducibility checks for the free comb's Gamma-reset mixed moment."""
import math
from scipy.integrate import quad
from scipy.stats import gamma as gamma_distribution
from scipy.special import gammaln

checks = 0

def close(a, b, rtol=3e-8, atol=3e-11):
    global checks
    assert math.isclose(a, b, rel_tol=rtol, abs_tol=atol), (a, b)
    checks += 1

def age_moment(k, rate, power):
    return math.exp(gammaln(k + power + 1) - gammaln(k + 1)) / ((power + 1) * rate ** power)

def renewal_age_moment_by_quadrature(k, rate, power):
    mean = k / rate
    fun = lambda a: (a ** power) * gamma_distribution.sf(a, a=k, scale=1 / rate) / mean
    return quad(fun, 0, math.inf, epsabs=2e-11, epsrel=2e-11, limit=300)[0]

def closed_cov(k, rate, dx, dy):
    return (4 * dx * math.sqrt(dy) / (15 * math.sqrt(math.pi) * rate ** 1.5) *
            math.exp(gammaln(k + 1.5) - gammaln(k + 1)) * (1 - k))

def moments_cov(k, rate, dx, dy):
    a05 = age_moment(k, rate, 0.5)
    a10 = age_moment(k, rate, 1)
    a15 = age_moment(k, rate, 1.5)
    ex2 = (2 * dx / math.sqrt(math.pi * dy)) * a05
    ey2 = 2 * dy * a10
    ex2y2 = (8 * dx * math.sqrt(dy) / (3 * math.sqrt(math.pi))) * a15
    return ex2y2 - ex2 * ey2

for k in [0.2, 0.5, 0.8, 1.0, 1.2, 2.0, 3.0, 5.0]:
    for rate in [0.5, 2.0, 5.0]:
        for p in [0.0, 0.5, 1.0, 1.5]:
            close(age_moment(k, rate, p), renewal_age_moment_by_quadrature(k, rate, p))
        for dx, dy in [(0.2, 0.7), (1.0, 1.0), (2.0, 3.0)]:
            got = moments_cov(k, rate, dx, dy)
            expected = closed_cov(k, rate, dx, dy)
            close(got, expected)
            mx = (2*dx/math.sqrt(math.pi*dy))*age_moment(k, rate, 0.5)
            my = 2*dy*age_moment(k, rate, 1.0)
            close(got/(mx*my), (1-k)/(5*(k+1)))
            assert (got > 1e-12) if k < 1 else (got < -1e-12 if k > 1 else abs(got) < 1e-12)
            checks += 1

# Independently integrate the Poisson stationary product density over quadrants.
for rate in [0.3, 1.0, 4.0]:
    for dx, dy in [(0.25, 1.5), (1.0, 1.0)]:
        alpha = math.sqrt(2 * math.sqrt(rate * dy) / dx)
        beta = math.sqrt(rate / dy)
        integral = quad(lambda x: (alpha / 2) * math.exp(-alpha*x), 0, math.inf)[0] * \
                   quad(lambda y: (beta / 2) * math.exp(-beta*y), 0, math.inf)[0]
        close(4 * integral, 1.0)
        close(2 / alpha**2, (2 * dx / math.sqrt(math.pi * dy)) * age_moment(1, rate, 0.5))
        close(2 / beta**2, 2 * dy * age_moment(1, rate, 1))
        close(moments_cov(1, rate, dx, dy), 0.0)

# The free-excursion mixed local-time moment: integrate Brownian return kernel.
for dx, dy in [(0.4, 0.9), (1.0, 2.5)]:
    for t in [0.2, 1.0, 4.0]:
        integrated = 4 * dx * dy * quad(
            lambda s: (t-s) / math.sqrt(4 * math.pi * dy * s),
            0, t, points=[0], epsabs=5e-11, epsrel=5e-11)[0]
        close(integrated, 8 * dx * math.sqrt(dy) / (3 * math.sqrt(math.pi)) * t**1.5)

print(f"PASS: {checks} numerical and analytical cross-checks")
