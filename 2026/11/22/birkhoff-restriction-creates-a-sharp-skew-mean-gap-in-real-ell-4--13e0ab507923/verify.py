"""Supplementary exact-algebra checks and deterministic finite samples.

Run: python verify.py  (requires SymPy). The analytic proof is in RESULT.md.
"""
import math
from sympy import (symbols, Rational, sqrt, simplify, factor, diff, expand,
                   Matrix, det, nroots, N)

checks = 0
def check(condition, label):
    global checks
    assert condition, label
    checks += 1

u, t, R, Q, a, b = symbols('u t R Q a b', real=True)
q = 1-u+u**2
J = u**Rational(1,4)*(1-u)/q**Rational(3,4)
B = sqrt(u/q)
c = (Rational(4,27))**Rational(1,4)
u0 = 2-sqrt(3)
# The quartic reduction is a polynomial identity, independent of optimization.
x1, x2, y1, y2 = symbols('x1 x2 y1 y2', real=True)
p4 = expand((x1+t*y1)**4+(x2+t*y2)**4)
poly = expand(x1**4+x2**4+4*t*(x1**3*y1+x2**3*y2)
              +6*t*t*(x1*x1*y1*y1+x2*x2*y2*y2)
              +4*t**3*(x1*y1**3+x2*y2**3)
              +t**4*(y1**4+y2**4))
check(expand(p4-poly)==0, 'quartic binomial')
# 2x2 matrix norm generalized characteristic polynomial.
K = Matrix([[2*(1+t**4), 2*t*(1-t*t)],
            [2*t*(1-t*t),1+6*t*t+t**4]])
D = Matrix([[2,0],[0,1]])
lam = symbols('lam')
M = 1+3*t*t+t**4
check(simplify(det(K-lam*D)/2 - (lam**2-2*M*lam+(1+t*t)**4))==0, 'generalized eigen polynomial')
check(expand(M**2-(1+t*t)**4-t*t*(1+2*t*t)*(2+t*t))==0, 'discriminant')
# Leading maximizer J in (0,1).
J4 = u*(1-u)**4/q**3
check(simplify(diff(J4,u)/J4 + (u+1)*(u*u-4*u+1)/(u*(u-1)*q))==0, 'critical polynomial')
check(abs(float(N(J.subs(u,u0)-c,18)))<1e-13, 'leading constant')
check(simplify(B.subs(u,u0)-1/sqrt(3))==0, 'mixed term')
f1 = J/2
f2 = Rational(3,2)*B-Rational(3,4)*J**2
f3 = -J/2-Rational(9,4)*J*B+Rational(7,4)*J**3
f1dd = diff(f1,u,2).subs(u,u0)
f2d = diff(f2,u).subs(u,u0)
f3max = f3.subs(u,u0)-f2d*f2d/(2*f1dd)
check(abs(float(N(f1dd+c*(7+4*sqrt(3))/4,20)))<1e-12, 'second derivative')
check(abs(float(N(f2d-(1+sqrt(3)/2),20)))<1e-12, 'second coefficient slope')
check(abs(float(N(f2.subs(u,u0)-1/sqrt(3),20)))<1e-12,'quadratic coefficient')
check(abs(float(N(-f2d/f1dd-(6*sqrt(3)-9)*c,20)))<1e-12, 'extremizer displacement')
check(abs(float(N(f3max-c*(7*sqrt(3)-9)/18,20)))<1e-12, 'optimized cubic coefficient')
# Finite consistency checks of norm formulas and strict gap (not an infinite proof).
for T in (0.004,0.015,0.05,0.1,0.2,0.5,0.8,1,1.2,2,5):
    unit_unrestricted = float((1+3*T*T+T**4+T*math.sqrt((1+2*T*T)*(2+T*T)))**.25)
    grid = []
    for k in range(1,101):
        s=k/101
        un=s**4
        xx=(1,s)
        yy=(s**3,-1)
        xn=(xx[0]**4+xx[1]**4)**.25
        yn=(yy[0]**4+yy[1]**4)**.25
        X=(xx[0]/xn,xx[1]/xn)
        Y=(yy[0]/yn,yy[1]/yn)
        check(abs(X[0]**3*Y[0]+X[1]**3*Y[1])<1e-11, 'Birkhoff orthogonality')
        Jval=float(J.subs(u,un)); Bval=float(B.subs(u,un))
        for sign in (1,-1):
            Qnorm=(((X[0]+sign*T*Y[0])**4+(X[1]+sign*T*Y[1])**4)**.25+
                   ((T*X[0]-sign*Y[0])**4+(T*X[1]-sign*Y[1])**4)**.25)/2
            U1=(1+6*Bval*T*T-sign*4*Jval*T**3+T**4)**.25
            U2=(1+sign*4*Jval*T+6*Bval*T*T+T**4)**.25
            check(abs(Qnorm-(U1+U2)/2)<2e-12, 'quartic formula')
            grid.append(Qnorm)
    check(max(grid)<=unit_unrestricted+1e-10, 'finite upper bound')
print('BIRKHOFF_RESTRICTED_SKEW_MEAN_CHECK_OK', checks)
