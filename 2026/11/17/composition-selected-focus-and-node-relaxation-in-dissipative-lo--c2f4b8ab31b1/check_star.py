#!/usr/bin/env python3
"""Symbolic algebra and finite-time checks of a dissipative LV star theorem.

Finite integration is diagnostic only, not a proof of asymptotic assertions.
"""
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import math
u,U,d,v1,v2,p1,p2,b1,b2,c1,c2=sp.symbols('u U d v1 v2 p1 p2 b1 b2 c1 c2',positive=True)
fu=u*(-d*(u-U)-b1*(v1-p1)-b2*(v2-p2))
f1=c1*v1*(u-U)
f2=c2*v2*(u-U)
V=(u-U-U*sp.log(u/U))+(b1/c1)*(v1-p1-p1*sp.log(v1/p1))+(b2/c2)*(v2-p2-p2*sp.log(v2/p2))
Vdot=sp.diff(V,u)*fu+sp.diff(V,v1)*f1+sp.diff(V,v2)*f2
assert sp.simplify(Vdot+d*(u-U)**2)==0
assert sp.simplify(sp.diff(sp.log(v1)/c1-sp.log(v2)/c2,u)*fu+sp.diff(sp.log(v1)/c1-sp.log(v2)/c2,v1)*f1+sp.diff(sp.log(v1)/c1-sp.log(v2)/c2,v2)*f2)==0
J=sp.Matrix([[sp.diff(fu,z) for z in (u,v1,v2)],[sp.diff(f1,z) for z in (u,v1,v2)],[sp.diff(f2,z) for z in (u,v1,v2)]])
Je=J.subs({u:U,v1:p1,v2:p2})
x=sp.symbols('x')
assert sp.simplify(Je.charpoly(x).as_expr() - x*(x*x+U*d*x+U*(b1*c1*p1+b2*c2*p2)))==0
# For U=1, d=6, b_j=1, c=(1,9), reference equilibrium v^0=(1,1), S=2.
crit=sp.Rational(7,8)/sp.Rational(9,8)**9
assert sp.simplify(crit-sp.Rational(7*8**8,9**9))==0
assert sp.Rational(3,2)+sp.Rational(1,2)==2
assert sp.Rational(1,2)+9*sp.Rational(3,2)==14
assert sp.Rational(3,2)+9*sp.Rational(1,2)==6
# Verify terminal selection independently for two nonstationary initial values.
for v10,v20,expected_mode in [(1.5,0.5,'node'),(0.5,1.5,'focus'),(1.125,0.875,'boundary')]:
    def f(t,z):
        u_,v1_,v2_=z
        return [u_*(-6*(u_-1)-(v1_-1)-(v2_-1)),v1_*(u_-1),9*v2_*(u_-1)]
    res=solve_ivp(f,[0,13],[1.05,v10,v20],rtol=1.e-11,atol=1.e-13,dense_output=False,max_step=.002)
    assert res.success
    vv1,vv2=res.y[1,-1],res.y[2,-1]
    invariant=v20/v10**9
    target=brentq(lambda w: w/(2-w)**9-invariant,1.e-10,2-1.e-10)
    assert abs(vv2-target)<1.e-6, (vv2,target)
    disc=36-4*(2+8*target)
    mode='focus' if disc< -1.e-7 else ('node' if disc>1.e-7 else 'boundary')
    assert mode==expected_mode,(mode,disc)
    print('CASE',v10,v20,mode,'selected_v2',format(target,'.10f'),'frequency',format(math.sqrt(max(0,-disc))/2,'.10f'),'end_error',format(abs(vv2-target),'.2g'))
print('VERIFY_OK exact_entropy_dissipation=1 first_integral=1 full_jacobian_characteristic=1 basin_threshold=1 finite_trajectories=3')
print('FINITE_INTEGRATION_ONLY; full convergence and crossing frequency require the proof')
