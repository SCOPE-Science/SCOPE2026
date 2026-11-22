#!/usr/bin/env python3
"""Direct numerical geometry, exact polynomial identity and CDF checks.
Requires Python 3.10+ and sympy (only for exact differentiation).
"""
import math
from fractions import Fraction as F
from math import comb
import random
import sympy as S

B = [
 ['6','6','6','6'],
 ['79/8','191/24','97/24','17/8'],
 ['223/14','214/21','33/14','3/7'],
 ['351/14','263/21','47/42','0'],
 ['268/7','512/35','12/35','0'],
 ['394/7','334/21','0','0'],
 ['552/7','320/21','0','0'],
 ['104','32/3','0','0'],
 ['128','0','0','0'],
]
B = [[F(s) for s in row] for row in B]
assert len(B)==9 and all(len(row)==4 for row in B)
assert all(v>=0 for row in B for v in row)
assert all(B[0][j]>0 for j in range(4))

def coeff_poly(d,x):
 c=2*x-1
 return -(20*c**3*d**3-4*c**3*d+4*c**2*d**6-12*c**2*d**4-40*c**2*d**2+c*d**7-19*c*d**5+31*c*d**3+35*c*d-d**8+5*d**6+7*d**4-21*d**2-6)

def bernstein(d,x):
 return sum(B[i][j]*comb(8,i)*d**i*(1-d)**(8-i)*comb(3,j)*x**j*(1-x)**(3-j) for i in range(9) for j in range(4))

# Exact interpolation equality, combined with degree at most (8,3), is a polynomial identity.
for i in range(9):
 for j in range(4):
  d=F(i,8); x=F(j,3)
  assert coeff_poly(d,x)==bernstein(d,x)

# Symbolic derivative: J^2 = r^2(W-r^2)(W+4r)^2/W^2.
d,c=S.symbols('d c',real=True)
r=(1-d**2)/2
W=1+d**2-2*d*c
J2=r*r*(W-r*r)*(W+4*r)**2/W**2
D=(1-d*d)*W*(3-d*d-2*d*c)*(3+6*d*d-d**4-8*d*c)
assert S.cancel(S.diff(J2,d)/J2 + 8*d*coeff_poly(d,(1+c)/2)/D)==0


def setup(a):
 r=(1-a*a)/2
 low=math.sqrt((1-a)**2-r*r)
 high=math.sqrt((1+a)**2-r*r)
 midmax=2*r*high/(1+a)**2
 midmin=2*r*low/(1-a)**2
 assert low < midmax < midmin < high
 def area_t(t): return r*t*(1+4*r/(r*r+t*t))
 return r, low,midmax,midmin,high,area_t

def area(a,theta):
 r=(1-a*a)/2
 t=math.sqrt(1+a*a-2*a*math.cos(theta)-r*r)
 return r*t*(1+4*r/(r*r+t*t))

def cdf(a,z):
 r,lo,cm,cM,hi,j=setup(a)
 jlo,jhi=j(lo),j(hi)
 if z<=jlo: return 0.0
 if z>=jhi: return 1.0
 def root(l,u,up):
  for _ in range(65):
   m=(l+u)/2
   if (j(m)<z)==up: l=m
   else: u=m
  return (l+u)/2
 t1=root(lo,cm,True);t2=root(cm,cM,False);t3=root(cM,hi,True)
 def ang(t):return math.acos(max(-1,min(1,(1+a*a-r*r-t*t)/(2*a))))
 return (ang(t1)+ang(t3)-ang(t2))/math.pi

def area_from_tangent_geometry(a,theta):
 p=(math.cos(theta),math.sin(theta))
 vx,vy=p[0]-a,p[1]
 rr=(1-a*a)/2;L2=vx*vx+vy*vy
 f=rr/L2; g=math.sqrt(L2-rr*rr)/L2
 q=[]
 for sign in (-1,1):
  nx=f*vx-sign*g*vy; ny=f*vy+sign*g*vx
  ux,uy=-ny,nx
  t=-2*(p[0]*ux+p[1]*uy)
  q.append((p[0]+t*ux,p[1]+t*uy))
 a1=(q[0][0]-p[0],q[0][1]-p[1]);a2=(q[1][0]-p[0],q[1][1]-p[1])
 return abs(a1[0]*a2[1]-a1[1]*a2[0])/2

rng=random.Random(941)
for a in (.04,.2,.5,.77,.96):
 for k in range(120):
  theta=rng.random()*2*math.pi
  assert abs(area(a,theta)-area_from_tangent_geometry(a,theta))<3e-12
 r,lo,cm,cM,hi,j=setup(a)
 for i in range(1,10):
  z=j(lo)+(j(hi)-j(lo))*i/10
  # Independent deterministic angular quadrature of the exact geometric area.
  n=24000
  estimate=sum(area(a,(k+.5)*math.pi/n)<=z for k in range(n))/n
  assert abs(estimate-cdf(a,z))<4/n+2e-8, (a,i,estimate,cdf(a,z))
 # Endpoints and small-displacement asymptotics are checked separately in exact formulas.
 for th in (.23,1.1,2.4):
  h=1e-6
  if a+h<1:
   assert area(a+h,th)<area(a,th)

for a in (.003,.006,.01):
 for th in (.3,.7,1.3,2.1,2.9):
  z=(area(a,th)-3*math.sqrt(3)/4+math.sqrt(3)*a*a)/(math.sqrt(3)*a**3/9)
  assert abs(z+math.cos(3*th))<.065, (a,th,z)

print('PASS: 36 exact Bernstein interpolation identities; 1 symbolic rational derivative identity;')
print('600 direct tangent-geometry comparisons; 45 CDF quadratures; 15 monotonic comparisons;')
print('15 small-offset harmonic diagnostics; all complete.')
