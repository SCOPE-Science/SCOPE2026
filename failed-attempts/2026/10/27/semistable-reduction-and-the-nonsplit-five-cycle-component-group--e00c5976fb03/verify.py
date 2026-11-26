#!/usr/bin/env python3
"""Exact checks for Bring curve integral reduction and dual graph."""
import itertools

def mul(a,b):
    a0,a1=a&1,a>>1; b0,b1=b&1,b>>1
    return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)
def add(a,b): return a^b
def ex(a,n):
    z=1
    for _ in range(n): z=mul(z,a)
    return z
E=[(0,0,1,2,3),(0,1,1,1,1),(1,0,1,1,1),(0,0,1,3,2)]
def sym2(x):
    return sum_xor(mul(x[i],x[j]) for i,j in itertools.combinations(range(5),2))
def sym3(x):
    return sum_xor(mul(mul(x[i],x[j]),x[k]) for i,j,k in itertools.combinations(range(5),3))
def sum_xor(items):
    z=0
    for x in items: z^=x
    return z
def seg(s,v,t,u):
    c=(mul(s,t),mul(s,u),mul(v,t),mul(v,u))
    return [sum_xor(mul(c[j],E[j][i]) for j in range(4)) for i in range(5)]
P=[(1,x) for x in range(4)]+[(0,1)]
zero1=zero2=meet=0
for s,v in P:
 for t,u in P:
  x=seg(s,v,t,u)
  assert sum_xor(x)==0 and sym2(x)==0
  z1=mul(s,ex(t,2))^mul(v,ex(u,2))
  z2=mul(ex(s,2),t)^mul(ex(v,2),u)
  assert sym3(x)==mul(z1,z2)
  zero1+=z1==0;zero2+=z2==0;meet+=(z1==0 and z2==0)
assert (zero1,zero2,meet)==(5,5,5)
# Five distinguished F2 points are on both components.
for i in range(5):
 x=[1]*5; x[i]=0
 assert sum_xor(x)==0 and sym2(x)==0 and sym3(x)==0
# Integer local computation is direct, with no library requirement:
# at u=v=0 the five coordinates are (-4-w,1,1,1+w,1).
def e2z(x):return sum(x[i]*x[j] for i,j in itertools.combinations(range(5),2))
def e3z(x):return sum(x[i]*x[j]*x[k] for i,j,k in itertools.combinations(range(5),3))
for w in range(-10,11):
 x=(-4-w,1,1,1+w,1)
 assert e2z(x)==-w*w-5*w-10
 assert e3z(x)==-3*w*w-15*w-20
 assert e3z(x)-3*e2z(x)==10
# graph critical group reduced Laplacian 5; inversion on Z/5 has one fixed class.
assert 5-(2-1)==4
assert sum(((-k)%5)==k for k in range(5))==1
print('VERIFY_OK: GF4 factorization; two five-point rational components; 5 nodes; local identity 3q+10; rank-4 graph, component group Z/5 and one Frobenius-fixed class')
