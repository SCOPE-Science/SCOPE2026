from itertools import combinations,product
from collections import Counter, deque
from math import comb

def comps(n):
 if n==0: yield ()
 else:
  for x in range(1,n+1):
   for tail in comps(n-x):yield (x,)+tail

def formula(parts,T):
 N=sum(parts); p=[];q=[]; i=0
 for n in parts:
  p.append(len(set(range(i,i+n))&T));q.append(n-p[-1]);i+=n
 C=sum(p[i]*p[j] for i in range(len(p)) for j in range(i+1,len(p)))
 H=sum(q[i]*q[j] for i in range(len(q)) for j in range(i+1,len(q)))
 Q=sum(q)
 out={C:1}
 def multiply(out,factor):
  z=Counter()
  for a,va in out.items():
   for b,vb in factor.items():z[a+b]+=va*vb
  return dict(z)
 for _ in range(H):out=multiply(out,{0:1,1:1})
 for j in range(len(p)):
  for _ in range(Q-q[j]):
   if p[j]:out=multiply(out,{p[j]-1:p[j],p[j]:1})
 return out

def count(parts,T):
 groups=[];i=0
 for s in parts:groups.append(list(range(i,i+s)));i+=s
 edges=[(u,v) for i,g in enumerate(groups) for h in groups[i+1:] for u in g for v in h]
 n=sum(parts)
 orig=[[] for _ in range(n)]
 for u,v in edges:orig[u].append(v);orig[v].append(u)
 def dists(adj,s):
  dis=[n+1]*n;dis[s]=0;q=deque([s])
  while q:
   u=q.popleft()
   for v in adj[u]:
    if dis[v]>dis[u]+1:dis[v]=dis[u]+1;q.append(v)
  return dis
 base={t:dists(orig,t) for t in T}
 out=Counter()
 for mask in range(1<<len(edges)):
  adj=[[] for _ in range(n)]
  for i,(u,v) in enumerate(edges):
   if not(mask>>i&1):adj[u].append(v);adj[v].append(u)
  if all(dists(adj,t)[s]>base[t][s] for t,s in combinations(T,2)):out[mask.bit_count()]+=1
 return dict(out)

cases=0
for n in range(2,7):
 for parts in comps(n):
  if len(parts)<2:continue
  if sum(parts[i]*parts[j] for i in range(len(parts)) for j in range(i+1,len(parts)))>13:continue
  for mask in range(1<<n):
   T={i for i in range(n) if mask>>i&1}
   if len(T)<2:continue
   a=formula(parts,T);b=count(parts,T)
   assert a==b,(parts,T,a,b)
   cases+=1
print('SEMI_CUT_MULTIPARTITE_FULL_GRAPH_DISTANCE_EXHAUSTIVE_PASS cases=',cases)
