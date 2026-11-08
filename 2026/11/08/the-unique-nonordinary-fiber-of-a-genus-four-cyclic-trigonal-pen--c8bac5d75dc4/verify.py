#!/usr/bin/env python3
"""Exact characteristic-thirteen coefficient, matrix and Jacobi carry checks."""
from itertools import permutations
from fractions import Fraction
from math import comb
P=13

def add(x,y):
 out=[0]*max(len(x),len(y))
 for i,v in enumerate(x):out[i]=(out[i]+v)%P
 for i,v in enumerate(y):out[i]=(out[i]+v)%P
 while len(out)>1 and out[-1]==0:out.pop()
 return out

def mul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,u in enumerate(x):
  for j,v in enumerate(y):z[i+j]=(z[i+j]+u*v)%P
 while len(z)>1 and not z[-1]:z.pop()
 return z

def scale(x,s):return [(s*v)%P for v in x]

def pw(x,n):
 y=[1]
 for _ in range(n):y=mul(y,x)
 return y

def coeff(e,d):
 # (x^5+a*x^2+1)^e; coefficient of x^d as polynomial in a
 z=[0]*(e+1)
 for j in range(e+1):
  if d-2*j<0 or (d-2*j)%5:continue
  i=(d-2*j)//5
  if i+j<=e:z[j]=(z[j]+comb(e,j)*comb(e-j,i))%P
 while len(z)>1 and not z[-1]:z.pop()
 return z

def det(m):
 n=len(m);ans=[0]
 for perm in permutations(range(n)):
  inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  t=[1]
  for i,j in enumerate(perm):t=mul(t,m[i][j])
  ans=add(ans,scale(t,-1 if inv%2 else 1))
 return ans

B1=[[coeff(4,13*(k+1)-i-1) for i in range(1)] for k in range(1)]
B2=[[coeff(8,13*(k+1)-i-1) for i in range(3)] for k in range(3)]
a=[0,1]; target1=scale(a,-1)
D=add(pw(a,5),[-2%P]);target2=scale(mul(a,pw(D,2)),3)
assert B1[0][0]==target1,(B1,target1)
assert det(B2)==target2,(det(B2),target2)
assert mul(det(B1),det(B2))==scale(mul(pw(a,2),pw(D,2)),-3)

def specialize(m,v):
 return [[sum(c*(v**i) for i,c in enumerate(z))%P for z in row] for row in m]

def rank(mat):
 m=[row[:] for row in mat];nr=len(m);nc=len(m[0]);r=0
 for c in range(nc):
  pivot=next((i for i in range(r,nr) if m[i][c]),None)
  if pivot is None:continue
  m[r],m[pivot]=m[pivot],m[r]
  inv=pow(m[r][c],-1,P);m[r]=[z*inv%P for z in m[r]]
  for i in range(nr):
   if i!=r and m[i][c]:
    f=m[i][c];m[i]=[(x-f*y)%P for x,y in zip(m[i],m[r])]
  r+=1
 return r
assert rank(specialize(B1,0))+rank(specialize(B2,0))==2
for v in range(P):
 if pow(v,5,P)==2:continue
 R=rank(specialize(B1,v))+rank(specialize(B2,v))
 assert R==(2 if v==0 else 4),(v,R)
for u in [1,2]:
 for v in [1,2,3,4]:
  carries=[int(Fraction((u*pow(13,i,3))%3,3)+Fraction((v*pow(13,i,5))%5,5)>=1) for i in range(4)]
  assert sum(carries)==(1 if u==1 else 3),(u,v,carries)
assert rank(specialize(B2,0))==2
print('VERIFY_TRIGONAL13_OK')
