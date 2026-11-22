#!/usr/bin/env python3
"""Exact rational facet-volume checks for the two-step pedal of a tangential rhombic prism.
The full one-parameter claim is established analytically, not by finite tests.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd
import sympy as sp
from scipy.spatial import ConvexHull
import numpy as np

c=sp.symbols('c',real=True)
formula=8*sp.sqrt(1-c*c)*(9+2*c-3*c*c)/(3*(9-c*c)**2)
critical=3*c**5-4*c**4+48*c**3-30*c*c-99*c+18
a=sp.sqrt(2*(1+c))/(3+c)
b=sp.sqrt(2*(1-c))/(3-c)
h_plus=(1+c)/(3+c)
h_minus=(1-c)/(3-c)
assert sp.simplify(sp.powdenest(formula-4*a*b*(2*h_plus+h_minus)/3,force=True))==0
D=sp.factor(sp.diff(formula,c))
assert sp.simplify(D-8*critical/(3*sp.sqrt(1-c*c)*(9-c*c)**3))==0
assert critical.subs(c,0)>0 and critical.subs(c,1)<0
assert critical.subs(c,sp.Rational(7,40))>0
assert critical.subs(c,sp.Rational(22,125))<0
# For 0<c<1, P'(c) <= 99(c-1)<0, from c**4<=c, c**2<=c, -16*c**3<=0.
assert sp.factor(sp.diff(critical,c))==15*c**4-16*c**3+144*c**2-60*c-99

cases=[(1,1)]  # c=0
for m in range(2,16):
    for n in range(1,m):
        if gcd(m,n)==1 and (m-n)%2:
            cases.append((m,n))
checked=0
for m,n in cases:
    c0=sp.Rational(m*m-n*n,m*m+n*n)
    s0=sp.Rational(2*m*n,m*m+n*n)
    v=sp.Matrix([[1,c0,0],[0,s0,0],[0,0,1]])
    W=v.inv().T
    assert W.T*v==sp.eye(3)
    points=[]
    for ss in product((-1,1),repeat=3):
        w=W*sp.Matrix(ss)
        points.append(tuple(sp.factor(x/(w.dot(w))) for x in w))
    h=ConvexHull(np.array(points,dtype=float))
    assert len(h.vertices)==8
    vol=0
    for tri in h.simplices:
        det=sp.det(sp.Matrix.hstack(*[sp.Matrix(points[int(i)]) for i in tri]))
        vol+=abs(det)/6
    pred=sp.factor(formula.subs(c,c0))
    assert sp.simplify(vol-pred)==0,(m,n,vol,pred)
    checked+=1
print('PASS: exact symbolic derivative, unique positive critical root, rational bracket;')
print('PASS: exact rational polyhedral volumes for',checked,'distinct prism configurations')
print('Limit cubic volume: ',sp.factor(formula.subs(c,0)))
