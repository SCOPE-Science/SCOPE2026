#!/usr/bin/env python3
"""Standalone numerical diagnostics for the adult-abundance stationarity theorem.

These tests complement, and do not replace, the analytic proof.
Only Python's standard library is used.
"""
import math
import random


def inv_expm1(t):
    if t > 700.0:
        return 0.0
    return 1.0 / math.expm1(t)


def H(beta, t):
    return beta - (1.0 - beta) * inv_expm1((1.0 - beta) * t) + inv_expm1(t)


def adult(N, L, gamma, alpha, mu0, h):
    t = (mu0 + alpha * N) * L / gamma
    a = h / L
    # Stable at small/large t in ordinary diagnostic regimes.
    return N * math.exp(-a * t) * (-math.expm1(-(1 - a) * t)) / (-math.expm1(-t))


def entry_flux(N, L, gamma, alpha, mu0):
    t = (mu0 + alpha * N) * L / gamma
    return N * (mu0 + alpha * N) / (-math.expm1(-t))


def optimum(L, gamma, alpha, mu0, h):
    beta = h / L
    t0 = mu0 * L / gamma
    def f(t):
        return (t-t0)*H(beta,t)-1.0
    lo = t0
    hi = max(t0 + 2, 2)
    while f(hi) < 0:
        hi *= 2
    for _ in range(115):
        mid = (lo+hi)/2
        if f(mid) < 0:
            lo=mid
        else:
            hi=mid
    t = (lo+hi)/2
    N = (t-t0)*gamma/(alpha*L)
    return t, N, entry_flux(N,L,gamma,alpha,mu0)


def test_midpoint():
    # W(exp(-1)) is the unique positive root of w*exp(w)=exp(-1).
    lo, hi = 0.0, 1.0
    for _ in range(110):
        w=(lo+hi)/2
        if w * math.exp(w) < math.exp(-1):lo=w
        else:hi=w
    w=(lo+hi)/2
    _, N, p = optimum(1,1,1,0,0.5)
    assert abs(N-2*(1+w))<1e-12
    assert abs(adult(N,1,1,1,0,.5)-2*w)<1e-12
    assert abs(N-2.556929085522148)<1e-11
    assert abs(p-7.087466207985555)<1e-11
    assert abs(adult(N,1,1,1,0,.5)-.556929085522148)<1e-11


def test_parameters():
    rng=random.Random(26270328)
    for _ in range(380):
        L=10**rng.uniform(-.6,.6)
        gamma=10**rng.uniform(-.6,.6)
        alpha=10**rng.uniform(-.6,.6)
        h=L*rng.uniform(.07,.93)
        mu0=gamma/L*rng.uniform(0,7)
        t,N,p=optimum(L,gamma,alpha,mu0,h)
        assert p>0 and N>0 and t>mu0*L/gamma
        assert abs((t-mu0*L/gamma)*H(h/L,t)-1)<2e-11
        A=adult(N,L,gamma,alpha,mu0,h)
        assert A>0
        for fac in (.6,.85,.98,1.02,1.15,1.4):
            assert adult(N*fac,L,gamma,alpha,mu0,h)<A*(1+2e-12)
        assert entry_flux(N*.6,L,gamma,alpha,mu0)<p<entry_flux(N*1.4,L,gamma,alpha,mu0)
        # The profile closure equals the total count.
        q=(mu0+alpha*N)/gamma
        direct=(p/gamma)*(-math.expm1(-q*L))/q
        assert abs(direct/N-1)<2e-12
        # Direct integration over mature sizes is identical to the conditional fraction.
        directA=(p/gamma)*math.exp(-q*h)*(-math.expm1(-q*(L-h)))/q
        assert abs(directA/A-1)<2e-12
    print('PASS: midpoint identities, 380 representative parameter cases, stationary closures')

if __name__=='__main__':
    test_midpoint()
    test_parameters()
