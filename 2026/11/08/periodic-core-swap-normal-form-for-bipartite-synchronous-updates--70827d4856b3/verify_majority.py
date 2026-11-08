#!/usr/bin/env python3
"""Exhaustive odd-degree bipartite majority census and sharp tie counterexample."""
from itertools import combinations
from collections import deque

def analyze(n, edges, retain_ties):
 adj=[[] for _ in range(n)]
 for i,j in edges:adj[i].append(j);adj[j].append(i)
 def F(x):
  ans=0
  for i in range(n):
   a=sum((x>>j)&1 for j in adj[i]);deg=len(adj[i])
   b=(x>>i)&1 if 2*a==deg and retain_ties else int(2*a>deg)
   ans|=b<<i
  return ans
 K=sum(F(x)==x for x in range(1<<n))
 K2=sum(F(F(x))==x for x in range(1<<n))
 return K,K2

def bipartite(n, edges):
 adj=[[] for _ in range(n)];c=[-1]*n
 for i,j in edges: adj[i].append(j);adj[j].append(i)
 for s in range(n):
  if c[s]>=0:continue
  c[s]=0;q=[s]
  for i in q:
   for j in adj[i]:
    if c[j]==c[i]: return False
    if c[j]==-1: c[j]=1-c[i];q.append(j)
 return True

checked={};tot_states=0
for n in range(2,7):
 E=list(combinations(range(n),2));cnt=0
 for mask in range(1<<len(E)):
  edges=[e for k,e in enumerate(E) if (mask>>k)&1]
  if not edges:continue
  if any(sum(i in e for e in edges)%2!=1 for i in range(n)):continue
  if not bipartite(n,edges):continue
  k,p=analyze(n,edges,False)
  assert p==k*k, (n,edges,k,p)
  cnt+=1;tot_states+=(1<<n)
 checked[n]=cnt
print(f'MAJORITY_OK checked_odd_degree_bipartite_graphs_by_n={checked} enumerated_states={tot_states}')
# Root with 3 children, each of these with 2 leaves: all degrees odd.
edges=[(0,i) for i in (1,2,3)]+[(j,4+2*(j-1)+t) for j in (1,2,3) for t in range(2)]
k,p=analyze(10,edges,False)
assert (k,p,p-k)==(8,64,56)
print(f'TERNARY_TREE_OK fixed={k} period_dividing_two={p} primitive_two={p-k} orbits_two={(p-k)//2}')
# Odd-degree hypothesis is essential for tie-retaining majority: P4.
k,p=analyze(4,[(0,1),(1,2),(2,3)],True)
assert (k,p,p-k)==(4,6,2)
print(f'P4_TIE_COUNTEREXAMPLE fixed={k} period_dividing_two={p} primitive_two={p-k} vs_square_law_prediction={k*(k-1)}')
