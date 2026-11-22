"""Rational-arithmetic checks for the inverse-fiber theorem.
Run: python check.py . These finite tests supplement the analytical proof.
"""
from fractions import Fraction as Q
from math import sqrt, isclose

def A(a,y): return 1+a/(1+y*y)
def forward(a,b,c,d,x,y): return x*A(a,y)+b, y+c*x+d
def phi(a,U,y): return y+U-U*a/(1+a+y*y)
def jac(a,c,x,y): return 1+a/(1+y*y)+2*a*c*x*y/(1+y*y)**2
def phi_y(a,U,y): return 1+2*U*a*y/(1+a+y*y)**2
count=0
for ai in [Q(-4,5),Q(-1,2),Q(1,5),Q(1),Q(2),Q(7,2)]:
 for bi in [Q(0),Q(-3,5)]:
  for ci in [Q(1),Q(-2),Q(3,7)]:
   for di in [Q(0),Q(5,4)]:
    for xi in [Q(-4,3),Q(0),Q(9,7)]:
     for yi in [Q(-2),Q(0),Q(1,3),Q(5,2)]:
      X,Y=forward(ai,bi,ci,di,xi,yi)
      U,V=ci*(X-bi),Y-di
      assert V==phi(ai,U,yi)
      assert xi==U/(ci*A(ai,yi))
      assert jac(ai,ci,xi,yi)==A(ai,yi)*phi_y(ai,U,yi)
      count+=1
# a=2, U=4, V=1: inverse cubic -(y+1)^3.
def poly_coeff(a,U,V):
 # (V-U-y)*(1+a+y*y)+U*a, coefficients descending
 return (Q(-1), V-U, -(1+a), (V-U)*(1+a)+U*a)
assert poly_coeff(Q(2),Q(4),Q(1))==tuple(map(Q,[-1,-3,-3,-1]))
assert poly_coeff(Q(2),Q(-4),Q(-1))==tuple(map(Q,[-1,3,-3,1]))
# At a=2, U=5, V=3/2, the inverse cubic has three real distinct roots:
# -(2*y+?); exactly -1/2*(y+1)*(2*y*y+5*y+1).
assert poly_coeff(Q(2),Q(5),Q(3,2))==(Q(-1),Q(-7,2),Q(-3),Q(-1,2))
for y in [-1,(-5+sqrt(17))/4,(-5-sqrt(17))/4]:
 assert abs(float(phi(Q(2),Q(5),y))-1.5)<1e-12
# Numerical verification of the fold opening coefficient for several a values.
def fold_width(a,U):
 B=1+a; ss=sqrt(B/3)
 def h(y): return 1+2*U*a*y/(B+y*y)**2
 def bisect(lo,hi):
  flo=h(lo)
  for _ in range(130):
   mid=(lo+hi)/2
   if h(mid)*flo>0:lo=mid;flo=h(mid)
   else:hi=mid
  return (lo+hi)/2
 if a>0:
  left=bisect(-1e4,-ss)
  right=bisect(-ss,0)
 else:
  left=bisect(0,ss)
  right=bisect(ss,1e4)
 def f(y):return y+U-U*a/(B+y*y)
 return f(left)-f(right)
for a in [-0.8,-0.5,0.2,1,2,5]:
 B=1+a; uc=8*B*sqrt(B/3)/(3*abs(a))
 for eps in [0.003,0.001]:
  measured=fold_width(a,uc+eps)
  expected=8*sqrt(B)/9*(eps/uc)**1.5
  assert measured>0 and abs(measured/expected-1)<0.005, (a,eps,measured,expected)
print('PASS: %d exact rational forward-inverse and Jacobian identities; two exact cusp polynomials; three-preimage witness; 12 cusp-opening checks' % count)
