#!/usr/bin/env python3
"""Independent finite-field sample and exhaustive GF(49)-point check.

GF(49)=GF(7)[z]/(z^2-3). Uses only Python standard library.
The complete geometric classification is proven in verify_strata.py.
"""
P=7

def add(x,y):return (x+y)%7+7*((x//7+y//7)%7)
def neg(x):return (-x)%7+7*((-(x//7))%7)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x%7,x//7;c,d=y%7,y//7
 return (a*c+3*b*d)%7+7*((a*d+b*c)%7)
def powf(x,n):
 r=1
 while n:
  if n&1:r=mul(r,x)
  x=mul(x,x);n//=2
 return r
def inv(x):
 assert x
 return powf(x,47)
def matmul(X,Y):
 n=len(X);z=[[0]*n for _ in range(n)]
 for i in range(n):
  for j in range(n):
   for k in range(n):z[i][j]=add(z[i][j],mul(X[i][k],Y[k][j]))
 return z
def rank(M):
 a=[row[:] for row in M];m=len(a);n=len(a[0]);r=0
 for j in range(n):
  pivot=next((i for i in range(r,m) if a[i][j]!=0),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];v=inv(a[r][j]);a[r]=[mul(v,t) for t in a[r]]
  for i in range(m):
   if i!=r and a[i][j]:
    t=a[i][j];a[i]=[sub(a[i][k],mul(t,a[r][k])) for k in range(n)]
  r+=1
  if r==m:break
 return r

def polytrim(p):
 while p and p[-1]==0:p.pop()
 return p

def gcdpoly(f,g):
 f=polytrim(f[:]);g=polytrim(g[:])
 while g:
  a=f[:];d=inv(g[-1])
  while len(a)>=len(g):
   c=mul(a[-1],d);delta=len(a)-len(g)
   for i,b in enumerate(g):a[i+delta]=sub(a[i+delta],mul(c,b))
   polytrim(a)
  f,g=g,a
 return f

def smooth(a,b):
 # h(T)=T^4+aT^3+bT^2+aT+1. Its roots must be distinct.
 q=[1,a,b,a,1];dq=[a,mul(2,b),mul(3,a),4]
 return len(gcdpoly(q,dq))==1

def matrix(a,b):
 # Directly cube f(x), rather than using any symbolic matrix formula.
 f=[0]*10
 for d,c in [(1,1),(3,a),(5,b),(7,a),(9,1)]:f[d]=c
 g=[1]
 for _ in range(3):
  h=[0]*(len(g)+len(f)-1)
  for i,c in enumerate(g):
   for j,d in enumerate(f):h[i+j]=add(h[i+j],mul(c,d))
  g=h
 return [[g[7*(i+1)-(j+1)] if 0<=7*(i+1)-(j+1)<len(g) else 0 for j in range(4)] for i in range(4)]

counts={}
for a in range(49):
 for b in range(49):
  if not smooth(a,b):continue
  H=matrix(a,b);r1=rank(H)
  if r1==4:prank=4
  else:
   assert r1==2
   H7=[[powf(v,7) for v in row] for row in H]
   r2=rank(matmul(H7,H));assert r2 in (0,2)
   # Check stabilization with the next semilinear stage.
   H49=[[powf(v,49) for v in row] for row in H]
   assert rank(matmul(H49,matmul(H7,H)))==r2
   prank=r2
  counts[(r1,prank)]=counts.get((r1,prank),0)+1
print('GF49_COUNTS',sorted(counts.items()))
assert (4,4) in counts and (2,2) in counts and (2,0) in counts
# The only rank-zero parameter pairs in GF(49) are (a,b)=(2,0),(-2,0).
assert counts[(2,0)]==2
for a,b,expect in [(0,0,(4,4)),(2,0,(2,0)),(5,0,(2,0)),(0,21,(2,2))]:
 assert smooth(a,b)
 H=matrix(a,b);H7=[[powf(v,7) for v in row] for row in H]
 got=(rank(H),rank(matmul(H7,H)))
 assert got==expect,(a,b,got,expect)
print('GF49_INDEPENDENT_PASS',sum(counts.values()),counts[(2,0)])
