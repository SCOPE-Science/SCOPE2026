#!/usr/bin/env python3
"""Reproduce the variance, unique-maximum equation and numerical checks.

This script supplies deterministic checks. The global uniqueness proof is analytic
and appears in RESULT.md, not in a finite numerical search.

Dependencies: Python 3.10+, scipy, mpmath.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtr
import mpmath as mp

PI = math.pi
counter = [0]


def near(a, b, tolerance=3e-9):
    assert math.isfinite(float(a)) and math.isfinite(float(b)), (a, b)
    assert abs(float(a) - float(b)) <= tolerance, (a, b)
    counter[0] += 1


def positive(v):
    assert v > 0, v
    counter[0] += 1


def variance_correlation(a):
    return quad(
        lambda r: math.sqrt(1-r*r) * (
            math.exp(-a/(1+r)) - (math.exp(-a/(1-r)) if r < 1 else 0.0)
        ) / PI,
        0.0, 1.0, epsabs=2e-12, limit=300,
    )[0]


def derivative_correlation(a):
    return quad(
        lambda r: math.sqrt(1-r*r) * (
            (math.exp(-a/(1-r))/(1-r) if r < 1 else 0.0)
            - math.exp(-a/(1+r))/(1+r)
        ) / PI,
        0.0, 1.0, epsabs=2e-12, limit=300,
    )[0]


def weight(s):
    return math.sqrt(2*s-1) / s**3


def a_integral(a):
    return quad(lambda s: s*weight(s)*math.exp(-a*s), 0.5, 1.0,
                epsabs=2e-13)[0]


def b_integral(a):
    return quad(lambda s: s*weight(s)*math.exp(-a*s), 1.0, math.inf,
                epsabs=2e-13)[0]


def gaussian_rectangle(z, r):
    # Independent conditional-normal integral; no Plackett identity is used.
    c = math.sqrt(1-r*r)
    phi = lambda x: math.exp(-x*x/2) / math.sqrt(2*PI)
    return quad(lambda x: phi(x)*(ndtr((z-r*x)/c)-ndtr((-z-r*x)/c)),
                -z,z,epsabs=6e-11, limit=300)[0]


def variance_rectangle(z):
    p=2*ndtr(z)-1
    return quad(lambda r: 2*r*(gaussian_rectangle(z,r)-p*p), 0, 1,
                epsabs=5e-11, limit=300)[0]


def main():
    for z in (0.3, 0.82952378, 1.0, 1.96):
        a = z*z
        v=variance_correlation(a)
        positive(v)
        near(v, variance_rectangle(z), 7e-10)
        near(derivative_correlation(a), (b_integral(a)-a_integral(a))/PI, 2e-11)
    for rho in (0.15, 0.5, 0.85):
        for z in (0.25, 0.8, 1.96):
            h=2e-5
            approximate=(gaussian_rectangle(z,rho+h)-gaussian_rectangle(z,rho-h))/(2*h)
            exact=(math.exp(-z*z/(1+rho))-math.exp(-z*z/(1-rho)))/(PI*math.sqrt(1-rho*rho))
            near(approximate,exact,1e-8)
    for a in (0.1, 0.5, 0.6881, 1.0, 2.0):
        positive(a_integral(a))
        positive(b_integral(a))
    for l,r in ((0.1,0.5), (0.5,1.), (1.,2.), (2.,4.)):
        positive(a_integral(r)*b_integral(l)-a_integral(l)*b_integral(r))
    near(derivative_correlation(0.0),2/PI,3e-11)
    aroot=brentq(derivative_correlation,0.2,1.6,xtol=1e-14)
    near(aroot,0.6881097032034672,2e-13)
    positive(derivative_correlation(0.4))
    positive(-derivative_correlation(1.2))
    near(a_integral(aroot),b_integral(aroot),6e-13)
    z=math.sqrt(aroot)
    v=variance_correlation(aroot)
    delta=2*(1-ndtr(z))
    nominal=1-delta
    near(z,0.8295237809752456,2e-13)
    near(delta,0.4068080858459806,2e-13)
    near(nominal,0.5931919141540194,2e-13)
    near(v,0.08135656185520381,2e-13)
    near(math.sqrt(v),0.2852307168858288,2e-13)
    # Independent high-precision quadrature, not reusing SciPy implementation.
    mp.mp.dps=38
    M=lambda x:mp.mpf(str(x))
    def mp_variance(a):
        return mp.quad(lambda r: mp.sqrt(1-r*r)*(
            mp.exp(-a/(1+r))-mp.exp(-a/(1-r))),
            [0,mp.mpf('0.5'),mp.mpf('0.9'),1])/mp.pi
    def mp_derivative(a):
        return mp.quad(lambda r: mp.sqrt(1-r*r)*(
            mp.exp(-a/(1-r))/(1-r)-mp.exp(-a/(1+r))/(1+r)),
            [0,mp.mpf('0.5'),mp.mpf('0.9'),1])/mp.pi
    high_root=mp.findroot(mp_derivative,(mp.mpf('.6'),mp.mpf('.9')))
    high_variance=mp_variance(high_root)
    near(aroot, high_root, 2e-13)
    near(v, high_variance, 2e-13)
    for z0 in (0.4,1.96,3.0):
        near(variance_correlation(z0*z0),mp_variance(M(z0*z0)),4e-12)
    print(f"assertions_passed={counter[0]}")
    print(f"unique_root_a={mp.nstr(high_root,32)}")
    print(f"unique_root_z={mp.nstr(mp.sqrt(high_root),32)}")
    print(f"noncoverage_delta={mp.nstr(1-mp.erf(mp.sqrt(high_root/2)),32)}")
    print(f"nominal_coverage={mp.nstr(mp.erf(mp.sqrt(high_root/2)),32)}")
    print(f"max_variance={mp.nstr(high_variance,32)}")
    print(f"max_sd={mp.nstr(mp.sqrt(high_variance),32)}")
    print("analytic_uniqueness_check=prove_support_separation_in_RESULT.md")


if __name__ == '__main__':
    main()
