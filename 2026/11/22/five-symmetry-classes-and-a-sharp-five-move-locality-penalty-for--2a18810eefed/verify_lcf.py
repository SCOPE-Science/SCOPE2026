"""Independent certificate using the Hamiltonian LCF model and set propagation.
Standard library only. Run with python3 verify_lcf.py.
"""
from itertools import combinations
from collections import Counter,deque
n=18; lcf=[5,7,-7,7,-7,-5]
edge=set()
for v in range(n):
 edge.add(tuple(sorted((v,(v+1)%n))))
 edge.add(tuple(sorted((v,(v+lcf[v%6])%n))))
assert len(edge)==27
adj=[set() for _ in range(n)]
for u,v in edge:adj[u].add(v);adj[v].add(u)
assert all(len(a)==3 for a in adj)
# Explicit LCF-to-affine incidence isomorphism, checked before enumeration.
phi=(0,9,2,17,3,12,6,16,1,13,7,11,8,14,5,10,4,15)
affedge=set()
for x in range(3):
 for y in range(3):
  u=3*x+y
  for k in range(3):
   if x==k:affedge.add((u,9+k))
   if y==k:affedge.add((u,12+k))
   if (y-x)%3==k:affedge.add((u,15+k))
assert {tuple(sorted((phi[u],phi[v]))) for u,v in edge}==affedge
# Incremental rather than simultaneous forcing, with a fresh scan after each force.
def power(S):
 obs=set(S)
 for s in S:obs|=adj[s]
 while True:
  choice=None
  for v in sorted(obs):
   missing=adj[v]-obs
   if len(missing)==1:
    choice=next(iter(missing));break
  if choice is None:return len(obs)==n
  obs.add(choice)
assert all(not power(s) for k in (1,2) for s in combinations(range(n),k))
S=[frozenset(s) for s in combinations(range(n),3) if power(s)]
assert len(S)==486
# Deliberately construct transitions from all unordered state pairs, not swaps.
J=[set() for _ in S];T=[set() for _ in S]
for i,A in enumerate(S):
 for j in range(i+1,len(S)):
  B=S[j];lost=A-B;gained=B-A
  if len(lost)!=1:continue
  J[i].add(j);J[j].add(i)
  if next(iter(gained)) in adj[next(iter(lost))]:
   T[i].add(j);T[j].add(i)
def BFS(graph,start):
 d=[-1]*len(graph);d[start]=0;q=deque([start])
 while q:
  i=q.popleft()
  for j in graph[i]:
   if d[j]<0:d[j]=d[i]+1;q.append(j)
 assert -1 not in d
 return d
histJ=Counter();histT=Counter();delta=Counter();ecc=Counter();nbad=0
for i in range(len(S)):
 j=BFS(J,i);t=BFS(T,i)
 ecc[max(t)]+=1
 for k in range(i+1,len(S)):
  histJ[j[k]]+=1;histT[t[k]]+=1;delta[t[k]-j[k]]+=1
  if j[k]!=len(S[i]-S[k]):nbad+=1
assert sum(map(len,J))==14256 and sum(map(len,T))==3240
assert histJ==Counter({1:7128,2:43902,3:66825})
assert histT==Counter({1:1620,2:6480,3:18063,4:31644,5:33912,6:20358,7:5454,8:324})
assert delta==Counter({0:9423,1:29808,2:42174,3:28026,4:7938,5:486})
assert ecc==Counter({7:54,8:432}) and nbad==162
print('PASS LCF; minimum=3, bases=486, edges jump=7128 slide=1620')
print('distance histograms',sorted(histJ.items()),sorted(histT.items()))
print('penalties',sorted(delta.items()),'centers',ecc,'jump detours',nbad)
