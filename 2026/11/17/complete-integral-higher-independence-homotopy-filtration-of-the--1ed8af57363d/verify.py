#!/usr/bin/env python3
"""Exhaustive integer verification of the r-independence homotopy types of the 15-vertex full binary tree."""
from collections import Counter, deque
N=15
A=[0]*N
for i in range(7):
 for j in (2*i+1,2*i+2):
  A[i]|=1<<j
  A[j]|=1<<i
ORDERS={
1:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
2:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
3:[10,1,6,7,12,13,0,3,8,11,5,2,9,4,14],
4:[8,2,11,5,12,13,9,7,10,1,0,4,14,3,6],
5:[2,3,10,6,12,0,9,5,14,8,4,13,11,1,7],
6:[7,8,10,12,6,11,5,0,14,9,2,1,3,13,4],
7:[7,14,4,1,5,12,10,8,9,6,11,0,2,3,13],
8:[3,14,7,8,2,0,6,13,4,5,12,11,1,10,9],
9:[5,14,0,8,4,3,6,2,10,12,11,7,13,1,9],
10:[5,1,8,4,12,3,7,13,14,2,10,11,6,0,9],
11:[6,14,0,3,2,10,9,8,1,4,5,11,13,12,7],
12:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
13:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
14:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
15:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
}
EXPECTED={1:{},2:{},3:{5:1},4:{7:9},5:{9:9},6:{11:1},7:{6:1},8:{7:7},9:{8:21},10:{9:35},11:{10:35},12:{11:21},13:{12:7},14:{13:1},15:{}}

def largest_component(mask):
 remain=mask; maximum=0
 while remain:
  component=0; frontier=remain & -remain
  while frontier:
   bit=frontier & -frontier; frontier ^=bit
   if component & bit:continue
   component |=bit
   v=bit.bit_length()-1
   frontier |= A[v] & mask & ~component
  maximum=max(maximum,component.bit_count())
  remain &=~component
 return maximum

LARGEST=[largest_component(m) for m in range(1<<N)]
assert LARGEST[0]==0 and LARGEST[(1<<N)-1]==15
for r in range(1,16):
 faces=[f for f in range(1,1<<N) if LARGEST[f]<=r]
 allfaces=set(faces)|{0}
 unused=set(allfaces); pairs=[]
 assert sorted(ORDERS[r])==list(range(N))
 for v in ORDERS[r]:
  bit=1<<v
  for f in faces:
   if (f&bit) or f not in unused:continue
   hi=f|bit
   if hi in unused:
    unused.remove(f);unused.remove(hi);pairs.append((f,hi))
  if 0 in unused and bit in unused:
   unused.remove(0);unused.remove(bit);pairs.append((0,bit))
 pairs=set(pairs)
 assert 2*len(pairs)+len(unused)==len(allfaces)
 critical=dict(Counter(f.bit_count()-1 for f in unused))
 assert critical==EXPECTED[r], (r,critical)
 # Construct and topologically order the whole directed gradient Hasse graph:
 out={f:[] for f in allfaces}; indeg={f:0 for f in allfaces}
 for upper in allfaces:
  bits=upper
  while bits:
   lowbit=bits&-bits;bits^=lowbit;lower=upper^lowbit
   assert lower in allfaces
   source,target=(lower,upper) if (lower,upper) in pairs else (upper,lower)
   out[source].append(target);indeg[target]+=1
 queue=deque(f for f in allfaces if indeg[f]==0);visited=0
 while queue:
  f=queue.popleft();visited+=1
  for g in out[f]:
   indeg[g]-=1
   if indeg[g]==0:queue.append(g)
 assert visited==len(allfaces), (r,'cycle in directed Morse Hasse graph')
 alternate=sum((-1)**(f.bit_count()-1) for f in faces)-1
 alternatemorse=sum((-1)**d*n for d,n in critical.items())
 assert alternate==alternatemorse,(r,alternate,alternatemorse)
 print(f'r={r:2d} faces={len(faces):5d} pairs={len(pairs):5d} critical={critical} gradient_DAG_nodes={visited}')
print('PASS: every face, matching pair, directed Hasse cover, critical dimension and Euler value verified for all fifteen thresholds.')
