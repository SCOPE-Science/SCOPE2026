"""Exact rational spot checks for two-mode range-sketch residual comparison.
Mathematical identities and a separate analytic Gaussian integral appear in RESULT.md.
"""
from fractions import Fraction as F
from math import sin,cos,pi,sqrt,isclose

def residual(a,b,x,y):
    return a*b*(x+y)/(a*x+b*y)

n=0
for ia in range(2,16):
 for ib in range(1,ia):
  a,b=F(ia),F(ib)
  rr=2*a*b/(a+b)
  for ix in range(1,8):
   for iy in range(1,8):
    x,y=F(ix),F(iy)
    avg=(residual(a,b,x,y)+residual(a,b,y,x))/2
    excess=a*b*(a-b)**2*(x-y)**2/(2*(a+b)*(a*x+b*y)*(a*y+b*x))
    assert avg-rr == excess
    assert excess>=0
    n+=1
for ia in range(2,20):
 for ib in range(1,ia):
  a,b=float(ia),float(ib)
  ntheta=50000
  numerical=sum(a*b/(a*cos((k+.5)*2*pi/ntheta)**2+b*sin((k+.5)*2*pi/ntheta)**2) for k in range(ntheta))/ntheta
  assert isclose(numerical,sqrt(a*b),rel_tol=2e-12,abs_tol=2e-12)
  n+=1
print(f'PASS {n} exact-rational and numerical cases')
