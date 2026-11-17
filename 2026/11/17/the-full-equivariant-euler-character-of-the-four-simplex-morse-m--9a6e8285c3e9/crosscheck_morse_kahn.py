#!/usr/bin/env python3
"""Independent finite check of cycle tests by directed full Hasse graph."""
from collections import Counter
from morse_equivariant_euler import simplex_model,representative

def direct_orbits(partition):
 n=sum(partition);cover,_=simplex_model(n);p=representative(partition)
 def act(a):
  return sum(1<<p[i] for i in range(n) if (a>>i)&1)
 lookup={pair:i for i,pair in enumerate(cover)}
 visited=set();valid=[]
 for start in range(len(cover)):
  if start in visited:continue
  orbit=[];j=start
  while j not in visited:
   visited.add(j);orbit.append(j);a,b=cover[j];j=lookup[(act(a),act(b))]
  assert j==start
  ends=0
  for k in orbit:
   a,b=cover[k];new=(1<<a)|(1<<b)
   if ends&new:break
   ends|=new
  else: valid.append((ends,sum(1<<k for k in orbit)))
 valid.sort(key=lambda x:x[0].bit_count(),reverse=True)
 return cover,valid

def acyclic_by_full_hasse(matched,covers,n):
 # Direct *all* Hasse incidence edges down, reversing matched edges up.
 adj=[[] for _ in range(1<<n)]
 indeg=[0]*(1<<n)
 for i,(a,b) in enumerate(covers):
  if matched&(1<<i):src,dst=a,b
  else:src,dst=b,a
  adj[src].append(dst);indeg[dst]+=1
 q=[a for a in range(1,1<<n) if indeg[a]==0]
 done=0
 while q:
  src=q.pop();done+=1
  for dst in adj[src]:
   indeg[dst]-=1
   if indeg[dst]==0:q.append(dst)
 return done==(1<<n)-1

def calc(partition):
 cover,candidates=direct_orbits(partition)
 count=Counter();raw=[0]
 def rec(j,used,selected,n_orbits):
  if j==len(candidates):
   raw[0]+=1
   if acyclic_by_full_hasse(selected,cover,sum(partition)):
    count[n_orbits]+=1
   return
  rec(j+1,used,selected,n_orbits)
  facebits,edgebits=candidates[j]
  if not used&facebits:
   rec(j+1,used|facebits,selected|edgebits,n_orbits+1)
 rec(0,0,0,0)
 lefs=-sum(((-1)**k)*v for k,v in count.items())
 return lefs,sum(count.values()),raw[0]

if __name__=='__main__':
 for part in [(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]:
  l,f,r=calc(part)
  print('KAHN_FULL_HASSE',part,'reduced_lefschetz',l,'valid',f,'raw_matching_orbit_subsets',r,flush=True)
 assert [calc(p)[0] for p in [(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]]==[-16,0,-1,-1,0,1]
 print('INDEPENDENT_HASSE_ORIENTATION_CHECK_PASS')
