#!/usr/bin/env python3
"""Numerical sanity checks for exact Gabor frame-bound formulas.

The analytical argument is in RESULT.md; finite tests are not its proof.
Run: python3 check_asym_gabor.py
"""
import cmath
import math
import random


def formulas(a, b):
    r, s = math.exp(-a), math.exp(-b)
    u = 1/(1+s*s)
    v = r*r/(1+r*r)
    w = r*(r+s)/((1+s*s)*(1+r*r))
    q = (w*(a-b) + math.sqrt((w*(a-b))**2+4*a*b*u*v))/(2*a*v)
    x = math.log(q)/(a+b)
    lower = 2*(u*math.exp(-2*b*x) + v*math.exp(2*a*x)
               - 2*w*math.exp((a-b)*x))
    upper = 2*((1/(1-s*s)+r*r/(1-r*r))**2
               +(s/(1-s*s)+r/(1-r*r))**2)
    return x, lower, upper


def zak(a, b, x, theta):
    r, s = math.exp(-a), math.exp(-b)
    z = cmath.exp(1j*theta)
    return math.exp(-b*x)/(1-s/z) + math.exp(a*x)*r*z/(1-r*z)


def symbol(a, b, x, theta):
    return abs(zak(a,b,x,theta))**2 + abs(zak(a,b,x,theta+math.pi))**2


def main():
    rng = random.Random(20221104)
    checks = 0
    pars = [(1.0, 1.0), (0.5, 2.0), (2.0, 0.5), (1.0, 5.0),
            (3.0, 0.2), (1.1, 4.7), (3.8, 0.8), (2.5, 2.5)]
    pars += [(rng.uniform(.3,4.2), rng.uniform(.3,4.2)) for _ in range(20)]
    for a,b in pars:
        x,lo,hi = formulas(a,b)
        assert 0 < x < 1 and 0 < lo < hi
        assert abs(symbol(a,b,x,math.pi/2)-lo)<3e-9
        assert abs(symbol(a,b,0,0)-hi)<3e-9
        checks += 3
        for _ in range(220):
            z = rng.random()
            t = math.pi*rng.random()
            val = symbol(a,b,z,t)
            assert val >= lo-1e-9, (a,b,z,t,val,lo)
            assert val <= hi+1e-9, (a,b,z,t,val,hi)
            checks += 2
    # Independent truncated Zak series check, distinct from rational expression.
    for a,b in [(1.,1.), (.7,2.), (2.3,.4)]:
        for x in [.07,.33,.79]:
            for theta in [.19, 1.01, 2.47]:
                direct = sum((math.exp(-b*(x-n)) if x>=n
                              else math.exp(a*(x-n)))*cmath.exp(1j*n*theta)
                             for n in range(-110,111))
                assert abs(direct-zak(a,b,x,theta))<2e-11
                checks+=1
    print('ASYMMETRIC_EXPONENTIAL_GABOR_CHECKS_PASS',checks)

if __name__ == '__main__':
    main()
