#!/usr/bin/env python3
"""Independent numerical consistency checks for the sharp circle-heat variation law.

All formulas in this file are explicit and use Python's standard library.
Numerical quadrature and sampling do not replace the analytical proofs.
"""
from math import pi, exp, sqrt, sin, cos, erf, erfc, fsum
from random import Random


def kernel(t, x):
    """Wrapped Gaussian, explicitly periodized with negligible truncated tails."""
    return fsum(exp(-(x+2*pi*k)**2/(4*t)) for k in range(-10, 11)) / sqrt(4*pi*t)


def k_fourier(t, x):
    acc = 1.0
    for m in range(1, 200):
        term = 2*exp(-m*m*t)*cos(m*x)
        acc += term
        if m > 10 and 2*exp(-m*m*t) < 1e-15:
            break
    return acc/(2*pi)


def K_fourier(t):
    return 4/pi*fsum((-1.0)**j * exp(-(2*j+1)**2*t)/(2*j+1) for j in range(100))


def K_gaussian(t):
    # CDF of each wrapped Gaussian contribution in the central semicircle.
    sig = sqrt(2*t)
    cdf = fsum((erf((pi/2+2*pi*j)/(sig*sqrt(2)))-erf((-pi/2+2*pi*j)/(sig*sqrt(2))))/2 for j in range(-10,11))
    return 2*cdf-1


def K_shift(t,h, N=2400):
    # Distance between two translated heat kernels, one-half of their L1 difference.
    dx=2*pi/N
    return dx*fsum(abs(kernel(t,-pi+(j+0.5)*dx)-kernel(t,-pi+(j+0.5)*dx-h)) for j in range(N))/2


def K_small_defect(t):
    leading = 8/(pi**1.5)*sqrt(t)*exp(-pi*pi/(16*t))
    return leading*(1-8*t/pi**2)


def check():
    tests = [0.035,0.08,0.2,0.7,1.6]
    for t in tests:
        K=K_fourier(t)
        assert 0<K<1
        assert abs(K-K_gaussian(t)) < 3e-13, (t,K,K_gaussian(t))
        for x in (0, .25, .7, 1.2, pi/2, 2.3, pi):
            assert abs(kernel(t,x)-k_fourier(t,x)) < 2e-12
        assert abs(K_shift(t,pi)-K)<2e-5
        for h in (.2, .45, 1.1, pi/2, 2.4):
            assert K_shift(t,h) < K - 5e-6, (t,h,K_shift(t,h),K)
        print('FOURIER_GAUSSIAN_ANTIPODAL_GAIN_PASS',t,round(K,13))

    # Two different unsigned Jordan supports: the variation cannot exceed K.
    rng=Random(20261115)
    n=720
    dx=2*pi/n
    grid=[-pi+(j+.5)*dx for j in range(n)]
    for t in (.1,.4,1.0):
        K=K_fourier(t)
        for _ in range(35):
            loc_p=[rng.uniform(-pi,pi) for i in range(3)]
            loc_q=[rng.uniform(-pi,pi) for i in range(4)]
            wp=[rng.random()+.02 for x in loc_p]
            wq=[rng.random()+.02 for x in loc_q]
            wp=[w/sum(wp) for w in wp]; wq=[w/sum(wq) for w in wq]
            mu=[sum(w*kernel(t,z-a) for w,a in zip(wp,loc_p))-sum(w*kernel(t,z-b) for w,b in zip(wq,loc_q)) for z in grid]
            v=dx*sum(abs(x) for x in mu)/2
            assert v<K+2e-5,(t,v,K)
        print('RANDOM_JORDAN_MEASURE_CONTRACTION_PASS',t,35)

    # Monotonicity and strict failure of multiplicativity.
    for a,b in ((.05,.08),(.2,.3),(.5,1.0),(.7,2.0)):
        assert K_fourier(a+b)<K_fourier(a)*K_fourier(b)-1e-9
        assert K_fourier(a+b)<K_fourier(a)
    print('STRICT_SEMIGROUP_SUBMULTIPLICATIVITY_PASS')

    # Leading and one correction term of the small-time Gaussian tail.
    for t in (.04,.06,.09):
        exact=1-K_gaussian(t)
        predicted=K_small_defect(t)
        assert abs(exact/predicted - 1)<.03,(t,exact,predicted)
    print('SMALL_TIME_NONPERTURBATIVE_DEFICIT_PASS')

    for t in (1.5,2,3):
        approx=4/pi*exp(-t)-4/(3*pi)*exp(-9*t)
        assert abs(K_fourier(t)-approx) < max(1e-14,4/pi*exp(-25*t))
    print('LARGE_TIME_TWO_MODE_EXPANSION_PASS')
    print('ALL_CIRCLE_HEAT_BV_CHECKS_PASS')

if __name__=='__main__': check()
