"""Exact rational identities supporting the scalar uniformity-statistic construction.

Requires SymPy (see requirements.txt). Run: python verify.py
All equalities below are symbolic polynomial identities, not Monte Carlo evidence.
"""
import sympy as sp

x, t, e, a, b, c = sp.symbols('x t e a b c', real=True)
H = x * (1 - x)
G1 = H * (1 - 2*x)
G3 = H * (1 - 2*x)**3


def integrate(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def delta(F):
    return sp.expand(integrate(2*(1-x)*F - F**2))


def project(F):
    # For F(0)=0,F(1)=1 and a polynomial F, this equals
    # 2 E[max(x,X)]-2x+x^2 for X distributed with CDF F.
    T = (F - x).subs(x, t)
    return sp.expand(1 + 2*x**2 - 2*x - 2*sp.integrate(T, (t, x, 1)))


def variance(F):
    p = sp.diff(F, x)
    v = project(F)
    ev = integrate(p*v)
    return sp.expand(integrate(p*v*v)-ev**2)


def assert_equal(u, v, label):
    d = sp.factor(u-v)
    assert d == 0, f'{label}: {d}'
    print('PASS', label)


F = x + a*G1 + b*G3 + c*H
assert_equal(F.subs(x, 0), 0, 'left boundary')
assert_equal(F.subs(x, 1), 1, 'right boundary')
assert_equal(F.subs(x, sp.Rational(1, 2)), sp.Rational(1, 2)+c/4,
             'non-uniform CDF at midpoint')
D = delta(F)
assert_equal(delta(x), 0, 'uniform departure')
assert_equal(sp.diff(D, a).subs({a:0,b:0,c:0}), sp.Rational(1,15), 'departure derivative a')
assert_equal(sp.diff(D, b).subs({a:0,b:0,c:0}), sp.Rational(1,35), 'departure derivative b')
assert_equal(sp.diff(D, c).subs({a:0,b:0,c:0}), 0, 'departure derivative c')
assert_equal(delta(x+c*H),-c**2/30, 'departure along c')

assert_equal(project(x), 1+2*x*x-2*x, 'uniform projection')
assert_equal(variance(x), sp.Rational(1,45), 'uniform projection variance')
assert_equal(variance(x+c*H), sp.Rational(1,45)-c*c/420-c**4/225,
             'exact variance along c')

# Independent direct symbolic differentiation in each coordinate, rather
# than relying only on the weight-function calculation.
for label, g, answer in [('a',G1,0),('b',G3,sp.Rational(4,945)),('c',H,0)]:
    direct = sp.diff(variance(x+e*g),e).subs(e,0)
    assert_equal(direct, answer, 'variance derivative '+label)

q = 2*x*x-2*x+sp.Rational(1,3)
W = sp.expand(-sp.diff(q*q,x)-4*sp.integrate(q.subs(x,t),(t,0,x)))
assert_equal(W,-sp.Rational(4,3)*(2*x-1)*(7*x*x-7*x+1),'variance derivative weight')
for label,g,answer in [('a',G1,0),('b',G3,sp.Rational(4,945)),('c',H,0)]:
    assert_equal(integrate(W*g),answer,'weight integral '+label)

J = sp.Matrix([[sp.Rational(1,15),sp.Rational(1,35)],
               [0,sp.Rational(4,945)]])
assert_equal(J.det(),sp.Rational(4,14175),'nonzero Jacobian determinant')
A2=sp.Rational(29,112); B2=sp.Rational(9,16)
assert_equal(A2/15+B2/35,sp.Rational(1,30),'departure order-c² cancellation')
assert_equal(B2*sp.Rational(4,945),sp.Rational(1,420),'variance order-c² cancellation')

# Exact generic contrast-to-integral identity by integration by parts.
# For continuous F with F(0)=0 and F(1)=1,
# Emax = 1 - integral(F^2), EX = 1-integral(F),
# EX² = 1 - 2 integral(x F).
assert_equal(
    delta(F),
    1-integrate(F**2)-2*(1-integrate(F))+1-2*integrate(x*F),
    'population U-kernel and CDF integral agree'
)
print('All symbolic identities passed. The analytic implicit-function theorem')
print('and the bounded-kernel U-statistic CLT complete the infinite-sample proof.')
