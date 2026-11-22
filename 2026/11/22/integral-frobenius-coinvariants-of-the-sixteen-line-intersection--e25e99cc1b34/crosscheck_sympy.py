#!/usr/bin/env python3
"""Independent SymPy Smith-normal-form crosscheck of the Clebsch line adjacency quotient.
Requires Python >=3.9 and SymPy. No network or downloaded data.
"""
from itertools import permutations
from collections import Counter
from sympy import Matrix, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

vertices=tuple(x for x in range(32) if x.bit_count()%2)
where={x:i for i,x in enumerate(vertices)}
A=Matrix(16,16,lambda i,j:int((vertices[i]^vertices[j]).bit_count()==4))
assert tuple(abs(int(x)) for x in smith_normal_form(A,domain=ZZ).diagonal()) == (1,)*11+(3,)*4+(15,)

def signed_type(p,flip):
 seen=set();res=[]
 for i in range(5):
  if i in seen:continue
  k=i;length=0;sign=0
  while k not in seen:
   seen.add(k);length+=1;sign^=(flip>>k)&1;k=p[k]
  res.append((length,sign))
 return tuple(sorted(res))

def coin(p,flip):
 g=[]
 for x in vertices:
  y=flip
  for i in range(5):
   if (x>>i)&1:y ^= 1<<p[i]
  g.append(where[y])
 ids=[-1]*16;n=0
 for i in range(16):
  if ids[i]!=-1:continue
  j=i
  while ids[j]==-1:ids[j]=n;j=g[j]
  n+=1
 B=zeros(n,n)
 for z in range(n):
  rep=ids.index(z)
  for i in range(16):B[ids[i],z]+=A[i,rep]
 ds=tuple(abs(int(x)) for x in smith_normal_form(B,domain=ZZ).diagonal())
 assert len(ds)==n and all(x>0 for x in ds)
 return tuple(x for x in ds if x>1)

expected={
 ((1,0),(1,0),(1,0),(1,0),(1,0)):(1,(3,3,3,3,15)),
 ((1,0),(1,0),(1,0),(1,1),(1,1)):(10,(3,3,15)),
 ((1,0),(1,0),(1,0),(2,0)):(20,(3,3,3,15)),
 ((1,0),(1,0),(1,1),(2,1)):(60,(3,15)),
 ((1,0),(1,0),(3,0)):(80,(3,3,15)),
 ((1,0),(1,1),(1,1),(1,1),(1,1)):(5,(15,)),
 ((1,0),(1,1),(1,1),(2,0)):(60,(3,15)),
 ((1,0),(1,1),(3,1)):(160,(15,)),
 ((1,0),(2,0),(2,0)):(60,(3,3,15)),
 ((1,0),(2,1),(2,1)):(60,(15,)),
 ((1,0),(4,0)):(240,(3,15)),
 ((1,1),(1,1),(1,1),(2,1)):(20,(5,)),
 ((1,1),(1,1),(3,0)):(80,(15,)),
 ((1,1),(2,0),(2,1)):(120,(15,)),
 ((1,1),(4,1)):(240,(5,)),
 ((2,0),(3,0)):(160,(3,15)),
 ((2,1),(3,1)):(160,(5,)),
 ((5,0),):(384,(15,))
}
count=Counter()
for p in permutations(range(5)):
 for flip in range(32):
  if flip.bit_count()%2:continue
  t=signed_type(p,flip);count[t]+=1
  assert coin(p,flip)==expected[t][1],t
assert len(count)==18 and sum(count.values())==1920
assert all(count[t]==n for t,(n,_) in expected.items())
print('SymPy independent Smith normal forms of 1920 quotients: PASS')
