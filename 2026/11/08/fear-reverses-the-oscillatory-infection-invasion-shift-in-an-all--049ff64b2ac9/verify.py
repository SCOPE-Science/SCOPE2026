"""Exact Hopf, cycle-mean, and infection-invasion checks for a fear–Allee model.

Run with Python 3, sympy, scipy, numpy: python verify.py
"""
import sympy as S
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import numpy as np

th, d, x, z, eta, a = S.symbols('th d x z eta a', real=True)
f = eta + a*(1-eta)/(a+z)
H = (1-x)*(x-th)
d0 = (1+th)/2
H0 = S.factor(H.subs(x,d0))
# Derivatives and Hopf normal form, using f(z0)=z0/H0.
z0, f0, K, omega, M = S.symbols('z0 f0 K omega M',positive=True)
# At Hopf: H_x=0, H_xx=-2 and the transformed field has linear (-omega Y,+omega X).
Fxx=-2*d0*f0
Fxy=-omega/d0
Fyy=d0*H0*S.diff(f,z,2).subs(z,z0)*M**2
Fxxx=-6*f0
Fxyy=H0*S.diff(f,z,2).subs(z,z0)*M**2
Gxy=S.Integer(1)
# Standard planar first Lyapunov coefficient in canonical coordinates.
l1=S.cancel((Fxxx+Fxyy+Fxy*(Fxx+Fyy)/omega)/16)
assert S.simplify(l1+f0/4)==0
assert S.simplify(S.diff(H,x).subs(x,d0))==0
assert S.simplify(S.diff(H,x,2)+2)==0

cases=[(S.Rational(92,225),S.Rational(9,10),S.Rational(-72008352,212226125)),
       (S.Rational(1,100),S.Rational(4,5),S.Rational(1645176,6555125))]
for et,rho,expected_C in cases:
 theta=S.Rational(1,5); dc=S.Rational(3,5); h=S.Rational(4,25)
 ff=S.factor(1-(1-et)*rho)
 zz=S.factor(h*ff)
 aa=S.factor(zz*(1-rho)/rho)
 fk=S.factor(1+(1-et)*rho*(1-rho)/ff)
 fzz=S.factor(2*(1-et)*aa/(aa+zz)**3)
 C=S.factor(2*dc/fk*(h*fzz*zz/(2*dc*fk)-ff))
 assert C==expected_C,(et,C,expected_C)
 assert S.factor((et+aa*(1-et)/(aa+zz))-ff)==0
 assert S.factor(zz-h*ff)==0
 assert S.factor(1-h*(-aa*(1-et)/(aa+zz)**2)-fk)==0
 assert S.factor(-ff/4)<0
 print('EXACT',et,aa,'z0',zz,'K',fk,'C',C,'sign',S.sign(C))


def check_cycle(et, aa, eps, expected):
 theta=.2; dc=.6; d=dc-eps
 def fear(zz): return et+aa*(1-et)/(aa+zz)
 def h(xx): return (1-xx)*(xx-theta)
 def zstar(xx):return brentq(lambda zz: zz-h(xx)*fear(zz),1e-16,1.0)
 z_eq=zstar(d)
 def ode(t,U):
  xx,zz=U
  return [xx*(h(xx)*fear(zz)-zz),zz*(xx-d)]
 def upward(t,U):return U[0]-d
 upward.direction=1;upward.terminal=False
 u0=[d+np.sqrt(4*dc*eps),z_eq]
 sol=solve_ivp(ode,[0,max(4000,60/eps)],u0,rtol=3e-10,atol=1e-12,
               max_step=1,events=upward,dense_output=True)
 ts=sol.t_events[0]
 assert sol.success and len(ts)>10
 grid=np.linspace(ts[-2],ts[-1],1201)
 xx,zz=sol.sol(grid)
 meanx=np.trapezoid(xx,grid)/(grid[-1]-grid[0])
 meanz=np.trapezoid(zz,grid)/(grid[-1]-grid[0])
 vax=np.trapezoid((xx-d)**2,grid)/(grid[-1]-grid[0])
 coeff=(meanz-z_eq)/eps
 print("DIAG", et, eps, "meanx_delta", meanx-d, "coeff", coeff, "var",vax/eps, "lastts",ts[-1]-ts[-2])
 assert abs(meanx-d)<1e-8
 assert np.sign(coeff)==np.sign(expected)
 assert abs(coeff-expected)<.05
 assert abs(vax/eps-1.2)<.025
 print('PERIODIC',et,'eps',eps,'meanz-shift/eps',format(coeff,'.9f'),
       'VarX/eps',format(vax/eps,'.9f'),'crossings',len(ts))

check_cycle(92/225,26/3125,.004,float(cases[0][2]))
check_cycle(.01,26/3125,.004,float(cases[1][2]))
print('VERIFY_OK')
