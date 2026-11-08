#!/usr/bin/env python3
"""Exact rational and numerical checks of a circular-gap covariance law."""
from fractions import Fraction as F
from math import comb, fsum


def harmonic(n):
    return sum((F(1, j) for j in range(1, n + 1)), F(0))


def closed_cov(n, t):
    """Proposed covariance of maximum gap and count of gaps > t."""
    t = F(t)
    mu_part = (1 - t) ** (n - 1) * ((n - 1) * t - (harmonic(n) - 1))
    extra = sum((F((-1) ** (j + 1) * comb(n - 1, j), j * (j + 1)) *
                 max(F(0), 1 - (j + 1) * t) ** n
                 for j in range(1, n)), F(0))
    return mu_part + extra


def positive_polynomial_integral(lo, hi, cap, rate, power):
    """Integrate (cap-rate*s)_+**power ds by its endpoint primitive."""
    hi = min(hi, cap / rate)
    if hi <= lo:
        return F(0)
    return ((cap - rate * lo) ** (power + 1) -
            (cap - rate * hi) ** (power + 1)) / (rate * (power + 1))


def direct_layer_cake_cov(n, t):
    """Independent layer-cake integral of P(M>s, X_1>t).

    For s>=t, take the union of {X_1>s} and {X_i>s, i>=2},
    apply inclusion-exclusion, and integrate each joint simplex tail.
    """
    t = F(t)
    q = (1-t) ** (n-1)
    joint = t*q + positive_polynomial_integral(t, F(1), F(1), 1, n-1)
    for j in range(1, n):
        coefficient = (-1) ** (j+1) * comb(n-1, j)
        term_a = positive_polynomial_integral(t, F(1), 1-t, j, n-1)
        term_b = positive_polynomial_integral(t, F(1), F(1), j+1, n-1)
        joint += coefficient * (term_a-term_b)
    return n * (joint - harmonic(n)/n*q)


def conditional_g(n, x):
    """Compute E[max(X_1,...,X_n) | X_1=x] by max-tail integration."""
    if x >= 1:
        return 1.
    if n == 2:
        return max(x, 1-x)
    lower = x/(1-x)
    if lower >= 1:
        return float(x)
    def sf(z):
        return fsum(((-1)**(j+1))*comb(n-1,j)*max(0,1-j*z)**(n-2)
                    for j in range(1,n))
    from scipy.integrate import quad
    pts = sorted([lower, 1] + [1/j for j in range(1,n) if lower < 1/j < 1])
    integral = sum(quad(sf,a,b,epsabs=3e-13,epsrel=3e-13)[0]
                   for a,b in zip(pts[:-1],pts[1:]))
    return x+(1-x)*integral


def integration_cov(n,t):
    from scipy.integrate import quad
    t = float(t)
    mu = float(harmonic(n)/n)
    pts = sorted(set([t, 1.] + [1/j for j in range(2,n+1) if t < 1/j < 1]))
    def f(x):
        return (conditional_g(n,x)-mu)*(n-1)*(1-x)**(n-2)
    return n*sum(quad(f,a,b,epsabs=1e-11,epsrel=1e-11)[0]
                 for a,b in zip(pts[:-1],pts[1:]))


def main():
    checks = 0
    for n in range(2,19):
        for den in [3,4,5,7,9,11,13,17,19,23,31]:
            for num in range(0,den+1):
                t = F(num,den)
                assert closed_cov(n,t) == direct_layer_cake_cov(n,t),(n,t)
                checks += 1
        assert closed_cov(n,0) == 0 and closed_cov(n,1) == 0
        checks+=2
    print('Exact layer-cake/closed-form Fraction comparisons:', checks)
    from scipy.optimize import brentq
    for n in [2,3,4,5,8,10,20,30,50]:
        root = brentq(lambda t: float(closed_cov(n,F(str(t)))),0.25/n, min(0.99,4.5/n),xtol=1e-14)
        print('n=',n,'unique_zero=',f'{root:.12f}',
              'negative_at_halfroot=',float(closed_cov(n,F(str(root*.5)))),
              'positive_after=',float(closed_cov(n,F(str((root+1)*.5)))))
    float_checks=0
    for n in [2,3,4,5,7,9]:
        for t in [0.015,0.07,0.15,0.29,0.4,0.54,0.71,0.9]:
            a=float(closed_cov(n,F(str(t))))
            b=integration_cov(n,t)
            assert abs(a-b) <= 4e-9,(n,t,a,b)
            float_checks+=1
    print('Independent conditional-integration numerical checks:',float_checks)
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
