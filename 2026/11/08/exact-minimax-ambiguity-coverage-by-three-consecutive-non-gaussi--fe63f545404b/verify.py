#!/usr/bin/env python3
"""Exact check of the Hermite-window Laguerre minimax certificate (Python 3, SymPy)."""
import sympy as s

u, t = s.symbols('u t', real=True)
r = u**3 - 9*u**2 + 24*u - 12
L1 = 1-t
L2 = 1-2*t+t**2/s.Integer(2)
L3 = 1-3*t+s.Rational(3,2)*t**2-t**3/s.Integer(6)
c = 3-3*u+u**2/s.Integer(2)
B = 3*(3*u**2-23*u+48)/(9-u)
D = (1-u)/(3*(9-u))
E = (39-u-2*u**2)/(9-u)**2
Q = (t**2-(9-u)*t+B)**2/s.Integer(36)+D*t**2+E
G = c*L1**2+L3**2-(1+c)*(1-u)**2

# Quotient ring Q[u]/(r): clear denominators first and reduce in u.
def verify_mod_root(expr):
    rat = s.cancel(expr)
    numerator, denominator = s.fraction(rat)
    remainder = s.rem(s.expand(numerator), r, u)
    assert s.expand(remainder) == 0, s.factor(remainder)
    assert denominator != 0

verify_mod_root(G-(t-u)**2*Q)
verify_mod_root(L3.subs(t,u)+(1-u))
verify_mod_root(s.expand((1-u)**2-L2.subs(t,u)**2) - u*(2-u)*(u*u-6*u+4)/4)

# Rational isolating interval plus complete real-root uniqueness for r:
# r(3/5)<0<r(2/3), and r is increasing on (-infty,2),
# decreasing on (2,4), increasing on (4,infty), with r(4)>0.
assert r.subs(u,s.Rational(3,5)) < 0
assert r.subs(u,s.Rational(2,3)) > 0
assert r.subs(u,s.Integer(4)) > 0
assert s.expand(s.diff(r,u)-3*(u-2)*(u-4)) == 0

# All SOS coefficients positive on u in (3/5,2/3).
# B>0 because 3u^2-23u+48>0 on (0,1).
assert (3*s.Rational(2,3)**2-23*s.Rational(2,3)+48)>0
assert (39-s.Rational(2,3)-2*s.Rational(2,3)**2)>0
assert (s.Rational(2,3)**2-6*s.Rational(2,3)+4)>0

# Check Gaussian-relative ambiguity polynomial order 1, 2, 3,
# and compare the tight value against direct finite evaluation.
u0 = float([z for z in s.nroots(r, n=35) if abs(s.im(z)) < 1.e-25][0])
c0 = float(c.subs(u,u0)); W=[c0/(1+c0),0,1/(1+c0)]; C=(1-u0)**2
assert 0.6 < u0 < 2/3 and abs(sum(W)-1)<1e-13
for i in range(5001):
    x=16.0*i/5000
    score=W[0]*float(L1.subs(t,x))**2 +W[2]*float(L3.subs(t,x))**2
    assert score >= C-1e-11, (x,score,C)
assert abs(W[0] - 0.5601925600938)<1e-10
assert abs(C-0.12623908314228)<1e-10
print('HERMITE_123_MINIMAX_CERTIFICATE_PASS 5001',f'u={u0:.14f}',f'C={C:.14f}')
