"""Finite independent diagnostics for the analytic Hermite strip phase theorem.
Run: python checker.py.  The all-parameter proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import erf
import sympy as sp

def h(t,a):
    u=2*a*t
    return u/math.tanh(u)-t*t

def p(t,g):
    return (g+t*t)*math.exp(-t*t)/(math.sqrt(math.pi)*(g+0.5))

def mass(t,a,g):
    b=t+a; c=t-a
    return (erf(b)-erf(c))/2-(b*math.exp(-b*b)-c*math.exp(-c*c))/(2*math.sqrt(math.pi)*(g+0.5))

def outer(tmin,a,g):
    ts=np.linspace(max(tmin,1.e-7),a+7,3001)
    yy=np.array([h(float(t),a)-a*a-g for t in ts])
    roots=[brentq(lambda t: h(t,a)-a*a-g,ts[i],ts[i+1]) for i in range(len(ts)-1) if yy[i]*yy[i+1]<0]
    return roots[-1] if roots else None

a,t,g=sp.symbols('a t g', positive=True)
u=sp.symbols('u')
assert sp.series(u/sp.tanh(u),u,0,6).removeO()==1+u**2/sp.Integer(3)-u**4/sp.Integer(45)
assert sp.simplify((1-g)*4/sp.Integer(3)-1)==(1-4*g)/3
assert sp.simplify((16/sp.Integer(45))*(sp.Rational(3,4))**2)==sp.Rational(1,5)
assert abs(2*1.5/(math.exp(3)-1))<.25
for gg in [0.05,0.10,0.125,0.20,0.24]:
    ac=math.sqrt(1-gg)
    def delta(aa):
        tm=outer(1.e-7,aa,gg)
        return mass(tm,aa,gg)-mass(0,aa,gg) if tm is not None else -1
    u0=ac+.005
    while delta(u0)>0:u0+=.005
    astar=brentq(delta,ac,u0,xtol=1.e-13)
    tt=outer(1.e-7,astar,gg)
    assert astar>ac and tt>0 and abs(delta(astar))<1e-11
    assert p(astar+tt,gg)<p(astar,gg)
    assert delta((ac+astar)/2)>0
    assert delta((astar+u0)/2)<0
    print('gamma=%.3f, w=%.6f, a_c=%.9f, a_star=%.12f, t_star=%.12f' % (gg,2*gg/(1+2*gg),ac,astar,tt))
# Check continuous and tricritical scaling near a_c.
for gg, power in [(0.4,.5),(0.25,.25)]:
    ac=math.sqrt(1-gg)
    eps=1.e-5 if gg==.4 else 1.e-7
    aa=math.sqrt(ac*ac-eps)
    tt=outer(1.e-7,aa,gg)
    predicted=math.sqrt(3*eps/(4*gg-1)) if gg>.25 else (5*eps)**.25
    assert abs(tt/predicted-1)<.02,(gg,tt,predicted)
print('PASS: exact symbolic coefficients, five jumps, and both critical exponents')
