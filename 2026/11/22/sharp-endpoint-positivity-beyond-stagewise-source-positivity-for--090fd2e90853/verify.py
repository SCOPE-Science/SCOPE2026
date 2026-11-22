#!/usr/bin/env python3
"""Exact symbolic and rational checks for the two-stage cubic matrix update.
Dependency: sympy (pip install sympy). No random/remote input.
"""
from fractions import Fraction as F
from math import sqrt
import sympy as S

def check():
    x,h,a,u=S.symbols('x h a u',real=True)
    y=x+h*(x-x**3)
    z=S.expand((x+y+h*(y-y**3))/2)
    z_over_x=S.cancel(z/x)
    expected=1+(1-x**2)*h+(1-x**2)*(1-3*x**2)*h**2/2-3*x**2*(1-x**2)**2*h**3/2-x**2*(1-x**2)**3*h**4/2
    assert S.simplify(z_over_x-expected)==0
    G=(a**4-a**3+a+1)/(a*(a*a-1))
    derivative=(a*a+1)*(a**4-4*a*a+1)/(a*a*(a-1)**2*(a+1)**2)
    assert S.simplify(S.diff(G,a)-derivative)==0
    critical_a=S.sqrt(2+S.sqrt(3)); H=2*S.sqrt(2)-1
    assert S.simplify(G.subs(a,critical_a)-H)==0
    U=(1+a*a)/(1+a+a**4-a**3)
    assert S.simplify((z_over_x.subs(h,(a-1)/(1-x*x))).subs(x*x,U))==0 or S.simplify((z_over_x.subs(h,(a-1)/(1-x*x))).subs(x**2,U))==0
    xcrit=S.sqrt(U.subs(a,critical_a))
    assert 0<float(xcrit)<1
    assert abs(float(z_over_x.subs({x:xcrit,h:H}).evalf(45)))<1e-35
    assert z.subs({x:S.Rational(7,10),h:2}) == -S.Rational(44518243,125000000)
    assert S.simplify((y-1)/(1-x)-(h*x*(x+1)-1))==0
    # A grid of exact rational checks, illustrative only (analytic proof is separate).
    count=0
    for k in range(1,101):
        q=S.Rational(k,101)
        for t in [S.Rational(1,10), S.Rational(1,2), S.Integer(1), S.Rational(3,2),S.Rational(9,5)]:
            assert z.subs({x:q,h:t})>0
            count+=1
    assert z.subs({x:S.Rational(7,10),h:2})<0
    print('PASS exact symbolic identities, radical threshold, endpoint example and',count,'rational interior diagnostics')

if __name__=='__main__':
    check()
