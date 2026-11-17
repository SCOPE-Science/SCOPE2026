"""Supplemental numerical and symbolic cross-checks of a phase-resolved blow-up law.
This finite test is supplemental to the analytic proof in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
import sympy as sp

x,y,L,eps,omega = sp.symbols('x y L eps omega',real=True)
rad = x*x+y*y
f = rad+eps*(x*x-y*y)
P=L*x-f*x-omega*rad*y
Q=L*y-f*y+omega*rad*x
assert sp.expand((x*P+y*Q)-L*rad+rad*f)==0
assert sp.expand((x*Q-y*P)-omega*rad*rad)==0

lam,om,e=2.0,3.0,0.5
a,b=2/om,e/om
rho=lambda th: math.exp(-a*th-b*math.sin(2*th))
def wstar(th):
    integral=quad(lambda u: math.exp(-a*u-b*(math.sin(2*th)-math.sin(2*(th-u)))),0,100,epsabs=1e-12)[0]
    return 2*lam/om * integral

def w(th):
    return wstar(th)+rho(th)
def dt(th):
    # elapsed time since the finite backward blow-up (phase reference at th)
    return quad(lambda u: 1/(om*w(th-u)),0,100,epsabs=1e-13,epsrel=1e-12)[0]

for th in [-9.,-14.,-19.,-24.]:
    lhs=dt(th)*w(th)
    rhs=wstar(th)/(2*lam)
    assert abs(lhs-rhs)<5e-3, (th,lhs,rhs)

th0=-11.0
for m in [3,4,5]:
    ratio=dt(th0-(m+1)*math.pi)/dt(th0-m*math.pi)
    assert abs(ratio-math.exp(-2*math.pi/om))<0.002,(m,ratio)
assert max(wstar(t) for t in np.linspace(0,math.pi,20))-min(wstar(t) for t in np.linspace(0,math.pi,20))>0.1
assert abs(wstar(0)-wstar(math.pi))<1e-9
print('STAR_NODE_PHASE_BLOWUP_PROFILE_OK')
