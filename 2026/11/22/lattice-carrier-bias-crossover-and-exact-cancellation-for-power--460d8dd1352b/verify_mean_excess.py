#!/usr/bin/env python3
"""Numerical consistency checks for a power-DEGPD residual-life asymptotic.

Requires mpmath 1.3.0. These finite checks illustrate, but do not prove,
the infinite-index asymptotics established analytically in RESULT.md.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 70


def mean_excess(p: str, c: str, kappa: str, u: int, truncation: int = 22):
    p, c, kappa = (mp.mpf(q) for q in (p, c, kappa))
    x = mp.mpf(u) + c
    a = c**p
    coefficients = [(-1)**(j+1)*mp.binomial(kappa,j)*a**j
                    for j in range(1, truncation+1)]
    numerator = sum(w*mp.zeta(j*p, x+1)
                    for j,w in enumerate(coefficients,1))
    denominator = 1-(1-a/x**p)**kappa
    # Independent evaluation of denominator by the binomial expansion.
    den_series = sum(w*x**(-j*p) for j,w in enumerate(coefficients,1))
    assert abs(denominator-den_series) < mp.mpf('1e-52')
    return numerator/denominator


def bias(p, c, kappa, u):
    p, c, kappa = (mp.mpf(q) for q in (p,c,kappa))
    x=mp.mpf(u)+c
    return mean_excess(str(p),str(c),str(kappa),u)-x/(p-1)+mp.mpf('0.5')


def close(x,y,tol):
    assert abs(x-y)<mp.mpf(tol), f"observed {x}; expected {y}"


# Dominant power-carrier correction above the variance boundary.
p=mp.mpf('1.5'); c=mp.mpf('1'); k=mp.mpf('0.5'); u=400
x=u+c
carrier=(k-1)*c**p*p/(2*(p-1)*(2*p-1))
close((bias(p,c,k,u)-p/(12*x))*x**(p-1),carrier,'0.001')
assert bias(p,c,k,u)<0

# Dominant positive half-step/Euler correction below the boundary.
p=mp.mpf('3')
close(bias(p,'1','0.5',400)*401,p/12,'0.003')

# All-generator critical index: a tunable x^(-1) cancellation and sharp x^(-3) remainder.
for c,k,u,third in [('1','0.5',400,mp.mpf('-1')/20),
                    ('2','0.875',400,mp.mpf('-1')/4)]:
    x=mp.mpf(u)+mp.mpf(c)
    b=bias('2',c,k,u)
    assert b<0
    close(x**3*b,third,'0.00002')

# On both sides of the cancellation curve the sign is opposite at large thresholds.
assert bias('2','1','0.3',400)<0
assert bias('2','1','0.8',400)>0

# DGPD baseline (kappa=1) has an exact Hurwitz zeta expression.
x=mp.mpf(101); p=mp.mpf('1.5')
expected=x**p*mp.zeta(p,x+1)
close(mean_excess('1.5','1','1',100), expected,'1e-55')
close(bias('1.5','1','1',400)*401,p/12,'0.003')

print('All 9 mean-excess formula, phase, boundary and numerical consistency checks passed.')
