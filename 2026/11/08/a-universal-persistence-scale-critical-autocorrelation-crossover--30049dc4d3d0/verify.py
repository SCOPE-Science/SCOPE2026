#!/usr/bin/env python3
"""Deterministic numerical diagnostics for a critical Gaussian spherical Debye model.

Requires only Python 3 standard library. The analytical proof is in RESULT.md.
"""
from math import atan, erfc, exp, expm1, gamma, pi, sqrt


def integrate(f, lo, hi, n=60000):
    assert n % 2 == 0
    step = (hi - lo) / n
    s = f(lo) + f(hi)
    for j in range(1, n):
        s += (4 if j % 2 else 2) * f(lo + j * step)
    return s * step / 3.0


def exprel(y):
    if abs(y) < 1e-7:
        return 1 + y / 2 + y * y / 6 + y**3 / 24
    return expm1(y) / y


def erfi_series(x):
    term = x
    total = term
    for n in range(1, 150):
        term *= x*x/n
        add = term/(2*n+1)
        total += add
        if abs(add) < 1e-16 * max(1., abs(total)):
            break
    return 2*total/sqrt(pi)


def transformed_kernel(x, s):
    if x == 0:
        return 0.
    if x == 1:
        return exp(-s)
    z = x/(1-x)
    return s*exp(-s)*z*z*exprel(s*(1-z*z))/(1+z*z)/(1-x)**2


def phi_integral(s):
    return integrate(lambda x: transformed_kernel(x, s), 0., 1.)


def phi_closed(s):
    return pi/4*(exp(-s)*(1+erfi_series(sqrt(s))) - exp(s)*erfc(sqrt(s)))


def scaled_finite_a(s, tau):
    zmax = sqrt(tau)
    xmax = zmax / (1+zmax)
    scale = 1/(1-atan(zmax)/zmax)
    return scale * integrate(lambda x: transformed_kernel(x, s), 0., xmax)


def scaled_finite_b(s, tau):
    # Independent direct mode-space quadrature of C(t)-exp(-t/tau).
    zmax = sqrt(tau)
    scale = 1/(1-atan(zmax)/zmax)
    def f(w):
        z = zmax*w
        return w*w/(1+tau*w*w)*s*exp(-s)*exprel(s*(1-z*z))
    # 5*T_c = tau/(1-atan(sqrt(tau))/sqrt(tau))
    return tau**1.5*scale*integrate(f, 0., 1.)


def run():
    tests = 0
    for s in [0.04, 0.2, 1., 2.]:
        v = phi_integral(s)
        closed = phi_closed(s)
        assert abs(v-closed) < 2e-6, ('special function identity',s,v,closed)
        assert v>0
        tests+=2
    for s in [0.2, 1.0, 2.0]:
        target = phi_closed(s)
        errs=[]
        for tau in [1e3,1e4,1e5]:
            a = scaled_finite_a(s, tau)
            b = scaled_finite_b(s, tau)
            assert abs(a-b) < 3e-5, ('independent mode quadratures',s,tau,a,b)
            assert a>0
            errs.append(abs(a-target))
            tests+=2
        assert errs[2]<errs[1]<errs[0], ('asymptotic convergence',s,errs)
        assert errs[2] < 0.06, ('limit accuracy',s,errs)
        tests+=2
    # Power-law asymptotics in five Debye dimensions.
    for s in [1e-5, 4e-5, 1.6e-4]:
        approx=sqrt(pi)*sqrt(s)
        exact=phi_closed(s)
        assert 0.94 < exact/approx < 1.01, ('small-s exponent',s,exact/approx)
        tests+=1
    for s in [20., 40., 80.]:
        approx=sqrt(pi)/4*s**(-1.5)
        exact=phi_integral(s)
        assert 0.95 < exact/approx < 1.25, ('large-s exponent',s,exact/approx)
        tests+=1
    print('PASS:',tests,'deterministic numerical diagnostics')
    print('Phi_5(1)=%.15f' % phi_closed(1.))
    print('These finite checks do not establish the theorem.')

if __name__=='__main__':
    run()
