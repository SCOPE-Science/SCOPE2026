#!/usr/bin/env python3
"""Independent numerical identities for the weak-contraction stationary tail asymptotic.

Uses numpy and scipy. The asymptotic theorem is proved analytically in RESULT.md;
finite numerical comparisons do not certify the limits.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import spence


def lam(t):
    # spence(z) = Li_2(1-z)
    return float(spence(1.0 - t*t))


def lamp(t):
    return -2.0*math.log1p(-t*t)/t if t != 0 else 0.0


def lampp(t):
    if t == 0:
        return 2.0
    return 4.0/(1.0-t*t) + 2.0*math.log1p(-t*t)/(t*t)


def saddle(y):
    assert y > 0
    return brentq(lambda t: lamp(t)-y, 1e-12, 1.0-1e-13,
                  xtol=1e-14)


def rate(y):
    t = saddle(y)
    return y*t - lam(t)


def geometric_terms(h):
    j = np.arange(1+int(math.ceil(-math.log(1e-15)/h)))
    return np.exp(-h*j)


def finite_log_mgf(h, t, b=None):
    if b is None:
        b = geometric_terms(h)
    return float(-np.log1p(-(t*t)*b).sum())


def tilted_fourier_tail_ratio(h, y):
    """Exact Fourier integral / leading asymptotic, both under a positive tilt.

    Under tilt t, the tail integral is (1/pi)*int_0^infty
    Re[M(t+is)/M(t) exp(-is*y/h)/(t+is)] ds.
    The factor exp(-I/h) cancels analytically in the ratio to avoid
    catastrophic loss of significance for rare events.
    """
    t = saddle(y)
    b = geometric_terms(h)
    w = y/h
    log_mt = finite_log_mgf(h, t, b)
    log_factors_t = np.log1p(-(t*t)*b)

    def integrand(s):
        z = t + 1j*s
        log_ratio = np.sum(log_factors_t - np.log1p(-(z*z)*b))
        return float((np.exp(log_ratio-1j*s*w)/(t+1j*s)).real)

    # The first 1/h factors bound the tilted characteristic function by
    # (1+exp(-1)*s*s)^(-floor(1/h)), making the s>5 tail negligible here.
    integral, error = quad(integrand, 0.0, 8.0, epsabs=5e-12,
                           epsrel=5e-11, limit=220)
    integral /= math.pi
    leading_coefficient = math.sqrt(h) / (t*math.sqrt(
        2*math.pi*lampp(t)*(1-t*t)))
    ratio = math.exp(log_mt-lam(t)/h)*integral/leading_coefficient
    return ratio, error


def run():
    count = 0
    for t in (0.13, 0.31, 0.67, 0.86):
        assert abs(lampp(t) - (lamp(t+1e-5)-lamp(t-1e-5))/2e-5) < 2e-7
        count += 1
        prev = None
        for h in (0.20, 0.10, 0.05, 0.025):
            b = geometric_terms(h)
            m = finite_log_mgf(h, t, b)
            # Euler--Maclaurin endpoint term; the residual is O(h).
            residual = m - lam(t)/h + math.log1p(-t*t)/2
            assert abs(residual) < 0.50*h
            if prev is not None:
                assert abs(residual) < abs(prev)*0.65
            prev = residual
            count += 1
            # The first factor and remaining product satisfy the stationary
            # Fourier transform recursion (up to numerical truncation).
            a = math.exp(-h/2)
            lhs = finite_log_mgf(h, t, b)
            rhs = -math.log1p(-t*t) + finite_log_mgf(h, a*t, b)
            assert abs(lhs-rhs) < 2e-10
            count += 1
    for y in (.10, .30):
        q = rate(y)
        assert abs(q - (y*y/4-y**4/64)) < 1.7*y**6
        count += 1
    for y in (16.0, 20.0):
        difference = rate(y)-y+math.pi**2/6
        assert abs(difference/math.exp(-y/2)-1.0) < .02
        count += 1
    # Two independently evaluated quantities: an exact tilted Fourier
    # integral and the asymptotic from dilogarithm/saddle curvature.
    for y in (1.0, 2.0):
        ratios=[]
        for h in (.25,.12,.06):
            ratio, error = tilted_fourier_tail_ratio(h,y)
            assert 0.70 < ratio < 1.001
            assert error < 2e-9
            ratios.append(ratio)
            count += 1
        assert ratios[0] < ratios[1] < ratios[2]
        assert ratios[-1] > (.89 if y == 1 else .96)
        count += 1
        print('tail ratio y=',y,'h=0.25/0.12/0.06:',
              ', '.join(f'{r:.9f}' for r in ratios))
    print(f'PASS: {count} deterministic identity and asymptotic assertions')

if __name__=='__main__':
    run()
