"""Supplementary numerical cross-checks for unequal-reliability interval coverage.

The mathematical proof is analytic; floating-point checks are not used as
certificates of its global quantifiers.
"""
from math import erf, exp, log, sqrt, isfinite
from random import Random


def gauss_c(radius, scale, reliability):
    if not (radius > 0 and scale > 0 and 0 < reliability < 1):
        raise ValueError('parameters outside theorem domain')
    a = exp(-2 * (radius / scale) ** 2)
    # Stable implementation: z is the positive root of a*z*z-(1-q)*z-q*a=0.
    # Here moderate width/scale ratios are used to avoid floating underflow.
    z = ((1-reliability) + sqrt((1-reliability)**2 + 4*reliability*a*a))/(2*a)
    return scale*scale * log(z) / (2*radius)


def cdf(x, scale):
    return 0.5 * (1 + erf(x/(sqrt(2)*scale)))


def objective(c, radius, scale, reliability):
    return cdf(c, scale)-cdf(c-2*radius, scale) + reliability*(cdf(c+2*radius, scale)-cdf(c, scale))


def general_optimal_c(radius, reliability, density):
    # Binary search using the proven monotonic derivative-density ratio.
    lo, hi = 0.0, radius
    for _ in range(80):
        c = (lo+hi)/2
        d = (1-reliability)*density(c)-density(c-2*radius)+reliability*density(c+2*radius)
        if d > 0: lo = c
        else: hi = c
    return (lo+hi)/2


def check():
    rng = Random(2024)
    assertions = 0
    for _ in range(160):
        radius = rng.uniform(0.35,2)
        scale = rng.uniform(0.65,2.7)
        q = rng.uniform(0.03,0.97)
        c = gauss_c(radius,scale,q)
        assert 0 < c < radius
        assertions += 1
        optimum = objective(c,radius,scale,q)
        for j in range(161):
            x = -3*radius + 6*radius*j/160
            assert optimum + 1e-11 >= objective(x,radius,scale,q)
            assertions += 1
        # For every fixed auxiliary probability the optimum improves both
        # the symmetric touching arrangement and a centered primary alone.
        assert optimum > objective(0,radius,scale,q)
        assert optimum > cdf(radius,scale)-cdf(-radius,scale)
        assertions += 2
    for radius in [0.5,1,2]:
        for q in [0.1,0.4,0.8]:
            density = lambda x: 1/(2+2*__import__('math').cosh(x))
            c = general_optimal_c(radius,q,density)
            assert 0 < c < radius
            f = lambda x: 1/(1+exp(-x))
            p = f(c)-f(c-2*radius)+q*(f(c+2*radius)-f(c))
            for j in range(81):
                x = -2*radius+5*radius*j/80
                assert p + 1e-11 >= f(x)-f(x-2*radius)+q*(f(x+2*radius)-f(x))
                assertions += 1
            assertions += 1
    assert isfinite(gauss_c(1.0,1.0,0.5))
    assertions += 1
    print('PASS', assertions, 'supplementary assertions')


if __name__=='__main__':
    check()
