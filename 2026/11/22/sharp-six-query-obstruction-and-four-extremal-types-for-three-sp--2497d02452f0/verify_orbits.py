#!/usr/bin/env python3
from collections import Counter
n=9
S={tuple(map(int,line.split())) for line in open('best_kernels_9.txt')}
def canon(rows):
 r=list(rows); rank=0
 for c in range(n):
  piv=next((i for i in range(rank,3) if (r[i]>>c)&1),None)
  if piv is None:continue
  r[piv],r[rank]=r[rank],r[piv]
  for i in range(3):
   if i!=rank and ((r[i]>>c)&1):r[i]^=r[rank]
  rank+=1
  if rank==3:break
 assert rank==3
 return tuple(r)
def swap(row,c):
 a=(row>>c)&1;b=(row>>(c+1))&1
 return row^(((a^b)<<c)|((a^b)<<(c+1)))
assert len(S)==2304
orbits=[]
while S:
 start=next(iter(S));q=[start];S.remove(start)
 for x in q:
  for c in range(n-1):
   y=canon([swap(v,c) for v in x])
   if y in S:S.remove(y);q.append(y)
 orbits.append((len(q),min(q)))
print(sorted(orbits,reverse=True))
