#!/usr/bin/env python3
"""Numerical and algebraic checks for discrete fractional heat gradients.

Requires scipy. This finite check is supporting evidence, not a proof of
unrestricted positivity, uniqueness of the crossover, or asymptotic theorems.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import iv, gammaln

TOL = 3e-9


def energy(theta):
    return 4.0 * math.sin(theta / 2.0) ** 2


def sharp_norm(s, t):
    return (2.0 / math.pi) * quad(
        lambda theta: math.exp(-t * energy(theta) ** s),
        0.0, math.pi, epsabs=2e-12, epsrel=2e-12, limit=300
    )[0]


def moment(s):
    return math.exp(s * math.log(4.0) + gammaln(s + 0.5)
                    - 0.5 * math.log(math.pi) - gammaln(s + 1.0))


def distribution_cdf(u):
    if u <= 0.0:
        return 0.0
    if u >= 4.0:
        return 1.0
    return 2.0 / math.pi * math.asin(math.sqrt(u) / 2.0)


def cdf_power(y, s):
    return distribution_cdf(y ** (1.0 / s))


def crossing_integral(a, b, t):
    # Distribution-function difference; split at the unique sign boundary.
    end = 4.0 ** b
    z = quad(lambda y: math.exp(-t*y)*(cdf_power(y,a)-cdf_power(y,b)),
             0.0, 1.0, epsabs=2e-11, limit=300)[0]
    z += quad(lambda y: math.exp(-t*y)*(cdf_power(y,a)-cdf_power(y,b)),
             1.0, end, epsabs=2e-11, limit=300)[0]
    return t*z


def check():
    # Gamma beta-integral moment, and endpoint Bessel formula.
    for s in (0.18, 0.25, 0.5, 0.75, 1.0):
        approx = quad(lambda th:energy(th)**s/math.pi,0,math.pi,
                      epsabs=2e-12,limit=300)[0]
        assert abs(approx-moment(s)) < 3e-9
    for t in (0.03, 0.3, 1.2, 2.5, 8.0):
        assert abs(sharp_norm(1.0,t)-2.0*math.exp(-2*t)*iv(0,2*t)) < 1e-11
    print('MOMENT_GAMMA_AND_CLASSICAL_BESSEL_NORMALIZATION_PASS')

    # Independent kernel Fourier coefficients must be strictly decreasing.
    for s in (0.25, 0.5, 0.9, 1.0):
        for t in (0.15, 0.7, 1.5, 4.0):
            p = [quad(lambda th:math.exp(-t*energy(th)**s)*math.cos(k*th)/math.pi,
                      0,math.pi,epsabs=2e-12,limit=300)[0]
                 for k in range(9)]
            assert all(p[k] > p[k+1] + 1e-12 for k in range(8))
            assert abs(sum(abs(p[k]-p[k+1]) for k in range(8))-(p[0]-p[8]))<1e-12
            assert abs(sharp_norm(s,t)-2*p[0])<2e-9
    print('FINITE_FOURIER_UNIMODALITY_AND_SHARP_GRADIENT_IDENTITY_PASS')

    # Equivalent CDF representation and order crossing for representative pairs.
    tests = ((0.25, 0.5, 1.41865666092558),
             (0.5, 1.0, 1.35174324607504),
             (0.75, 1.0, 1.29424293188783),
             (0.3, 0.9, 1.39073785343110))
    for a,b,ref in tests:
        for t in (0.12,0.5,1.2,1.7,3.5):
            direct=(sharp_norm(a,t)-sharp_norm(b,t))/2
            cdf=crossing_integral(a,b,t)
            assert abs(direct-cdf)<TOL,(a,b,t,direct,cdf)
        root=brentq(lambda t: sharp_norm(a,t)-sharp_norm(b,t),0.1,5.,xtol=5e-13)
        assert abs(root-ref)<1e-10,(a,b,root,ref)
        assert sharp_norm(a,root*0.75)>sharp_norm(b,root*0.75)
        assert sharp_norm(a,root*1.25)<sharp_norm(b,root*1.25)
        print('CROSSOVER_SAMPLE_PASS',a,b,format(root,'.12f'))
    print('CDF_LAPLACE_IDENTITY_AND_FOUR_CROSSINGS_PASS')

    # Derivative of the e^t/t-rescaled transform is negative at sample times;
    # the actual strict global derivative sign is proved analytically.
    for a,b,_ in tests:
        for t in (0.0,0.3,1.0,3.0,7.0):
            integrand=lambda y:(y-1.0)*math.exp(-t*(y-1.0))*(cdf_power(y,a)-cdf_power(y,b))
            z=quad(integrand,0.,1.,epsabs=1e-11,limit=300)[0]
            z+=quad(integrand,1.,4.**b,epsabs=1e-11,limit=300)[0]
            assert z>0,(a,b,t,z)
    print('RESCALED_TRANSFORM_DERIVATIVE_SIGN_SAMPLES_PASS')
    print('ALL_FRACTIONAL_LATTICE_CROSSING_CHECKS_PASS')


if __name__=='__main__':
    check()
