"""Reproduce exact algebraic identities for a predator-equilibrium optimum.

Requires sympy and scipy. Numerical samples are illustrations, not proof.
"""
from sympy import symbols, diff, simplify, Matrix, Rational, sqrt
from scipy.optimize import brentq

u, v, b = symbols('u v b', positive=True)
r, k, alpha, a, c, m, eta = symbols('r k alpha a c m eta', positive=True)
den = 1 + k*v + alpha*u
F = r/den - a*u - b*v
G = c*b*u - m - eta*v
f = r*u/den - a*u*u - v*(m+eta*v)/c
p = {u:1,v:1,b:4,r:25,k:1,alpha:3,a:1,c:1,m:1,eta:3}
assert simplify(F.subs(p)) == 0
assert simplify(G.subs(p)) == 0
assert simplify(f.subs(p)) == 0
assert simplify(diff(f,u).subs(p)) == 0
assert simplify(diff(f,u,2).subs(p)) == Rational(-22,5)
assert simplify(diff(f,v).subs(p)) == -8
J = Matrix([ [diff(F,u),diff(F,v)], [diff(G,u),diff(G,v)] ])
assert simplify(J.subs(p).det()) == 32
rhs = Matrix([v, -c*u])
ub, vb = J.subs(p).inv()*rhs.subs(p)
assert ub == Rational(-1,4)
curv_h = -diff(f,u,2).subs(p)/diff(f,v).subs(p)
assert curv_h == Rational(-11,20)
assert curv_h*ub**2 == Rational(-11,320)
U = (sqrt(301)-1)/6
b0 = 1/U
assert simplify(b0-(sqrt(301)+1)/50) == 0
assert 0 < float(b0) < 4

def pop(B):
    def residual(x):
        y = (B*x - 1)/3
        return 25/(1+y+3*x)-x-B*y
    x = brentq(residual, 1/B, float(U))
    return x, (B*x-1)/3

previous = None
for B in [0.5, 1, 2, 3, 4, 5, 6, 8, 12, 100]:
    x, y = pop(B)
    assert 0 < x < float(U) and y > 0
    if previous is not None:
        assert x < previous[0]
        if B <= 4:
            assert y > previous[1]
        elif previous[2] >= 4:
            assert y < previous[1]
    previous = (x,y,B)
print('PASS exact stationary, derivative, Jacobian and rational curvature identities')
print('PASS supplementary sample of the unimodal equilibrium curve (not a proof)')
