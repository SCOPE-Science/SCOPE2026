"""Reproduce exact commutator and finite-step collapse calculations.
Run: python verify.py (requires sympy and scipy for optional ODE checks).
No observations from numerical testing are used to prove the universal theorem.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp

x, y, g, w = sp.symbols('x y gamma omega', real=True)
V = sp.Function('V')
f1=sp.Matrix([-g*x,0])
f2=sp.Matrix([-w*sp.diff(V(y),y),w*x])
def bracket(f,h):
    z=sp.Matrix([x,y])
    return sp.simplify(h.jacobian(z)*f - f.jacobian(z)*h)
b12=bracket(f1,f2)
c=bracket(f1,b12)
assert all(sp.simplify(v)==0 for v in c-g**2*f2), (b12,c)
print('PASS: arbitrary-potential nested commutator equals gamma^2 times Hamiltonian field.')

h=sp.symbols('h', positive=True)
a=1-g**2*h**2/sp.Integer(72)
hstar=6*sp.sqrt(2)/g
assert sp.simplify(a.subs(h,hstar)) == 0
s=w*h*a/sp.Integer(2)
assert sp.simplify(sp.diff(s,h).subs(h,hstar)+w)==0
print('PASS: exact universal cancellation and frequency detuning derivative.')

# Exact rational one-step collapse for gamma=1, h*=6*sqrt(2).
G=1.0; W=1.3; hs=6*math.sqrt(2)/G
b0=math.exp(-2*G*hs/3)
def step(hh,Y):
    xx=0.0; yy=Y
    xx*=math.exp(-G*hh/6)
    t=0.5*hh*W*(1-G*G*hh*hh/72)
    def F(_t, state):
        X,Z=state
        return [-Z-Z**3,X]
    for k in range(2):
        if t!=0:
            sol=solve_ivp(F,(0.,t),(xx,yy),method='DOP853',rtol=1e-12,atol=1e-14)
            assert sol.success
            xx,yy=map(float,sol.y[:,-1])
        if k==0: xx*=math.exp(-2*G*hh/3)
    xx*=math.exp(-G*hh/6)
    return xx,yy
X,Y = step(hs,1.1)
assert abs(X)<1e-12 and abs(Y-1.1)<1e-12
expected=-(1+b0)*W*W*(1.1+1.1**3)
for delta in (0.08,0.04,0.02,0.01):
    _,yn=step(hs+delta,1.1)
    approx=(yn-1.1)/delta**2
    assert abs(approx/expected-1)<0.30,(delta,approx,expected)
print('PASS: nonlinear quartic-potential collapse and quadratic detuning consistency.')
print('Expected detuning coefficient:', expected)

# Exact trace/determinant of linearized map and the near-freezing slow multiplier.
u, k, z = sp.symbols('u k z', positive=True)
# z = cos(phi); sin(phi)^2 = 1-z^2
tr = (1+u**6)*z**2-(u**2+u**4)*(1-z**2)
det = u**6
assert sp.simplify(tr.subs(z,1)-(1+det))==0
K=sp.simplify(sp.diff(tr,z).subs(z,1)/2)  # trace decrease for phi^2 to leading order
assert sp.factor(K - (1+u**2)*(1+u**4))==0
# If L = 1 - alpha*phi^2 then its characteristic equation gives alpha=K/(1-det).
alpha=K/(1-det)
assert sp.simplify((1-det)*alpha-K)==0

import numpy as np
from scipy.linalg import expm
G=1.; W=1.3; kap=2.75
hs=6*math.sqrt(2)/G
U=math.exp(-G*hs/6)
coefficient=kap*W**2*(1+U**2)*(1+U**4)/(1-U**6)
def lin_matrix(hh):
   D1=np.diag([math.exp(-G*hh/6),1.])
   D2=np.diag([math.exp(-2*G*hh/3),1.])
   t=0.5*hh*W*(1-G*G*hh*hh/72)
   C=expm(t*np.array([[0.,-kap],[1.,0.]]))
   return D1@C@D2@C@D1
assert np.linalg.norm(lin_matrix(hs)-np.diag([math.exp(-G*hs),1.]))<1e-12
for delta in (0.06,0.03,0.015,0.0075):
   ev=np.linalg.eigvals(lin_matrix(hs+delta))
   rho=max(abs(ev))
   approx=(1-rho)/delta**2
   assert abs(approx/coefficient-1)<0.30,(delta,approx,coefficient)
print('PASS: exact trace factorization and sharp quadratic slow-eigenvalue coefficient.')
print('Expected slow-mode coefficient:',coefficient)
