"""Reproducible supplementary checks of the finite-window two-bloom theorem.

Uses only the Python standard library. The universal proof is in RESULT.md.
"""
from math import exp, atanh, sqrt, isclose


def R(z, a, w=1.0, sigma=1.0):
    return exp(-((z-a)/sigma)**2/2)+exp(-((z+a)/sigma)**2/2)


def derivative(z, a, w=1.0, sigma=1.0):
    return R(z+w, a, w, sigma)-R(z-w, a, w, sigma)


def bisect(func, lo, hi, iters=95):
    assert func(lo)*func(hi)<0, (lo, hi, func(lo), func(hi))
    sign = func(lo)>0
    for _ in range(iters):
        mid = (lo+hi)/2
        if (func(mid)>0)==sign:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def threshold(w=1.0, sigma=1.0):
    return bisect(lambda a:a*w/(sigma*sigma)-atanh(w/a), w*(1+1e-9), max(w+5*sigma, 2*w))


def positive_mode(a, w=1.0, sigma=1.0):
    # The derivative is positive close to zero in the split regime.
    return bisect(lambda z:derivative(z,a,w,sigma), 1e-4, a+w+8*sigma)


def verify():
    w=sigma=1.0
    critical=threshold(w,sigma)
    assert abs(critical-1.199678640257734)<1e-12
    assert critical>w
    assert derivative(1e-3,1.0,w,sigma)<0
    assert derivative(1e-3,1.5,w,sigma)>0
    assert derivative(6.0,1.5,w,sigma)<0
    mode=positive_mode(1.5,w,sigma)
    assert abs(mode-1.35065977854278)<1e-9
    assert abs(derivative(mode,1.5,w,sigma))<1e-11
    assert abs(derivative(-mode,1.5,w,sigma))<1e-11
    assert derivative(mode-0.03,1.5,w,sigma)>0
    assert derivative(mode+0.03,1.5,w,sigma)<0
    coefficient=sqrt((3*sigma*sigma/critical)*(1+sigma*sigma/(critical*critical-w*w)))
    assert abs(coefficient-2.86251431024264)<1e-9
    for eps in (1e-3,1e-4):
        center=positive_mode(critical+eps,w,sigma)
        assert abs(center/sqrt(eps)-coefficient)<0.003
    for separation, width in ((0.4,0.01),(0.9,0.1),(1.01,0.15),(1.5,2.0),(2.0,4.0)):
        # Both a <= sigma or w >= a force the central optimum.
        if separation<=sigma or width>=separation:
            assert derivative(0.005,separation,width,sigma)<0
    for width in (0.1,0.5,1.0,2.0):
        crit=threshold(width,sigma)
        assert crit>width
        assert abs(crit*width/(sigma*sigma)-atanh(width/crit))<1e-9
        assert derivative(0.001,crit*0.99,width,sigma)<0
        assert derivative(0.001,crit*1.01,width,sigma)>0
    print('PASS: threshold, symmetry, sample modes, edge signs, split coefficient, multiwidth checks')


if __name__=='__main__':
    verify()
