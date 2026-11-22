"""Reproducibility checks for high-noise two-point Brownian trajectory recovery.

Requires Python 3, sympy, scipy, numpy. Symbolic equalities exact;
finite numerical checks illustrate and do not replace the analytic proof.
"""
import sympy as sp
import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar

x,y,z,u,v,t=sp.symbols('x y z u v t', real=True)
eta=1/z
A=lambda w: w**2-sp.Rational(2,3)*w**3
C=x*y - x*y**2/2 - x**3/6
B=sp.factor(y*A(x)+x*A(y)-2*x*C)
assert sp.simplify(B - x*(x-y)*(x**2-x*y+2*y**2-3*y)/3)==0
S=sp.Matrix([[x+eta,x],[x,y+eta]])
T=sp.Matrix([[A(x),C],[C,A(y)]])
F0=sp.factor(sp.trace(S.inv()*T))
F=sp.cancel((z*(A(x)+A(y))+z*z*B)/(1+z*(x+y)+z*z*x*(y-x)))
assert sp.simplify(F0-F)==0

G2=sp.factor(sp.diff(F,z,2).subs(z,0)/2)
Hx=sp.diff(G2,x).subs({x:1,y:1})
Hy=sp.diff(G2,y).subs({x:1,y:1})
assert Hx==-1 and Hy==-sp.Rational(1,3)
assert (Hy-Hx)==sp.Rational(2,3)
# Exact identities showing that an optimal design cannot be repeated or hit the terminal endpoint.
split=sp.factor((sp.diff(F,y)-sp.diff(F,x)).subs(y,x))
assert sp.simplify(split-2*z*z*x*x*(3-2*x)/(3*(1+2*z*x)**2))==0
D=1+z*(x+1)+z*z*x*(1-x)
terminal=-z*z*(1+z*x*(1-x)**2*(x+2)+z*z*x*x*(1-x)**3)/(3*D*D)
assert sp.simplify(sp.diff(F,y).subs(y,1)-terminal)==0
assert sp.simplify(sp.diff(F,x).subs({x:1,y:1})+z*z/(1+2*z)**2)==0

scaled=sp.series(F.subs({x:1-u*z,y:1-v*z}),z,0,5).removeO().expand()
assert sp.simplify(scaled.coeff(z,1)-sp.Rational(2,3))==0
assert sp.simplify(scaled.coeff(z,2)+sp.Rational(4,3))==0
assert sp.simplify(scaled.coeff(z,3)-(-u*u+u-v*v+v/3+sp.Rational(8,3)))==0
assert sp.simplify(scaled.coeff(z,3).subs({u:sp.Rational(1,2),v:sp.Rational(1,6)})-sp.Rational(53,18))==0

F_rep=sp.cancel(2*z*A(t)/(1+2*z*t))
rep_scaled=sp.series(F_rep.subs(t,1-u*z),z,0,4).removeO().expand()
assert sp.simplify(rep_scaled.coeff(z,3)-(-2*u*u+sp.Rational(4,3)*u+sp.Rational(8,3)))==0
assert rep_scaled.coeff(z,3).subs(u,sp.Rational(1,3))==sp.Rational(26,9)
assert sp.Rational(53,18)-sp.Rational(26,9)==sp.Rational(1,18)

f=sp.lambdify((x,y,z),F,'numpy')
rep=sp.lambdify((t,z),F_rep,'numpy')
for noise in (10,30,100,300,1000):
    zz=1/noise
    fit=differential_evolution(lambda q:-f(min(q),max(q),zz),[(0,1),(0,1)],
                               tol=1e-11,popsize=17,seed=2026,polish=True)
    lo,hi=sorted(fit.x)
    rr=minimize_scalar(lambda q:-rep(q,zz),bounds=(0,1),method='bounded', options={'xatol':1e-12})
    assert 0<lo<hi<1
    assert f(lo,hi,zz)>rep(rr.x,zz)
    assert abs(noise*(1-lo)-.5)<6/noise
    assert abs(noise*(1-hi)-1/6)<4/noise
    assert abs(noise**3*(f(lo,hi,zz)-rep(rr.x,zz))-1/18)<0.15 if noise>=100 else True
    print('eta',noise,'x',round(lo,10),'y',round(hi,10),
          'scaled_offsets',round(noise*(1-lo),7),round(noise*(1-hi),7),
          'replication_gain',f'{noise**3*(f(lo,hi,zz)-rep(rr.x,zz)):.7f}')
print('ALL SYMBOLIC IDENTITIES PASS; numerical checks passed')
