#!/usr/bin/env python3
"""Independent finite-field enumeration for the projective involution commuting law.
Use: python pgl2_dual_check.py . No dependencies outside Python's standard library.
This script checks finite prime fields q=3 and q=5 directly, not a general proof.
"""
from itertools import product
from collections import Counter

def prod(A,B,p):
 a,b,c,d=A; e,f,g,h=B
 return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)

def inv(A,p):
 a,b,c,d=A
 z=pow((a*d-b*c)%p,-1,p)
 return (d*z%p,-b*z%p,-c*z%p,a*z%p)

def add(A,B,p):return tuple((a+b)%p for a,b in zip(A,B))

def neg(A,p):return tuple((-a)%p for a in A)

def canon(A,p):
 s=next(x for x in A if x)
 t=pow(s,-1,p)
 return tuple(x*t%p for x in A)

def involution_test(q):
 allg={canon(A,q) for A in product(range(q),repeat=4) if (A[0]*A[3]-A[1]*A[2])%q}
 assert len(allg)==q*(q*q-1)
 bvals=sorted(A for A in allg if A!=(1,0,0,1) and prod(A,A,q)[1]==0 and prod(A,A,q)[2]==0 and prod(A,A,q)[0]==prod(A,A,q)[3]); assert len(bvals)==q*q
 vspace=[(x,y,z,(-x)%q) for x,y,z in product(range(q),repeat=3)]
 orbit={}
 for A in bvals:
  inva=inv(A,q)
  orbit[A]=[v for v in vspace if add(v,prod(prod(A,v,q),inva,q),q)==(0,0,0,0)]
  assert len(orbit[A])==q*q
 def commute(s,x,t,y):
  # Equation in semidirect product sl_2(k) : [x,s][y,t] = [y,t][x,s]
  if canon(prod(s,t,q),q)!=canon(prod(t,s,q),q):return False
  lhs=add(x,prod(prod(s,y,q),inv(s,q),q),q)
  rhs=add(y,prod(prod(t,x,q),inv(t,q),q),q)
  return lhs==rhs
 degree=Counter(); pair=0; perbase=Counter(); graph={}
 for A in bvals:
  xs=orbit[A]
  for x in xs:
   nei=0
   graph[(A,x)]=set()
   for B in bvals:
    if canon(prod(A,B,q),q)!=canon(prod(B,A,q),q):continue
    for y in orbit[B]:
     if commute(A,x,B,y):
      nei+=1
      perbase[(A,B)]+=1
      if (A,x)!=(B,y): graph[(A,x)].add((B,y))
   assert nei in (1+q*(q-1),1+q*(q+1)),(q,A,nei)
   degree[nei]+=1
   pair+=nei
 assert pair==q**6,(q,pair)
 assert degree[1+q*(q-1)]==q**3*(q+1)//2,(q,degree)
 assert degree[1+q*(q+1)]==q**3*(q-1)//2,(q,degree)
 for (A,B),n in perbase.items():assert n==(q*q if A==B else q**3),(q,A,B,n)
 assert (pair-q**4)%6==0
 assert sum(map(len,graph.values())) == pair-q**4
 for v,adj in graph.items():
  for w in adj:
   assert len(adj & graph[w])==1,(q,v,w)
 print(f'q={q}: |PGL2|={len(allg)}, involutions={q**4}, ordered commuting pairs={pair}, Klein fours={(pair-q**4)//6}, degrees={dict(degree)}')
for q in (3,5):involution_test(q)
print('PGL2_DUAL_INVOLUTION_CHECKS_PASSED')
