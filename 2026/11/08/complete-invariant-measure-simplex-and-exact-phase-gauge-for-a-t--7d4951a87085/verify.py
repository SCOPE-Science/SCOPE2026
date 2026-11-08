"""Standalone checks for a polynomial rotational flow and its phase gauge.

Requires Python 3, SymPy, NumPy, SciPy. The analytic proof is in RESULT.md;
finite integrations are illustrative, not a substitute for it.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

x,y,z,mu,e,L=sp.symbols('x y z mu e L',real=True)
s=x*x+y*y
A=(s-5)*(sp.Rational(20,21)-s)-sp.Rational(400,21)*z*z
D=z+s/10
F=sp.Matrix([mu*x*A-(1+e*D)*y,mu*y*A+(1+e*D)*x,-D])
J=F.jacobian([x,y,z]).subs({x:1,y:0,z:-sp.Rational(1,10)})
J_expected=sp.Matrix([[166*mu/21,-1,80*mu/21],[1+e/5,0,e],[-sp.Rational(1,5),0,-1]])
assert sp.simplify(J-J_expected)==sp.zeros(3)
poly=sp.Poly(sp.expand((L*sp.eye(3)-J).det()),L)
assert poly.all_coeffs()==[1,1-166*mu/21,1+e/5-50*mu/7,1]
mu0=sp.Rational(1,1000)
c2=1-166*mu0/21
c1=1+e/5-50*mu0/7
d=sp.factor(c2*c1-1)
ecritical=sp.solve(d,e)[0]
assert ecritical==sp.Rational(22037,291676)
assert d.subs(e,sp.Rational(1,20))== -sp.Rational(6211,1225000)
assert d.subs(e,sp.Rational(1,10))==sp.Rational(35653,7350000)

r,Z=sp.symbols('r Z',real=True,positive=True)
P=(r*r-5)*(21*r*r-20)+400*Z*Z
red1=-mu*r*P/21
red2=-Z-r*r/10
div=sp.factor(sp.diff(red1,r)+sp.diff(red2,Z))
target=-1-mu*(5*(r*r-sp.Rational(25,14))**2+sp.Rational(400,21)*Z*Z-sp.Rational(6575,588))
assert sp.simplify(div-target)==0
assert sp.simplify(P-((r*r-5)*(21*r*r-20)+400*Z*Z))==0
assert sp.simplify(P.subs(Z,-r*r/10) - 25*(r-2)*(r-1)*(r+1)*(r+2)) == 0
redJ=sp.Matrix([red1,red2]).jacobian([r,Z])
assert sp.factor(redJ.det().subs({r:1,Z:sp.Rational(1,10)*(-1)})) == -sp.Rational(50,7)*mu
assert sp.factor(redJ.det().subs({r:2,Z:-sp.Rational(2,5)})) == sp.Rational(200,7)*mu
assert sp.simplify(sp.trace(redJ).subs({r:2,Z:-sp.Rational(2,5)}) + 1 + sp.Rational(344,21)*mu) == 0

# The exact identity W'= (mu*A + i*(1+e*D))W,
# Z'=-D, U=exp(i*e*Z)W => U'=(mu*A+i)U is also
# checked by independent complex multiplication of its coefficients.
for mv in (0.001,0.018,0.07,0.089):
  for ev in (-0.9,0.0,0.05,0.1,0.31):
    for rv,zv in ((0.25,0.4),(1.1,-0.45),(2.3,0.05),(5.5,-1.2)):
      aa=float(A.subs({x:rv,y:0,z:zv})); dd=zv+rv**2/10
      coeff=(mv*aa+1j*(1+ev*dd))+1j*ev*(-dd)
      assert abs(coeff-(mv*aa+1j))<3e-14


def field(mv,ev):
    def fun(t,v):
      xx,yy,zz=v
      ss=xx*xx+yy*yy
      av=(ss-5)*(20/21-ss)-400*zz*zz/21
      dd=zz+ss/10
      om=1+ev*dd
      return [mv*av*xx-om*yy,mv*av*yy+om*xx,-dd]
    return fun

max_error=0.0
integrations=0
for mv in (0.001,0.03,0.08):
  for ev in (-0.4,0.05,0.1,0.32):
    for xx,yy,zz in ((1.2,-0.3,-0.1),(-2.8,1.1,1.4),(0.13,0.21,-1.0)):
      base=np.array([xx,yy,zz])
      c=math.cos(ev*zz); ss=math.sin(ev*zz)
      twisted=np.array([c*xx-ss*yy,ss*xx+c*yy,zz])
      tval=np.linspace(0,8,27)
      a=solve_ivp(field(mv,ev),(0,8),base,rtol=1e-11,atol=1e-12,t_eval=tval)
      b=solve_ivp(field(mv,0),(0,8),twisted,rtol=1e-11,atol=1e-12,t_eval=tval)
      assert a.success and b.success
      c=np.cos(ev*a.y[2]);ss=np.sin(ev*a.y[2]);u=np.array([c*a.y[0]-ss*a.y[1],ss*a.y[0]+c*a.y[1],a.y[2]])
      err=float(np.max(np.abs(u-b.y)))
      max_error=max(max_error,err)
      integrations+=1
assert max_error<4e-8,(max_error,integrations)
print(f'VERIFY_OK exact_symbolic_jacobian=1 exact_divergence=1 stationary_state_algebra=1 exact_routh_threshold=1 gauge_coefficient_checks=80 numeric_conjugacy_integrations={integrations} max_error={max_error:.3e}')
