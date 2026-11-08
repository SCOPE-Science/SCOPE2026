"""Standalone computational checks for two-scale sampled-polygon area/perimeter laws.
Requires standard Python and SymPy for symbolic identities."""
from itertools import combinations
from math import pi, sin, cos, factorial, isclose
import math
import sympy as sp

def geometry(n, inds):
    pts=[(math.cos(2*pi*j/n),math.sin(2*pi*j/n)) for j in inds]
    pp=sum(math.hypot(pts[(k+1)%len(pts)][0]-pts[k][0], pts[(k+1)%len(pts)][1]-pts[k][1]) for k in range(len(pts)))
    aa=abs(sum(pts[k][0]*pts[(k+1)%len(pts)][1]-pts[(k+1)%len(pts)][0]*pts[k][1] for k in range(len(pts)))/2)
    return pp,aa

def via_gaps(n,inds):
    gg=[(inds[(i+1)%len(inds)]-inds[i])%n for i in range(len(inds))]
    return 2*sum(sin(pi*g/n) for g in gg),sum(sin(2*pi*g/n) for g in gg)/2,gg

count=0; max_err=0.; strict_count=0
for n in range(4,13):
  for m in range(3,n+1):
    for inds in combinations(range(n),m):
      p,a=geometry(n,inds);p2,a2,gg=via_gaps(n,inds)
      e=max(abs(p-p2),abs(a-a2));max_err=max(max_err,e)
      assert e<5e-12,(n,m,inds,e)
      dp=2*n*sin(pi/n)-p;da=n*sin(2*pi/n)/2-a
      if m<n:
        assert dp>0 and da>0 and (2*dp-da)>-8e-12,(n,m,inds,dp,da)
        strict_count+=1
      count+=1
print('DIRECT_GEOMETRY_SUBSETS',count,'NONTRIVIAL',strict_count,'MAX_ERROR',max_err)

p,z=sp.symbols('p z',positive=True)
f=p*z/(1-(1-p)*z); M={0:sp.Integer(1)}
for k in range(1,11):
    f=sp.factor(z*sp.diff(f,z)); M[k]=sp.factor(f.subs(z,1))
V1=sp.factor(M[2]-M[1]**2)
def cov(i,j):return sp.factor(M[i+j]-M[i]*M[j])
W3=sp.factor(cov(3,3)-cov(3,1)**2/V1)
W5=sp.factor(cov(5,5)-cov(5,1)**2/V1)
W35=sp.factor(cov(3,5)-cov(3,1)*cov(5,1)/V1)
assert sp.factor(W3-36*(5-p)*(2-p)*(1-p)**2/p**6)==0
assert sp.factor(W35-180*(p-4)*(p-2)*(p-1)**2*(p*p-17*p+20)/p**8)==0
assert sp.factor(W5-900*(p-2)*(p-1)**2*(p**5-53*p**4+624*p**3-2480*p**2+3680*p-1808)/p**10)==0
assert sp.factor(p*M[3]-1-6*(1-p)/p**2)==0
assert sp.factor(p*M[5]-1-30*(1-p)*(2-p)**2/p**4)==0
for q in [sp.Rational(i,20) for i in range(1,20)]:
 assert W3.subs(p,q)>0 and W5.subs(p,q)>0 and (W3*W5-W35**2).subs(p,q)>0
print('MOMENT_SYMBOLIC_CHECKS_PASSED',len(M), 'covariances positive definite at 19 fractions')

# Taylor coefficients of chord length and shoelace area, to fifth order.
t=sp.symbols('t'); ct=sp.series(2*sp.sin(t),t,0,8).removeO();at=sp.series(sp.sin(2*t)/2,t,0,8).removeO()
assert sp.expand(2*ct-at).coeff(t,3)==0
assert sp.expand(2*ct-at).coeff(t,5)==-sp.Rational(1,10)
print('CUBIC_CANCELLATION_AND_FIFTH_GAP_PASSED')

# Check the conditional sum representation by exact enumeration and pairwise moments.
from fractions import Fraction
for n,m in [(7,3),(8,4),(10,5),(11,6),(12,7)]:
    vals=[]
    for inds in combinations(range(n),m):
        _,_,gg=via_gaps(n,inds)
        vals.append((sum(g**3 for g in gg),sum(g**5 for g in gg)))
    ex3=Fraction(sum(v[0] for v in vals),len(vals));ex5=Fraction(sum(v[1] for v in vals),len(vals))
    den=math.comb(n-1,m-1)
    e3=sum(Fraction(m*(g**3)*math.comb(n-g-1,m-2),den) for g in range(1,n-m+2))
    e5=sum(Fraction(m*(g**5)*math.comb(n-g-1,m-2),den) for g in range(1,n-m+2))
    assert ex3==e3 and ex5==e5
print('FINITE_COMPOSITION_MOMENTS_PASSED')
