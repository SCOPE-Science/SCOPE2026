"""Reproducible finite and symbolic checks for two-option public-bad lotteries.

Run: python check.py
Uses only Python standard library plus SymPy for exact integration.
"""
from fractions import Fraction as Q
from itertools import product
from math import log, sqrt
from random import Random
import sympy as sp


def features(a, b, c, d):
    """Endpoint derivatives of the log Nash product."""
    left = Q(a - b, b) + Q(c - d, d)
    right = Q(a - b, a) + Q(c - d, c)
    return left, right


def predicted_count(a, b, c, d):
    left, right = features(a, b, c, d)
    if a == b and c == d:
        return None
    return int(left >= 0) + int(right <= 0) + int(left > 0 > right)


def pf_from_ratios(a, b, c, d, t):
    x = Q(b) + t * (a-b)
    y = Q(d) + t * (c-d)
    val_a = Q(a, 1) / x + Q(c, 1) / y
    val_b = Q(b, 1) / x + Q(d, 1) / y
    return val_a >= 2 and val_b >= 2


def interior_root(a, b, c, d):
    # For two agents the derivative numerator is linear in t.
    da, dc = a-b, c-d
    const = da*d + dc*b
    coeff = 2*da*dc
    if coeff == 0:
        return None
    t = -Q(const, coeff)
    return t if 0 < t < 1 else None


cases = 0
verified = 0
for a,b,c,d in product(range(1,10), repeat=4):
    cases += 1
    pred = predicted_count(a,b,c,d)
    if pred is None:
        # F constant, all lotteries are PF.
        assert pf_from_ratios(a,b,c,d,Q(0)) and pf_from_ratios(a,b,c,d,Q(1,2))
        continue
    root = interior_root(a,b,c,d)
    pts = [Q(0),Q(1)] + ([root] if root is not None else [])
    actual = sum(pf_from_ratios(a,b,c,d,t) for t in pts)
    assert actual == pred, (a,b,c,d,actual,pred)
    # Any other tested rational lottery has no PF status.
    for t in [Q(1,7),Q(1,5),Q(1,3),Q(2,5),Q(1,2),Q(3,5),Q(2,3),Q(4,5),Q(6,7)]:
        if t not in pts:
            assert not pf_from_ratios(a,b,c,d,t), (a,b,c,d,t)
    verified += 1

r=sp.symbols('r',positive=True)
u = 1/(2-r)
ell = 2-1/r
hu = 2/(1+r)**2
Hexp = lambda z: 2*z/(1+z)
area_uniform=sp.integrate(u,(r,0,sp.Rational(1,2)))+sp.integrate(u-ell,(r,sp.Rational(1,2),1))
area_exponential=sp.integrate(hu*Hexp(u),(r,0,sp.Rational(1,2)))+sp.integrate(hu*(Hexp(u)-Hexp(ell)),(r,sp.Rational(1,2),1))
assert sp.simplify(area_uniform-(2*sp.log(2)-1))==0
assert sp.simplify(area_exponential-sp.log(3)/2)==0

rng=Random(260726053)
N=240000
counts = []
for family in ['uniform','exponential']:
    ct=0
    for _ in range(N):
        if family=='uniform':
            a,b,c,d=(rng.random() for i in range(4))
        else:
            a,b,c,d=(rng.expovariate(1.0) for i in range(4))
        f0=(a-b)/b+(c-d)/d
        f1=(a-b)/a+(c-d)/c
        if f0 > 0 and f1 < 0:
            ct+=1
    val=ct/N
    exact=log(2)-.5 if family=='uniform' else log(3)/4
    assert abs(val-exact)<6*sqrt(.25/N), (family,val,exact)
    counts.append((family,ct,val,exact))

print('PASS: exact-rational enumeration',cases,'profiles,',verified,'nonconstant profiles')
print('PASS: symbolic iid uniform probability = log(2) - 1/2')
print('PASS: symbolic iid exponential probability = log(3)/4')
for fam,ct,val,exact in counts:
    print(f'PASS: {fam} Monte Carlo {ct}/{N} = {val:.8f}; closed form {exact:.8f} (sampling sanity only)')
