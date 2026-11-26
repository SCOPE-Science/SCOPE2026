#!/usr/bin/env python3
"""Executable checks for a one-dimensional maximal hard-core model."""
from itertools import product
from math import acos, log, sqrt
import sympy as S

z=S.symbols('z',positive=True); l,t=S.symbols('l t')
T=S.Matrix([[0,z,0],[0,0,1],[1,z,0]])
assert S.expand(T.charpoly(l).as_expr())==l**3-z*l-z
assert S.factor(S.discriminant(T.charpoly(l).as_expr(),l))==z**2*(4*z-27)
assert S.factor(S.diff(l**3/(l+1),l))==l**2*(2*l+3)/(l+1)**2
assert S.expand((l**3-z*l-z).subs({l:S.Integer(3),z:S.Rational(27,4)}))==0
assert S.simplify(T.subs(z,S.Rational(27,4)).charpoly(l).as_expr()-(l-3)*(l+S.Rational(3,2))**2)==0
# Explicitly check defectiveness: two-dimensional algebraic eigenspace is 1-dimensional
assert len((T.subs(z,S.Rational(27,4))+S.Rational(3,2)*S.eye(3)).nullspace())==1
# Transfer counts agree with direct cyclic words, not with an arbitrary open-boundary model.
for n in range(3,15):
    brute=S.Integer(0)
    for x in product((0,1),repeat=n):
        if all(not(x[i] and x[(i+1)%n]) and (x[i] or x[(i-1)%n] or x[(i+1)%n]) for i in range(n)):
            brute+=z**sum(x)
    exact=S.expand(S.trace(T**n))
    assert S.simplify(brute-exact)==0,(n,brute,exact)
# Renewal generating function at critical z=27/4: residence gaps 2 and 3.
s=S.symbols('s')
U=1/(1-S.Rational(3,4)*s**2-S.Rational(1,4)*s**3)
assert S.simplify(U-(S.Rational(4,9)/(1-s)+S.Rational(2,9)/(1+s/2)+S.Rational(1,3)/(1+s/2)**2))==0
# density 4/9; exact connected occupancy correlations for all r>=0.
u=[S.Rational(1)]
for r in range(1,81):
    u.append((S.Rational(3,4)*u[r-2] if r>=2 else 0)+(S.Rational(1,4)*u[r-3] if r>=3 else 0))
for r in range(81):
    assert S.factor(S.Rational(4,9)*(u[r]-S.Rational(4,9)))==S.Rational(4,81)*(3*r+5)*(-S.Rational(1,2))**r
# For all positive z sampled, no other pole with dominant modulus; unique crossover:
for zval in [S.Rational(1,1000),S.Rational(1,10),S.Integer(1),S.Rational(27,4),S.Integer(8),S.Integer(100),S.Integer(10000)]:
    roots=[complex(a) for a in S.nroots(l**3-zval*l-zval)]
    lam=max(roots,key=lambda a:a.real).real
    others=[a for a in roots if a.real < 0]
    assert len(others)==2
    assert abs(lam**3-float(zval)*(lam+1))<1e-6*max(1,lam**3)
    if zval<S.Rational(27,4):
        rho=1/sqrt(lam+1)
        assert all(abs(abs(a)/lam-rho)<1e-9 for a in others)
        theta=acos(-sqrt(lam+1)/2)
        assert 2*3.141592653589793/3 < theta < 3.141592653589793
    if zval>S.Rational(27,4):
        delta=sqrt((lam-3)/(lam+1))
        assert abs(max(abs(a) for a in others)/lam-(1+delta)/2)<1e-9
# Explicit zero-energy limit at z->0 and high-activity limit checked against rigorous asymptotics.
for zv in [1e-9,1e-12]:
    import scipy.optimize
    lam=scipy.optimize.brentq(lambda x:x**3-zv*x-zv,0,1)
    xi=2/log(1+lam)
    assert abs(xi/(2*zv**(-1/3))-1)<.002
for zv in [1e6,1e8]:
    import scipy.optimize
    lam=scipy.optimize.brentq(lambda x:x**3-zv*x-zv,0,2*sqrt(zv))
    d=sqrt((lam-3)/(lam+1))
    xi=1/log(2/(1+d))
    assert abs(xi/sqrt(zv)-1)<.002
print('VERIFY_OK: symbolic discriminant, defective double eigenvalue, 12 exact ring partitions, 81 exact correlations, 7 spectra, endpoint scales')
