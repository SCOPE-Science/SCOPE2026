"""Reproducible symbolic and independent quadrature checks of a copula's directed rank-dependence identities."""
from __future__ import annotations
import math
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

z=sp.symbols('z',positive=True)
b=z/(z+1)
# Squared conditional CDF integrated over the conditioning variable.
V_given_U_low=2*z*sp.Symbol('v',nonnegative=True)/(2*z+1)
v=sp.Symbol('v',nonnegative=True)
V_given_U_high=v*v+z*z*(1-v)**2/(1+2*z)
xi_vu=sp.factor(6*(sp.integrate(V_given_U_low-v*v,(v,0,b))+
                   sp.integrate(V_given_U_high-v*v,(v,b,1))))
J=1-sp.Integer(2)/(z+2)+1/(2*z+3)
xi_uv=sp.factor(6*((1-b/2)*J)-2)
assert sp.simplify(xi_vu-2*z*z/((z+1)*(2*z+1)))==0
assert sp.simplify(xi_uv-2*z/(2*z+3))==0
D=sp.factor(xi_uv-xi_vu)
assert sp.simplify(D-2*z/((z+1)*(2*z+1)*(2*z+3)))==0
assert sp.simplify(sp.diff(D,z) + 2*(8*z**3+12*z**2-3)/((z+1)**2*(2*z+1)**2*(2*z+3)**2))==0
for t in [0.125,0.4396926207859084,1.,2.5,10.]:
    bb=t/(t+1)
    def F_v_given_u(u, vv):
        r=1-u
        if vv < bb*r: return 0.
        if vv <= bb: return 1-(bb*r/vv)**t
        return 1-(1+t)*(1-vv)*r**t
    def F_u_given_v(u, vv):
        r=1-u
        if vv < bb*r: return 0.
        if vv <= bb: return 1-(bb*r/vv)**(1+t)
        return 1-r**(1+t)
    # Adaptive quadrature with true conditional CDFs, splitting their support and formula boundaries.
    def integrate_Fsq_vu(vv):
        start=max(0.,1-vv/bb) if vv<=bb else 0.
        return quad(lambda u:F_v_given_u(u,vv)**2,start,1.,epsabs=2e-11)[0]
    def integrate_Fsq_uv(vv):
        start=max(0.,1-vv/bb) if vv<=bb else 0.
        return quad(lambda u:F_u_given_v(u,vv)**2,start,1.,epsabs=2e-11)[0]
    got_vu=6*(quad(integrate_Fsq_vu,0.,bb,epsabs=2e-10)[0]+quad(integrate_Fsq_vu,bb,1.,epsabs=2e-10)[0])-2
    got_uv=6*(quad(integrate_Fsq_uv,0.,bb,epsabs=2e-10)[0]+quad(integrate_Fsq_uv,bb,1.,epsabs=2e-10)[0])-2
    expected_vu=2*t*t/((1+t)*(1+2*t))
    expected_uv=2*t/(2*t+3)
    assert abs(got_vu-expected_vu)<5e-8,(t,got_vu,expected_vu)
    assert abs(got_uv-expected_uv)<5e-8,(t,got_uv,expected_uv)
    print(f'theta={t:.12f}: xi(V|U)={got_vu:.12f}, xi(U|V)={got_uv:.12f}, gap={got_uv-got_vu:.12f}')
r=brentq(lambda t:8*t**3+12*t*t-3,0.,1.)
assert 0.43969 < r < 0.43970
assert sp.factor(sp.diff(D,z)).subs(z,0.1)>0
assert sp.factor(sp.diff(D,z)).subs(z,1)<0
assert D.subs(z,r)>D.subs(z,.439)
print('sharp maximum theta =',format(r,'.15f'),'Delta =',format(float(D.subs(z,r)),'.15f'))
print('ALL CHECKS PASSED')
