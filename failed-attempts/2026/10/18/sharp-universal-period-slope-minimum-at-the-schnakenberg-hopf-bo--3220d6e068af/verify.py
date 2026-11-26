#!/usr/bin/env python3
"""Exact symbolic identities for the Schnakenberg near-Hopf period coefficient.

Requires Python 3 and SymPy. Run: python3 verify.py
The calculation checks the displayed algebra, not the analytic Hopf theorem.
"""
import sympy as sp

s, mu, m, theta = sp.symbols('s mu m theta', positive=True, real=True)
a = s * (1 - s**2 - mu) / 2
b = s * (1 + s**2 + mu) / 2
x, y, q, p = sp.symbols('x y q p', real=True)
f = a - x + x**2*y
g = b - x**2*y
J = sp.Matrix([f, g]).jacobian([x, y]).subs({x:s, y:b/s**2})
assert sp.simplify(J.trace() - mu) == 0
assert sp.simplify(J.det() - s**2) == 0

# q=x-s; p=s[(x+y)-(s+b/s^2)]; tau=s*t
xx = s+q
yy = s+b/s**2+p/s-xx
F = sp.expand((a-xx+xx**2*yy)/s)
G = sp.expand((s*((a-xx+xx**2*yy)+(b-xx**2*yy)))/s)
A = (1-3*s**2+mu)/(2*s**2)
assert sp.simplify(F - (p+(mu/s)*q+A*q**2+2*q*p/s-q**3/s+q**2*p/s**2)) == 0
assert sp.simplify(G + q) == 0
A0 = A.subs(mu, 0)
B, C, D = 2/s, -1/s, 1/s**2
q1, p1 = sp.cos(theta), -sp.sin(theta)
q2 = A0*sp.sin(2*theta)/3+B*sp.cos(2*theta)/3
p2 = -A0/2+A0*sp.cos(2*theta)/6-B*sp.sin(2*theta)/6
assert sp.trigsimp(sp.diff(q2,theta)-p2-A0*q1**2-B*q1*p1)==0
assert sp.trigsimp(sp.diff(p2,theta)+q2)==0
h = (m/s)*q1+2*A0*q1*q2+B*(q1*p2+q2*p1)+C*q1**3+D*q1**2*p1
h_cos = sp.simplify(sp.integrate(sp.expand_trig(h)*q1, (theta,0,2*sp.pi))/sp.pi)
h_sin = sp.simplify(sp.integrate(sp.expand_trig(h)*sp.sin(theta), (theta,0,2*sp.pi))/sp.pi)
assert sp.simplify(h_cos-(4*m*s**2-1)/(4*s**3))==0
N = 9*s**4-5*s**2+1
assert sp.simplify(h_sin-N/(12*s**4))==0
mstar = sp.solve(h_cos, m)[0]
omega2 = -h_sin/2
Cperiod = sp.simplify(-omega2/mstar)
assert sp.simplify(mstar-1/(4*s**2))==0
assert sp.simplify(Cperiod-N/(6*s**2))==0
assert sp.simplify(Cperiod-(1+(3*s-1/s)**2)/6)==0

# Cubic Hopf coefficient from the polynomial vector field using a
# near-identity complex change at mu=0. Its negative real part
# separately confirms the nondegenerate supercritical Hopf.
I=sp.I
from collections import defaultdict
NDEG=3
def truncate(P):
    return {k:sp.expand(v) for k,v in P.items() if v!=0 and sum(k)<=NDEG}
def add(*PP):
    d=defaultdict(lambda:sp.Integer(0))
    for P in PP:
        for k,v in P.items(): d[k]+=v
    return truncate(d)
def scale(P,c): return truncate({k:v*c for k,v in P.items()})
def mul(P,Q):
    d=defaultdict(lambda:sp.Integer(0))
    for (j,k),v in P.items():
        for (u,w),z in Q.items():
            if j+k+u+w <= NDEG: d[(j+u,k+w)] += v*z
    return truncate(d)
def power(P,n):
    out={(0,0):sp.Integer(1)}
    for _ in range(n): out=mul(out,P)
    return out
def deriv(P,i):
    return truncate({(j-1,k):j*v for (j,k),v in P.items() if j>0}) if i==0 else truncate({(j,k-1):k*v for (j,k),v in P.items() if k>0})
def star(P): return truncate({(k,j):sp.conjugate(v) for (j,k),v in P.items()})
def error(H, L):
    T=add({(1,0):1},H); Tb=star(T)
    Q=scale(add(T,Tb),sp.Rational(1,2)); P=scale(add(T,scale(Tb,-1)),1/(2*I))
    vector=add(scale(T,-I),scale(power(Q,2),A0),scale(mul(Q,P),B),scale(power(Q,3),C),scale(mul(power(Q,2),P),D))
    normal=add({(1,0):-I},L)
    chain=add(mul(deriv(T,0),normal),mul(deriv(T,1),star(normal)))
    return add(vector,scale(chain,-1))
H={}; L={}
for degree in (2,3):
    E=error(H,L)
    for (j,k),v in sorted(E.items()):
        if j+k != degree: continue
        v=sp.simplify(v)
        if j-k==1: L[(j,k)]=v
        else: H[(j,k)]=sp.simplify(-v/(I*(j-k-1)))
c21=sp.simplify(L[(2,1)])
assert sp.simplify(sp.re(c21)+1/(8*s**3))==0
assert sp.simplify(sp.im(c21)-N/(24*s**4))==0
assert all(sp.simplify(v)==0 for v in error(H,L).values())
print('CHECK_OK: trace, determinant, transformed system, Fourier resonances,')
print('supercritical cubic normal form, period coefficient, sharp bound')
