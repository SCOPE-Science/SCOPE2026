#!/usr/bin/env python3
"""Standalone arithmetic cross-checks for an exact real toral dynamical map."""
import math,itertools
A=((2,1,3),(3,2,5),(2,1,4))
def mul(X,Y):return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def det(X):return X[0][0]*(X[1][1]*X[2][2]-X[1][2]*X[2][1])-X[0][1]*(X[1][0]*X[2][2]-X[1][2]*X[2][0])+X[0][2]*(X[1][0]*X[2][1]-X[1][1]*X[2][0])
assert det(A)==1
assert all(v>0 for row in A for v in row)
tr=sum(A[i][i] for i in range(3));B=mul(A,A)
e2=(tr*tr-sum(B[i][i] for i in range(3)))//2
assert (tr,e2,det(A))==(8,6,1)
def poly(t):return t**3-8*t*t+6*t-1
assert poly(0)<0<poly(.3)
assert poly(.5)>0>poly(.6)
assert poly(7)<0<poly(8)
P=((1,0,0),(0,1,0),(0,0,1))
for k in range(1,25):
 P=mul(P,A)
 for i,j in itertools.product(range(3),repeat=2):
  assert sum((P[j][h] if h!=i else 0)>0 for h in range(3))==2
lo,hi=7.0,8.0
for _ in range(90):
 mid=(lo+hi)/2
 if poly(mid)>0:hi=mid
 else:lo=mid
lam=(lo+hi)/2
assert 7.18421012<lam<7.18421014
bound=1+math.log2(lam)
assert 3.84482<bound<3.84484
print('PASS: determinant, characteristic polynomial, root brackets, rank witnesses, entropy ceiling')
print('lambda=',lam,'entropy ceiling bits=',bound)
