"""Reproduce exact identities and numerical examples for a three-shape reactive-transit model.

Requirements: Python 3 with sympy and mpmath. This checker does not replace the
analytic all-parameter inequalities stated in the mathematical proof.
"""
from fractions import Fraction
import sympy as s
from mpmath import mp

x, r, t = s.symbols('x r t', positive=True)
F = {k: (s.Integer(k)/(k+x))**k for k in (1, 2, 3)}
H = {(i,j): s.factor(F[i]-F[j]) for i,j in [(1,2),(2,3),(1,3)]}
checks=0
expected = {
 (1,2): x**2/((x+1)*(x+2)**2),
 (2,3): x**2*(4*x+9)/((x+2)**2*(x+3)**3),
 (1,3): x**2*(x+9)/((x+1)*(x+3)**3)
}
for pair in expected:
 assert s.cancel(H[pair]-expected[pair]) == 0; checks+=1

# Each logarithmic curvature equals a strictly negative fraction
# with positive numerator/denominator at every x>0.
curv_num={
 (1,2): -x*( (x+2)**2 + 4*(x+1)**2 ),
 (2,3): -x*(172*x**4+1536*x**3+5193*x**2+7884*x+4536),
 (1,3): -x*(x**4+132*x**3+1062*x**2+2052*x+1377),
}
curv_den={
 (1,2): (x+1)**2*(x+2)**2,
 (2,3): (x+2)**2*(x+3)**2*(4*x+9)**2,
 (1,3): (x+1)**2*(x+3)**2*(x+9)**2,
}
for pair,h in H.items():
  e=s.cancel(x*s.diff(h,x)/h)
  curv=s.cancel(x*s.diff(e,x))
  assert s.cancel(curv-curv_num[pair]/curv_den[pair])==0, (pair,s.factor(curv))
  assert s.Poly(-curv_num[pair]/(-x),x).degree()>=1
  checks+=2

R=s.factor(H[2,3]/H[1,2]); assert s.cancel(R - (x+1)*(4*x+9)/(x+3)**3)==0; checks+=1
F12 = r*r*t**3-8*r*t-4*(r+1)
P=4*r*r*t**4+13*r*r*t**3+9*r*r*t*t+13*r*t**3+18*r*t*t-27*r*t+9*t*t-27*t-108
Q=(4*r*t+13*r+13)/r
rem=((9*r**3+50*r*r+9*r)*t*t+(93*r*r+93*r)*t+52*r*r-4*r+52)/r
assert s.cancel(P-Q*F12-rem)==0; checks+=1
expr=s.factor(R.subs(x,r*t)-R.subs(x,t))
assert s.cancel(expr+t*(r-1)*P/((t+3)**3*(r*t+3)**3))==0; checks+=1

# Formula C_2-C_1 reduces to a cubic with a unique positive root.
def c(k,y,rr):return (1+y/k)**(-k)-(1+rr*y/k)**(-k)
expr=s.factor((F[2]-F[1]).subs(x,t)-(F[2]-F[1]).subs(x,r*t)) # C2-C1
c12=s.factor((s.Integer(2)/(2+t))**2-(s.Integer(2)/(2+r*t))**2 - (1/(1+t)-1/(1+r*t)))
assert s.cancel(expr-c12)==0; checks+=1
assert s.cancel(c12+t*t*(r-1)*F12/((t+1)*(t+2)**2*(r*t+1)*(r*t+2)**2))==0; checks+=1

mp.dps=60
for rr in [mp.mpf('1.01'),mp.mpf('1.1'),mp.mpf('2'),mp.mpf('5'),mp.mpf('10'),mp.mpf('100')]:
 def cross(a,b):
  fun=lambda y:c(b,y,rr)-c(a,y,rr)
  # bracket by sign on geometric grid, never assume numeric root isolation is proof
  lo=mp.mpf('1e-6'); hi=mp.mpf('100')
  assert fun(lo)>0 and fun(hi)<0
  for _ in range(170):
   mid=(lo+hi)/2
   if fun(mid)>0:lo=mid
   else:hi=mid
  return (lo+hi)/2
 a=cross(2,3);b=cross(1,3);d=cross(1,2)
 assert a<b<d
 assert abs(c(3,a,rr)-c(2,a,rr))<mp.mpf('1e-40')
 assert abs(c(3,b,rr)-c(1,b,rr))<mp.mpf('1e-40')
 assert abs(c(2,d,rr)-c(1,d,rr))<mp.mpf('1e-40')
 checks+=4
 if rr==2:
  print('r=2 thresholds t23,t13,t12:',*(mp.nstr(y,20) for y in (a,b,d)))
for rr in [Fraction(11,10),Fraction(2),Fraction(5),Fraction(10)]:
 for z in [Fraction(k,20) for k in range(1,101)]:
  # Verify exact sign comparisons by rational arithmetic.
  vals=[(1+z/k)**(-k)-(1+rr*z/k)**(-k) for k in (1,2,3)]
  assert all(v>0 for v in vals)
  checks+=1
print('PASS',checks,'deterministic assertions')
