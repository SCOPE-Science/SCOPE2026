#!/usr/bin/env python3
"""Supplementary numerical and exact-arithmetic checks for the cubic-flow formula.

Run: python3 checker.py
This script does not substitute for the analytic proof of any infinite statement.
"""
import math
from fractions import Fraction


def simpson(f, left, right, n=4096):
    assert n > 0 and n % 2 == 0
    h = (right - left) / n
    z = f(left) + f(right)
    for i in range(1, n):
        z += (4 if i % 2 else 2) * f(left + i*h)
    return h*z/3


def profile(theta, a, b):
    upper = 40.0/a
    return math.exp(b*math.sin(2*theta)) * simpson(
        lambda v: math.exp(-2*a*v - b*math.sin(2*(theta-v))),
        0.0, upper, 4096)


def polynomial_identification():
    cases = 0
    for a in (Fraction(1), Fraction(2), Fraction(3, 5)):
        for b in (Fraction(-2), Fraction(0), Fraction(5)):
            for x in range(-3, 4):
                for y in range(-3, 4):
                    R2 = x*x + y*y
                    D = ((-a+b)*x*x + (-a-b)*y*y)
                    f = D*x - R2*y
                    g = D*y + R2*x
                    assert x*f+y*g == R2*(-a*R2+b*(x*x-y*y))
                    assert x*g-y*f == R2*R2
                    cases += 1
    return cases


def profile_checks(a, b):
    for theta in (0.0, 0.29, 0.84, 1.71, 2.77):
        q = profile(theta,a,b)
        assert q > 0
        assert abs(q-profile(theta+math.pi,a,b)) < 1e-8*max(q,1)
        h=1.e-4
        der = (profile(theta+h,a,b)-profile(theta-h,a,b))/(2*h)
        rhs = 1+(-2*a+2*b*math.cos(2*theta))*q
        assert abs(der-rhs) < 0.02*max(1,abs(rhs)), (theta,der,rhs)
    clock = simpson(lambda theta: 1/profile(theta,a,b),0,math.pi,512)
    assert abs(clock-2*a*math.pi) < 2e-5, clock
    return clock


def time_shift_and_return(a,b,theta0,r0):
    C=profile(theta0,a,b)/r0**2
    def radial_sq(theta):
        return r0*r0*math.exp(-2*a*(theta-theta0)+b*(math.sin(2*theta)-math.sin(2*theta0)))
    for dtheta in (0.2,0.8,1.5,math.pi):
        theta=theta0+dtheta
        t=simpson(lambda th:1/radial_sq(th),theta0,theta,6000)
        assert abs((t+C)*radial_sq(theta)-profile(theta,a,b)) < 1e-5*max(1,profile(theta,a,b))
    for n in (1,2):
        theta=theta0+n*math.pi
        t=simpson(lambda th:1/radial_sq(th),theta0,theta,16000)
        exact=C*math.expm1(2*a*math.pi*n)
        assert abs(t/exact-1) < 5e-6, (n,t,exact)
        assert abs(math.sqrt(radial_sq(theta))/(r0*math.exp(-a*math.pi*n))-1) < 1e-12
    return C


def onset_check(a):
    target=1/(a*math.sqrt(1+a*a))
    estim=[]
    for b in (.015,.0075):
        vals=[profile(math.pi*j/192,a,b) for j in range(193)]
        estim.append((max(vals)-min(vals))/b)
    assert abs(estim[-1]-target) < .03
    return target,estim


if __name__ == '__main__':
    n=polynomial_identification()
    p1=profile_checks(1.0,5.0)
    p2=profile_checks(2.0,0.2)
    p3=profile_checks(1.0,0.0)
    c=time_shift_and_return(1.0,.6,.3,.8)
    target, estimates=onset_check(1.0)
    sample=[profile(j*math.pi/400,1.0,5.0) for j in range(401)]
    assert min(sample) < .111 and max(sample) > 681
    print('PASS: exact Cartesian-to-polar identities:',n,'integer/rational cases')
    print('PASS: Q positivity, pi periodicity, differential equation and angular clocks')
    print('PASS: time-shift formula and two exact geometric half-turn clocks')
    print('PASS: anisotropy first-order profile range',target,estimates)
    print('Supplementary profile range (grid, not rigorous bounds):',min(sample),max(sample))
    print('Supplementary time-shift constant:',c)
    print('No finite computation was used as a proof of convergence or sharpness.')
