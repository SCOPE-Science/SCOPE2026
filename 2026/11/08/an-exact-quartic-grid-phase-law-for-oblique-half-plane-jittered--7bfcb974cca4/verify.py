"""Exact independent checks of lattice-stratified threshold variance."""
from fractions import Fraction as Q
from math import gcd, floor

def F(z,a,b):
    z=Q(z)
    if z<=0: return Q(0)
    if z<=a:return z*z/Q(2*a*b)
    if z<=b:return (z-Q(a,2))/b
    if z<=a+b:return 1-(a+b-z)**2/Q(2*a*b)
    return Q(1)

def v(z,a,b):
    f=F(z,a,b)
    return f*(1-f)

def C(a,b):
    return Q(-a**4+5*a**3*b+10*a*b**3+1,60*a*b*b)

def W(theta,a,b):
    return sum((v(k+theta,a,b) for k in range(a+b)),Q(0))

def N(m,a,b):
    return sum(1 for i in range(m//a+1) for j in range(m//b+1) if a*i+b*j==m) if m>=0 else 0

def exact_variance_direct(n,a,b,c):
    return sum((v(n*c-a*i-b*j,a,b) for i in range(n) for j in range(n)),Q(0))/n**4

def exact_variance_counts(n,a,b,c):
    m=(n*c).__floor__(); theta=n*c-m
    return sum((N(m-k,a,b)*v(k+theta,a,b) for k in range(a+b)),Q(0))/n**4

checks=0
for a in range(1,6):
 for b in range(a,7):
  if gcd(a,b)!=1: continue
  for theta in (Q(0),Q(1,7),Q(1,2),Q(4,7),Q(99,100)):
   assert W(theta,a,b)==C(a,b)-theta**2*(1-theta)**2/Q(2*a*b*b),(a,b,theta,W(theta,a,b))
   checks+=1
  for n in (1,2,4,7,11):
   for c in (Q(a,3),Q(2*a,3),Q(a*7,11)):
    assert exact_variance_direct(n,a,b,c)==exact_variance_counts(n,a,b,c),(n,a,b,c)
    checks+=1
# Explicit worst and best phases on the diagonal threshold a=b=1
assert C(1,1)==Q(1,4)
assert W(Q(1,2),1,1)==Q(7,32)
checks+=2
# A simple exact n^3 expansion can be audited via checking each floor-count O(1).
for a,b in ((1,1),(1,3),(2,3),(3,5),(5,6)):
 for s in range(0,300):
  assert abs(Q(N(s,a,b))-Q(s,a*b))<=a+b
  checks+=1
print('PASS:',checks,'independent exact-rational assertions')
