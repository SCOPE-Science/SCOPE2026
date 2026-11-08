#!/usr/bin/env python3
"""Finite quadratic-extension check on the displayed (4,5) P3(F3) space filler.
GF(9)=F3[a]/(a*a+1). This checks point counts and line incidences,
not geometric smoothness (established for the example in its source).
"""
from itertools import product,combinations

def add(x,y):return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
def neg(x):return ((-x%3)%3)+3*((-(x//3))%3)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x%3,x//3;c,d=y%3,y//3
 return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
def pow9(x,n):
 z=1
 for _ in range(n):z=mul(z,x)
 return z
def inv(x):return pow9(x,7)
def scale(x,c):return tuple(mul(t,c) for t in x)
def norm(x):return scale(x,inv(next(y for y in x if y)))
def P(n):return sorted({norm(v) for v in product(range(n),repeat=4) if any(v)})
def phi(v,i,j):return sub(mul(pow9(v[i],3),v[j]),mul(v[i],pow9(v[j],3)))
def g(v):return add(phi(v,0,1),phi(v,2,3))
def f(v):
 x,y,z,w=v
 terms=[(neg(x),0,1),(add(x,y),0,2),(sub(add(x,y),z),0,3),
        (sub(sub(x,y),z),1,2),(sub(x,w),1,3),
        (neg(add(add(x,y),add(z,w))),2,3)]
 r=0
 for c,i,j in terms:r=add(r,mul(c,phi(v,i,j)))
 return r
p3=P(3);p9=P(9)
assert len(p3)==40 and len(p9)==820
assert all(g(t)==f(t)==0 for t in p3)
pts=[t for t in p9 if g(t)==0 and f(t)==0]
assert set(pts)==set(p3) and len(pts)==40
# The isotropic lines of g in PG(3,3) are determined by g(u+a*v)=0,
# with a primitive element of GF(9) outside F3.
lines=set()
for u,v in combinations(p3,2):
 line=frozenset(norm(tuple(add(mul(u[i],s),mul(v[i],t)) for i in range(4)))
  for s,t in product(range(3),repeat=2) if s or t)
 lines.add(line)
assert len(lines)==130
iso=0
for line in lines:
 u,v=tuple(line)[:2]
 p=norm(tuple(add(u[i],mul(3,v[i])) for i in range(4)))
 if g(p)==0:
  iso+=1
  assert f(p)!=0
assert iso==40
print('TERNARY_P3_FILLING_PASS',len(p3),'F3 points and',len(pts),'F9 points')
print('TERNARY_SYMPLECTIC_LINES_PASS',len(lines),'F3 lines of which',iso,'lie on the degree-4 surface')
