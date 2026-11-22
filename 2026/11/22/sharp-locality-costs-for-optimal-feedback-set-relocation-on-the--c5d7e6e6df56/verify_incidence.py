#!/usr/bin/env python3
"""Complete exact metric census for minimum decycling sets of H(5,2)."""
import itertools
from collections import Counter,deque
import json

V=tuple(range(20))
subs2=list(itertools.combinations(range(5),2))
subs3=list(itertools.combinations(range(5),3))
E=set()
for i,a in enumerate(subs2):
 for j,b in enumerate(subs3):
  if set(a).issubset(b):E.add((i,10+j))
assert len(E)==30
adj=[set() for i in V]
for u,v in E:adj[u].add(v);adj[v].add(u)
ISO=[0,2,13,19,11,17,8,4,15,6,1,10,9,3,12,16,14,18,7,5]
assert sorted(ISO)==list(range(20))
P=set()
for i in range(10):
 P.add(tuple(sorted((i,(i+1)%10))))
 P.add(tuple(sorted((i,10+i))))
 P.add(tuple(sorted((10+i,10+(i+3)%10))))
assert {tuple(sorted((ISO[a],ISO[b]))) for a,b in E}==P

def acyclic(mask):
 seen=0
 for r in V:
  if (mask>>r)&1 or (seen>>r)&1:continue
  seen|=1<<r
  stack=[(r,-1)]
  while stack:
   u,par=stack.pop()
   for v in adj[u]:
    if (mask>>v)&1 or v==par:continue
    if (seen>>v)&1:return False
    seen|=1<<v
    stack.append((v,u))
 return True

# The size-six lower bound follows independently from 2k=10+e(S)+c.
states=[sum(1<<i for i in comb) for comb in itertools.combinations(V,6) if acyclic(sum(1<<i for i in comb))]
assert len(states)==2860
lookup={s:i for i,s in enumerate(states)}

def neighbors(slide):
 out=[[] for _ in states]
 for i,s in enumerate(states):
  for u in V:
   if not (s>>u)&1:continue
   for v in (adj[u] if slide else V):
    if (s>>v)&1:continue
    j=lookup.get(s^(1<<u)^(1<<v))
    if j is not None:out[i].append(j)
  out[i]=sorted(set(out[i]))
  for j in out[i]: assert i in out[j] or j>i # checked globally below
 assert all(i in out[j] for i,row in enumerate(out) for j in row)
 return out

def apsp(rows):
 alld=[]
 for root in range(len(rows)):
  d=[-1]*len(rows); d[root]=0; q=deque([root])
  while q:
   u=q.popleft()
   for v in rows[u]:
    if d[v]==-1:d[v]=d[u]+1;q.append(v)
  assert min(d)>=0
  alld.append(d)
 return alld
jrows=neighbors(False);srows=neighbors(True)
j=apsp(jrows);s=apsp(srows)
stats={"vertex_count":20,"edge_count":len(E),"minimum_fvs_size":6,"minimum_fvs_count":len(states),"pairs":len(states)*(len(states)-1)//2,"jump_edges":sum(map(len,jrows))//2,"slide_edges":sum(map(len,srows))//2,"jump_degree_distribution":dict(sorted(Counter(map(len,jrows)).items())),"slide_degree_distribution":dict(sorted(Counter(map(len,srows)).items())),"jump_eccentricity_distribution":dict(sorted(Counter(max(x) for x in j).items())),"slide_eccentricity_distribution":dict(sorted(Counter(max(x) for x in s).items()))}
for label,matrix in [('jump',j),('slide',s)]:
 stats[label+'_distance_distribution']=dict(sorted(Counter(matrix[i][h] for i in range(len(states)) for h in range(i+1,len(states))).items()))
stats['slide_minus_johnson']=dict(sorted(Counter(s[i][h]-6+(states[i]&states[h]).bit_count() for i in range(len(states)) for h in range(i+1,len(states))).items()))
stats['slide_minus_jump']=dict(sorted(Counter(s[i][h]-j[i][h] for i in range(len(states)) for h in range(i+1,len(states))).items()))
stats['jump_minus_johnson']=dict(sorted(Counter(j[i][h]-6+(states[i]&states[h]).bit_count() for i in range(len(states)) for h in range(i+1,len(states))).items()))
mx=max(s[i][h]-j[i][h] for i in range(len(states)) for h in range(i+1,len(states)))
for i in range(len(states)):
 for h in range(i+1,len(states)):
  if s[i][h]-j[i][h]==mx:
   stats['witness_slide_minus_jump']={'first_mask':states[i],'second_mask':states[h],'slide_distance':s[i][h],'jump_distance':j[i][h],'johnson_distance':6-(states[i]&states[h]).bit_count()};break
 else:continue
 break
print(json.dumps(stats,sort_keys=True,indent=2))
