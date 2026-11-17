#!/usr/bin/env python3
"""Independent exact calculations for a sixty-four-point Hamming flag complex.
Python standard library only.
"""
from itertools import product,combinations
from collections import deque,Counter
from array import array
import time
T=time.monotonic()
V=list(product(range(4),repeat=3)); m=len(V)
N=[0]*m
for i in range(m):
 for j in range(m):
  if i!=j and sum(a!=b for a,b in zip(V[i],V[j]))<=2:N[i]|=1<<j
maxcl=[]
def bk(R,P,X):
 if P==0 and X==0:
  maxcl.append(R);return
 poss=P|X
 if poss:
  best=max((j for j in range(m) if poss>>j&1), key=lambda j:(P&N[j]).bit_count())
  candidates=P&~N[best]
 else:candidates=P
 while candidates:
  bit=candidates&-candidates;v=bit.bit_length()-1;candidates-=bit
  bk(R|bit,P&N[v],X&N[v]);P-=bit;X|=bit
bk(0,(1<<m)-1,0)
print('MAXIMAL_CLIQUES',len(maxcl),Counter(f.bit_count() for f in maxcl),flush=True)
assert Counter(f.bit_count() for f in maxcl)=={16:12,10:64,4:432}
allf={0}
for facet in maxcl:
 v=[i for i in range(m) if facet>>i&1]
 # expand each facet's power set
 subsets=[0]
 for j in v:subsets += [s|(1<<j) for s in subsets]
 allf.update(subsets)
print('ALL_FACES',len(allf),round(time.monotonic()-T,2),flush=True)
assert len(allf)==830101
# deterministic staged matching in the published theorem, independently implemented
unused=set(allf);pairs={}
for v in range(m):
 bit=1<<v
 # only lower faces; all at this stage are disjoint pairs
 for f in list(unused):
  if not(f&bit) and (f|bit) in unused:
   unused.discard(f);unused.discard(f|bit)
   pairs[f]=f|bit
print('MATCHED',len(pairs),'CRITICAL',len(unused),Counter(s.bit_count() for s in unused),round(time.monotonic()-T,2),flush=True)
assert len(pairs)==414848 and Counter(s.bit_count() for s in unused)=={4:405}
# matched includes empty; deduce ordinary matching vertex and 405 tetrahedra
# check whole augmented directed Hasse graph acyclic via explicit edges.
faces=sorted(allf)
idmap={s:i for i,s in enumerate(faces)}
in_deg=array('I',[0])*len(faces)
for upper in faces[1:]:
 mask=upper
 while mask:
  bit=mask&-mask;mask-=bit;lower=upper-bit
  if pairs.get(lower)==upper:in_deg[idmap[upper]]+=1
  else:in_deg[idmap[lower]]+=1
queue=deque(i for i,d in enumerate(in_deg) if d==0)
seen=0
while queue:
 ix=queue.popleft();seen+=1
 f=faces[ix]
 # outward unmatched upper->lower
 mask=f
 while mask:
  bit=mask&-mask;mask-=bit;lo=f-bit
  if pairs.get(lo)!=f:
   j=idmap[lo];in_deg[j]-=1
   if in_deg[j]==0:queue.append(j)
 # outward matched lower->upper
 if f in pairs:
  j=idmap[pairs[f]];in_deg[j]-=1
  if in_deg[j]==0:queue.append(j)
print('ACYCLIC_VISITED',seen,'TIME',round(time.monotonic()-T,2),flush=True)
assert seen==len(faces)
print('PREMISE_Q4_WEDGE_405_VERIFIED',flush=True)
