from itertools import combinations
from random import Random
from collections import deque
from math import comb

def conn(adj,ban=None):
 n=len(adj);valid=set(range(n))-{ban} if ban is not None else set(range(n)); s=next(iter(valid));reach={s};q=[s]
 for u in q:
  for v in adj[u]&valid:
   if v not in reach:reach.add(v);q.append(v)
 return len(reach)==len(valid)

def bfs(adj):
 d=[]
 for i in range(len(adj)):
  di=[999]*len(adj);di[i]=0;q=[i]
  for x in q:
   for y in adj[x]:
    if di[y]>di[x]+1:di[y]=di[x]+1;q.append(y)
  d.append(di)
 return d

def beta(adj):
 n=len(adj);A=[set() for i in range(2*n)]
 for i in range(n):
  for j in adj[i]:A[i].add(j)
  A[i].add(n+i);A[n+i].add(i)
 d=bfs(A)
 root_dist=bfs(adj)
 b=sum(not any(root_dist[k][i]==root_dist[k][j] for k in range(n) if k!=i and k!=j) for i in range(n) for j in adj[i] if i<j)
 idx={p:j for j,p in enumerate(combinations([i for i in range(2*n) if i!=n],2))}
 piv={}
 for a,bb,c in combinations(range(2*n),3):
  ds=[d[a][bb],d[a][c],d[bb][c]]
  if max(ds)*2==sum(ds):continue
  val=0
  for x,y in ((a,bb),(a,c),(bb,c)):
   if n not in (x,y):val^=1<<idx[x,y]
  while val:
   k=val.bit_length()-1
   if k in piv:val^=piv[k]
   else:piv[k]=val;break
 return len(idx)-len(piv), n+b,b

rng=Random(87032)
for n in range(3,9):
 pairs=list(combinations(range(n),2));todo=[]
 if n<=5:todo=range(1<<len(pairs))
 else:todo=[rng.getrandbits(len(pairs)) for _ in range(170 if n==6 else 200 if n==7 else 100)]
 num=0
 for mask in todo:
  adj=[set() for _ in range(n)]
  for e,(u,v) in enumerate(pairs):
   if mask>>e&1:adj[u].add(v);adj[v].add(u)
  if not conn(adj):continue
  if any(not conn(adj,i) for i in range(n)):continue
  x,y,b=beta(adj)
  assert x==y,(n,mask,x,y,b,adj)
  num+=1
 print('base_vertices',n,'2vertexconnected_graphs_tested',num,flush=True)
