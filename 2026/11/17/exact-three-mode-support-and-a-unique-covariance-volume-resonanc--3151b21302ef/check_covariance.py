#!/usr/bin/env python3
"""Exact symbolic verification of three-mode dichotomous-input response identities.

Dependency: SymPy (tested with SymPy 1.x). Run: python check_covariance.py
"""
import sympy as sp

k, m, x = sp.symbols('k m x', positive=True)
rate = (1, 2, 3)
C = sp.Matrix([[sp.Rational(i*j, i+j) *
                (1/(k+i) + 1/(k+j))
                for j in rate] for i in rate])
D = k**2*(k+6)/(150*(k+1)**2*(k+2)**2*(k+3)**2)
assert sp.cancel(C.det()-D) == 0
Q = 3*k**4+30*k**3+61*k**2-18*k-72
assert sp.cancel(sp.diff(D,k) + k*Q/(150*(k+1)**3*(k+2)**3*(k+3)**3)) == 0
for val in (sp.Rational(1,10), sp.Rational(1,2), 1, 2, 5, 100):
    M = C.subs(k,val)
    assert M.is_positive_definite
    assert sp.factor(M.det()) == sp.factor(D.subs(k,val))

z_min = 3*x*x/(4*m)+m**3/4
z_max = 1-3*(1-x)**2/(4*(1-m))-(1-m)**3/4
gap = 3*(x-m*m)*(2*m-m*m-x)/(4*m*(1-m))
assert sp.cancel(z_max-z_min-gap) == 0
assert sp.simplify(sp.integrate(gap,(x,m*m,2*m-m*m))-m*m*(1-m)**2) == 0
assert sp.integrate(m*m*(1-m)**2,(m,0,1)) == sp.Rational(1,30)
for mv in (sp.Rational(1,4), sp.Rational(1,2), sp.Rational(3,4)):
    for theta in (sp.Rational(0),sp.Rational(1,3),sp.Rational(2,3),sp.Rational(1)):
        xv=mv**2+theta*(2*mv-2*mv**2)
        assert sp.simplify(gap.subs({m:mv,x:xv}))>=0
assert Q.subs(k,sp.Rational(9,10))<0<Q.subs(k,1)
print('THREE_MODE_TELEGRAPH_EXACT_OK determinant=1 derivative=1 support=1 volume=1 rational_cases=6')
