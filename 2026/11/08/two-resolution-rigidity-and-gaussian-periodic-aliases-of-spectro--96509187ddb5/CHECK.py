#!/usr/bin/env python3
"""Independent deterministic quadrature checks for Gaussian-log-curvature aliasing.

Run: python CHECK.py. Only Python's standard library is required.
"""
import math


def simpson_values(fn, lo=-7.0, hi=8.0, intervals=16000):
    assert intervals % 2 == 0
    step = (hi-lo)/intervals
    total = fn(lo)+fn(hi)
    for j in range(1, intervals):
        total += (4 if j % 2 else 2)*fn(lo+j*step)
    return total*step/3


def intensity(density, c, center):
    def moment(power):
        return simpson_values(lambda x: x**power * math.exp(-c*(x-center)**2)*density(x))
    z0, z1, z2 = moment(0), moment(1), moment(2)
    mu = z1/z0
    return 2*c*(z2/z0-mu*mu)


def main():
    c1, c2, c3 = 2*math.pi, 4*math.pi, 3*math.pi
    a, b, h = 1.0, 0.3, 0.7
    k1 = h*(a+c2)/(c2-c1)
    k2 = h*(a+c1)/(c2-c1)
    assert math.isclose(k1-k2,h,rel_tol=0,abs_tol=1e-13)
    assert math.isclose((a+c1)*k1,(a+c2)*k2,rel_tol=0,abs_tol=1e-13)

    def modulation(x):
        return 1+0.25*math.cos(2*math.pi*x/h)
    def spectrum(x):
        return math.exp(-a*x*x+b*x)*modulation(x)
    def alias(x):
        return math.exp(2*c1*k1*x-c1*k1*k1)*spectrum(x-k1)

    # The identity is scalar proportionality for either width, not equality of spectra.
    def gauge2(x):
        return math.exp(2*c2*k2*x-c2*k2*k2)*spectrum(x-k2)
    ratios = [alias(x)/gauge2(x) for x in (-3, -1.3, 0, 0.9, 3.7)]
    assert max(ratios)-min(ratios)<2e-10
    assert not math.isclose(alias(0)/spectrum(0),alias(1)/spectrum(1),rel_tol=1e-5)

    centers=(-2.3,-0.5,0,1.1,2.3)
    for c in (c1,c2):
        for center in centers:
            lhs,rhs=intensity(spectrum,c,center),intensity(alias,c,center)
            assert abs(lhs-rhs)<3e-8,(c,center,lhs,rhs)

    # A genuinely nonconstant periodic factor breaks equality at a generic third width.
    assert abs(intensity(spectrum,c3,0)-intensity(alias,c3,0))>0.05

    # Independent Gaussian-spectrum normalization: conditional variance 1/[2(c+a)].
    gaussian=lambda x: math.exp(-a*x*x+b*x)
    for c in (c1,c2,c3):
        for center in centers:
            assert abs(intensity(gaussian,c,center)-c/(a+c))<1e-8
    print('TWO_RESOLUTION_GAUSSIAN_PERIODIC_CHECKS_PASSED')


if __name__=='__main__':
    main()
