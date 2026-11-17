#!/usr/bin/env python3
"""Independent finite checks for sharp geometric decay in three-state excitation."""
from itertools import product
from math import ceil

def layered(delta,theta,h):
 b=delta-theta
 assert 0<b<theta
 sizes=[1]
 if h>=1:
  sizes.append(theta)
 for i in range(2,h+1):
  sizes.append(ceil(theta*sizes[-1]/b))
 sizes=sizes[::-1]
 offsets=[0]
 for m in sizes: offsets.append(offsets[-1]+m)
 adj=[set() for i in range(offsets[-1])]
 for t in range(h):
  a=sizes[t];c=sizes[t+1]
  for j in range(c):
   for k in range(theta):
    u=offsets[t]+((theta*j+k)%a)
    v=offsets[t+1]+j
    adj[u].add(v);adj[v].add(u)
 assert all(len(x)<=delta for x in adj)
 assert len(adj)==offsets[-1]
 return adj,sizes,offsets

def step(adj,x,theta):
 return tuple(2 if x[v]==1 else (1 if x[v]==0 and sum(x[w]==1 for w in adj[v])>=theta else 0) for v in range(len(x)))

def verify_wave(delta,theta,h):
 adj,sizes,o=layered(delta,theta,h)
 x=tuple([1]*sizes[0]+[0]*(o[-1]-sizes[0]))
 counts=[]
 for t in range(h+3):
  counts.append(sum(z==1 for z in x))
  expected=[i for i in range(o[t],o[t+1])] if t<=h else []
  assert [i for i,z in enumerate(x) if z==1]==expected,(delta,theta,h,t)
  x=step(adj,x,theta)
 assert not any(x)
 assert counts==sizes+[0,0],(counts,sizes)
 return sizes,o[-1]

for delta,theta in [(3,2),(5,3),(7,4),(7,5),(8,5),(9,7)]:
 for h in range(1,5):
  sizes,n=verify_wave(delta,theta,h)
  print('WAVE',delta,theta,h,n,','.join(map(str,sizes)))
# Independent exhaustive check of inequality on all states of small nontrivial graphs.
for delta,theta in [(3,2),(4,3),(5,3)]:
 for h in [1,2]:
  adj,sizes,o=layered(delta,theta,h)
  if len(adj)>9: continue
  for x in product(range(3), repeat=len(adj)):
   xs=[x]
   for t in range(3):xs.append(step(adj,xs[-1],theta))
   a=[sum(z==1 for z in v) for v in xs]
   assert theta*a[2]<=(delta-theta)*a[1],(delta,theta,h,x,a)
   assert theta*a[3]<=(delta-theta)*a[2],(delta,theta,h,x,a)
  print('EXHAUSTIVE',delta,theta,h,len(adj),3**len(adj))
print('PASS')
