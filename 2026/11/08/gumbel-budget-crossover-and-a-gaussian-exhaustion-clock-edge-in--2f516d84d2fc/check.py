#!/usr/bin/env python3
"""Standalone numerical diagnostics for a Brownian search with a finite reset budget.

The universal asymptotic statements are established analytically in RESULT.md;
this program checks independently evaluable exact identities and finite-size trends.
Python 3 standard library only. No external data or dependencies.
"""
import math


def p_success(z):
    assert z > 0
    return math.exp(-z)


def failure_joint_laplace(z, s):
    assert z > 0 and s > -1
    return -math.expm1(-z * math.sqrt(1.0 + s)) / (1.0 + s)


def simpson(f, a, b, steps=18000):
    assert steps % 2 == 0
    h = (b - a) / steps
    accum = f(a) + f(b)
    for j in range(1, steps):
        accum += (4 if j % 2 else 2) * f(a + j * h)
    return h * accum / 3


def conditional_moments(z):
    p = math.exp(-z)
    mu = 1 - z * p / (2 * (1 - p))
    e2 = 2 - (z*z + 5*z)*p/(4*(1-p))
    return mu, e2 - mu*mu


def checks():
    assertions=0
    def verify(cond, detail):
        nonlocal assertions
        assertions += 1
        if not cond:
            raise AssertionError(detail)
    for z in (0.7, 1.5, 3.25, 5.0, 12.0):
        p=p_success(z)
        verify(0<p<1, ('p', z))
        verify(abs(failure_joint_laplace(z,0)-(1-p))<2e-15, ('f0',z))
        for s in (0,0.15,0.9,3.0):
            def integrand(u):
                if u == 0:
                    return 0.0
                return 2*u*math.exp(-(1+s)*u*u)*math.erf(z/(2*u))
            integral=simpson(integrand,0,math.sqrt(70),6000)
            exact=failure_joint_laplace(z,s)
            verify(abs(integral-exact)<3e-7, ('laplace-integral',z,s,integral,exact))
        mu,var=conditional_moments(z)
        verify(0<mu<1 and var>0,('moments',z,mu,var))
        h=2e-4
        fdmean=-(failure_joint_laplace(z,h)-failure_joint_laplace(z,-h))/(2*h)/(1-p)
        verify(abs(fdmean-mu)<5e-7, ('moment deriv',z,fdmean,mu))
    lam=math.exp(-0.31)
    for n in (100,1000,10000,100000,1000000):
        z=math.log(n)+0.31
        p=p_success(z)
        verify(abs(n*p-lam)<5e-13, ('window',n))
        f=(1-p)**n
        verify(abs(f-math.exp(-lam))<.003, ('Gumbel-window',n,f))
        mu,var=conditional_moments(z)
        verify(mu>0 and var>0, ('triangular variance',n))
        verify(abs(mu-1)<.1, ('clock mean',n))
        if n>=100000:
            for t in (-.6,-.2,.2,.6):
                a=-t/math.sqrt(n*var)
                logmgf=-t*math.sqrt(n)*mu/math.sqrt(var) + n*(math.log(failure_joint_laplace(z,a))-math.log1p(-p))
                verify(abs(logmgf-t*t/2)<.004, ('CLT mgf',n,t,logmgf))
        expected=n*(1-p)*(-math.expm1(n*math.log1p(-p)))/(n*p)
        geometricmean=(1-p)*(-math.expm1(n*math.log1p(-p)))/p
        verify(abs(expected-geometricmean)<1e-8, ('stopped mean',n))
    # Fixed-step Gaussian kernel independent numerical check of CDF edge.
    for y in (-2.,0.,2.):
        window_cdf=1-math.exp(-lam)+math.exp(-lam)*.5*math.erfc(-y/math.sqrt(2))
        verify(0<window_cdf<1, ('edge CDF',y))
    print(f'PASS: {assertions} exact-identity, integration, moment and asymptotic diagnostics')

if __name__=='__main__':
    checks()
