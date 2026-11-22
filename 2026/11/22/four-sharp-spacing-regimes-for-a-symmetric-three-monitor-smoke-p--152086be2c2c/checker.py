#!/usr/bin/env python3
"""Independent finite numerical checks for a symmetric three-monitor Gaussian design.
The analytic proof, not these finite checks, establishes global optimality.
"""
import math
import random

SQRT2 = math.sqrt(2.0)

def cdf(x, sigma):
    return 0.5 * (1.0 + math.erf(x / (SQRT2 * sigma)))

def mass_radius(a, sigma):
    return cdf(a, sigma) - cdf(-a, sigma)

def candidate_d(r, sigma, p):
    ell = -sigma * sigma * math.log1p(-p) / r
    if ell <= r:
        return ell
    if ell <= 2 * r:
        return r
    if ell <= 4 * r:
        return ell / 2
    return 2 * r

def piecewise(d, r, sigma, p):
    q = 1 - p
    M = lambda a: mass_radius(a, sigma)
    if d <= r:
        return p * (M(r+d) + q*M(r) + q*q*M(r-d))
    if d <= 2*r:
        pair = 2*(cdf(r, sigma) - cdf(d-r, sigma))
        return p * (M(r+d) + q * pair)
    return p * (M(r) + 2*(cdf(d+r,sigma)-cdf(d-r,sigma)))

def direct(d, r, sigma, p):
    centers = [-d, 0.0, d]
    bounds = sorted(set([z-r for z in centers] + [z+r for z in centers]))
    total = 0.0
    for left,right in zip(bounds[:-1],bounds[1:]):
        middle = (left+right)/2
        cover = sum(abs(middle-z)<r for z in centers)
        total += (1-(1-p)**cover) * (cdf(right,sigma)-cdf(left,sigma))
    return total

rng = random.Random(12715)
checks = 0
for k in range(240):
    sigma = math.exp(rng.uniform(-1.5,1.5))
    r = math.exp(rng.uniform(-1.5,1.5))
    p = rng.uniform(0.015,0.985)
    dstar = candidate_d(r,sigma,p)
    assert 0 <= dstar <= 2*r
    checks += 1
    optimum = piecewise(dstar,r,sigma,p)
    assert abs(optimum-direct(dstar,r,sigma,p))<3e-13
    checks += 1
    for j in range(201):
        d = (3.2*r) * j/200
        formula = piecewise(d,r,sigma,p)
        brute = direct(d,r,sigma,p)
        assert abs(formula-brute)<5e-13, (k,j,formula,brute)
        assert optimum+4e-13 >= brute, (k,j,optimum,brute,dstar,d)
        checks += 2
    for edge in (r,2*r):
        assert abs(piecewise(edge-1e-9*r,r,sigma,p)-piecewise(edge+1e-9*r,r,sigma,p))<1e-8
        checks += 1
for eta, interval in ((0.4,'triple'),(1.4,'pinned'),(3.0,'neighbor'),(5.0,'disjoint')):
    r = sigma = 1.0
    p = -math.expm1(-eta)
    d = candidate_d(r,sigma,p)
    expected = {'triple':eta,'pinned':1.0,'neighbor':eta/2,'disjoint':2.0}[interval]
    assert abs(d-expected)<2e-14
    checks += 1
print('PASS:',checks,'finite numerical assertions; four analytic regimes sampled')
