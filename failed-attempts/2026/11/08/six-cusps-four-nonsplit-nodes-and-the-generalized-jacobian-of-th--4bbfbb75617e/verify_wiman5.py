#!/usr/bin/env python3
"""Exact arithmetic checks for the characteristic-five Wiman plane sextic."""
import itertools
P=5
# Coefficients of a homogeneous polynomial encoded by exponent triples.
def plus(a,b):
 c=dict(a)
 for e,v in b.items():c[e]=(c.get(e,0)+v)%P
 return {e:v for e,v in c.items() if v}
def mulpol(a,b):
 c={}
 for e,v in a.items():
  for f,w in b.items():
   t=tuple(e[i]+f[i] for i in range(3))
   c[t]=(c.get(t,0)+v*w)%P
 return {e:v for e,v in c.items() if v}
def power(a,n):
 r={(0,0,0):1}
 for i in range(n):r=mulpol(r,a)
 return r
x={(1,0,0):1};y={(0,1,0):1};z={(0,0,1):1}
x2=power(x,2);y2=power(y,2);z2=power(z,2)
S=plus(plus(x2,y2),z2)
F0=plus(plus(plus(power(x,6),power(y,6)),power(z,6)),mulpol(S,plus(plus(power(x,4),power(y,4)),power(z,4))))
F0=plus(F0,{e:(-12*v)%P for e,v in mulpol(mulpol(x2,y2),z2).items()})
F=plus({e:2*v%P for e,v in power(S,3).items()},mulpol(mulpol(x2,y2),z2))
assert F0==F
# Derivative formula as polynomial equality.
def derivative(a,j):
 b={}
 for e,v in a.items():
  if e[j]:
   f=list(e);f[j]-=1;b[tuple(f)]=e[j]*v%P
 return {e:v for e,v in b.items() if v}
for j in range(3):
 others=[x2,y2,z2]
 p2=mulpol(others[(j+1)%3],others[(j+2)%3]); q=plus(power(S,2),p2)
 rhs={e:2*v%P for e,v in mulpol([x,y,z][j],q).items()}
 assert derivative(F,j)==rhs

def evalpoly(a,xyz):
 return sum(v*xyz[0]**e[0]*xyz[1]**e[1]*xyz[2]**e[2] for e,v in a.items())%P
nodes=[(a,b,1) for a in (1,4) for b in (1,4)]
cusps=[(0,2,1),(0,3,1),(2,0,1),(3,0,1),(2,1,0),(3,1,0)]
for p in nodes+cusps:
 assert evalpoly(F,p)==0
 assert all(evalpoly(derivative(F,j),p)==0 for j in range(3))
# The tangent discriminant at a standard node is 3, a nonsquare in F5.
for pt in nodes:
 hxx=evalpoly(derivative(derivative(F,0),0),pt)
 hxy=evalpoly(derivative(derivative(F,0),1),pt)
 hyy=evalpoly(derivative(derivative(F,1),1),pt)
 disc=(hxy*hxy-hxx*hyy)%P
 assert disc==3, (pt,hxx,hxy,hyy,disc)
 assert disc not in {j*j%5 for j in range(5)}
# Geometric singular-point classification follows symbolically from the gradient equations.
# Enumerate rational projective points in F5 and F25; the proof covers geometric closure.
A=[(a,b) for a in range(5) for b in range(5)]
zero=(0,0);one=(1,0)
def add(u,v):return ((u[0]+v[0])%5,(u[1]+v[1])%5)
def mul(u,v):return ((u[0]*v[0]+2*u[1]*v[1])%5,(u[0]*v[1]+u[1]*v[0])%5)
def sq(u):return mul(u,u)
def cub(u):return mul(sq(u),u)
def val(u,v,w):
 s=add(add(sq(u),sq(v)),sq(w))
 return add(mul((2,0),cub(s)),mul(mul(sq(u),sq(v)),sq(w)))
def points(K):
 c=0
 for u,v in itertools.product(K,repeat=2):
  if val(u,v,one)==zero:c+=1
 for u in K:
  if val(u,one,zero)==zero:c+=1
 if val(one,zero,zero)==zero:c+=1
 return c
assert points([(i,0) for i in range(5)])==10
assert points(A)==22
print('REDUCTION_OK')
print('TEN_SINGULAR_WITNESSES_OK')
print('NODE_NON_SPLIT_DISCRIMINANT_3_OK')
print('POINTS_F5=10')
print('POINTS_F25=22')
print('VERIFY_OK')
