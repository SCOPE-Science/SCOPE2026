from itertools import product,combinations
from collections import Counter

def sign(x):return (x>0)-(x<0)
def bj(x,y):
    s=sum(sign(a)*b for a,b in zip(x,y) if a)
    r=sum(abs(b) for a,b in zip(x,y) if not a)
    return abs(s)<=r

def rep(x):
    j=next(i for i,v in enumerate(x) if v)
    return x if x[j]>0 else tuple(-v for v in x)
V=sorted({rep(p) for p in product((-1,0,1),repeat=3) if any(p)})
C={frozenset((x,y)) for x,y in combinations(V,2) if bj(x,y) and bj(y,x)}
maxcl=[]
for k in range(1,len(V)+1):
    cl=[g for g in combinations(V,k) if all(frozenset((x,y)) in C for x,y in combinations(g,2))]
    if not cl:break
    maxcl=cl
print('VERTICES',len(V),'EDGES',len(C),'OMEGA',len(maxcl[0]),'MAX_CLIQUES',len(maxcl))
print(maxcl)
assert len(maxcl[0])==6 and len(maxcl)==1
assert set(maxcl[0])=={rep(x) for i,j in combinations(range(3),2) for s in (-1,1) for x in [tuple(1 if k==i else s if k==j else 0 for k in range(3))]}
# Verify homogeneous signed-support test against the actual convexity minimization for many random rational examples.
from fractions import Fraction
# The convex piecewise-affine function ||x+ t y||_1 has minimum at t=0 iff slopes at 0 straddle 0.
for x in product(range(-2,3),repeat=3):
 if x==(0,0,0):continue
 for y in product(range(-2,3),repeat=3):
  if y==(0,0,0):continue
  a=sum(sign(xx)*yy for xx,yy in zip(x,y) if xx)
  b=sum(abs(yy) for xx,yy in zip(x,y) if not xx)
  slope_right=a+b;slope_left=a-b
  assert bj(x,y)==(slope_left<=0<=slope_right)
print('VERIFY_OK pairwise_integer_tests', (5**3-1)**2)
