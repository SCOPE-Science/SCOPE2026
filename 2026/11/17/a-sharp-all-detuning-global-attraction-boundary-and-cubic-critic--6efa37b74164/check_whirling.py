#!/usr/bin/env python3
"""Reproduce algebraic identities and finite illustrations for Miles' averaged string flow.

Requires sympy, scipy, numpy.  Numerical checks illustrate rather than prove the
claims for all parameter values and all times.
"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

x,y,z,w,ga,al,de,Q=sp.symbols('x y z w gamma alpha Delta Q',real=True)
E=x*x+y*y+z*z+w*w
J=z*y-w*x
K=z*x+w*y
om=de-sp.Rational(3,2)*E
X=-ga*x+om*y+J*z
Y=-ga*y-om*x+J*w-al
Z=-ga*z+om*w-J*x
W=-ga*w-om*z-J*y
assert sp.expand(2*(x*X+y*Y+z*Z+w*W)+2*ga*E+2*al*y)==0
assert sp.expand(2*(z*Z+w*W)+2*ga*(z*z+w*w)+2*J*K)==0
assert sp.expand(J*J+K*K-(x*x+y*y)*(z*z+w*w))==0
print('energy_and_transverse_identities=3')

p=Q*(ga**2+(de-sp.Rational(3,2)*Q)**2)
qc=4*sp.sqrt(3)*ga/9
dc=sp.sqrt(3)*ga
ac2=16*sp.sqrt(3)*ga**3/27
for expr in [p-ac2,sp.diff(p,Q),sp.diff(p,Q,2)]:
    assert sp.simplify(expr.subs({Q:qc,de:dc}))==0
assert sp.diff(p,Q,3)==sp.Rational(27,2)
assert sp.simplify(sp.Rational(16,27)*sp.sqrt(3)-2)<0
print('cusp_triple_root=1')

# One sample strictly beyond the cusp demonstrates an exact three-root phase.
poly=sp.Poly(sp.expand(p.subs({ga:1,de:sp.Rational(9,5)})-sp.Rational(109,100)),Q)
assert poly.count_roots(0,sp.oo)==3
print('three_planar_roots=1')

r=3**sp.Rational(-1,4)
xx=-r/sp.sqrt(3); yy=-r
acc=4/3**sp.Rational(5,4)
u,v=sp.symbols('u v',real=True)
xv=xx-u/sp.sqrt(3)+v
yv=yy+u
hh=sp.sqrt(3)-sp.Rational(3,2)*(xv*xv+yv*yv)
uv=-yv-hh*xv-acc
vv=(-xv+hh*yv)+uv/sp.sqrt(3)
a=2*3**sp.Rational(3,4)/3
uc=sp.series(uv.subs(v,a*u*u),u,0,4).removeO().expand()
vc=sp.series(vv.subs(v,a*u*u),u,0,3).removeO().expand()
assert sp.simplify(uc.coeff(u,2))==0
assert sp.simplify(uc.coeff(u,3)+2/sp.sqrt(3))==0
assert sp.simplify(vc.coeff(u,2))==0
assert sp.simplify(uv.subs({u:0,v:0}))==0
print('critical_center_cubic=1')

# Finite-time illustration near the nonhyperbolic equilibrium; not an infinite proof.
for sign in [-1,1]:
    u0=sign*0.18
    v0=float(a)*u0*u0-float(sp.Rational(4,3))*u0**3
    y0=float(yy)+u0
    x0=float(xx)-u0/np.sqrt(3)+v0
    def rhs(t,p):
        xr,yi=p
        hh=np.sqrt(3)-1.5*(xr*xr+yi*yi)
        return [-xr+hh*yi,-yi-hh*xr-float(acc)]
    result=solve_ivp(rhs,[0,8000],[x0,y0],rtol=1e-10,atol=1e-12,
                     t_eval=[8000],method='DOP853',max_step=25)
    assert result.success
    empirical=8000*(result.y[1,-1]-float(yy))**2
    assert abs(empirical-np.sqrt(3)/4)<0.003
print('critical_relaxation_examples=2')
print('VERIFY_OK')
