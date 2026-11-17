"""Independent algebraic and quadrature spot checks for a quadratic chemical center.
Requires Python 3, sympy, scipy; run: python CHECK.py.
"""
import sympy as s
import numpy as np
from scipy.integrate import quad

x,y,A,D,C,F,t=s.symbols('x y A D C F t', positive=True)
om=s.symbols('omega', positive=True)
a=(C-F)/(D-A)
yc=C/A
X=x*(A*x-A*y+C)
Y=x*(D*x-A*y+F)
w=A/om*(x-y+yc)
u=x-a
H=s.simplify(u*u+w*w)
# Enforce omega**2=A*(D-A): check coefficients after eliminating om^2.
dH=s.factor(s.diff(H,x)*X+s.diff(H,y)*Y)
assert s.simplify(dH.subs(om**2,A*(D-A)))==0
# Directly verify the rational pulse under the center relation.
q=1+(om*a*t)**2
xp=2*a/q
yp=yc+2*a*(1+(om**2*a/A)*t)/q
for lhs, rhs in [(s.diff(xp,t), xp*(A*xp-A*yp+C)),
                 (s.diff(yp,t), xp*(D*xp-A*yp+F))]:
    resid=s.cancel(lhs-rhs)
    resid=s.factor(resid.subs(D,A+om**2/A))
    assert s.simplify(resid)==0, resid
# Check center parameter recovery and sample quadratures.
A0,D0,C0,F0=1.0,2.0,1.0,0.0
om0=np.sqrt(A0*(D0-A0));a0=(C0-F0)/(D0-A0);yc0=C0/A0
for R in [0.12,0.45,0.92]:
    E=R*R
    formula=2*np.pi/(om0*np.sqrt(a0*a0-E))
    integral=quad(lambda th:1/(om0*(a0+R*np.cos(th))),0,2*np.pi,epsabs=1e-11)[0]
    assert abs(formula-integral)<1e-9
    xmean=(2*np.pi/om0)/formula
    ymean=quad(lambda th:(a0+R*np.cos(th)+yc0+(om0/A0)*R*np.sin(th))/(om0*(a0+R*np.cos(th))),0,2*np.pi,epsabs=1e-11)[0]/formula
    assert abs(xmean-np.sqrt(a0*a0-E))<1e-9
    assert abs(ymean-(yc0+xmean))<1e-9
# Critical pulse numerical substitution and integrals.
assert abs(quad(lambda tt:2/(1+tt*tt),-np.inf,np.inf)[0]-2*np.pi)<1e-9
print('VERTICAL_HOPF_FULL_PHASE_CLOCK_AND_PULSE_OK')
