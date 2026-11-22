#!/usr/bin/env python3
"""Independent finite verifier on the GP(10,3) representation, no dependencies."""
import itertools
import json
from collections import Counter

N=20
edges=set()
for r in range(10):
 edges.add(tuple(sorted((r,(r+1)%10))))
 edges.add((r,10+r))
 edges.add(tuple(sorted((10+r,10+(r+3)%10))))
assert len(edges)==30
neighbors=[0]*N
for a,b in edges:
 neighbors[a]|=1<<b;neighbors[b]|=1<<a

def is_forest(deleted):
 parent=list(range(N))
 def find(x):
  while parent[x]!=x:
   x=parent[x]
  return x
 for a,b in edges:
  if (deleted>>a)&1 or (deleted>>b)&1:continue
  pa=find(a);pb=find(b)
  if pa==pb:return False
  parent[pa]=pb
 return True

opt=[]
for tup in itertools.combinations(range(N),6):
 s=0
 for v in tup:s|=1<<v
 if is_forest(s):opt.append(s)
assert len(opt)==2860
# No feedback set of size <=5 follows from cubic edge accounting;
# this extra enumeration checks that premise directly.
assert not any(is_forest(sum(1<<v for v in t)) for t in itertools.combinations(range(N),5))

index={s:i for i,s in enumerate(opt)}

def move_rows(local):
 out=[[] for _ in opt]
 for i,s in enumerate(opt):
  for v in range(N):
   if not (s>>v)&1:continue
   allowed=neighbors[v] if local else ((1<<N)-1)
   allowed &= ~s
   while allowed:
    bit=allowed&-allowed
    allowed^=bit
    target=s^(1<<v)^bit
    j=index.get(target)
    if j is not None:out[i].append(j)
  out[i]=sorted(set(out[i]))
 assert all(i in out[j] for i,row in enumerate(out) for j in row)
 return out

unrestricted=move_rows(False);restricted=move_rows(True)

def metric(rows):
 size=len(rows)
 all_dist=[]
 for r in range(size):
  lengths=[-1]*size
  lengths[r]=0
  queue=[r]
  for cur in queue:
   for nxt in rows[cur]:
    if lengths[nxt]<0:
     lengths[nxt]=lengths[cur]+1
     queue.append(nxt)
  assert len(queue)==size
  all_dist.append(lengths)
 return all_dist

D0=metric(unrestricted);D1=metric(restricted)
out={"states":len(opt),"jump_edges":sum(map(len,unrestricted))//2,"slide_edges":sum(map(len,restricted))//2}
out['jump_eccentricity_distribution']=dict(sorted(Counter(max(row) for row in D0).items()))
out['slide_eccentricity_distribution']=dict(sorted(Counter(max(row) for row in D1).items()))
for key,mat in [('jump',D0),('slide',D1)]:
 out[key+'_distance_distribution']=dict(sorted(Counter(mat[i][j] for i in range(len(opt)) for j in range(i+1,len(opt))).items()))
for key,calculator in [
 ('slide_minus_jump',lambda i,j:D1[i][j]-D0[i][j]),
 ('slide_minus_johnson',lambda i,j:D1[i][j]-(6-(opt[i]&opt[j]).bit_count())),
 ('jump_minus_johnson',lambda i,j:D0[i][j]-(6-(opt[i]&opt[j]).bit_count()))]:
 out[key]=dict(sorted(Counter(calculator(i,j) for i in range(len(opt)) for j in range(i+1,len(opt))).items()))
expected={
 'states':2860,'jump_edges':27780,'slide_edges':8280,
 'jump_eccentricity_distribution':{6:2860},
 'slide_eccentricity_distribution':{9:520,10:2340},
 'jump_distance_distribution':{1:27780,2:204240,3:743050,4:1413660,5:1276290,6:423350},
 'slide_distance_distribution':{1:8280,2:36960,3:137800,4:413910,5:846960,6:1164710,7:958800,8:429960,9:84960,10:6030},
 'slide_minus_jump':{0:430950,1:1275090,2:1482330,3:741480,4:148080,5:10230,6:210},
 'slide_minus_johnson':{0:419550,1:1261860,2:1487700,3:752460,4:155520,5:11040,6:240},
 'jump_minus_johnson':{0:4024770,1:62760,2:840}}
assert out==expected,(out,expected)
print(json.dumps(out,indent=2,sort_keys=True))
