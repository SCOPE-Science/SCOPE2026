"""Finite checks of antipodal fixed graphic-forest complexes, ordinary definitions."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import factorial

def acyclic(n,edgelist):
 p=list(range(n))
 def find(x):
  while p[x]!=x:
   p[x]=p[p[x]];x=p[x]
  return x
 for u,v in edgelist:
  a,b=find(u),find(v)
  if a==b:return False
  p[a]=b
 return True

def orbit_classes(m):
 n=2*m
 edges=list(combinations(range(n),2));seen=set(); arr=[]; labels=[]
 for e in edges:
  if e in seen:continue
  a,b=e
  ep=tuple(sorted(((a+m)%n,(b+m)%n)))
  orb=tuple(sorted({e,ep}));seen.update(orb)
  if len(orb)==1:
   label=(0,a%m)
  else:
   u,v=a%m,b%m
   if u>v:u,v=v,u
   # plus type: pairs within same half; minus: cross-half
   typ=1 if a//m==b//m else 2
   label=(typ,u,v)
  arr.append(orb);labels.append(label)
 return arr,labels

def contracted_edge(label):
 if label[0]==0:return 0,label[1]+1
 return label[1]+1,label[2]+1

def verify(m):
 orbits,labels=orbit_classes(m)
 assert len(labels)==m*m
 count0=Counter();count1=Counter();checks=0
 for r in range(len(labels)+1):
  for idx in combinations(range(len(labels)),r):
   es=[e for j in idx for e in orbits[j]]
   es2=[contracted_edge(labels[j]) for j in idx]
   v=acyclic(2*m,es);w=acyclic(m+1,es2)
   assert v==w,('Mismatch',m,idx,labels,es,es2)
   checks+=1
   if v:count0[r]+=1
   if w:count1[r]+=1
 assert count0==count1
 beta=(-1)**m*sum((-1)**s*v for s,v in count0.items())
 assert beta>=0
 print('m',m,'orbits',len(labels),'subsets',checks,'face_vector',dict(sorted(count0.items())),'top_beta',beta)
 return beta
for m in range(1,5):
 b=verify(m)
 assert b=={1:0,2:2,3:24,4:396}[m]
print('ANTIPODAL_FOREST_QUOTIENT_MATCH_PASS')
