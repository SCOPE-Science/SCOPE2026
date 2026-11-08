#!/usr/bin/env python3
'''Exact verification of the 21 reflection-line configuration over Z[w]/(w^2+w+2).'''
from collections import Counter
from itertools import combinations
I=(1,0); Z=(0,0); W=(0,1)
def c(n):return (n,0)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]-2*a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def norm(a):return a[0]**2-a[0]*a[1]+2*a[1]**2
def det(v):
 x,y,z=v
 return sub(add(add(mul(x[0],mul(y[1],z[2])),mul(x[1],mul(y[2],z[0]))),mul(x[2],mul(y[0],z[1]))),add(add(mul(x[2],mul(y[1],z[0])),mul(x[1],mul(y[0],z[2]))),mul(x[0],mul(y[2],z[1]))))
mi=neg(I);mw=neg(W)
L=[(I,Z,Z),(Z,I,I),(W,I,mi),(W,mi,I),(Z,mi,I),(I,W,mi),(W,mi,mi),(mi,I,W),(W,I,I),(mi,W,I),(mi,mi,W),(I,Z,I),(mi,W,mi),(I,W,I),(mi,Z,I),(I,mi,W),(I,I,W),(Z,Z,I),(mi,I,Z),(I,I,Z),(Z,I,Z)]
assert len(L)==21
D={t:det([L[i] for i in t]) for t in combinations(range(21),3)}
N=Counter(norm(a) for a in D.values())
assert 0 in N and all(n>0 and (n&(n-1))==0 for n in N if n)
classes=set()
for i,j in combinations(range(21),2):
 through=frozenset([i,j]+[k for k in range(21) if k not in (i,j) and D[tuple(sorted((i,j,k)))]==Z])
 classes.add(through)
M=Counter(len(g) for g in classes)
assert M=={3:28,4:21},M
assert sum(m*(m-1)//2 for m in M.elements())==210
print('TOTAL_TRIPLES',len(D),'DETERMINANT_NORMS',dict(sorted(N.items())))
print('INTERSECTION_CLASSES',dict(sorted(M.items())))
for q in (7,9,11,23,25,49,81,121):
 print('EXPECTED_COMPLEMENT',q,(q-9)*(q-11))
print('CERTIFICATE_OK')
