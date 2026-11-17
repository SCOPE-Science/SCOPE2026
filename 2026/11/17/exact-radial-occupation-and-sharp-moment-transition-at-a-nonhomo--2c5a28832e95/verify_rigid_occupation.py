#!/usr/bin/env python3
"""Independent numerical checks for a quartic rigid oscillator's exact radial law.

These finite checks illustrate, rather than prove, the accompanying analytic theorem.
Standard-library-only Python 3.
"""
from math import pi, atan, sin, cos, sqrt, acos, gamma, log, isclose


def J(r, a=1.0, b=1.0):
    assert r > 0 and a > 0 and b > 0
    w = sqrt(b/a)/r
    if w < 0.2:
        difference = sum(((-1)**(k+1))*w**(2*k+1)/(2*k+1)
                         for k in range(1, 18))
    else:
        difference = w-atan(w)
    return sqrt(a)/b**1.5*difference


def invJ(q, a=1.0, b=1.0):
    assert q > 0
    low, high = 1.e-12, 1.0
    while J(high, a, b) > q:
        high *= 2
    while J(low, a, b) < q:
        low *= 0.5
    for _ in range(85):
        mid = (low+high)/2
        if J(mid, a, b) > q:
            low = mid
        else:
            high = mid
    return (low+high)/2


def exact_survival(radius, delta, a=1.0, b=1.0):
    y = J(radius, a, b)-delta
    return 0.0 if y <= 0 else 1.0 if y >= 2 else acos(1-y)/pi


def moment(delta, p, a=1.0, b=1.0, n=16000):
    return sum(invJ(delta+1-cos(pi*(j+0.5)/n), a, b)**p
               for j in range(n))/n


def check():
    for a, b in [(1.,1.), (2.,3.), (0.7,1.5)]:
        for r in (0.2,0.9,5.,60.):
            h = 1.e-5*r
            numerical_derivative = (J(r+h,a,b)-J(r-h,a,b))/(2*h)
            expected = -1/(r*r*(b+a*r*r))
            assert isclose(numerical_derivative, expected, rel_tol=2.e-6, abs_tol=3.e-12)
            assert isclose(J(invJ(J(r,a,b),a,b),a,b),J(r,a,b),rel_tol=1.e-8)
    a,b=1.,1.
    for delta in (0.01, 0.001):
        for theta in (0.2,1.1,2.5,5.8):
            radius=invJ(delta+1-sin(theta))
            assert isclose(J(radius)+sin(theta),1+delta,rel_tol=1.e-10)
    tail_coefficient=sqrt(2/3)/pi
    assert 0.999 < exact_survival(100.,0.)/(tail_coefficient*100.**(-1.5)) < 1.001
    assert 0.999 < exact_survival(1000.,0.)/(tail_coefficient*1000.**(-1.5)) < 1.001
    c2=3**(-2/3)/sqrt(2*pi)*gamma(1/6)/gamma(2/3)
    ratio=moment(1.e-5,2.)/(c2*(1.e-5)**(-1/6))
    assert 0.80 < ratio < 0.95
    c15=1/(pi*sqrt(6.))
    d1,d2=1.e-3,1.e-5
    m1,m2=moment(d1,1.5),moment(d2,1.5)
    assert abs((m2-m1)-c15*log(d1/d2)) < 0.04
    print('RIGID_QUARTIC_OCCUPATION_MOMENTS_OK')


if __name__ == '__main__':
    check()
