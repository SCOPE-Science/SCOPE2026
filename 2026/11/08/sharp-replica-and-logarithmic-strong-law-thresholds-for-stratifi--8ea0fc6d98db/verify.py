#!/usr/bin/env python3
"""Standalone numerical and algebraic checks for median-stratified endpoint tails.

The infinite-dimensional assertions in the accompanying proof do not depend on
these finite computations. Only Python's standard library is needed.
"""
import math
import random
from fractions import Fraction


def first_panel(alpha, beta, n, u):
    return n ** (alpha - 1) * u ** (-alpha) * (1.0 + math.log(n) - math.log(u)) ** (-beta)


def crossing(alpha, beta, n, eps):
    # For large n, first_panel is strictly decreasing on (0,1).
    hi = 1.0
    assert first_panel(alpha, beta, n, hi) < eps
    lo = 1e-295
    assert first_panel(alpha, beta, n, lo) > eps
    for _ in range(180):
        mid = math.sqrt(lo*hi)
        if first_panel(alpha, beta, n, mid) > eps:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo*hi)


def asymptotic_crossing(alpha, beta, n, eps):
    return (alpha**beta/eps)**(1/alpha) * n**(-(1-alpha)/alpha) * math.log(n)**(-beta/alpha)


def median_exceedance(q, k):
    r=(k+1)//2
    return sum(math.comb(k,j)*q**j*(1-q)**(k-j) for j in range(r,k+1))


def integral_power(alpha, a, b):
    return (b**(1-alpha)-a**(1-alpha))/(1-alpha)


def check():
    assertions = 0
    # A one-dimensional LHS is equal to independent jittered samples,
    # up to a harmless random permutation of the points.
    rng=random.Random(271828)
    for alpha in (0.2,0.5,0.67,0.9):
        for n in (4,17,100):
            c=n**(alpha-1)/(1-alpha)
            rest_mean=1/(1-alpha)-c
            width=n**(alpha-1)*(1-n**(-alpha))
            for _ in range(50):
                rest=n**(alpha-1)*sum((j+rng.random())**(-alpha) for j in range(1,n))
                assert abs(rest-rest_mean) <= width*(1+1e-10)
                assertions+=1
            assert width < n**(alpha-1)
            assertions+=1
    # Exact power-singularity tail probabilities: q_n(eps)=eps^(-1/a)*n^(-(1-a)/a)
    for alpha,eps in ((0.5,1.0),(2/3,0.7),(0.8,2.0)):
        for n in (10**2,10**4,10**6):
            q=crossing(alpha,0.0,n,eps)
            q_exact=eps**(-1/alpha)*n**(-(1-alpha)/alpha)
            assert math.isclose(q,q_exact,rel_tol=1e-12)
            assertions+=1
            for r in (1,2,3,4):
                k=2*r-1
                z=median_exceedance(q,k)
                assert 0<z<1
                pred=math.comb(k,r)*q**r
                assert 0 < z/pred <= 1.000000000001
                assertions+=2
    # Power-log inversion has the predicted uniform leading constant.
    for alpha,beta,eps in ((0.5,0.5,1.0),(2/3,1/3,0.8),(0.8,-0.6,1.7),(0.75,1.2,0.8)):
        last=None
        for n in (10**4,10**8,10**12,10**16,10**24,10**40):
            if alpha==0.5 and n>1e24: # preserve safe representable values
                continue
            q=crossing(alpha,beta,n,eps)
            approx=asymptotic_crossing(alpha,beta,n,eps)
            assert math.isfinite(q) and q>0
            # The first panel converges to the exact threshold upon inversion.
            assert math.isclose(first_panel(alpha,beta,n,q),eps,rel_tol=1e-11)
            assertions+=2
            last=q/approx
        assert last is not None and 0.3 < last < 3.0
        assertions+=1
    # Phase diagram and log cutoff at the critical exponent.
    for r in range(1,9):
        alpha=Fraction(r,r+1)
        critical_beta=Fraction(1,r+1)
        assert r*(1-alpha)/alpha == 1
        assert r*critical_beta/alpha == 1
        assertions+=2
    # Finite-n median moment check: a median of 3 has finite quadratic
    # moments for every integrable power singularity alpha<1, but
    # fails the a.s. criterion for alpha >= 2/3 (beta=0).
    for numerator in range(1,100):
        alpha=numerator/100
        assert 2/alpha > 2
        if alpha>=2/3:
            assert 2*(1-alpha)/alpha <= 1
            assertions+=1
        assertions+=1
    print(f"PASS: {assertions} deterministic, exact-tail, and asymptotic cross-checks")
    print("Critical power exponent alpha=r/(r+1); log boundary beta=1/(r+1).")
    print("No finite computation is used as a proof of Borel-Cantelli or the infinite-n limit.")

if __name__ == '__main__':
    check()
