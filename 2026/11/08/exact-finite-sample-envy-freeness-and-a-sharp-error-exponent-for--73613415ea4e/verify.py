#!/usr/bin/env python3
"""Exact checks for a two-person utilitarian-allocation fairness law.
Uses only the Python standard library; no network or external datasets.
"""
from fractions import Fraction
from math import factorial, comb, exp, sqrt, pi
import random


def fair_probability(m):
    if not isinstance(m, int) or m < 1:
        raise ValueError('m must be an integer >= 1')
    positive = Fraction(0)
    for r in range(m + 1):
        for s in range(m - r + 1):
            u = m - r - s
            a = r - u
            if a <= 0:
                continue
            mult = factorial(m) // (factorial(r)*factorial(s)*factorial(u))
            for j in range(r + 1):
                degree = 2*m - s - j
                positive += Fraction(mult * comb(r,j) * (-1)**(r-j) * a**degree,
                                     factorial(degree))
    return 2*positive - 1


def M(t):
    # Integral definition gives stable evaluation near zero.
    n = 16000
    h = 1.0/n
    acc = 0.0
    for i in range(n):
        x = (i + .5)*h
        acc += x * exp(t*x) + (1-x) * exp(-t*x)
    return acc*h


def Mp(t):
    n = 16000
    h = 1.0/n
    acc = 0.0
    for i in range(n):
        x = (i+.5)*h
        acc += x*x*exp(t*x) - x*(1-x)*exp(-t*x)
    return acc*h


def Mpp(t):
    n = 16000
    h = 1.0/n
    acc = 0.0
    for i in range(n):
        x = (i+.5)*h
        acc += x**3*exp(t*x) + x*x*(1-x)*exp(-t*x)
    return acc*h


def saddlepoint():
    left, right = -5.0, 0.0
    assert Mp(left) < 0 < Mp(right)
    for _ in range(45):
        mid=(left+right)/2
        if Mp(mid)>0:right=mid
        else:left=mid
    theta=(left+right)/2
    rho=M(theta)
    sigma=sqrt(Mpp(theta)/rho)
    coeff=2/(abs(theta)*sigma*sqrt(2*pi))
    return theta,rho,sigma,coeff


def independent_monte_carlo(m, draws=150000, seed=20260925):
    rng=random.Random(seed+m)
    fair=0
    for _ in range(draws):
        sa=sb=0.0
        for _ in range(m):
            x,y=rng.random(),rng.random()
            if x>y:
                sa+=x
                sb-=y
            else:
                sa-=x
                sb+=y
        fair += (sa>=0 and sb>=0)
    return fair/draws


def main():
    expected={1:Fraction(0),2:Fraction(1,3),3:Fraction(23,60),
              4:Fraction(55,126),5:Fraction(4927,10080),
              6:Fraction(1762909,3326400)}
    for m,p in expected.items():
        assert fair_probability(m)==p, (m,p,fair_probability(m))
    # Independent derivation for m=2: A positive-signed sample has
    # max(U,V) law, a negative-signed magnitude min(U,V) law.
    # With one of each (probability 1/2), max>min with probability 5/6.
    assert fair_probability(2)==2*(Fraction(1,4)+Fraction(1,2)*Fraction(5,6))-1
    for m in (2,3,4,6,9,12):
        actual=independent_monte_carlo(m)
        exact=float(fair_probability(m))
        assert abs(actual-exact)<0.0075,(m,actual,exact)
    theta,rho,sigma,coeff=saddlepoint()
    assert -0.554<theta<-0.552
    assert 0.9552<rho<0.9554
    assert 0.539<sigma<0.540
    assert 2.67<coeff<2.68
    assert abs(Mp(theta))<1e-12
    assert abs(M(0)-1)<1e-9
    print('PASS: six exact rational values, independent m=2 order-statistic identity,')
    print('six seeded allocation simulations, and numerical tilted-law checks.')
    print('saddlepoint theta={:.10f}, rho={:.10f}, sigma={:.10f}, coeff={:.10f}'.format(theta,rho,sigma,coeff))

if __name__=='__main__':main()
