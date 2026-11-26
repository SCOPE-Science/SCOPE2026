#!/usr/bin/env python3
"""A Kneser-coordinate exhaustive checker of 4-color Petersen recoloring."""
from itertools import combinations,permutations
from collections import Counter,deque
import hashlib,json
V=list(combinations(range(5),2));N=len(V);I={u:i for i,u in enumerate(V)}
A=[tuple(j for j,w in enumerate(V) if set(u).isdisjoint(w)) for u in V]
order=sorted(range(N),key=lambda i:-len(A[i])); C=[];state=[-1]*N
def rec(k):
 if k==N:C.append(tuple(state));return
 i=order[k];occupied={state[j] for j in A[i] if state[j]>=0}
 for col in range(4):
  if col not in occupied:state[i]=col;rec(k+1)
 state[i]=-1
rec(0)
D={w:i for i,w in enumerate(C)};edges=[[] for w in C]
for i,c in enumerate(C):
 for p in range(N):
  for col in range(4):
   if c[p]!=col and all(c[j]!=col for j in A[p]):
    t=list(c);t[p]=col;edges[i].append(D[tuple(t)])
assert all(i in edges[j] for i,arr in enumerate(edges) for j in arr)
# Convert every coloring to a canonical unlabeled partition.
def normalize(c):
 m={};out=[]
 for x in c:
  if x not in m:m[x]=len(m)
  out.append(m[x])
 return tuple(out)
reps={};canon=[normalize(c) for c in C]
for i,cc in enumerate(canon):reps.setdefault(cc,i)
perms=[]
for perm in permutations(range(5)):
 pi=[I[tuple(sorted((perm[a],perm[b])))] for a,b in V]
 perms.append(pi)
seen=set();orbit_reps=[];orbit_sizes=[]
for cc,rep in reps.items():
 if cc in seen:continue
 orbit=set()
 for pi in perms:
  c1=[0]*N
  for k,j in enumerate(pi):c1[j]=cc[k]
  orbit.add(normalize(c1))
 seen.update(orbit)
 orbit_reps.append(rep);orbit_sizes.append(len(orbit)*24)
assert len(seen)==len(reps)
# BFS on representative for graph radius, diameter, all component eccentricities
result=[]
for rep in orbit_reps:
 dist=[-1]*len(C);dist[rep]=0;Q=[rep]
 for i in Q:
  for j in edges[i]:
   if dist[j]<0:dist[j]=dist[i]+1;Q.append(j)
 assert len(Q)==len(C)
 h=Counter(dist)
 result.append({'idx':rep,'degree':len(edges[rep]),'orbit_size':orbit_sizes[len(result)],'eccentricity':max(dist),'dist_hist':dict(sorted(h.items()))})
assert len(C)==12960 and sum(map(len,edges))//2==53280
assert min(x['eccentricity'] for x in result)==13 and max(x['eccentricity'] for x in result)==14
assert sum(x['orbit_size'] for x in result if x['eccentricity']==13)==3360
assert sum(orbit_sizes)==12960
print(json.dumps({'colorings':len(C),'edges':sum(map(len,edges))//2,'components':1,'degree_hist':dict(sorted(Counter(map(len,edges)).items())),'num_orbits':len(result),'radius':min(x['eccentricity'] for x in result),'diameter':max(x['eccentricity'] for x in result),'orbits':result,'eccentricity_counts':dict(sorted(Counter({13:3360,14:9600}).items()))},indent=2))
