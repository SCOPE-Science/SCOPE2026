#!/usr/bin/env python3
"""Independent matching-permutation and three-position switch verification."""
from collections import Counter,deque
from itertools import combinations

n=8
vcount=16
adj=[set() for _ in range(vcount)]
for i in range(n):
 for a,b in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+3)%n)):
  adj[a].add(b);adj[b].add(a)
assert all(len(s)==3 for s in adj)
colors=[-1]*vcount;colors[0]=0;Q=deque([0])
while Q:
 a=Q.popleft()
 for b in adj[a]:
  if colors[b]==-1:colors[b]=1-colors[a];Q.append(b)
  else:assert colors[a]!=colors[b]
L=[i for i in range(vcount) if colors[i]==0]
R=[i for i in range(vcount) if colors[i]==1]
assert len(L)==len(R)==8
Rindex={v:j for j,v in enumerate(R)}
allowed=[[Rindex[b] for b in sorted(adj[a])] for a in L]
perms=[]
def fill(k,used,seq):
 if k==8:
  perms.append(tuple(seq));return
 for j in allowed[k]:
  if not (used>>j&1):fill(k+1,used|(1<<j),seq+[j])
fill(0,0,[])
perms.sort()
assert len(perms)==33

signs=[]
for p in perms:
 inv=sum(p[a]>p[b] for a in range(8) for b in range(a+1,8))
 signs.append(-1 if inv%2 else 1)
assert Counter(signs)=={1:3,-1:30}
# Any two distinct valid bijections that differ at exactly 3 left vertices
# have a simple alternating 6-cycle as symmetric difference.
links=[set() for _ in perms]
for a in range(len(perms)):
 for b in range(a+1,len(perms)):
  H=sum(x!=y for x,y in zip(perms[a],perms[b]))
  if H==3:
   links[a].add(b);links[b].add(a)
   assert signs[a]==signs[b]
assert sum(map(len,links))//2==96
comps=[];rem=set(range(33))
while rem:
 base=min(rem);comp={base};queue=[base]
 for k in queue:
  for j in links[k]:
   if j not in comp:comp.add(j);queue.append(j)
 rem-=comp;comps.append(comp)
assert sorted(map(len,comps))==[1,1,1,30]
long=next(c for c in comps if len(c)==30)
assert {signs[x] for x in long}=={-1}
assert all(len(links[next(iter(c))])==0 for c in comps if len(c)==1)
assert Counter(map(len,links))=={0:3,6:24,8:6}

# Reconstruct individual edge masks to compare with an independently generated
# certificate, without using its cycle enumerator.
import json,sys
if len(sys.argv)>1:
 cert=json.load(open(sys.argv[1],encoding='utf-8'))
 edge_map={tuple(x):k for k,x in enumerate(cert['edge_order'])}
 assert L==cert['left_order'] and R==cert['right_order']
 mask_to_perm={}
 for i,p in enumerate(perms):
  mask=0
  for a,b in enumerate(p):
   e=tuple(sorted((L[a],R[b])))
   mask |=1<<edge_map[e]
  mask_to_perm[mask]=i
 assert set(mask_to_perm)=={int(x,16) for x in cert['matching_masks']}
 mids=[int(x,16) for x in cert['matching_masks']]
 for i,m in enumerate(mids):
  assert {mask_to_perm[mids[j]] for j in cert['flip_adjacency'][i]}==links[mask_to_perm[m]]
 print('INDEPENDENT_CERTIFICATE_OK 33_matchings_all_adjacencies_identical=true')

maxdist=0
for a in long:
 dist={a:0};queue=[a]
 for x in queue:
  for b in links[x]:
   if b not in dist:dist[b]=dist[x]+1;queue.append(b)
 assert len(dist)==30
 maxdist=max(maxdist,max(dist.values()))
assert maxdist==4
print('PERMUTATION_VERIFY_OK bijections=33 signs=30+3 switches=96')
print('PERMUTATION_VERIFY_OK components=30+1+1+1 degrees=6x24+8x6 diameter=4')
