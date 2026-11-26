"""Finite reproducibility tests for an exact one-probe Gaussian range-finder risk theorem.
The universal proof is in RESULT.md; these checks do not certify an infinite domain.
Requires Python 3 and SymPy.
"""
from fractions import Fraction as F
from math import acos, cos, sin, sqrt, pi
import sympy as S

# Algebra: exact risk, isotropic comparison, derivative and stationary point.
a,b,r,c=S.symbols('a b r c',positive=True)
u=1+(r*r-1)*c
v=r*r+1-u
D=a*a*u+b*b*v+2*a*b*r
N=a*b*(a*b*(r*r+1)+r*(a*a+b*b))
R=N/D
Q=(c*(a*a+b*b)-b*b)*r*r+2*a*b*(2*c-1)*r+c*(a*a+b*b)-a*a
assert S.factor(a*b*D-N-a*b*(a-b)*(r-1)*((a+b)*(r+1)*c-a-b*r))==0
assert S.factor(S.diff(N,r)*D-N*S.diff(D,r)+a*b*(a-b)*(a+b)*Q)==0
assert S.factor(S.discriminant(Q,r)-4*c*(1-c)*(a*a-b*b)**2)==0
checks=3

# Exact rational cases, including all three monotonicity regions and equality.
for aa in range(2,10):
 for bb in range(1,aa):
  for rr in (F(1),F(3,2),F(2),F(7,3),F(4),F(9)):
   for cc in (F(0),F(1,20),F(1,5),F(2,5),F(1,2),F(3,4),F(1)):
    u=1+(rr*rr-1)*cc
    v=rr*rr+1-u
    den=aa*aa*u+bb*bb*v+2*aa*bb*rr
    num=aa*bb*(aa*bb*(rr*rr+1)+rr*(aa*aa+bb*bb))
    diff=F(aa*bb)-num/den
    expect=F(aa*bb*(aa-bb))*(rr-1)*((aa+bb)*(rr+1)*cc-aa-bb*rr)/den
    assert diff==expect
    checks+=1

# Exact witness: weakening or strengthening an imperfect prior changes risk order.
def rational_risk(aa,bb,rr,cc):
 u=1+(rr*rr-1)*cc
 v=rr*rr+1-u
 return F(aa*bb)*(aa*bb*(rr*rr+1)+rr*(aa*aa+bb*bb))/(aa*aa*u+bb*bb*v+2*aa*bb*rr)
assert rational_risk(3,1,F(2),F(2,5))==F(525,173)>3
assert rational_risk(3,1,F(4),F(2,5))==F(273,97)<3
checks+=2

# Independent angular integration of the one-probe estimator, not risk formula.
def angular_integral(aa,bb,rr,cc,Nstep=4096):
 ct=sqrt(float(cc)); st=sqrt(1-float(cc))
 total=0.0
 for j in range(Nstep):
  t=2*pi*(j+.5)/Nstep
  g1,g2=cos(t),sin(t)
  y1=aa*(rr*ct*g1-st*g2)
  y2=bb*(rr*st*g1+ct*g2)
  total+=aa*aa+bb*bb-(aa*aa*y1*y1+bb*bb*y2*y2)/(y1*y1+y2*y2)
 return total/Nstep
for aa,bb in ((3,1),(5,2),(6,5)):
 for rr in (1.,1.5,2.,4.,7.):
  for cc in (0.,0.125,0.4,0.5,0.7,1.):
   integral=angular_integral(aa,bb,rr,cc)
   closed=float(rational_risk(aa,bb,F(str(rr)),F(str(cc))))
   assert abs(integral-closed)<2e-10,(aa,bb,rr,cc,integral,closed)
   checks+=1

# Critical anisotropy is the only r>1 where risk rejoins isotropic baseline.
cc=F(2,5)
rc=(3-4*cc)/(4*cc-1)
assert rc==F(7,3) and rational_risk(3,1,rc,cc)==3
checks+=1

# Robust (worst-alignment) design: the minimum over r>=1 is at r=1
# or approached by the rank-one covariance limit. Finite grid tests illustrate.
for aa,bb in ((3,1),(5,2),(6,5)):
 for cc in (F(0),F(1,10),F(1,5),F(2,5),F(1,2),F(3,4),F(1)):
  limiting=F(aa*aa*bb*bb)/(aa*aa*cc+bb*bb*(1-cc))
  robust=min(F(aa*bb),limiting)
  for rr in (F(1),F(11,10),F(3,2),F(2),F(4),F(10),F(100),F(10000)):
   assert rational_risk(aa,bb,rr,cc)>=robust
   checks+=1
assert F(3*3)/(F(9)*F(2,5)+F(3,5))==F(15,7)
checks+=1

print('PASS',checks,'independent algebraic/rational/quadrature assertions')
