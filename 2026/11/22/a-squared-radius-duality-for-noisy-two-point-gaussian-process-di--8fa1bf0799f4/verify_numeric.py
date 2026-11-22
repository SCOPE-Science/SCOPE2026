"""Standalone numerical cross-checks of a two-point posterior derivative design.

Python 3 standard library only. The analytic theorem does not rely on a grid.
Run: python3 verify_numeric.py
"""
from math import exp, sqrt, isclose


def threshold(t):
    return (1+t)*exp(-2*t)/(1-t)


def root(noise):
    lo, hi = 0.0, 1.0 - 1e-14
    for _ in range(120):
        mid = (lo+hi)/2
        if threshold(mid) < 1+noise:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def risk(noise, h, kind):
    if kind == 'Gaussian':
        g = h*exp(-h*h/2)
        corr = exp(-2*h*h)
    else:
        g = h*exp(-h)
        corr = (1+2*h)*exp(-2*h)
    return 1 - 2*g*g/(1+noise-corr)


checks = 0
for noise in (1e-6, .01, .1, 1, 10, 100):
    t = root(noise)
    assert 0 < t < 1
    assert isclose(threshold(t), 1+noise, rel_tol=5e-11, abs_tol=1e-12)
    h_m, h_g = t, sqrt(t)
    assert isclose(h_m, h_g*h_g, rel_tol=1e-13)
    assert isclose(risk(noise, h_m, 'Matern'), t, abs_tol=5e-12)
    assert isclose(risk(noise, h_g, 'Gaussian'), 1-(1-t)*exp(t), abs_tol=5e-12)
    assert risk(noise, h_g, 'Gaussian') < risk(noise, h_m, 'Matern')
    for kind, optimal in (('Gaussian', h_g), ('Matern', h_m)):
        for multiplier in (.6, .8, 1.2, 1.7, 3):
            assert risk(noise, optimal*multiplier, kind) > risk(noise, optimal, kind)-1e-11
            checks += 1
    checks += 6
print('Numerical covariance and optimum checks: PASS ('+str(checks)+')')
