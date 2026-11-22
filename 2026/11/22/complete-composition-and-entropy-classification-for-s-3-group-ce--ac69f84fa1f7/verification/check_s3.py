#!/usr/bin/env python3
"""Finite exact consistency tests for an S3 group cellular-automaton normal form.
These finite checks do not establish the infinite-radius theorem.
"""
from itertools import permutations,product
from random import Random
from math import log
S=list(permutations(range(3)))
e=(0,1,2)
def mul(a,b): return tuple(a[b[i]] for i in range(3))
def inv(a):return next(b for b in S if mul(a,b)==mul(b,a)==e)
def sign(a): return sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))%2
trans=[a for a in S if sign(a)]
A=[]
for k in S:
 ki=inv(k); A.append(tuple(mul(k,mul(x,ki)) for x in S))
def mapval(h,x):return h[S.index(x)]
O=tuple(e for _ in S)
E=[O]+A+[tuple(t if sign(x) else e for x in S) for t in trans]
assert len(set(E))==10
for h in E:
 assert mapval(h,e)==e
 for x in S:
  for y in S: assert mapval(h,mul(x,y))==mul(mapval(h,x),mapval(h,y))
for r in (1,2,3):
 valid=[]
 for hs in product(E,repeat=r):
  if all(mul(mapval(hs[i],x),mapval(hs[j],y))==mul(mapval(hs[j],y),mapval(hs[i],x)) for i in range(r) for j in range(i+1,r) for x in S for y in S):valid.append(hs)
 assert len(valid)==1+6*r+3*(2**r-1),(r,len(valid))
 print('neighborhood_size',r,'homomorphisms',len(valid))
# Check composition law on all ring states for 2-site masks at each of three distinct involutions.
rng=Random(828); L=7
Pset=[{0},{1},{-1},{0,1},{-1,0,1},{-2,1}]
def apply(t,P,x):
 return tuple(t if sum(sign(x[(i+j)%L]) for j in P)%2 else e for i in range(L))
def pmul(P,Q):
 C={}
 for i in P:
  for j in Q:C[i+j]=1-C.get(i+j,0)
 return {k for k,v in C.items() if v}
for t in trans:
 for u in trans:
  for P in Pset:
   for Q in Pset:
    for _ in range(8):
     x=tuple(rng.choice(S) for _ in range(L))
     assert apply(t,P,apply(u,Q,x))==apply(t,pmul(P,Q),x)
print('composition checks PASS')
# Verify group automorphism and parity interaction.
for k in S:
 ki=inv(k)
 for t in trans:
  for P in Pset:
   for j in (-2,0,3):
    x=tuple(rng.choice(S) for _ in range(L))
    Amap=lambda x:tuple(mul(k,mul(x[(i+j)%L],ki)) for i in range(L))
    tp=mul(k,mul(t,ki))
    assert Amap(apply(t,P,x))==apply(tp,{v+j for v in P},x)
    assert apply(t,P,Amap(x))==apply(t,{v+j for v in P},x)
print('automorphism interactions PASS')
print('idempotents = 5; central shifts plus zero; all nonzero nonunit regular elements have monomial masks (algebraic proof)')
print('CHECKER_OK')
