"""Independent algebraic and numerical checks for two-query OU quadrature with erasures.
Run: python verify_erasure_ou.py. Requires numpy, scipy, sympy.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize

def covariance_integral(a):
    return 2*(a-1+math.exp(-a))/(a*a)

def w(a,x):
    return (2-math.exp(-a*x)-math.exp(-a*(1-x)))/a

def gain(a,p,s,t):
    assert 0<p<=1 and a>0 and 0<=s<=t<=1
    ws,wt=w(a,s),w(a,t)
    if abs(s-t)<1e-12:
        return p*(2-p)*ws*ws
    r=math.exp(-a*(t-s))
    g2=(ws*ws+wt*wt-2*r*ws*wt)/(1-r*r)
    return p*(1-p)*(ws*ws+wt*wt)+p*p*g2

def optimum(a,p):
    z=math.exp(-a/2)
    def p_of_u(u):
        return 4*z*math.sinh(u)*math.cosh(u)**2/(1-z*math.exp(-2*u)*math.cosh(u))
    u=brentq(lambda u:p_of_u(u)-p,0,a/2,xtol=1e-14)
    return .5-u/a,.5+u/a,u

a,p,u,z = sp.symbols('a p u z',positive=True,real=True)
A=1-z*sp.cosh(u)
B=1-p/sp.Integer(2)+p*sp.tanh(u)/2
# Original two-erasure gain agrees with scalar hyperbolic expression.
r=sp.exp(-2*u)
ws=2*A/a
G=2*p*(1-p)*ws**2+p**2*2*ws**2/(1+r)
H=8*p/a**2*A**2*B
assert sp.simplify(sp.expand((G-H)//(8*p*A**2/a**2)).rewrite(sp.exp))==0
# Endpoint logarithmic derivative, midpoint positive derivative, and stationarity formula.
assert sp.simplify(sp.diff(B,u)-p/(2*sp.cosh(u)**2))==0
assert sp.simplify(sp.diff(B,u,2)+p*sp.tanh(u)/sp.cosh(u)**2)==0
F=sp.factor(sp.diff(A*A*B,u))
P=4*z*sp.sinh(u)*sp.cosh(u)**2/(1-z*sp.exp(-2*u)*sp.cosh(u))
assert sp.simplify(sp.expand(F.subs(p,P)).rewrite(sp.exp))==0
# Midpoint-centering derivative identities for both posterior gains,
# with C=cosh(a*(s+t-1)/2) at a fixed half-gap u.
C=sp.symbols('C', real=True)
G1=8/a**2*((1-z*sp.cosh(u)*C)**2+z**2*sp.sinh(u)**2*(C*C-1))
G2=8/a**2*((1-z*sp.cosh(u)*C)**2/(1+r)+z**2*sp.sinh(u)**2*(C*C-1)/(1-r))
assert sp.simplify(sp.diff(G1,C)-16*z/a**2*(-sp.cosh(u)+z*C*sp.cosh(2*u)))==0
assert sp.simplify(sp.expand(sp.diff(G2,C)-16*z*sp.cosh(u)/(a*a*(1+r))*(z*C*sp.exp(u)-1)).rewrite(sp.exp))==0

checks=0
for av in (0.1,0.3,1.,2.,4.,9.):
 for pv in (0.03,0.2,0.5,0.8,1.):
    s,t,uv=optimum(av,pv)
    opt= gain(av,pv,s,t)
    assert 0<s<.5<t<1
    assert opt>gain(av,pv,.5,.5)
    assert opt>gain(av,pv,0,1)
    assert abs(gain(av,pv,s,t)-float(H.subs({a:av,p:pv,u:uv,z:math.exp(-av/2)})))<1e-10
    # Compare global continuous 2-dimensional direct optimization, plus random candidates.
    obj=lambda x:-gain(av,pv,min(x),max(x))
    rng=np.random.default_rng(721+round(av*100)+round(pv*100))
    for _ in range(16):
       pts=rng.random(2)
       assert gain(av,pv,min(pts),max(pts))<=opt+1e-9
    for init in ((.1,.8),(.25,.4),(.3,.9)):
       res=minimize(obj,np.array(init),method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':300},bounds=[(0,1),(0,1)])
       assert -res.fun<=opt+1e-7
    checks+=20
# Check small-erasure limit, and small/large correlation-length asymptotics.
for av in (.3,1.,3.):
 zval=math.exp(-av/2)
 for pv in (1e-5,3e-6):
    _,_,uv=optimum(av,pv)
    rel=uv/(((1-zval)/(4*zval))*pv)
    assert abs(rel-1)<1e-3
for pv in (.2,.5,1.):
 for av in (1e-3,3e-4):
    s,t,uv=optimum(av,pv)
    assert abs(uv/av-pv/(4*(2-pv)))<.001
 for av in (60.,90.):
    s,t,uv=optimum(av,pv)
    assert abs(uv-(av/6+math.log(2*pv)/3))<1e-4
print('PASS; symbolic identities and',checks,'numerical optimization/sampling checks')
for pv in (.2,.5,.8,1.):
 av=1
 s,t,uv=optimum(av,pv)
 print('a=1, p=',pv,'times',s,t,'gain',gain(av,pv,s,t),'variance',covariance_integral(av)-gain(av,pv,s,t),'coincident gain',gain(av,pv,.5,.5))
