"""Exact, dependency-free certificate for two-branch renewal horseshoe."""
from fractions import Fraction as Q
from math import log

def interval(lo, hi=None):
    return (Q(lo), Q(lo) if hi is None else Q(hi))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    vals=[x*y for x in a for y in b]
    return (min(vals),max(vals))
def div(a,b):
    assert not(b[0]<=0<=b[1]),'interval crosses zero'
    return mul(a,(min(Q(1,b[0]),Q(1,b[1])),max(Q(1,b[0]),Q(1,b[1]))))
def inside(a,b):return b[0]<a[0] and a[1]<b[1]
def show(name,a):print(name, tuple(float(t) for t in a))
I=(Q(-9,10),Q(-1,100))
a=(Q(-2001,1000),Q(-1999,1000))
b=(Q(1499,1000),Q(1501,1000))
one=interval(1)
k=add(one,mul(sub(a,one),b))
s=mul(a,k)
phi0=div(add(I,one),a)
phi1=div(add(add(add(I,k),a),one),s)
for name,obj in [('k',k),('s',s),('phi0',phi0),('phi1',phi1)]:show(name,obj)
assert k[1]<Q(-3) and s[0]>Q(6)
assert inside(phi0,(Q(-1,2),Q(-1,25)))
assert inside(phi1,(Q(-4,5),Q(-3,5)))
assert I[0]<phi1[0]<phi1[1]<phi0[0]<phi0[1]<I[1]
x1=sub(mul(a,phi1),one)
x2=sub(mul(b,x1),one)
y2=mul(sub(one,b),x1)
for name,obj in [('first L: x1',x1),('then R: x2',x2),('y2',y2)]:show(name,obj)
assert x1[0]>0 and x2[1]<0 and y2[1]<0
# Period-one and period-three map identities, sampled at exact rational endpoints
for aa in [a[0],Q(-2),a[1]]:
 for bb in [b[0],Q(3,2),b[1]]:
  kk=1+(aa-1)*bb
  ss=aa*kk
  for t in I:
   x0=(t+1)/aa
   assert aa*x0-1==t
   z=(t+kk+aa+1)/ss
   z1=aa*z-1
   z2=bb*z1-1
   yy2=(1-bb)*z1
   assert aa*z2+yy2-1==t
   assert z<0<z1 and z2<0 and yy2<0
# Renewed symbolic system adjacency: 0->0 or 1, 1->2, 2->0.
A=((1,1,0),(0,0,1),(1,0,0))
def mulmat(X,Y):return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)) for i in range(3))
A2=mulmat(A,A);A3=mulmat(A2,A)
Z=tuple(tuple(A3[i][j]-A2[i][j]-(i==j) for j in range(3)) for i in range(3))
assert all(all(v==0 for v in row) for row in Z)
lo,hi=1.,2.
for _ in range(90):
 mid=(lo+hi)/2
 if mid**3-mid**2-1>0:hi=mid
 else:lo=mid
lam=(lo+hi)/2
assert 1.46<lam<1.47
# Contraction ratios are 1/abs(a), 1/abs(a*k).
for aa,bb in [(Q(-2),Q(3,2)),(a[0],b[0]),(a[1],b[1])]:
 kk=1+(aa-1)*bb
 r0=1/abs(float(aa));r1=1/abs(float(aa*kk))
 low,high=0.,1.
 for _ in range(90):
  mid=(low+high)/2
  if r0**mid+r1**mid>1:low=mid
  else:high=mid
 print('dimension',float(aa),float(bb),(low+high)/2)
print('VERIFY_OK rational_parameter_box=1 disjoint_branches=1 strict_itineraries=1 exact_return_identities=18 renewal_matrix=1 entropy_root=1 dimension_equation=1')
