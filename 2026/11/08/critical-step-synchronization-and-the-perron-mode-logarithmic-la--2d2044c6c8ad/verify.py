#!/usr/bin/env python3
"""Exact algebraic checks of the endpoint tree-phase normal form."""
import sympy as S
import numpy as np
from math import log

def model(K, L, u):
    n=K.rows
    E=S.eye(n)
    u=S.simplify(u)
    assert S.simplify(u.dot(u))==1
    assert S.simplify(K*u-L*u)==S.zeros(n,1)
    A=S.simplify(E-2*K/L)
    Q=E-u*u.T
    s4=S.simplify(sum(z**4 for z in u))
    s6=S.simplify(sum(z**6 for z in u))
    c=s4/3
    v3=K*S.Matrix([z**3 for z in u])/(3*L)
    w3=S.simplify(-(E+A+u*u.T).inv()*Q*v3)
    assert S.simplify(u.dot(w3))==0
    assert S.simplify(-w3-A*w3-Q*v3)==S.zeros(n,1)
    v5=S.simplify(K*S.Matrix([u[j]**2*w3[j] for j in range(n)])/L-K*S.Matrix([z**5 for z in u])/(60*L))
    d=S.simplify(u.dot(v5))
    assert S.simplify(d - sum(u[j]**3*w3[j] for j in range(n))+s6/60)==0
    w5=S.simplify((E+A+u*u.T).inv()*(3*c*w3-Q*v5))
    assert S.simplify(3*c*w3-w5-A*w5-Q*v5)==S.zeros(n,1)
    B=S.simplify((2*d+3*c*c)/(2*c))
    return A,w3,w5,c,d,B

K1=S.Matrix([[2]])
r=model(K1,S.Integer(2),S.Matrix([1]))
assert r[3]==S.Rational(1,3) and r[4]==-S.Rational(1,60) and r[5]==S.Rational(9,20)
K2=S.Matrix([[2,1],[1,2]])
r2=model(K2,S.Integer(3),S.Matrix([1/S.sqrt(2),1/S.sqrt(2)]))
assert r2[3]==S.Rational(1,6) and r2[5]==S.Rational(9,40)
K3=S.Matrix([[2,1,0],[1,2,1],[0,1,2]])
r3=model(K3,2+S.sqrt(2),S.Matrix([S.Rational(1,2),1/S.sqrt(2),S.Rational(1,2)]))
assert r3[3]==S.Rational(1,8) and S.simplify(r3[5]-(17-S.sqrt(2))/96)==0

# Test the proposed two-term logarithmic law on the 4-vertex path.
u=np.array([float(z) for z in [S.Rational(1,2),1/S.sqrt(2),S.Rational(1,2)]])
K=np.array(K3,float)
L=2+2**.5
b=(17-2**.5)/96
z=np.array([.40,.05,.25])  # local lift near the phase-opposition equilibrium
snap={}
for j in range(1,350001):
    z=z-(2/L)*K@np.sin(z)
    if j in (10000,30000,100000,300000):
        a=float(u@z)
        snap[j]=1/a**2-j/4-b*log(j)
assert all(np.isfinite(x) for x in snap.values())
# Deviations approach a common finite limit, rather than growing linearly or logarithmically.
assert abs(snap[300000]-snap[100000])<0.01,(snap,r3[5])
print('VERIFY_OK symbolic_graphs=3 cubic_and_quintic_center_invariance=3 critical_P4_log='+str(r3[5])+' numerical_sums='+str(snap))
