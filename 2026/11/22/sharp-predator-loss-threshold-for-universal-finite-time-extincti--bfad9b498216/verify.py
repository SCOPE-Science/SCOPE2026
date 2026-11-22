#!/usr/bin/env python3
"""Standalone checks for the two-species sub-Allee extinction threshold.

Run: python3 verify.py
Only standard-library arithmetic is required. Numerical integrations illustrate,
not establish, the theorem proved in RESULT.md.
"""
from fractions import Fraction as Q
from math import exp, log


def exact_witness():
    b, L, K = Q(2), Q(1), Q(4)
    r, k, d, e = Q(1, 2), Q(1, 5), Q(1), Q(1, 10)
    s0, psmall, plarge = Q(1, 4), Q(1, 10), Q(2)
    q0 = Q(1, 2)  # s0**(1-r)
    beta = (1-r) * b * L
    c = (1-r) * d
    mu_fast = Q(3, 2)
    mu_slow = Q(1, 2)
    mu_critical = beta
    lam = mu_fast - e * Q(1, 2)  # s0**r = 1/2
    small_predator_wedge = q0 * (lam-beta) / c
    large_predator_bound = mu_fast * q0 / c
    assert K > L > s0 > 0 and 0 < r < 1
    assert beta == 1 and c == Q(1, 2)
    assert mu_slow < beta == mu_critical < mu_fast
    assert lam == Q(29,20) > beta
    assert psmall < small_predator_wedge == Q(9,20)
    assert plarge > large_predator_bound == Q(3,2)
    # Conservative explicit no-hit bound: q(t) >= positive*exp(-beta*t)
    prefactor = q0 - c * psmall / (lam-beta)
    assert prefactor == Q(7,18) > 0
    # Conservative finite-hit bound for the large-predator initial condition.
    t_bound = -log(1-float(mu_fast*q0/(c*plarge)))/float(mu_fast)
    assert 0 < t_bound < 1
    return prefactor, t_bound


def rhs(q, p, mu):
    # r=1/2 so s=q^2 and s^r=q on the positive branch.
    s = q*q
    b, L, K, k, d, e = 2., 1., 4., .2, 1., .1
    a = .5*b*(1-s/K)*(L-s)/(1+k*p)
    return -a*q-.5*d*p, (e*q-mu)*p


def trajectory(mu, p0, time_end=40., h=0.002):
    q, p, t = .5, p0, 0.
    while t < time_end:
        k1, v1 = rhs(q,p,mu)
        k2, v2 = rhs(q+h*k1/2,p+h*v1/2,mu)
        k3, v3 = rhs(q+h*k2/2,p+h*v2/2,mu)
        k4, v4 = rhs(q+h*k3,p+h*v3,mu)
        qn = q + h*(k1+2*k2+2*k3+k4)/6
        pn = p + h*(v1+2*v2+2*v3+v4)/6
        if qn <= 0:
            return 'finite', t+h*q/(q-qn), 0.
        q,p = qn,pn
        t += h
    return 'positive', t, q


def main():
    prefactor, tbound = exact_witness()
    scenarios = [(0.5,0.1,'finite'), (1.0,0.1,'finite'),
                 (1.5,0.1,'positive'), (1.5,2.,'finite')]
    for mu,p0,expect in scenarios:
        label,t,q = trajectory(mu,p0)
        assert label == expect, (mu,p0,label,t,q)
        if mu == 1.5 and p0 == 2:
            assert t < tbound
        if mu == 1.5 and p0 == 0.1:
            assert q > .1*exp(-t)  # weaker than exact analytic wedge
        print(f'mu={mu:.1f}, p0={p0:.1f}: {label}, t={t:.6f}, q(t)={q:.9g}')
    print(f'Exact no-hit lower prefactor: {prefactor}; finite-hit upper bound: {tbound:.9f}')
    print('Exact rational checks and all four numerical illustrations passed.')

if __name__ == '__main__':
    main()
