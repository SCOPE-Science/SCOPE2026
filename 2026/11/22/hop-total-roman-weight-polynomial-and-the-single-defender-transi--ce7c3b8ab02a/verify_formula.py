#!/usr/bin/env python3
"""Evaluate the exact polynomial from its elementary factorization."""
from math import comb
from collections import defaultdict

def add(*polys):
 o=defaultdict(int)
 for p in polys:
  for k,v in p.items():o[k]+=v
 return {k:v for k,v in o.items() if v}
def mul(*polys):
 d={0:1}
 for p in polys:
  q=defaultdict(int)
  for i,vi in d.items():
   for j,vj in p.items(): q[i+j]+=vi*vj
  d=dict(q)
 return d
def neg(p):return {k:-v for k,v in p.items()}
def pw(p,n):return mul(*(p for _ in range(n)))
def poly(ss):
 M=sum(ss)
 A=[pw({0:1,1:1,2:1},s) for s in ss]
 B=[pw({0:1,1:1},s) for s in ss]
 D=[add(pw({1:1,2:1},s),neg({s:1})) for s in ss]
 C=[add(A[i],neg(B[i])) for i in range(len(ss))]
 p=add(mul(*A),neg(mul(*B)))
 for i in range(len(ss)):
  p=add(p,mul(D[i],*(B[j] for j in range(len(ss)) if j!=i)),neg(mul(C[i],*(B[j] for j in range(len(ss)) if j!=i))))
 p=add(p,{M:1})
 return mul({1:1,2:1},p)
def main():
 for ss in ((2,2),(2,3),(3,3),(2,2,2),(3,4),(2,3,3),(4,4),(2,2,3,3),(3,3,3),(4,4,4)):
  p=poly(ss)
  print(','.join(map(str,ss)), 'gamma=',min(p), 'minCount=',p[min(p)], 'total=',sum(p.values()), 'poly=',sorted(p.items()))
  r2=sum(s==2 for s in ss);r3=sum(s==3 for s in ss)
  pred=2*r2 if r2 else sum(ss[i]*ss[j] for i in range(len(ss)) for j in range(i+1,len(ss))) +3*r3
  assert min(p)==(4 if r2 else 5) and p[min(p)]==pred
if __name__=='__main__': main()
