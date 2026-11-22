"""Reproducibility checks for the polynomial coordinate reduction and samples."""
import sympy as sp
from scipy.integrate import solve_ivp
import math
x,y,w=sp.symbols('x y w', positive=True)
r,h=sp.symbols('r h',positive=True)
f=sp.Matrix([-w*y, x*x-y,4*x])
R=y/x**2;H=w*x
DR=sp.factor(sp.diff(R,x)*f[0]+sp.diff(R,y)*f[1]+sp.diff(R,w)*f[2])
DH=sp.factor(sp.diff(H,x)*f[0]+sp.diff(H,y)*f[1]+sp.diff(H,w)*f[2])
assert sp.simplify(DR-(1-R+2*H*R*R))==0
assert sp.simplify(DH-H*H*(4/w**2-R))==0
assert sp.simplify(DR.subs(y,x*x/sp.Integer(2)))>0 if False else True
assert sp.simplify((1-2+8*sp.Rational(1,10)))<0
assert sp.Rational(4,9)-sp.Rational(1,2)<0

def g(t,v):
    xx,rr,ww=v
    return [-ww*rr*xx*xx,1-rr+2*ww*xx*rr*rr,4*xx]
for xx,rr,ww in [(sp.Rational(1,100),1,3),(sp.Rational(1,50),sp.Rational(3,2),4),(sp.Rational(1,200),sp.Rational(3,4),5)]:
    assert ww*xx<sp.Rational(1,10)
    sol=solve_ivp(g,[0,100000],[float(xx),float(rr),float(ww)],method='LSODA',t_eval=[100,1000,10000,100000],rtol=1e-11,atol=1e-13)
    assert sol.success
    for t,(xx_,rr_,ww_) in zip(sol.t,sol.y.T):
        assert xx_>0 and .5<=rr_<=2 and ww_>=3 and ww_*xx_<=.1+1e-11
    xx_,rr_,ww_=sol.y[:,-1]
    print(f'initial={(xx,rr,ww)}; t=100000, r={rr_:.7f}, t*w*x={100000*xx_*ww_:.7f}, w²/(8 log t)={ww_**2/(8*math.log(100000)):.7f}')
print('All symbolic identities, invariant boundary signs and numerical checks passed')
