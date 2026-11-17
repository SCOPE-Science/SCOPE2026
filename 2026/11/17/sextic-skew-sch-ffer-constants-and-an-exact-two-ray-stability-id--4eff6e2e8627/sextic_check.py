#!/usr/bin/env python3
"""Standalone exact-algebra and finite-sample checks for a sextic skew-transform identity.
Python 3; SymPy is needed only for the symbolic portion. Finite checks are not the proof.
"""
from fractions import Fraction
import math
import random
import sympy as sp

u, v, z = sp.symbols('u v z', real=True)
a = 15*z*z*(1+z*z)
b = 6*z*(1-z**4)
F = sp.expand((u+z*v)**6+(z*u-v)**6)
assert sp.expand(F - (1+z**6)*(u**6+v**6) - a*(u**4*v**2+u**2*v**4) - b*(u**5*v-u*v**5)) == 0
L = sp.symbols('L',nonzero=True,real=True)
rem = sp.factor(((1+z**6+L)*(u**6+v**6)-F - L*(u*u+v*v)*(u*u-v*v-b*u*v/(2*L))**2)*L)
assert sp.expand(rem - (L*L-a*L-b*b/4)*u*u*v*v*(u*u+v*v)) == 0
assert sp.expand((sp.Matrix([[1,z],[z,-1]])**2-(1+z*z)*sp.eye(2))) == sp.zeros(2)
print('Symbolic sextic expansion, square-deficit identity and involution: OK')

random.seed(1103)
checks = 0
for j in range(3000):
    tau=random.choice([1/30,1/7,1/2,2/3,1,1.13,1.5,2.7,10.0])
    A=15*tau**2*(1+tau**2)
    B=6*tau*(1-tau**4)
    lam=(A+math.hypot(A,B))/2
    gamma=B/(2*lam)
    M6=1+tau**6+lam
    x=random.uniform(-2,2)
    y=random.uniform(-2,2)
    f=(x+tau*y)**6+(tau*x-y)**6
    defect=M6*(x**6+y**6)-f
    square=lam*(x*x+y*y)*(x*x-y*y-gamma*x*y)**2
    assert math.isclose(defect,square,abs_tol=4e-7*(1+M6)*(1+abs(x)**6+abs(y)**6),rel_tol=2e-11)
    assert defect >= -1e-7*(1+M6)*(1+abs(x)**6+abs(y)**6)
    checks+=1
print(f'Pointwise identity random floating samples: {checks} OK')

for tau in (0.1,.25,.5,1.0,1.4,2.0,3.0):
    A=15*tau*tau*(1+tau*tau)
    B=6*tau*(1-tau**4)
    lam=(A+math.hypot(A,B))/2
    gamma=B/(2*lam)
    s=(math.sqrt(gamma*gamma+4)-gamma)/2
    aa=(1/(1+s**6))**(1/6)
    bb=(s**6/(1+s**6))**(1/6)
    x=(aa,bb)
    y=(s*aa,-bb/s)
    assert math.isclose(sum(i**6 for i in x),1,rel_tol=3e-14)
    assert math.isclose(sum(i**6 for i in y),1,rel_tol=3e-14)
    p=sum((xi+tau*yi)**6+(tau*xi-yi)**6 for xi,yi in zip(x,y))/2
    n6=1+tau**6+lam
    assert math.isclose(p,n6,rel_tol=3e-13)
    # For the lower bound, normalize the transform of an upper extremizer.
    normup=n6**(1/6)
    lowx=[(xi+tau*yi)/normup for xi,yi in zip(x,y)]
    lowy=[(tau*xi-yi)/normup for xi,yi in zip(x,y)]
    assert math.isclose(sum(z**6 for z in lowx),1,rel_tol=3e-13)
    assert math.isclose(sum(z**6 for z in lowy),1,rel_tol=3e-13)
    low=sum((xi+tau*yi)**6+(tau*xi-yi)**6 for xi,yi in zip(lowx,lowy))/2
    assert math.isclose(low,(1+tau*tau)**6/n6,rel_tol=5e-13)
print('Exact 2-atom max/min extremizer construction, seven parameter values: OK')

for tau in (.5,1,2):
    A=15*tau*tau*(1+tau*tau);B=6*tau*(1-tau**4)
    lam=(A+math.hypot(A,B))/2;g=B/(2*lam)
    K2=1+g*g/4
    # eigenvectors of the trace-free quadratic form have squared distance r^2/2 to zero cone.
    angle=.5*math.atan2(-g,2)
    x,y=math.cos(angle),math.sin(angle)
    q=x*x-y*y-g*x*y
    assert math.isclose(q*q, K2, rel_tol=1e-12)
print('Sharp pointwise distance-to-equality-cone coefficient: OK')
