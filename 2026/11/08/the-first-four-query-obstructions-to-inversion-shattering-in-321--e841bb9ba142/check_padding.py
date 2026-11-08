#!/usr/bin/env python3
"""Independent check of pattern-preserving expansion on selected positions."""
from itertools import combinations, permutations

def avoid(p):
 for i in range(len(p)):
  for j in range(i+1,len(p)):
   if p[i] <= p[j]: continue
   for k in range(j+1,len(p)):
    if p[j]>p[k]: return False
 return True

def lift(base,indices,n):
 m=len(base)
 starts=[0]+[indices[j] for j in range(1,m)]
 ends=[indices[j] for j in range(1,m)]+[n]
 size=[b-a for a,b in zip(starts,ends)]
 out=[None]*n
 for j in range(m):
  lo=sum(size[t] for t in range(m) if base[t]<base[j])
  for i in range(starts[j],ends[j]):out[i]=lo+(i-starts[j])
 assert tuple(out[i] for i in indices) and len(set(out))==n
 return out

total=0
for n in range(1,9):
 for m in range(1,n+1):
  for q in permutations(range(m)):
   if not avoid(q):continue
   for ids in combinations(range(n),m):
    p=lift(q,ids,n)
    assert avoid(p)
    for a in range(m):
     for b in range(a+1,m):
      assert (p[ids[a]]>p[ids[b]])==(q[a]>q[b])
    total+=1
print('PADDING_321_PASS',total)
