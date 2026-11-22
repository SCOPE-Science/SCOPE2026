#!/usr/bin/env python3
"""Standalone exact-arithmetic checks of the displayed rational-PGF identities.

Finite tests are supplementary; RESULT.md proves every-index claims.
"""
from fractions import Fraction as F
import sympy as s

x=s.symbols('x', positive=True)
a=x/(x+2); b=x/(x+3); c=(1-a)*(1-b)
h=3/((x+1)*(2*x+7)); t=1+h
d=1-t*(1-c); u=1-t
assert s.simplify(c-6/((x+2)*(x+3)))==0
assert s.simplify((1-t)*(1+(a+b)/a+(a*b)/(a*a))+t*c)==0
assert s.simplify(h-c/(2*(1+b/a)-c))==0
assert s.simplify((h/d)-a/(a+2*b))==0
assert s.simplify(a*b/(a+2*b)-x/(3*x+7))==0
z=s.symbols('z')
G=(1-a)*(1-b)/((1-a*z)*(1-b*z))
from_mixing=6/x*(1/(1+2/x-z)-1/(1+3/x-z))
assert s.simplify(G-from_mixing)==0


def exact_checks(beta, scale, count=160):
    a=beta/(beta+2);b=beta/(beta+3)
    c=(1-a)*(1-b)
    d=1-scale*(1-c)
    assert d>0
    u=1-scale
    S=u*(a+b)/d
    P=u*a*b/d
    L0=F(2); L1=S
    discrepancies=[None,a+b-L1]
    for n in range(2,count+1):
        Ln=S*L1-P*L0
        discrepancies.append(a**n+b**n-Ln)
        L0,L1=L1,Ln
    return discrepancies

for beta in (F(1,5),F(1),F(3),F(20)):
    tcrit=1+3/((beta+1)*(2*beta+7))
    a=beta/(beta+2);b=beta/(beta+3)
    assert exact_checks(beta,F(1,3))[1]>0
    assert all(v>=0 for v in exact_checks(beta,F(1,3))[1:])
    assert all(v>=0 for v in exact_checks(beta,F(1))[1:])
    assert all(v>=0 for v in exact_checks(beta,tcrit)[1:])
    assert all(v>=0 for v in exact_checks(beta,(tcrit+1)/2)[1:])
    # Explicitly beyond the threshold, even canonical coefficients eventually turn negative.
    c=(1-a)*(1-b)
    tmax=1/(1-c)
    above=tcrit+(tmax-tcrit)/4
    assert any(v<0 for j,v in enumerate(exact_checks(beta,above)[1:],1) if j%2==0)
print('PASS: exact mixing identity, zero-deflation cutoff, numerator root, and finite rational cross-checks')
