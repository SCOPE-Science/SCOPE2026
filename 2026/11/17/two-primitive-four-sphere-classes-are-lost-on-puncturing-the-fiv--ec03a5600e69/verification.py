#!/usr/bin/env python3
"""Self-contained finite acyclic-matching check for vertex-punctured five-by-five torus Rips at scale three."""
from collections import Counter,deque
N=5
V=range(N*N)
idx=lambda x,y: N*(x%N)+(y%N)
cycle_dist=lambda a,b:min((a-b)%N,(b-a)%N)
for p in V:
 for q in V:
  x,y=divmod(p,N);u,v=divmod(q,N)
  assert (cycle_dist(x,u)+cycle_dist(y,v)>3)==(cycle_dist(x,u)==2 and cycle_dist(y,v)==2)
forbidden=[0]*25
for x in range(N):
 for y in range(N):
  for dx in (-2,2):
   for dy in (-2,2): forbidden[idx(x,y)] |=1<<idx(x+dx,y+dy)
# This is the inverse of the change of coordinates (u,v)=(x+y,x-y).
order=[idx(3*(u+v),3*(u-v)) for u in range(N) for v in range(N)]
assert len(set(order))==25

def certificate(omitted, expected_dim, expected_rank):
 allowed=[v for v in order if v not in omitted]
 faces=[0]
 for v in allowed:
  bit=1<<v
  faces += [s|bit for s in faces if not s&forbidden[v]]
 loc={s:i for i,s in enumerate(faces)}
 assert len(loc)==len(faces)
 live=set(faces); mate={}
 for v in allowed:
  bit=1<<v
  for s in faces:
   if s&bit or s not in live: continue
   t=s|bit
   if t in live:
    live.remove(s);live.remove(t);mate[s]=t;mate[t]=s
 assert all(s.bit_count()-1==expected_dim for s in live)
 assert len(live)==expected_rank and 0 not in live
 assert len(mate)+len(live)==len(faces)
 # Verify that reversing every matched cover in the augmented Hasse graph is acyclic.
 nexts=[[] for _ in faces]; indeg=[0]*len(faces); edges=0
 for s in faces:
  i=loc[s]
  for v in allowed:
   bit=1<<v
   if s&bit: continue
   j=loc.get(s|bit)
   if j is None: continue
   a,b=(i,j) if mate.get(s)==s|bit else (j,i)
   nexts[a].append(b);indeg[b]+=1;edges+=1
 Q=deque(i for i,d in enumerate(indeg) if d==0);visited=0
 while Q:
  a=Q.popleft(); visited+=1
  for b in nexts[a]:
   indeg[b]-=1
   if indeg[b]==0:Q.append(b)
 assert visited==len(faces)
 print(f'case omitted={sorted(omitted)}, faces={len(faces)}, pairs={len(mate)//2}, critical={Counter(s.bit_count()-1 for s in live)}, Hasse={edges}, sorted={visited}')

base={0}
closed={0}|{i for i in range(25) if forbidden[0]>>i&1}
certificate(set(),4,9)
certificate(base,4,7)
certificate(closed,3,2)
print('TORUS_PUNCTURE_CHECK_PASS')
