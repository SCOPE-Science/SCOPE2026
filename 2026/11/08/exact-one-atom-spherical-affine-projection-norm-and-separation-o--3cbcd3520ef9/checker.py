"""Exact checks and independent integral comparisons for the one-atom spherical affine projector."""
from fractions import Fraction
import math
import random
import sympy as S
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
r,t=S.symbols('r t',real=True)
q=1+S.Rational(2,3)*r*t-r*(S.Rational(2,3)-r)*t**2
u=1-r*t
M=(9*q+u*u)/(6*S.sqrt(q))
P=S.expand((9*q-u*u)*S.diff(q,t)-4*r*q*u)
R=S.expand(P*P-144*r*r*q**3)
assert S.factor(R.subs(t,0)) == -S.Rational(1280,9)*r*r
assert S.factor(S.Poly(R,t).LC()) == 16*r**4*(3*r-2)**2*(4*r-3)**2/9
assert S.factor(q.subs(t,-2)-(1-2*r)**2)==0
assert S.factor(q.subs(t,4)-(1-4*r)**2)==0
assert S.factor((9*q-u*u).subs(t,-2)-8*(1-r)*(1-4*r)) == 0
assert S.factor((9*q-u*u).subs(t,4)-8*(1-4*r)**2) == 0
assert S.simplify(M.subs(t,0))==S.Rational(5,3)
assert S.simplify(S.diff(M-r*t,t).subs(t,0))==-S.Rational(8,9)*r
assert S.simplify(S.diff(M+r*t,t).subs(t,0))==S.Rational(10,9)*r
D=S.factor(P.subs(t,-2)/(12*(1-2*r)**3)-r)
assert S.factor(D-8*r*(r-1)**2*(6*r-1)/(9*(2*r-1)**3))==0
assert S.simplify(S.diff(M-r*t,t,2).subs({r:S.Rational(1,6),t:-2}))==S.Rational(5,48)
assert S.simplify((M+r*t).subs({r:S.Rational(1,6),t:S.Rational(5,4)})-(M-r*t).subs({r:S.Rational(1,6),t:-2}))==-S.Rational(113,72)+S.Rational(2795,41832)*S.sqrt(581)
assert float(-S.Rational(113,72)+S.Rational(2795,41832)*S.sqrt(581))>0.04
assert S.factor(S.diff(M+r*t,r).subs(r,0)-2*t*(5-2*t)/9)==0
assert S.factor(S.diff(M-r*t,r).subs(r,0)+4*t*(t+2)/9)==0
b_neg=36*q*(2+t/4)**2-(9*q+u*u)**2
b_pos=36*q*(2-t/4)**2-(9*q+u*u)**2
assert S.factor(b_neg.subs(r,S.Rational(1,4))+(t-4)*(t+2)*(8*t*t+29*t+44)/8)==0
assert S.factor(b_pos.subs(r,S.Rational(1,4))+(t-4)*(8*t**3-15*t**2-42*t+88)/8)==0
print('EXACT_KERNEL_ROOT_AND_PHASE_IDENTITIES_OK')
# Check kernel against direct support-integral formula independently (normal form based on moment covariance).
def F(w,zz):
 rr=w/(1+3*w);tt=1+3*zz
 qq=1+(2/3)*rr*tt-rr*(2/3-rr)*tt*tt
 return (9*qq+(1-rr*tt)**2)/(6*math.sqrt(qq))+rr*abs(tt)
def integrand_real(w,zz):
 a=(1+2*w-3*w*zz)/((1-w)*(1+3*w))
 bb=3*math.sqrt((1+3*w)**2*(1-zz*zz)+(zz-w)**2)/((1-w)*(1+3*w))
 return (1-w)*quad(lambda U:abs(a+bb*U)/2,-1,1,points=[-a/bb],epsabs=2e-12)[0]+w*abs((1+3*zz)/(1+3*w))
for w in (0.04,1/3,0.4,0.8,0.94):
 for z in (-1,-.8,-1/3,0,.2,.7,1):
  assert abs(F(w,z)-integrand_real(w,z))<5e-10,(w,z,F(w,z),integrand_real(w,z))
print('INDEPENDENT_SPHERE_INTEGRATION_OK 35')
# Verify finite real-root formula against dense/global optimized sampling.
for wr in (S.Rational(1,10),S.Rational(1,3),S.Rational(1,2),S.Rational(4,5),S.Rational(9,10)):
 rr=wr/(1+3*wr)
 roots=S.nroots(R.subs(r,rr),maxsteps=100)
 ts=[-2.,0.,4.]+[float(S.re(v)) for v in roots if abs(float(S.im(v)))<1e-8 and -2<float(S.re(v))<4]
 Rf=lambda a:F(float(wr),(a-1)/3)
 exact=max(Rf(a) for a in ts)
 samples=max(Rf(-2+6*i/5000) for i in range(5001))
 assert exact>=samples-1e-9 and exact-samples<2e-5,(wr,exact,samples)
print('DEGREE_SIX_CRITICAL_ROOT_ENUMERATION_CHECKED 5')
print('ALL_SPHERICAL_ATOM_CHECKS_OK')
