#!/usr/bin/env python3
"""Finite algebra and trajectory cross-checks for a massive segment with linear density.

Run: python check_impact.py
Requires numpy and scipy; finite tests are not an infinite-time proof.
"""
import math
import numpy as np
from scipy.integrate import quad, solve_ivp

G=1.0
c=0.35
r0=0.12

def potential_forces(x,r):
    p=math.hypot(1-x,r);m=math.hypot(1+x,r)
    S=math.asinh((1-x)/r)+math.asinh((1+x)/r)
    integral=(1+c*x)*S+c*(p-m)
    fx=c*S-(1+c)/p+(1-c)/m
    fr=-(1+c*x)*((1-x)/p+(1+x)/m)/r+c*r*(1/p-1/m)
    return integral,fx,fr

def quad_forces(x,r):
    f=lambda s: (1+c*s)/((s-x)**2+r*r)**1.5
    val=quad(lambda s:(1+c*s)/math.sqrt((s-x)**2+r*r),-1,1,epsabs=1e-11,points=[x])[0]
    fx=quad(lambda s:f(s)*(s-x),-1,1,epsabs=1e-10,points=[x])[0]
    fr=-r*quad(f,-1,1,epsabs=1e-9,points=[x])[0]
    return val,fx,fr

for x,r in [(0.21,.4),(-.35,.2),(.11,.06),(.53,.03)]:
    u,v=potential_forces(x,r),quad_forces(x,r)
    assert np.allclose(u,v,rtol=1e-9,atol=1e-9),(x,r,u,v)

# Integrate using logarithmic distance z=log(r0/r), with exact autonomous equations.
def rhs(z,y):
    x,v,w,t=y;r=r0*math.exp(-z)
    _,fx,fr=potential_forces(x,r)
    return [-r*v/w,-r*fx/w,-r*fr/w,-r/w]
sol=solve_ivp(rhs,(0,27),(0.,.05,-1.,0.),method='DOP853',rtol=3e-12,atol=3e-13,dense_output=True,max_step=.06)
assert sol.success
xstar,vstar,_,T=sol.y[:,-1]
assert abs(xstar)<1
H=.5*(.05**2+(-1.)**2)-potential_forces(0,r0)[0]
A=4*(1+c*xstar)
B=(1+c*xstar)*math.log(4*(1-xstar*xstar))-2*c*xstar
C=2*H+2*B-vstar*vstar
errors=[]
for z in (12,16,20,24):
    x,v,w,t=sol.sol(z)
    r=r0*math.exp(-z);L=math.log(1/r)
    _,fx,fr=potential_forces(x,r)
    # Exact kinetic finite-part limit and logarithmic tangential force.
    errC=abs((w*w-A*L)-C)
    errForce=abs(fx/(2*c*L)-1)
    errors.append((z,errC,errForce))
assert errors[-1][1]<1e-7
assert errors[-1][2]<0.014
assert errors[-1][2]<errors[0][2]
print('VERIFY_OK force_quadratures=4 impact_trajectory=1 checkpoints=4')
print('linear_density',c,'contact_x',round(xstar,12),'terminal_axial_speed',round(vstar,12))
print('A',round(A,12),'C',round(C,12),'finite_part',round(B,12))
for z,ec,ef in errors: print('z',z,'finite_part_abs_error',f'{ec:.3g}','relative_tangent_log_error',f'{ef:.3g}')
print('FINITE_CHECK_ONLY analytical limits require the proof in RESULT.md')
