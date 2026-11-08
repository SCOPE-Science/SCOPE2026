#!/usr/bin/env python3
"""Independent exact and numerical checks for fixed-allocation EF1 with exponential item values.
Run with: python3 check.py . No packages beyond the Python standard library.
"""
from fractions import Fraction
from math import comb, factorial, exp, isclose
import math, random


def rates_and_coefficients(r):
    if r < 2:
        raise ValueError('r must be at least 2')
    rates = [Fraction(t + 1, t) for t in range(1, r)]
    cs = []
    for i, rate in enumerate(rates):
        c = Fraction(1)
        for j, other in enumerate(rates):
            if i != j:
                c *= other / (other - rate)
        cs.append(c)
    return rates, cs


def q_exact(r, n):
    """Finite rational expansion of E[F_Y(Gamma(r,1))**(n-1)]."""
    rates, cs = rates_and_coefficients(r)
    total = Fraction(0)
    def recur(i, remaining, degree, param, coeff):
        nonlocal total
        if i == len(rates):
            total += ((-1)**degree * comb(n-1, degree)
                      * factorial(degree) * coeff / (1 + param)**r)
            return
        for c in range(remaining+1):
            recur(i+1, remaining-c, degree+c, param+c*rates[i],
                  coeff * cs[i]**c / factorial(c))
    recur(0, n-1, 0, Fraction(0), Fraction(1))
    return total


def q_r2_beta_harmonic(n):
    b = Fraction(4**n * factorial(n) * factorial(n-1), factorial(2*n))
    psi = sum((Fraction(2, 2*j+1) for j in range(n)), Fraction(0))
    return b * psi / 4


def q_numerical(r,n):
    """Simpson integration of the Gamma density against the cdf of a sum
    of independent exponentials; separate from the rational expansion."""
    rates, cs = rates_and_coefficients(r)
    rates = [float(x) for x in rates]
    cs = [float(x) for x in cs]
    def f(x):
        surv = sum(a * exp(-z*x) for z,a in zip(rates,cs))
        F = min(1.0, max(0.0, 1.0-surv))
        return x**(r-1) * exp(-x) / factorial(r-1) * F**(n-1)
    h=0.005
    N=12000
    acc=f(0.0)+f(N*h)
    for i in range(1,N):
        acc+=(4 if i%2 else 2)*f(i*h)
    return acc*h/3


def q_monte_carlo(r,n,iterations=50000):
    rng=random.Random(20945+r*100+n)
    success=0
    for _ in range(iterations):
        # An agent has independent private values for every bundle, own included.
        allgood=True
        for i in range(n):
            vals=[[rng.expovariate(1.0) for _ in range(r)] for j in range(n)]
            own=sum(vals[i])
            if any(own+1e-12 < sum(v)-max(v) for j,v in enumerate(vals) if j!=i):
                allgood=False
                break
        success+=allgood
    return success/iterations


def main():
    total=0
    for r in range(2,5):
        rates, cs = rates_and_coefficients(r)
        assert sum(cs)==1
        assert rates[-1]==Fraction(r,r-1)
        assert cs[-1]==(r-1)**(r-1)
        for n in range(2,7):
            q=q_exact(r,n)
            assert 0<q<1
            numerical=q_numerical(r,n)
            assert abs(float(q)-numerical)<1e-8, (r,n,q,numerical)
            if r==2:
                assert q==q_r2_beta_harmonic(n)
            total+=1
    assert q_exact(2,2)==Fraction(8,9)
    assert q_exact(2,3)==Fraction(184,225)
    assert q_exact(3,2)==Fraction(962,1125)
    for r,n in [(2,2),(2,3),(3,2),(3,3)]:
        p=float(q_exact(r,n)**n)
        empirical=q_monte_carlo(r,n)
        assert abs(p-empirical)<0.013, (r,n,p,empirical)
    print('PASS: 15 exact rational-vs-quadrature cases; 5 beta-harmonic identities;')
    print('PASS: 3 anchor fractions; 4 seeded whole-allocation Monte Carlo checks.')
    print('Anchor P_EF1(n=2,r=2) =', q_exact(2,2)**2)
    print('Anchor P_EF1(n=3,r=2) =', q_exact(2,3)**3)


if __name__=='__main__':
    main()
