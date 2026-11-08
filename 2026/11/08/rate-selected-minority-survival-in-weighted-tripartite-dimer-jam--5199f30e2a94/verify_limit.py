#!/usr/bin/env python3
"""Symbolic first integrals, ODE integration, and Monte Carlo checks."""
import math,random
import sympy as s
from scipy.integrate import solve_ivp
x,y,r=s.symbols('x y r',positive=True)
vec={x:-2*x*y, y:-x*y-r*y*y}
F=y*x**(-r/s.Integer(2))-x**(1-r/s.Integer(2))/(2-r)
assert s.simplify((s.diff(F,x)*vec[x]+s.diff(F,y)*vec[y]).cancel())==0
F2=y/x-s.log(x)/2
assert s.simplify((s.diff(F2,x)*vec[x]+s.diff(F2,y)*vec[y]).subs(r,2))==0
print('PASS: both analytic first integrals differentiate to exactly zero.')

def prediction(a,b,rho):
    if abs(rho-2)<1e-10:return a*math.exp(-2*b/a)
    z=1-(2-rho)*b/a
    if rho<2 and z<=0:return 0.
    return a*z**(2/(2-rho))

def ode(a,b,rho):
    def rhs(t,v):
        x,y=v
        return [-2*x*y,-x*y-rho*y*y]
    v=solve_ivp(rhs,(0,2e5),[a,b],method='DOP853',rtol=1e-12,atol=1e-13, dense_output=False)
    return v.y[0,-1]

for a,b,rho in ((1,1,1),(1,1,1.5),(1,1,2),(1,1,3),(.5,1,1),(.5,1,1.5),(.5,1,2),(.5,1,3),(2,1,.5)):
    target=prediction(a,b,rho)
    got=ode(a,b,rho)
    assert abs(got-target)<1e-4,(a,b,rho,target,got)
    print('ODE',a,b,rho,'terminal A',round(got,8),'pred',round(target,8))
print('PASS: ODE integration matches closed-form terminal densities.')

def sim(a,b,rho,rng):
    # Each available edge has rate 1 for AB/AC, and rho for BC.
    c=b
    while True:
        ab=a*b;ac=a*c;bc=rho*b*c
        tot=ab+ac+bc
        if tot==0:return a,b,c
        q=rng.random()*tot
        if q<ab:a-=1;b-=1
        elif q<ab+ac:a-=1;c-=1
        else:b-=1;c-=1

rng=random.Random(17423)
for a,b,rho,scale,trials in ((1,1,1,500,400),(1,1,1.5,500,400),(1,1,2,500,400),(1,1,3,500,400),(.5,1,3,800,400),(2,1,.5,400,400)):
    vals=[sim(round(scale*a),round(scale*b),rho,rng)[0]/scale for _ in range(trials)]
    avg=sum(vals)/trials
    pred=prediction(a,b,rho)
    assert abs(avg-pred)<0.035,(a,b,rho,avg,pred)
    print('MonteCarlo',a,b,rho,'mean',round(avg,5),'pred',round(pred,5),'trials',trials)
print('PASS: large finite stochastic systems agree with the proven fluid limit within a declared coarse Monte Carlo tolerance.')
