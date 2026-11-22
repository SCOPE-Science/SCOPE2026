#!/usr/bin/env python3
"""Consistency checks for a rotating cubic polynomial flow. Requires numpy, scipy, sympy."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.special import i0

x,y,lam,omega,sigma,kappa=sp.symbols('x y lam omega sigma kappa',real=True)
r2=x*x+y*y
vx=lam*x+(sigma*r2+kappa*(x*x-y*y))*x-omega*r2*y
vy=lam*y+(sigma*r2+kappa*(x*x-y*y))*y+omega*r2*x
assert sp.simplify(x*vy-y*vx-omega*r2*r2)==0
assert sp.simplify(x*vx+y*vy-lam*r2-(sigma*r2+kappa*(x*x-y*y))*r2)==0

L=1.3; O=1.7; K=0.83; B=K/O
r0=0.6; th0=0.4; R0=r0*r0

def F(t,s): return math.exp(2*s*t/O+B*math.sin(2*t))
def direct(t,z,s):
    r,th=z
    return [L*r+(s+K*math.cos(2*th))*r**3, O*r*r]

def W(t,s):
    J=quad(lambda q:1/F(q,s),th0,t,epsabs=1e-11,epsrel=1e-11)[0]
    return R0/F(th0,s)+(2*L/O)*J

def finite_time(s):
    a=2*s/O
    assert a>0
    block=quad(lambda v:math.exp(-a*v-B*math.sin(2*(th0+v))),0,math.pi,epsabs=1e-12)[0]
    tail=math.exp(-a*th0)*block/(-math.expm1(-a*math.pi))
    return math.log1p(2*L*F(th0,s)*tail/(O*R0))/(2*L)

def cycle(theta,s):
    a=2*s/O
    assert a<0
    block=quad(lambda v:math.exp(a*v+B*(math.sin(2*theta)-math.sin(2*(theta-v)))),0,math.pi,epsabs=1e-12)[0]
    return (2*L/O)*block/(-math.expm1(a*math.pi))

def profile(theta,s):
    a=2*s/O
    assert a>0
    block=quad(lambda v:math.exp(-a*v+B*(math.sin(2*theta)-math.sin(2*(theta+v)))),0,math.pi,epsabs=1e-12)[0]
    return block/(O*(-math.expm1(-a*math.pi)))

for s in [-0.3,0.0,0.18]:
    sol=solve_ivp(lambda t,z:direct(t,z,s),(0,.7),(r0,th0),rtol=2e-11,atol=2e-12,max_step=.001)
    assert sol.success
    th=sol.y[1,-1]
    exact_t=math.log(W(th,s)/(R0/F(th0,s)))/(2*L)
    assert abs(exact_t-0.7)<1e-8,(s,exact_t)

for s in [.08,.04,.01,.002]:
    asym=math.log(L*i0(B)*math.exp(B*math.sin(2*th0))/(s*R0))/(2*L)
    assert abs(finite_time(s)-asym)<.2
assert abs(finite_time(.002)-math.log(L*i0(B)*math.exp(B*math.sin(2*th0))/(.002*R0))/(2*L))<.001

for s in [-.05,-.01,-.003]:
    ratio=abs(s)*cycle(.3,s)/(L*i0(B)*math.exp(B*math.sin(.6)))
    assert abs(ratio-1)<.05,(s,ratio)

s=.31
values=np.array([profile(t,s) for t in np.linspace(0,math.pi,101)])
assert min(values)>0 and max(values)>min(values)*1.1
for t in [.1,.4,1.2,2.1]:
    h=3e-5
    derivative=(profile(t+h,s)-profile(t-h,s))/(2*h)
    rhs=(2*s/O+2*B*math.cos(2*t))*profile(t,s)-1/O
    assert abs(derivative-rhs)<1e-7,(t,derivative,rhs)

print('all checks passed')
