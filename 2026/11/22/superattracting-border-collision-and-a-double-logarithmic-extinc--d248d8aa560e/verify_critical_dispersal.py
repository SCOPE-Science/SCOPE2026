#!/usr/bin/env python3
"""Exact checks for the critical border two-cycle of a discontinuous logistic map.

The symbolic identities support, rather than replace, the analytic arguments.
Run with Python 3 and SymPy; no internet required.
"""
import sympy as s

r,x,u=s.symbols('r x u',real=True)
f=lambda z:r*z*(1-z)
rc=1+s.sqrt(5)
delta=(r-2)*(r*r-2*r-4)/16
C=r*r*(r/2-1)
expr=s.expand(f(f(s.Rational(1,2)+u))-s.Rational(1,2))
assert s.expand(expr-(-delta+u*u*(C-r**3*u*u)))==0
assert s.simplify(delta.subs(r,rc))==0
assert s.simplify(s.diff(delta,r).subs(r,rc)-(5-s.sqrt(5))/8)==0
assert s.simplify(delta.subs(r,s.Rational(13,4))-s.Rational(5,1024))==0
assert s.simplify(f(rc/4).subs(r,rc)-s.Rational(1,2))==0
assert s.simplify(f(s.Rational(1,2)).subs(r,rc)-rc/4)==0
q=s.factor(f(f(x))-x)
assert s.simplify(q-(-x*(r*x-r+1)*(r*r*x*x-r*(r+1)*x+r+1)))==0
roots=[(r+1+sgn*s.sqrt((r-3)*(r+1)))/(2*r) for sgn in (-1,1)]
for pt in roots:
    assert s.simplify((f(f(pt))-pt))==0
    assert s.simplify(s.diff(f(f(x)),x).subs(x,pt)-(-r*r+2*r+4))==0
assert s.simplify(roots[0].subs(r,rc)-s.Rational(1,2))==0
assert s.simplify(roots[1].subs(r,rc)-rc/4)==0
assert bool((C.subs(r,rc)-s.Rational(13,4)**3/100-6)>0)
assert bool(7-C.subs(r,s.Rational(13,4))>0)
assert bool((rc/4-s.Rational(3,5))>0)
assert bool((rc*s.Rational(24,100)-s.Rational(1,2))>0)
# Independently compare the recurrence to the two physical right-branch iterates
for gain in (s.Rational(3237,1000),s.Rational(13,4)):
    for starting in (s.Rational(1,10),s.Rational(1,20),s.Rational(1,100)):
        z=s.Rational(1,2)+starting
        direct=f(f(z)).subs(r,gain)
        recurrence=s.Rational(1,2)+(-delta+u*u*(C-r**3*u*u)).subs({r:gain,u:starting})
        assert direct==recurrence
# High-precision asymptotic diagnostic of the first exit index
import mpmath as mp
for p in (4,8,16,32,64,128,256):
    mp.mp.dps=p+50
    rr=1+mp.sqrt(5)+mp.power(10,-p)
    d=(rr-2)*(rr**2-2*rr-4)/16
    c=rr**2*(rr/2-1)
    xx=mp.mpf(1)/10
    K=0
    while xx>0:
        xx=-d+xx**2*(c-rr**3*xx**2)
        K+=1
        assert K<100
    assert abs(K-mp.log(p*mp.log(10),2))<5
print('PASS: symbolic recurrence, cubic factor, two-cycle multipliers, critical contacts, sharp constants, rational iterates and 7 high-precision exit diagnostics')
