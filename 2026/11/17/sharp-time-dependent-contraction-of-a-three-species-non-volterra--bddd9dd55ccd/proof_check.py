"""Exact identities and numerical sanity checks for a three-component quadratic flow."""
import sympy as S
x,y,U,V,t,r0=S.symbols('x y U V t r0', real=True)
w=1-x-y
fx=(y*y+w*w)/2+2*y*w-x
fy=(x*x+w*w)/2+2*x*w-y
sub={x:(U+2)/6+V/2,y:(U+2)/6-V/2}
assert S.simplify(3*(fx+fy).subs(sub)-(-2*U-U**2/4+3*V**2/4))==0
assert S.simplify((fx-fy).subs(sub)-(-2*V+U*V/2))==0
assert S.expand(9*(x+y)**2+3*(x-y)**2-6*(x*x+y*y+(x+y)**2))==0
E=S.exp(2*t)
R=8/(1+3*E)
assert S.simplify(S.diff(R,t)+2*R-R**2/4)==0
l=16*E/(1+3*E)**2
r=8*r0/(r0+(8-r0)*E)
assert S.simplify(S.diff(r,t)+2*r-r*r/4)==0
assert S.simplify(S.diff(r,r0).subs(r0,2)-l)==0
assert S.simplify(S.diff(S.log(l),t)-(-2+R/2))==0
assert S.simplify(l.subs(t,0)-1)==0
try:
 import numpy as np
 from scipy.integrate import solve_ivp
 rng=np.random.default_rng(2026)
 def f(_,xy):
  a,b=xy; c=1-a-b
  return [0.5*(b*b+c*c)+2*b*c-a,0.5*(a*a+c*c)+2*a*c-b]
 def vect(xy):return np.r_[xy,1-sum(xy)]
 for tau in (0.15, 0.7, 1.5):
  bound=float(l.subs(t,tau))
  for _ in range(8):
   a,b=rng.dirichlet((1.,1.,1.),size=2)
   end1=solve_ivp(f,(0,tau),a[:2],rtol=1e-11,atol=1e-12).y[:,-1]
   end2=solve_ivp(f,(0,tau),b[:2],rtol=1e-11,atol=1e-12).y[:,-1]
   assert np.linalg.norm(vect(end1)-vect(end2))/np.linalg.norm(a-b)<=bound+1e-8
except ImportError:
 print('Optional numerical dependencies unavailable; exact symbolic checks still passed')
print('SHARP_NONVOLTERRA_FLOW_LIPSCHITZ_OK')
