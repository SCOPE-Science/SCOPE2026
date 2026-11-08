"""Exact algebraic identities and direct numerical area-integral checks of cubic torus flow period tails."""
import math
from scipy.integrate import quad
import sympy as sp
u,c,a = sp.symbols('u c a', positive=True, real=True)
q=a*a+u-c*(1-u*u)
assert sp.expand(q-(c*(u+1/(2*c))**2+(a*a-c-1/(4*c))))==0
r,z,theta=sp.symbols('r z theta', real=True)
x=r*sp.cos(theta);y=r*sp.sin(theta)
A=r*r-c*z*z
P=A*y;Q=-A*x
assert sp.simplify(x*P+y*Q)==0
assert sp.simplify((x*Q-y*P)/r**2+A)==0
print('EXACT_POLYNOMIAL_FLOW_AND_SQUARE_COMPLETION_OK')
a0=1.5
cs=(a0*a0+math.sqrt(a0**4-1))/2
u0=-1/(2*cs)
gamma=1-u0*u0
w=lambda u: math.sqrt((1-u*u+4*(a0*a0+u)*u*u)/(1-u*u))
J=quad(w,-1,1,epsabs=1e-11,limit=400)[0]
pred=lambda lam:2*w(u0)/(J*math.sqrt(cs))*(math.sqrt(max(0,2*math.pi+gamma*lam))-math.sqrt(max(0,-2*math.pi+gamma*lam)))
for lam in (-10,-2,0,2,10):
 for t in (10000,1000000):
  cc=cs+lam/t
  delta=2*math.pi/t
  f=a0*a0-cc-1/(4*cc)
  hi=max(0,(delta-f)/cc)
  lo=max(0,(-delta-f)/cc)
  v=-1/(2*cc)
  if hi==0:val=0.
  else:
   sh=math.sqrt(hi); sl=math.sqrt(lo)
   val=(quad(w,v-sh,v-sl,epsabs=1e-11)[0]+quad(w,v+sl,v+sh,epsabs=1e-11)[0])/J
  print('lambda',lam,'t',t,'scaled_tail',round(val*math.sqrt(t),9),'limit',round(pred(lam),9))
print('CROSSOVER_FINITE_CHECK_OK')
