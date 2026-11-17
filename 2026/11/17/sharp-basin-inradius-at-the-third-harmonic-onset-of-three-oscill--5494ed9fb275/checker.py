#!/usr/bin/env python3
"""Reproduce symbolic and numerical identities in the accompanying phase-flow theorem."""
import math
import numpy as np
import sympy as sp
from scipy.optimize import root

x, y, d, t = sp.symbols('x y d t', real=True)
a = sp.Rational(1, 6) + d
H = lambda z: sp.sin(z) + a*sp.sin(3*z)
phase = [sp.Integer(0), 2*sp.pi/3 + x, 4*sp.pi/3 + y]
velocity = [sum(H(phase[j]-phase[i]) for j in range(3) if j != i) for i in range(3)]
F = sp.Matrix([sp.trigsimp(velocity[1]-velocity[0]), sp.trigsimp(velocity[2]-velocity[0])])
assert sp.simplify(F.subs({x: 0, y: 0})) == sp.zeros(2, 1)
assert sp.simplify(F.jacobian([x, y]).subs({x: 0, y: 0})+9*d*sp.eye(2)) == sp.zeros(2)
Q = sp.Matrix([sp.sqrt(3)*(x*x+2*x*y-2*y*y)/4, sp.sqrt(3)*(2*x*x-2*x*y-y*y)/4])
for i in range(2):
    series = sp.series(F[i].subs({x: t*x, y: t*y, d: t*d}), t, 0, 3).removeO().expand()
    assert sp.simplify(series.coeff(t, 2)-(-9*d*sp.Matrix([x, y])[i]+Q[i])) == 0
q = lambda z1, z2: sp.Rational(2,3)*(z1*z1-z1*z2+z2*z2)
assert sp.simplify(q(Q[0],Q[1])-sp.Rational(27,32)*q(x,y)**2) == 0
X, Y = sp.symbols('X Y', real=True)
G = -9*sp.Matrix([X,Y])+Q.subs({x:X,y:Y})
roots = sp.solve_poly_system(list(G), X, Y)
wanted = [(0,0),(8*sp.sqrt(3),4*sp.sqrt(3)),(-4*sp.sqrt(3),4*sp.sqrt(3)),(-4*sp.sqrt(3),-8*sp.sqrt(3))]
assert {tuple(map(sp.simplify, pair)) for pair in roots} == {tuple(pair) for pair in wanted}
for pair in wanted[1:]:
    assert sp.simplify(q(*pair)-96) == 0
    J = G.jacobian([X,Y]).subs({X:pair[0],Y:pair[1]})
    assert sorted(J.eigenvals().keys()) == [-27, 9]

Fnum = sp.lambdify((x,y,d), F, modules='numpy')
Jnum = sp.lambdify((x,y,d), F.jacobian([x,y]), modules='numpy')
R = 4*math.sqrt(6)
for delta in (0.002, 0.001, 0.0005):
    for pair in wanted[1:]:
        guess = np.array([float(pair[0]),float(pair[1])])*delta
        sol = root(lambda w: np.asarray(Fnum(w[0],w[1],delta),dtype=float).reshape(2), guess, jac=lambda w: np.asarray(Jnum(w[0],w[1],delta),dtype=float),tol=1e-11)
        assert np.linalg.norm(Fnum(*sol.x,delta)) < 2e-12
        assert np.linalg.norm(sol.x-guess) < 600*delta*delta
        rad = math.sqrt(2/3*(sol.x[0]**2-sol.x[0]*sol.x[1]+sol.x[1]**2))
        assert abs(rad/delta-R) < 400*delta
        ev = np.linalg.eigvals(np.asarray(Jnum(*sol.x,delta),float))
        assert min(ev) < -20*delta and max(ev) > 5*delta
print('PASS: exact Taylor coefficients; quotient-metric quadratic identity; four blow-up roots; saddle eigenvalues; numerical branches at three small parameters.')
