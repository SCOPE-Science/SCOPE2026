#!/usr/bin/env python3
"""Supplementary arithmetic and quadrature checks for a planar convexity estimate.

The analytic argument concerns all convex bodies; these tests verify its explicit
harmonic witnesses and representative smooth support-function examples.
"""
import math
from fractions import Fraction

TAU = 2.0 * math.pi


def integrate_periodic(fun, steps=65536):
    return TAU * sum(fun(TAU*j/steps) for j in range(steps)) / steps


def harmonic_checks():
    r = Fraction(3, 4)
    for n in range(2, 401):
        eps = r / (2 * (n*n - 1))
        # A uniform strictly positive curvature radius and inclusion in B(0,1).
        assert r - (n*n - 1)*eps == r/2
        assert r + eps <= Fraction(7, 8)
        assert 2*n*eps > eps
        # The harmonic witness has d_H = eps, d_N = 2*n*eps.
        # Perimeters are 2*pi*r for both bodies.
        if n <= 17:
            actual = 0.5 * integrate_periodic(
                lambda theta: abs(float(eps)*n*math.sin(n*theta)))
            expected = float(2*n*eps)
            assert abs(actual-expected) < 1e-7
            bound = math.sqrt(2*math.pi*float(eps)*(
                4*math.pi*float(r)+2*math.pi*float(eps)))
            assert expected <= bound + 1e-11
    # For each exponent alpha > 1/2, 2n eps / eps^alpha diverges.
    for alpha in (0.51, 0.6, 0.75, 1.0):
        def quotient(n):
            eps = float(r / (2 * (n*n - 1)))
            return 2*n*eps / (eps**alpha)
        assert quotient(100000) > quotient(1000)
    return 399


def low_constant_checks():
    # A positive single-peaked angular bump, centered to have zero average.
    # The geometric construction scales each bump until h+h'' > 0.
    def bump(t):
        if abs(t) >= 1.0:
            return 0.0
        return math.exp(1.0 - 1.0/(1.0-t*t))
    previous = 2.0
    for width in (0.7, 0.35, 0.14, 0.07):
        average = integrate_periodic(lambda th: bump(
            ((th+math.pi) % TAU - math.pi)/width)) / TAU
        ratio = 1.0/(1.0-average)
        assert 1.0 < ratio < previous
        previous = ratio
    assert previous < 1.02
    return 4


def smooth_pairs():
    from random import Random
    rng = Random(90177)
    for trial in range(75):
        r = 0.75
        aa = [(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(2,10)]
        # Both bodies are positively curved: sum of derivative curvature
        # magnitudes is less than r/4.
        scale = r/(8*sum((k*k-1)*(abs(a)+abs(b))
                         for k,(a,b) in enumerate(aa,2)))
        coeff = [(k, scale*a, scale*b) for k,(a,b) in enumerate(aa,2)]
        def val(theta):
            return sum(a*math.cos(k*theta)+b*math.sin(k*theta)
                       for k,a,b in coeff)
        def der(theta):
            return sum(k*(-a*math.sin(k*theta)+b*math.cos(k*theta))
                       for k,a,b in coeff)
        N=8192
        eps=max(abs(val(TAU*j/N)) for j in range(N))
        pdist=integrate_periodic(lambda theta: abs(der(theta)),N)/2
        # Fixed perimeter: mean support difference is zero, hence d_H <= d_N.
        assert eps <= pdist + 1e-9
        # A discrete maximum is <= the exact supremum; the upper bound is
        # checked with a Lipschitz-conservative approximation to the supremum.
        max_der=sum(k*(abs(a)+abs(b)) for k,a,b in coeff)
        eps_upper=eps + max_der*math.pi/N
        bound=math.sqrt(2*math.pi*eps_upper*(4*math.pi*r+2*math.pi*eps_upper))
        assert pdist < bound
    return 75


def main():
    n=harmonic_checks()
    b=low_constant_checks()
    c=smooth_pairs()
    print('PASS: %d harmonic curvature/inclusion identities, %d bump sequences, '
          '%d smooth-pair checks' % (n,b,c))
    print('The estimates for all bodies and sharpness for every alpha>1/2 '
          'are established analytically; finite checks are supplementary.')

if __name__=='__main__':
    main()
