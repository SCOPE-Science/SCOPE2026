#!/usr/bin/env python3
"""Independent exact-rational realization of the generic six-point Pascal configuration.
Run with Python 3 standard library; no external algebra system needed.
"""
from itertools import combinations, permutations
from math import gcd
from functools import reduce

def canon(h):
 h=tuple(h);return min([h[i:]+h[:i] for i in range(6)]+[h[::-1][i:]+h[::-1][:i] for i in range(6)])
H=sorted({canon(h) for h in permutations(range(6))})
def cross(u,v):return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def norm(u):
 g=reduce(gcd,u)
 assert g != 0
 u=tuple(x//g for x in u)
 s=next(x for x in u if x)
 return tuple(-x for x in u) if s<0 else u

def conic(t):return (1,t,t*t)
T=(0,1,3,9,27,81)
P=[conic(t) for t in T]
def pascal(h):
 sides=[cross(P[h[i]],P[h[(i+1)%6]]) for i in range(6)]
 inter=[norm(cross(sides[i],sides[i+3])) for i in range(3)]
 l=norm(cross(inter[0],inter[1]))
 assert sum(x*y for x,y in zip(l,inter[2]))==0
 return l
lines=[pascal(h) for h in H]
assert len(set(lines))==60
idx={h:i for i,h in enumerate(H)}
def signature(h):
 e=lambda i: frozenset((h[i],h[(i+1)%6]))
 return frozenset(e(i) for i in range(6))
E=[signature(h) for h in H]
kirk={frozenset(i for i,e in enumerate(E) if e.isdisjoint(e0)) for e0 in E}
assert len(kirk)==60

def trikey(h):
 q=lambda v:min(v,v[1:]+v[:1],v[2:]+v[:2])
 a=tuple(sorted(q(h[i::2]) for i in (0,1)))
 b=tuple(sorted(q(tuple(reversed(h[i::2]))) for i in (0,1)))
 return min(a,b)
from collections import defaultdict
steiner=defaultdict(set)
for i,h in enumerate(H):steiner[trikey(h)].add(i)
S={frozenset(x) for x in steiner.values()}
assert len(S)==20
points={}
for role,triples in [('K',kirk),('S',S)]:
 for tr in triples:
  a,b,c=sorted(tr)
  p=norm(cross(lines[a],lines[b]))
  assert sum(x*y for x,y in zip(p,lines[c]))==0
  assert p not in points, ('Coincident distinguished points',points.get(p),role)
  points[p]=role
print('EXACT_RATIONAL_PASCAL_GEOMETRY_VERIFIED_OK')
print('six_parameters=',T,'distinct_pascal_lines=',len(set(lines)))
print('distinct_steiner_points=',len(S),'distinct_kirkman_points=',len(kirk))
