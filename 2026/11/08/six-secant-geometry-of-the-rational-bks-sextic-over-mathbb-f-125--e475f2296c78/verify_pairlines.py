#!/usr/bin/env python3
"""Exact finite-field, pair-generated six-secant verification for the BKS plane sextic over F125."""
from collections import Counter
P=5;Q=125
D=[tuple((a//5**i)%5 for i in range(3)) for a in range(Q)]
def code(z):return sum((v%5)*5**i for i,v in enumerate(z))
def add(a,b):return code([D[a][i]+D[b][i] for i in range(3)])
def neg(a):return code([-v for v in D[a]])
def mul(a,b):
 z=[0]*5
 for i,ai in enumerate(D[a]):
  for j,bj in enumerate(D[b]):z[i+j]+=ai*bj
 # alternate irreducible polynomial T^3+T+4.
 for d in (4,3):
  c=z[d];z[d]=0;z[d-2]-=c;z[d-3]-=4*c
 return code(z[:3])
ADD=[[add(a,b) for b in range(Q)] for a in range(Q)]
MULT=[[mul(a,b) for b in range(Q)] for a in range(Q)]
NEG=[neg(a) for a in range(Q)]
def plus(a,b):return ADD[a][b]
def times(a,b):return MULT[a][b]
def minus(a,b):return ADD[a][NEG[b]]
def power(a,n):
 v=1
 while n:
  if n&1:v=times(v,a)
  a=times(a,a);n//=2
 return v
assert all(power(a,124)==1 for a in range(1,Q))
INV=[0]+[power(a,123) for a in range(1,Q)]
assert all(times(a,INV[a])==1 for a in range(1,Q))
def equation(u):
 x,y,z=u
 return plus(minus(power(y,6),plus(times(power(x,5),z),times(x,power(z,5)))),power(minus(times(y,y),times(2,times(x,z))),3))
def cross(u,v):
 a,b,c=u;d,e,f=v
 return (minus(times(b,f),times(c,e)),minus(times(c,d),times(a,f)),minus(times(a,e),times(b,d)))
def canonical(v):
 for a in v:
  if a:return tuple(times(t,INV[a]) for t in v)
 raise AssertionError('zero vector')
def incid(l,p):return plus(plus(times(l[0],p[0]),times(l[1],p[1])),times(l[2],p[2]))==0
V=[(1,x,y) for x in range(Q) for y in range(Q)]+[(0,1,t) for t in range(Q)]+[(0,0,1)]
E=[pt for pt in V if equation(pt)==0]
assert len(V)==15751 and len(E)==136
# Every six-secant contains a pair; generate candidate lines only from pairs.
candidates=set()
for i,u in enumerate(E):
 for v in E[i+1:]:candidates.add(canonical(cross(u,v)))
lines=[l for l in candidates if sum(incid(l,u) for u in E)==6]
assert len(lines)==120
m=Counter()
for line in lines:
 for pt in V:
  if incid(line,pt):m[pt]+=1
S=Counter(m[p] for p in V)
SE=Counter(m[p] for p in E)
OFF=Counter(m[p] for p in V if equation(p)!=0)
assert S=={0:6571,1:3720,2:5340,6:120},S
assert SE=={0:16,6:120},SE
assert OFF=={0:6555,1:3720,2:5340},OFF
# Distinct six-secants intersect only on the curve with multiplicity 6 or externally with multiplicity 2.
assert sum(v*(v-1)//2 for v in S.elements())==120*119//2
print('BKS125_ALTERNATE_FIELD_PAIR_SECANTS_PASS',len(E),len(lines),dict(sorted(S.items())))
print('BKS125_EXTERNAL_UNCOVERED_PASS',OFF[0], 'CURVE_6_FOLDS',SE[6])
