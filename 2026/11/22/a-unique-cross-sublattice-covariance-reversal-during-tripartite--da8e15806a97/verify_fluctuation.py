#!/usr/bin/env python3
"""Exact verification of the Gaussian fluctuation and sign-transition formulas."""
import sympy as sp
from scipy.optimize import brentq

x1,x2,x3=sp.symbols('x1 x2 x3')
x=sp.Matrix([x1,x2,x3]); t=sp.symbols('t',positive=True)
f=sp.Matrix([-x1*(x2+x3),-x2*(x1+x3),-x3*(x1+x2)])
B=sp.zeros(3)
for i,j in [(0,1),(0,2),(1,2)]:
    v=sp.zeros(3,1);v[i]=-1;v[j]=-1
    B+=x[i]*x[j]*v*v.T
u=1/(1+2*t)
subs={x1:u,x2:u,x3:u}
J=sp.simplify(f.jacobian(x).subs(subs))
B=sp.simplify(B.subs(subs))
I=sp.eye(3);H=sp.ones(3,3);P=H/3;Q=I-P
assert sp.simplify(J+u*(I+H))==sp.zeros(3)
assert sp.simplify(B-u*u*(I+H))==sp.zeros(3)
vc=sp.Rational(2,3)*(u-u**4)
vd=sp.log(1+2*t)*u/2
C=sp.simplify(vc*P+vd*Q)
assert sp.simplify(sp.diff(C,t)-J*C-C*J.T-B)==sp.zeros(3)
assert C.subs(t,0)==sp.zeros(3)
off=sp.factor(C[0,1]); expected=(4*(1-(1+2*t)**-3)-3*sp.log(1+2*t))/(18*(1+2*t))
assert sp.simplify(off-expected)==0
h=lambda y:4*(1-y**-3)-3*__import__('math').log(y)
yroot=brentq(h,4**(1/3),10,xtol=1e-14)
troot=(yroot-1)/2
assert 1.34734526<troot<1.34734528
print('J, noise covariance, ODE, initial condition and off-diagonal formula: exact PASS')
print('Threshold time t*: %.12f' % troot)
print('Derivative numerator = 3(4-y^3)/y^4: unique positive root by unimodality')
for val in [0.1,1.,troot,2.,10.]:
    print('time=%g covariance=%+.10f'%(val,float(off.subs(t,val))))
