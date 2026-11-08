#!/usr/bin/env python3
"""Reproduce exact two-community coefficients and illustrative critical trajectories.
Run: python verify.py. Requires Python 3, sympy, numpy, scipy.
The analytical theorem is proved in RESULT.md; numerical integration is diagnostic.
"""
from fractions import Fraction as Q
import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

c=sp.symbols('c', nonnegative=True)
B=sp.Matrix([[sp.Rational(1,4),sp.Rational(3,4)],
             [sp.Rational(3,4),sp.Rational(1,4)]])
r=sp.Matrix([sp.Rational(1,2),sp.Rational(1,2)])
l=sp.Matrix([[1,1]])
assert B*r==r and l*(B-sp.eye(2))==sp.zeros(1,2) and (l*r)[0]==1
G=sp.Matrix([[0,c/2],[c/2,0]])
K=sum(r[i]**2+sum(B[i,j]*r[j]*G[i,j] for j in range(2)) for i in range(2))
assert sp.simplify(K-(4+3*c)/8)==0
assert all(sp.simplify(r[i]/K-4/(4+3*c))==0 for i in range(2))
assert sp.simplify(G[0,1]/K-4*c/(4+3*c))==0
assert sp.simplify(K.subs(c,2)-sp.Rational(5,4))==0
assert Q(1,2)+Q(3,8)*Q(2)==Q(5,4)

def integrate(q, power):
    # four connections ordered (11,12,21,22), contact formation rate one
    y0=np.array([.75,.1])
    z0=np.array([[.2,.35],[.75,.1]])
    init=np.r_[y0,z0.ravel()]
    b=np.array(B,dtype=float)
    def f(t,state):
        y=state[:2]
        z=state[2:].reshape(2,2)
        s=(y[0]+y[1])/2
        response=s**power
        breaking=np.array([[0,q],[q,0]])*response
        dy=-y+(1-y)*((b*z)@y)
        dz=1-z-breaking*z
        return np.r_[dy,dz.ravel()]
    sol=solve_ivp(f,(0,1e5),init,rtol=2e-11,atol=1e-13,method='BDF')
    assert sol.success
    t=sol.t[-1]
    y=sol.y[:2,-1]
    zz=sol.y[2:,-1].reshape(2,2)
    return t*y,t*(1-zz[0,1]),t*(1-zz[1,0])

lin=integrate(2,1)
quad=integrate(2,2)
assert np.max(np.abs(lin[0]-0.4))<0.002,lin
assert abs(lin[1]-.8)<0.003 and abs(lin[2]-.8)<0.003,lin
assert np.max(np.abs(quad[0]-1.0))<0.004,quad
assert abs(quad[1])<0.005 and abs(quad[2])<0.005,quad
print('EXACT_COEFFICIENTS_OK',sp.factor(K))
print('LINEAR_RESPONSE_DIAGNOSTIC',lin)
print('QUADRATIC_RESPONSE_DIAGNOSTIC',quad)
print('VERIFY_OK')
