#!/usr/bin/env python3
"""Finite direct checks of geometric subgroup-fixed dissociation complexes.
Facets are derived from induced components, not from the homotopy argument.
"""
from collections import defaultdict
def reduced_betti(F):
    """Augmented simplicial chain ranks over GF(2), independent of theorem."""
    ranks={}
    maxdim=max(F)
    for d in range(0,maxdim+1):
        indexes={f:i for i,f in enumerate(F[d-1])}
        pivots={}
        for x in F[d]:
            column=0
            sub=x
            while sub:
                bit=sub & -sub
                sub ^= bit
                column ^= 1 << indexes[x^bit]
            while column:
                k=column.bit_length()-1
                if k in pivots:column ^= pivots[k]
                else:pivots[k]=column;break
        ranks[d]=len(pivots)
    return {d:len(F[d])-ranks.get(d,0)-ranks.get(d+1,0)
            for d in range(-1,maxdim+1)
            if len(F[d])-ranks.get(d,0)-ranks.get(d+1,0)}

from itertools import combinations

def partitions(n,low=1):
 if n==0:
  yield ()
 else:
  for s in range(low,n+1):
   for q in partitions(n-s,s):yield (s,)+q

def face_mask_ok(fullmask, adj, r=2):
 left=fullmask
 while left:
  bit=left&-left; left-=bit; comp=bit;front=bit
  while front:
   b=front&-front;front-=b
   v=b.bit_length()-1
   nei=adj[v]&left
   left^=nei;front|=nei;comp|=nei
  if comp.bit_count()>r:return False
 return True

def fixed_complex(part):
 m=sum(part);n=1+3*m
 adj=[0]*n
 # c=0, block arm i uses indices 1+3*i,2+3*i,3+3*i
 for i in range(m):
  path=[0,1+3*i,2+3*i,3+3*i]
  for x,y in zip(path,path[1:]):
   adj[x]|=1<<y;adj[y]|=1<<x
 orbits=[1]  # hub
 idx=0
 for sz in part:
  for t in range(3):
   orbit=0
   for i in range(idx,idx+sz):orbit|=1<<(1+3*i+t)
   orbits.append(orbit)
  idx+=sz
 F=defaultdict(list)
 for mask in range(1<<len(orbits)):
  original=0
  for j,orbit in enumerate(orbits):
   if mask>>j&1:original|=orbit
  if face_mask_ok(original,adj):F[mask.bit_count()-1].append(mask)
 return F

def main():
 count=0;faces_total=0
 for m in range(2,6):
  for part in partitions(m):
   F=fixed_complex(part)
   betti=reduced_betti(F)
   predicted={2*len(part)-1:1}
   assert betti==predicted,(m,part,betti,predicted)
   count+=1;faces_total+=sum(map(len,F.values()))
   print('m=%d H_arm_orbit_sizes=%s reduced_betti=%s faces=%d OK'%(
      m,part,betti,sum(map(len,F.values()))))
 print('FIXED_ORBIT_PARTITIONS_CHECKED',count)
 print('FIXED_COMPLEX_FACES_PROCESSED',faces_total)
 print('ALL_FIXED_SPIDER_CHECKS_OK')
if __name__=='__main__':main()
