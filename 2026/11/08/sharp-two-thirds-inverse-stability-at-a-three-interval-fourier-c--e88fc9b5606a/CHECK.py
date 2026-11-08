from fractions import Fraction as F
from math import isclose

def tri(x,L):return max(F(0),L-abs(x))
def integral_square(terms,L):
  knots=sorted({a+t for a,c in terms for t in (-L,F(0),L)})
  total=F(0)
  def val(x):return sum(c*tri(x-a,L) for a,c in terms)
  for x,y in zip(knots,knots[1:]):
    lo,hi=val(x),val(y)
    total+=(y-x)*(lo*lo+lo*hi+hi*hi)/3
  return total

def auto_diff(L,d,u,v):
  ref=[F(0),d,2*d]; new=[F(0),d+u,2*d+v]
  def pairs(a):return [a[j]-a[i] for i in range(3) for j in range(i+1,3)]
  shifts=[(a,F(1)) for a in pairs(new)]+[(a,F(-1)) for a in pairs(ref)]
  terms=shifts+ [(-a,c) for a,c in shifts]
  return integral_square(terms,L)

for L,d in [(F(1),F(4)),(F(2),F(8)),(F(3,2),F(6))]:
 for e in [F(1,20),F(1,8),F(1,4)]:
  val=auto_diff(L,d,e,F(0))
  assert val==8*e**3,(L,d,e,val,8*e**3)
  print('exact split',str(L),str(d),str(e),val)
 for u,v in [(F(1,20),F(1,25)),(F(-1,25),F(1,30)),(F(1,30),F(0))]:
  val=auto_diff(L,d,u,v)
  assert val>0
  s=u-v/2
  print('two-parameter',L,d,u,v,'energy2',val,'ratio',round(float(val**F(1,2))/(abs(float(s))**1.5+abs(float(v))),5))
print('THREE_INTERVAL_COLLISION_CHECKS_PASSED')
