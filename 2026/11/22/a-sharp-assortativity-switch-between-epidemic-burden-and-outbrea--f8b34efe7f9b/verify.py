#!/usr/bin/env python3
"""Self-contained symbolic consistency and illustrative numerical checks for a two-type SEIR limit."""
import sympy as s
import numpy as np
from math import isclose
U,V,e,c=s.symbols('U V e c',positive=True)
a=(1+e)/2;b=(1-e)/2
A=c*s.Matrix([[U*a,U*V*b],[b,V*a]])
B=A.T
h=(U-1)*(V+1)/((U+1)*(V-1))
DA=c*((U-1)*(V+1)-e*(U+1)*(V-1))/2
DB=c*(-(U+1)*(V-1)+e*(U-1)*(V+1))/2
assert s.simplify((A*s.ones(2,1))[0]-(A*s.ones(2,1))[1]-DA)==0
assert s.simplify((B*s.ones(2,1))[0]-(B*s.ones(2,1))[1]-DB)==0
assert s.simplify(DA.subs(e,h))==0
assert s.simplify(DB.subs(e,1/h))==0
assert s.simplify((A-B.T))==s.zeros(2)
assert s.simplify(h.subs({U:2,V:3})-s.Rational(2,3))==0
assert s.simplify(DA.subs({U:2,V:3,c:1,e:s.Rational(2,3)}))==0
assert s.simplify(DB.subs({U:2,V:3,c:1,e:s.Rational(2,3)}))<0
assert s.simplify((s.Matrix([[a,b],[b,a]])*s.ones(2,1))-s.ones(2,1))==s.zeros(2,1)

def fixed(M,kind):
    x=np.array([0.92,0.92])
    for _ in range(25000):
        y=M@x
        xnew= -np.expm1(-y) if kind=='burden' else y/(1+y)
        if max(abs(xnew-x)) < 2e-14:
            return xnew
        x=xnew
    raise RuntimeError('No convergence in positive fixed-point iteration')

samples=0
for UU,VV in [(2,3),(3,2),(2,2),(1.2,2.7),(3.8,1.1)]:
    for cc in [1.0,1.5,3.0]:
        for ee in [0.0,0.1,0.35,0.5,0.625,0.75,0.875,0.98]:
            aa=(1+ee)/2; bb=(1-ee)/2
            Mm=cc*np.array([[UU*aa,UU*VV*bb],[bb,VV*aa]],float)
            zz=fixed(Mm,'burden'); tt=fixed(Mm.T,'seeding')
            sza=(Mm[0].sum()-Mm[1].sum())
            stb=(Mm.T[0].sum()-Mm.T[1].sum())
            assert min(*zz,*tt)>0
            if abs(sza)>1e-8: assert np.sign(zz[0]-zz[1])==np.sign(sza)
            if abs(stb)>1e-8: assert np.sign(tt[0]-tt[1])==np.sign(stb)
            samples+=1

M1=np.array([[2*(1+2/3)/2,2*3*(1-2/3)/2],[(1-2/3)/2,3*(1+2/3)/2]],float)
z=fixed(M1,'burden');t=fixed(M1.T,'seeding')
assert abs(z[0]-z[1])<1e-12 and t[1]-t[0]>0.1
print('PASS: exact row-sum algebra, reciprocity, matrix transpose, balanced contacts')
print('PASS: %d numerical pairs of fixed points match the analytic signs' % samples)
print('PASS: exact rational example has burden tie and strict seeding separation')
