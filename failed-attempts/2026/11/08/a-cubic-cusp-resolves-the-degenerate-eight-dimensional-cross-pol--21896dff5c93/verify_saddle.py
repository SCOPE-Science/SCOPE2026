"""Reproducible symbolic checks for the 8-dimensional restricted cross-polytope saddle.
Run with Python 3 and sympy/mpmath: python verify_saddle.py
All critical identities are exact; numerical quadrature is supplementary.
"""
from sympy import (symbols, Rational, sqrt, pi, oo, integrate, simplify,
                   factor, gamma, factorial)
import mpmath as mp

x, s = symbols('x s', positive=True, real=True)
A0 = 1/(1+x*x/2)**2
A2 = (x*x/4 + Rational(7,8)*x**4)/(1+x*x/2)**4
I0 = simplify(integrate(A0, (x, 0, oo)))
assert I0 == pi*sqrt(2)/4
# Exact cancellation of the second variation in the collective tangent.
assert simplify(integrate(A2, (x, 0, oo)) - integrate(x*x*A0/4, (x, 0, oo))) == 0
assert factor(A2-x*x*A0/4) == -x**4*(x*x-10)/(x*x+2)**4
# Coefficient from the tail after subtracting the vanishing quadratic term.
J = simplify(56 * integrate((1+x*x)**(-8), (x, 0, oo)))
assert simplify(J - 3003*pi/512) == 0
c = simplify(4*J/(24**Rational(3,2)*I0))
assert simplify(c - 1001*sqrt(3)/3072) == 0
# The other, zero-sum tangent has a negative quadratic coefficient.
negative_q = simplify(A0*(x*x/(1+x*x/2)-x*x))
assert factor(negative_q) == -4*x**4/(x*x+2)**3
negative_relative = simplify(integrate(negative_q, (x, 0, oo))/I0)
assert negative_relative == -Rational(3,2)
# Both paths preserve sum=0 and Euclidean norm=1 identically.
from sympy import Matrix
p = Matrix([1/sqrt(2), -1/sqrt(2), 0,0,0,0,0,0])
e = Matrix([sqrt(Rational(3,8)),sqrt(Rational(3,8))] + [-1/sqrt(24)]*6)
f = Matrix([0,0,1/sqrt(2),-1/sqrt(2),0,0,0,0])
for v in (p,e,f):
    assert simplify(sum(v)) == 0 and simplify(v.dot(v)-1) == 0
assert simplify(p.dot(e)) == simplify(p.dot(f)) == 0

mp.mp.dps = 45
p_num = mp.sqrt(mp.mpf(1)/2)
g = mp.sqrt(mp.mpf(3)/8)
d = -1/mp.sqrt(24)
def norm_int(t, collective):
    u = mp.sqrt(1-t*t)
    if collective:
        coords = [u*p_num+t*g, -u*p_num+t*g]+[t*d]*6
    else:
        coords = [u*p_num,-u*p_num,t/mp.sqrt(2),-t/mp.sqrt(2),0,0,0,0]
    return mp.quad(lambda z: mp.fprod(1/(1+(v*z)**2) for v in coords),
                   [0,1,10,100,mp.inf])
v0 = norm_int(mp.mpf('0'),True)
assert abs(v0-mp.pi*mp.sqrt(2)/4) < mp.mpf('1e-38')
for tstr in ('0.02','0.01','0.005'):
    t = mp.mpf(tstr)
    pos = norm_int(t,True)/v0-1
    neg = norm_int(t,False)/v0-1
    assert pos > 0 and neg < 0, (tstr,pos,neg)
    assert abs(pos/t**3 - mp.mpf(str(c.evalf(40)))) < mp.mpf('0.05')
    assert abs(neg/t**2 + mp.mpf('1.5')) < mp.mpf('0.1')
print('SADDLE_EXACT_OK; positive_cubic=',c,'negative_quadratic=',negative_relative)
