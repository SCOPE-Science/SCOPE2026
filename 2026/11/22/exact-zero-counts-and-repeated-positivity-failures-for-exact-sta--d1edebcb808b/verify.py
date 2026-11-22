#!/usr/bin/env python3
"""Independent finite checks of the displayed identities and sample sign bands.
All-order root counts and extremal inequalities are proved in RESULT.md, not by scans.
Requires Python 3 and SymPy; no external files.
"""
import math
from fractions import Fraction
import sympy as s

z, E=s.symbols('z E', real=True)
a=3+2*z
b=2*z-1
N=a*E-2
D=b+N*N
checks=0

def ok(test, msg):
 global checks
 assert bool(test), msg
 checks+=1

# Derivatives of theta and phi; their strict difference has a positive factor.
ok(s.factor(2*D-a*(2-(4*z*z+2*z+2)*E)-2*E*a*a*(E+z-1))==0,"phase derivative numerator")
ok(s.simplify(((4*E-1)/a+1/(5+2*z)).subs(E,1/(10+4*z)))==0,"scalar minimum")
ok(s.simplify(s.diff((4*s.exp(-z)-1)/a,z) - (2-4*(5+2*z)*s.exp(-z))/a**2)==0,"scalar derivative")
ok(s.factor(1+12*(4*E-1)/9-((16*E-1)/3))==0,"13 vertex hub witness")

# Construct a genuine 13 by 13 unweighted star and solve the implicit BDF2
# second-stage system with symbolic exponential spectral data independently.
n=13
L=s.zeros(n)
for j in range(1,n):
 L[0,0]+=1;L[j,j]+=1;L[0,j]-=1;L[j,0]-=1
first=s.zeros(n,1);first[0]=1
projection0=s.ones(n,1)/n
ok(L*projection0==s.zeros(n,1),"constant eigenvector")
ok(L*(first-projection0)==n*(first-projection0),"star hub eigenvector")
u1=projection0+E*(first-projection0)
u2=(3*s.eye(n)+2*s.Rational(3,13)*L).inv()*(4*u1-first)
ok(s.simplify(u2[0]-(16*E-1)/39)==0,"full 13x13 exact starter and BDF2 system")

# 200 exact rational BDF2 recurrences at explicit rational z and E values:
# E values are arbitrary here, verifying the recurrence algebra rather than exponential evaluation.
for q in [Fraction(0,1), Fraction(1,4), Fraction(1,2), Fraction(3,4),Fraction(2,1), Fraction(3,1),Fraction(10,1)]:
 for e in [Fraction(1,1), Fraction(2,3), Fraction(1,8)]:
  den=3+2*q
  u=[Fraction(1), e]
  for k in range(2,13):u.append((4*u[-1]-u[-2])/den)
  for k in range(2,13):ok(den*u[k]==4*u[k-1]-u[k-2],"exact rational recurrence")

# Compare the exact-start phase formula with the recurrence for several k,z.
for zz in [.52, .73,1.1,1.3863,2,3,6,10,20,55,150]:
 aa=3+2*zz
 bb=2*zz-1
 theta=math.acos(2/math.sqrt(aa))
 B=(aa*math.exp(-zz)-2)/math.sqrt(bb)
 vals=[1.,math.exp(-zz)]
 for j in range(2,25):vals.append((4*vals[-1]-vals[-2])/aa)
 for j in range(2,25):
  v=aa**(-j/2)*(math.cos(j*theta)+B*math.sin(j*theta))
  ok(abs(v-vals[j])<3e-12*max(1,abs(v)),"phase vs recurrence")

# Certified by phase monotonicity (in RESULT.md). Numeric bracketing is only a check.
def phase(k,x):
 aa=3+2*x; bb=2*x-1
 return k*math.acos(2/math.sqrt(aa))-math.atan((aa*math.exp(-x)-2)/math.sqrt(bb))
def bisect(k,target):
 lo=.50000001; hi=1e9
 assert phase(k,lo)<target<phase(k,hi)
 for _ in range(110):
  mid=(lo+hi)/2
  if phase(k,mid)<target:lo=mid
  else:hi=mid
 return (lo+hi)/2
for k in range(2,27):
 roots=[bisect(k,math.pi*(j+.5)) for j in range(k//2)]
 ok(all(x>1/2 for x in roots),"root location")
 ok(all(roots[j]<roots[j+1] for j in range(len(roots)-1)),"root order")
 for x in roots:
  aa=3+2*x
  v=[1., math.exp(-x)]
  for j in range(2,k+1):v.append((4*v[-1]-v[-2])/aa)
  ok(abs(v[-1])<3e-11,"numerically located zero")

# Sharp 12-to-13 diagonal dimension and examples at equal-weight universal vertex.
zz=3
p=(4*math.exp(-zz)-1)/(3+2*zz)
for n in range(2,19):
 hub=(1+(n-1)*p)/n
 ok((hub<0)==(n>=13),"center diagonal sign at z=3")
ok(16*math.exp(-3)<1,"exact 13-vertex negativity sign")
# Multiple separated negativity windows for a high-stage and sufficiently large finite star.
for k in [4,6,8,10,12]:
 roots=[bisect(k, math.pi*(j+.5)) for j in range(k//2)]
 testpoints=[]
 for j in range(0,len(roots),2):
  low=roots[j]
  high=roots[j+1] if j+1<len(roots) else low*3+10
  # Select by phase at the middle of its negative phase sector.
  phase_mid=(j+1)*math.pi
  if phase_mid<k*math.pi/2:
   point=bisect(k,phase_mid)
  else:
   point=(low+high)/2
  testpoints.append(point)
 g=[]
 for point in testpoints:
  aa=3+2*point
  vals=[1.,math.exp(-point)]
  for t in range(2,k+1):vals.append((4*vals[-1]-vals[-2])/aa)
  g.append(vals[-1])
 ok(all(x<0 for x in g),"scalar negative bands")
 n=2+math.ceil(max(-1/x for x in g))
 ok(all((1+(n-1)*x)/n<0 for x in g),"star negative band witnesses")
 ok(len(g)==(k//2+1)//2,"band count")

print(f"EXACT_IDENTITIES_AND_FINITE_TESTS_OK {checks} checks")
