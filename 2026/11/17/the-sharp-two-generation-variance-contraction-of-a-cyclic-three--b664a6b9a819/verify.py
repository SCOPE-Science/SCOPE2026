"""Exact symbolic and finite sample verification for a cyclic quadratic population map.

Run with Python 3 and sympy installed: python verify.py.
The infinite-domain inequality follows from the analytic proof, not finite tests.
"""
import sympy as S

x,y=S.symbols('x y',real=True)
z=1-x-y
xx=(x,y,z)
p2=S.expand(x*y+y*z+z*x)
p3=S.expand(x*y*z)
V=lambda v: tuple(S.expand(sum(a*a for a in v)/3+2*v[i]*v[(i+1)%3]) for i in range(3))
v1=V(xx)
v2=V(v1)
Q=lambda v:S.expand(sum((t-S.Rational(1,3))**2 for t in v))
var0,var1,var2=Q(xx),Q(v1),Q(v2)
p,q=S.symbols('p q',real=True)
pv=S.Rational(1,3)-S.Rational(4,3)*p**2+4*q
qv=(16*p**3-12*p**2-72*p*q+216*q**2+36*q+1)/27
poly2=S.factor(S.Rational(8,3)*pv**2-8*qv)
assert S.expand(var0-(S.Rational(2,3)-2*p2))==0
assert S.expand(var1-(S.Rational(8,3)*p2**2-8*p3))==0
assert S.expand(var2-poly2.subs({p:p2,q:p3}))==0
assert S.simplify(S.diff(poly2,q)+S.Rational(32,9)*(8*p**2-6*p+12*q+1))==0
a=S.symbols('a',real=True)
rho_a=S.factor((poly2/(S.Rational(2,3)-2*p)).subs({p:2*a-3*a*a,q:a*a*(1-2*a)}))
assert S.factor(rho_a-S.Rational(16,9)*a**2*(6*a*a-2*a-1)**2)==0
rho_edge=S.factor((poly2/(S.Rational(2,3)-2*p)).subs(q,0))
assert S.factor(rho_edge-S.Rational(16,9)*p*p*(1-2*p)**2/(1-3*p))==0
astar=(2+S.sqrt(22))/18
rho=S.simplify(rho_a.subs(a,astar))
assert S.simplify(rho-(57968+10912*S.sqrt(22))/531441)==0
assert S.simplify(S.diff(rho_a,a).subs(a,astar))==0
assert S.simplify(S.diff(rho_a,a).subs(a,S.Rational(1,3)))>0
assert S.simplify(S.diff(rho_a,a).subs(a,S.Rational(1,2)))<0
assert S.simplify(rho_a.subs(a,S.Rational(1,2))-S.Rational(1,9))==0
assert S.simplify(rho_a.subs(a,S.Rational(1,3))-S.Rational(16,81))==0
assert S.simplify(var2.subs({x:astar,y:astar})-rho*var0.subs({x:astar,y:astar}))==0
for denom in (7,11,17):
 for i in range(denom+1):
  for j in range(denom-i+1):
   if 3*i==denom and 3*j==denom:continue
   point={x:S.Rational(i,denom),y:S.Rational(j,denom)}
   d0=var0.subs(point)
   assert d0>0
   assert var2.subs(point)<=rho*d0
   assert var1.subs(point)<=d0
print('MAMUROV_SHARP_TWO_STEP_VARIANCE_OK exact_symbolic_checks=PASS rational_grid_cases=285')
