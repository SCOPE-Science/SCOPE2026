#!/usr/bin/env python3
"""Independent exhaustive state-iterate check; requires NumPy."""
import numpy as np
from collections import Counter
EDGES=((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))
N=3**12; pp=3**np.arange(12,dtype=np.int64)
adj=[[] for _ in range(12)]
for v,w in EDGES: adj[v].append(w);adj[w].append(v)
assert all(len(row)==4 for row in adj)
index=np.arange(N,dtype=np.int64)
digits=(index[None,:]//pp[:,None]%3).astype(np.uint8)

def successor(mode):
 out=np.empty_like(digits)
 for v in range(12):
  val=digits[v]; following=(val+1)%3
  if mode=='CCA':
   cond=np.zeros(N,dtype=bool)
   for w in adj[v]: cond|=(digits[w]==following)
   out[v]=np.where(cond,following,val)
  else:
   cond=np.zeros(N,dtype=bool)
   for w in adj[v]: cond|=(digits[w]==1)
   out[v]=np.where(val!=0,following,np.where(cond,1,0))
 return np.sum(out.astype(np.int64)*pp[:,None],axis=0).astype(np.int32)

def census(mode):
 f=successor(mode)
 states=[np.arange(N,dtype=np.int32)]
 for t in range(24): states.append(f[states[-1]])
 entry=np.full(N,-1,dtype=np.int16); period=np.full(N,-1,dtype=np.int16)
 for t in range(13):
  for p in range(1,13):
   match=(entry<0)&(states[t]==states[t+p]);entry[match]=t;period[match]=p
 assert np.all(entry>=0)
 counts=Counter(zip(entry.tolist(),period.tolist()))
 orbits=Counter()
 for (t,p),n in counts.items():
  if t==0:
   assert n%p==0
   orbits[p]+=n//p
 print(mode,'orbits',sorted(orbits.items()),'maxentry',entry.max(),'states',sum(counts.values()))
 return entry,period,counts,orbits

a,pa,ca,oa=census('CCA')
b,pb,cb,ob=census('GH')
period_cross=Counter(zip(pa.tolist(),pb.tolist()))
print('period pairs',sorted(period_cross.items()))
print('period mismatches',int(np.count_nonzero(pa!=pb)))
print('maximum entry shells',int((a==a.max()).sum()),int((b==b.max()).sum()))
assert list(sorted(oa.items()))==[(1,3),(3,4768),(4,882),(7,3036),(10,1512),(11,48)]
assert list(sorted(ob.items()))==[(1,1),(3,4768),(4,294),(7,1012),(10,504),(11,8)]
assert np.array_equal(pa,pb)
assert int(a.max())==8 and int(b.max())==10
assert len(ca)==len(set(ca)) and len(cb)==len(set(cb))
