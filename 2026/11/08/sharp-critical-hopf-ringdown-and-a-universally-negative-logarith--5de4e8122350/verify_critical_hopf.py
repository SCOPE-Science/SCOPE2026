#!/usr/bin/env python3
"""Independent algebraic and finite-trajectory checks of the displayed critical Hopf coefficients."""
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp

theta=s.symbols('theta',real=True)
w,q=s.symbols('w q',positive=True)
c,z=s.cos(theta),s.sin(theta)
A=-q*c**3-w*c*c*z+c*z*z
B=-q*c**4
C=(1+q)*c*c*z+w*c*z*z
D=q*c**3*z

def avg(expr):
    return s.simplify(s.integrate(s.expand_trig(expr),(theta,0,2*s.pi))/(2*s.pi))
U=s.integrate(s.expand_trig(A),theta)/w
U=U-avg(U)
assert avg(A)==0 and avg(C)==0 and avg(D)==0
assert s.simplify(avg(B)+3*q/8)==0
assert s.simplify(avg(A*C)+w*q/8)==0
assert s.simplify(avg(U*C)-(w*w-5*q*q-4*q+1)/(48*w))==0
assert s.simplify(avg(C*C)-(w*w+q*q+2*q+1)/16)==0
mu=s.factor(avg(B)-avg(A*C)/w)
nu=s.factor(avg(U*C)-avg(C*C)/w)
assert s.simplify(mu+q/4)==0
assert s.simplify(nu+(w*w+4*q*q+5*q+1)/(24*w))==0

for a,eps in [(0.5,1.0),(0.3,0.7)]:
    ph=1/(2-a)
    V=(1-ph)*(1-a)
    omega=(V/eps)**0.5
    qq=ph/eps
    chi=-(omega**2+4*qq**2+5*qq+1)/(12*omega*qq)
    horizon=16000 if eps==1 else 10000
    times=np.linspace(0,horizon,30001)
    def ode(t,y):
        X,Z=y
        u,v=1+X,V+eps*omega*Z
        return [u*((1-ph*u)*(u-a)-v)/eps, v*(u-1)/(eps*omega)]
    solution=solve_ivp(ode,(0,horizon),[0.09,0.027],t_eval=times,rtol=3e-9,atol=2e-11,method='DOP853')
    assert solution.success
    X,Y=solution.y
    radii=X*X+Y*Y
    angles=np.unwrap(np.arctan2(Y,X))
    for frac in [0.60,0.85,1.0]:
        idx=int((len(times)-1)*frac)
        observed=times[idx]*radii[idx]
        assert abs(observed-2/qq)<0.25,(a,eps,observed,2/qq)
    residual=angles-omega*times-chi*np.log(np.maximum(times,1))
    ix=np.searchsorted(times,horizon*.65)
    iy=np.searchsorted(times,horizon*.95)
    assert abs(residual[iy]-residual[ix])<0.26,(a,eps,residual[ix],residual[iy])
print('VERIFY_OK exact_trig_means=7 exact_radial_and_phase_coefficients=2 finite_parameter_cases=2 negative_phase_sign=1')
