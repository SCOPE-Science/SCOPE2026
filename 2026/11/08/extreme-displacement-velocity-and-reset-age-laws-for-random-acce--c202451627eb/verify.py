#!/usr/bin/env python3
"""Reproducibility checks for conditional extreme-excursion asymptotics.

Python standard library only. These finite checks supplement, not replace,
the analytic Laplace-principle and Gaussian-limit proofs in RESULT.md.
"""
from fractions import Fraction
from math import erfc, exp, isfinite, log, sqrt


def simpson(func, a=-12.0, b=12.0, n=24000):
    assert n % 2 == 0
    h = (b-a)/n
    ans = 0.0
    for i in range(n+1):
        x = a+h*i
        ans += (1 if i == 0 or i == n else 4 if i % 2 else 2)*func(x)
    return ans*h/3.0


def phi(z):
    return z+1.0/(3.0*z**3)


def weighted_y(y, lam, moment=0):
    z = 1.0+y/sqrt(lam)
    if z <= 0:
        return 0.0
    return z**(moment-1.5)*exp(-lam*(phi(z)-4.0/3.0))


def moment(lam, power):
    return simpson(lambda y: weighted_y(y,lam,power))/simpson(lambda y: weighted_y(y,lam,0))


def F(z,u):
    return phi(z)+(u-1.0/z)**2/z


def golden_minimum(func, a=0.1, b=20.0, n=180):
    ratio=(sqrt(5.0)-1.0)/2.0
    c=b-ratio*(b-a)
    d=a+ratio*(b-a)
    for _ in range(n):
        if func(c) < func(d):
            b=d
            d=c
            c=b-ratio*(b-a)
        else:
            a=c
            c=d
            d=a+ratio*(b-a)
    z=(a+b)/2.0
    return z,func(z)


# Independent rational covariance computation from integrated Brownian motion.
D=Fraction(7,4); t=Fraction(5,3)
var_x=Fraction(2,3)*D*t**3
var_v=2*D*t
cov=D*t**2
assert cov/var_x == Fraction(3,2)/t
assert var_v-cov**2/var_x == D*t/2
assert (Fraction(9,4)*Fraction(4,9)) == 1

# Exact rate minimizer at a zero oriented velocity, and quadratic local curvature.
z0, minimum=golden_minimum(lambda z:F(z,0.0))
I0=4.0*(sqrt(2.0)-1.0)/3.0
assert abs(z0-sqrt(2.0)) < 1e-7
assert abs(minimum-4.0/3.0-I0) < 1e-10
assert abs(F(1.0,1.0)-4.0/3.0) < 1e-12
for eps in (0.01, 0.005):
    _,value=golden_minimum(lambda z:F(z,1.0+eps))
    assert abs((value-4.0/3.0)/eps**2-2.0/3.0) < 0.02

# Conditional Gaussian age-mixture moments; no random sampling involved.
for lam in (100.0, 300.0):
    e1=moment(lam,1)
    e2=moment(lam,2)
    em1=moment(lam,-1)
    em2=moment(lam,-2)
    # A=(T-tau)/sqrt(tau/r), B=(V-v*)/sqrt(D*tau).
    age_variance=lam*(e2-e1*e1)
    velocity_variance=e1/2 + lam*(em2-em1*em1)
    covariance=lam*(1-e1*em1)
    assert abs(age_variance-.25)<.006
    assert abs(velocity_variance-.75)<.006
    assert abs(covariance+.25)<.006
    assert isfinite(age_variance+velocity_variance+covariance)

# The wrong-way conditional velocity probability has rate I(0).
# The normal CDF is 0.5*erfc( sqrt(lam)/z^(3/2) ).
for lam in (100.0,300.0):
    denominator=simpson(lambda y:weighted_y(y,lam))
    def integrand(y):
        z=1.0+y/sqrt(lam)
        if z<=0: return 0.0
        return weighted_y(y,lam)*0.5*erfc(sqrt(lam)/z**1.5)
    numerator=simpson(integrand)
    rate=-log(numerator/denominator)/lam
    assert rate>I0 and abs(rate-I0)<.06
    print('lambda',lam,'wrong-way observed rate',format(rate,'.9f'),
          'theoretical limit',format(I0,'.9f'))

print('PASS: exact covariance, rate minimizer, local curvature,',
      'conditional moments, wrong-way large-deviation rate')
