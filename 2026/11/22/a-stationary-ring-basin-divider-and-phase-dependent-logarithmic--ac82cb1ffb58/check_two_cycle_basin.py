#!/usr/bin/env python3
"""Reproduction checks for the stated polynomial-flow identities.

This program tests identities and selected numerical cases. The proof of
all-parameter and infinite-time assertions is contained in RESULT.md.
"""
import math
import sympy as sp
from scipy.integrate import quad, solve_ivp

x, y, eps = sp.symbols('x y eps', real=True)
u, v = x-2, y-2
s = u*u+v*v
h = 16*s*s-25*s+9
hx, hy = sp.diff(h,x),sp.diff(h,y)
fx = x*y*(-h*hx-eps*hy)
fy = x*y*(-h*hy+eps*hx)
ds = sp.expand(2*u*fx+2*v*fy)
angular = sp.expand(u*fy-v*fx)
assert sp.simplify(ds+4*x*y*s*h*(32*s-25))==0
assert sp.simplify(angular-2*eps*x*y*s*(32*s-25))==0
s_star=sp.Rational(25,32)
z=sp.symbols('z')
assert (16*z*z-25*z+9).subs(z,s_star)==-sp.Rational(49,64)
assert sp.simplify(98*s_star-sp.Rational(1225,16))==0
assert {sp.Rational(9,16),sp.Integer(1)}==set(sp.solve(16*sp.Symbol('z')**2-25*sp.Symbol('z')+9,sp.Symbol('z')))
for s0 in [sp.Rational(9,16),sp.Integer(1),sp.Rational(25,32)]:
    a=float(s0); r=math.sqrt(a)
    q=quad(lambda t: 1.0/((2+r*math.cos(t))*(2+r*math.sin(t))),0,2*math.pi,epsabs=1e-12)[0]
    closed=8*math.pi/((8-a)*math.sqrt(4-a))
    assert abs(q-closed)<1e-10
    if a!=float(s_star):
        period=q/(2*7*3.0)
        exact=4*math.pi/(7*3*(8-a)*math.sqrt(4-a))
        assert abs(period-exact)<1e-12
        exponent=-4*math.pi*a*7/3
        assert exponent<0
# Test the radial ejection from the equilibrium circle against the predicted
# phase-dependent leading logarithmic crossing clock at fixed angle.
star=float(s_star)
rstar=math.sqrt(star)
eta=.04
for phi in [0.0,1.1,3.0]:
    e=.25
    initial_ang=phi
    w=(2+rstar*math.cos(phi))*(2+rstar*math.sin(phi))
    coeff=16/(1225*w)
    delays=[]
    for delta in [2e-4,2e-5,2e-6]:
        s0=star+delta
        state=[2+math.sqrt(s0)*math.cos(initial_ang),2+math.sqrt(s0)*math.sin(initial_ang)]
        def field(t,z):
            X,Y=z; U,V=X-2,Y-2; zsq=U*U+V*V
            H=16*zsq*zsq-25*zsq+9
            g=2*(32*zsq-25)
            return [X*Y*(-H*g*U-e*g*V),X*Y*(-H*g*V+e*g*U)]
        def event(t,z):return (z[0]-2)**2+(z[1]-2)**2-star-eta
        event.terminal=True;event.direction=1
        r=solve_ivp(field,[0,2],state,events=event,rtol=1e-11,atol=1e-12,max_step=.0003)
        assert r.status==1
        delays.append(r.t_events[0][0])
    observed=(delays[2]-delays[1])/math.log(10)
    assert abs(observed/coeff-1)<.025,(phi,observed,coeff)
print('TWO_CYCLE_BASIN_CHECK_OK')
