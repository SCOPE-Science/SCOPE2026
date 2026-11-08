"""Standalone illustrative consistency checks for cubic sphere flow."""
import math
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

u,v,w,a,b,c=sp.symbols('u v w a b c', positive=True)
du=2*u*(a*v-b*w)
dv=2*v*(-a*u+c*w)
dw=2*w*(b*u-c*v)
assert sp.expand(du+dv+dw)==0
assert sp.expand(c*du/u+b*dv/v+a*dw/w)==0
S=a+b+c
J=sp.Matrix([du.subs(w,1-u-v),dv.subs(w,1-u-v)]).jacobian([u,v])
J0=sp.simplify(J.subs({u:c/S,v:b/S}, simultaneous=True))
assert sp.simplify(sp.trace(J0))==0
assert sp.simplify(sp.det(J0)-4*a*b*c/S)==0
print('SPHERE_CUBIC_EXACT_INTEGRAL_AND_CENTER_OK')

def period(A,B,C,h):
    t=brentq(lambda t:t**(B+C)*(1-2*t)**A-h,1e-14,0.25,xtol=1e-15)
    def rhs(_,point):
        U,V=point
        W=1-U-V
        return [2*U*(A*V-B*W),2*V*(-A*U+C*W)]
    def cross(_,point):return point[0]-point[1]
    cross.direction=0
    sol=solve_ivp(rhs,(0,200),(t,t),rtol=5e-11,atol=5e-14,max_step=0.02,events=cross)
    ev=sol.t_events[0]
    assert len(ev)>2
    return ev[2]
for aa,bb,cc,hh,tol in [(1,1,1,1e-8,.002),(2,3,5,1e-16,.002)]:
    T=period(aa,bb,cc,hh)
    predicted=(aa+bb+cc)/(2*aa*bb*cc)*math.log(1/hh)
    assert abs(T/predicted-1)<tol,(T,predicted)
    print(f'SPHERE_CUBIC_PERIOD_ASYMPTOTIC_OK ({aa},{bb},{cc}) T={T:.10g} prediction={predicted:.10g}')
print('SPHERE_CUBIC_CHECK_OK')
