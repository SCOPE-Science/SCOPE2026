#!/usr/bin/env python3
"""Exhaustive simplicial/Morse check for the edge-deleted cube forest filtration."""
from collections import Counter,deque
from fractions import Fraction
V=range(8)
E={(i,j) for i in V for j in V if i<j and (i^j).bit_count()==1 and (i,j)!=(0,1)}
N={i:{j for j in V if tuple(sorted((i,j))) in E} for i in V}
ORDERS=((0,1,2,3,4,5,6,7),(0,1,2,3,4,5,6,7),(0,1,2,3,4,5,6,7),(0,1,2,3,4,5,6,7))
EXPECTED=({0:1,1:2},{0:1,2:1},{0:1,4:3},{0:1,4:3})
def forest(mask):
 parent=list(V)
 def root(v):
  while parent[v]!=v:v=parent[v]
  return v
 for u,v in sorted(E):
  if (mask>>u)&1 and (mask>>v)&1:
   a,b=root(u),root(v)
   if a==b:return False
   parent[a]=b
 return True
def is_face(mask,d):
 vs={v for v in V if (mask>>v)&1}
 return all(len(N[v]&vs)<=d for v in vs) and forest(mask)
def oracle(mask,d):
 vs={v for v in V if (mask>>v)&1}
 seen=set();edges=sum(u in vs and v in vs for u,v in E)
 comps=0
 for v in vs:
  if v not in seen:
   comps+=1; seen.add(v);stack=[v]
   while stack:
    for w in N[stack.pop()]&vs-seen:
     seen.add(w);stack.append(w)
 return edges==len(vs)-comps and all(len(N[v]&vs)<=d for v in vs)
def morse(F,order):
 live=set(F); pairs=[]
 for v in order:
  for m in sorted(F):
   t=m|(1<<v)
   if not (m>>v)&1 and m in live and t in live:
    live.remove(m);live.remove(t);pairs.append((m,t))
 pairset=set(pairs); indeg={m:0 for m in F}; arrows={m:[] for m in F}
 for m in F:
  for v in V:
   if m>>v&1:
    s=m^(1<<v)
    if s in F:
     a,b=(s,m) if (s,m) in pairset else (m,s)
     arrows[a].append(b);indeg[b]+=1
 queue=deque(m for m in F if indeg[m]==0);visited=0
 while queue:
  m=queue.popleft();visited+=1
  for n in arrows[m]:
   indeg[n]-=1
   if indeg[n]==0:queue.append(n)
 assert visited==len(F)
 return Counter(m.bit_count()-1 for m in live),len(pairs)
faces=[]
for d in range(4):
 F={m for m in range(1,256) if is_face(m,d)}
 assert F=={m for m in range(1,256) if oracle(m,d)}, d
 crit,pairs=morse(F,ORDERS[d]);assert crit==EXPECTED[d],(d,crit)
 f=tuple(sum(m.bit_count()==i+1 for m in F) for i in range(max(x.bit_count() for x in F)))
 print('degree',d,'face-vector',f,'Morse-critical',dict(crit),'matched-pairs',pairs)
 faces.append(F)
assert all(faces[i]<=faces[i+1] for i in range(3))
# Relative collapse F3 onto F2
live=set(faces[3]);target=faces[2];removed=[]
while live!=target:
 options=[]
 for m in sorted(live-target,key=lambda x:(-x.bit_count(),x)):
  supers=[t for t in live if t!=m and t&m==m]
  if len(supers)==1 and supers[0].bit_count()==m.bit_count()+1 and supers[0] not in target:options.append((m,supers[0]))
 assert options, 'No free relative face'
 m,t=options[0];live.remove(m);live.remove(t);removed.append((m,t))
assert len(removed)==10
print('ten explicit collapse pairs',[(hex(a),hex(b)) for a,b in removed]);print('ALL_CHECKS_PASS')
