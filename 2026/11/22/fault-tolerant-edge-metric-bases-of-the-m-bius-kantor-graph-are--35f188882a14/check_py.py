#!/usr/bin/env python3
"""Independent exhaustive verifier for edge-location fault tolerance on GP(8,3)."""
from itertools import combinations
from collections import Counter, deque
N=8; V=tuple(range(2*N))
E={tuple(sorted((i,(i+1)%N))) for i in range(N)}
E|={tuple(sorted((i,N+i))) for i in range(N)}
E|={tuple(sorted((N+i,N+(i+3)%N))) for i in range(N)}
E=tuple(sorted(E)); assert len(E)==24
nbr=[set() for _ in V]
for a,b in E:nbr[a].add(b);nbr[b].add(a)
def distances(s):
 d=[-1]*len(V);d[s]=0;front=deque([s])
 while front:
  a=front.popleft()
  for b in nbr[a]:
   if d[b]<0:d[b]=d[a]+1;front.append(b)
 return d
D=[distances(v) for v in V]
assert all(all(x>=0 for x in row) for row in D)
profiles={v:tuple(min(D[v][a],D[v][b]) for a,b in E) for v in V}
def resolves(S):
 return len({tuple(profiles[v][e] for v in S) for e in range(len(E))})==len(E)
def fault_tolerant(S):
 return all(resolves(tuple(v for v in S if v!=x)) for x in S)
ordinary3=[S for S in combinations(V,3) if resolves(S)]
assert len(ordinary3)==0,ordinary3
base=[S for S in combinations(V,4) if resolves(S)]
assert len(base)==368
ft4=[S for S in combinations(V,4) if fault_tolerant(S)]
ft5=[S for S in combinations(V,5) if fault_tolerant(S)]
assert len(ft4)==0 and len(ft5)==16
B=tuple(sorted({tuple(sorted(v for v in V if D[x][v]==3)) for x in V}))
assert len(B)==16 and set(ft5)==set(B)
shore0={0,2,4,6,9,11,13,15};shore1=set(V)-shore0
assert all((set(S)<=shore0 or set(S)<=shore1) for S in B)
assert all(all(b not in nbr[a] for a,b in combinations(S,2)) for S in B)
ints=Counter(len(set(A)&set(B)) for A,B in combinations(ft5,2))
assert ints=={0:64,2:8,3:48},ints
for k,want in [(1,(0,(1,)*16)),(2,(48,(8,8))),(3,(56,(8,8))),(4,(56,(8,8))),(5,(120,(16,)))]:
 adj=[set() for x in ft5]
 for i,j in combinations(range(16),2):
  if 5-len(set(ft5[i])&set(ft5[j]))<=k:adj[i].add(j);adj[j].add(i)
 visited=set();sizes=[]
 for i in range(16):
  if i in visited:continue
  q=[i];visited.add(i)
  for x in q:
   for y in adj[x]:
    if y not in visited:visited.add(y);q.append(y)
  sizes.append(len(q))
 assert (sum(map(len,adj))//2,tuple(sorted(sizes)))==want,(k,sizes)
print('PYTHON PASS: 24 edges; ordinary edge bases=368; 4-sensor fault-tolerant=0; 5-sensor fault-tolerant=16')
print('PYTHON PASS: exactly 16 distinct distance-3 spheres; each independent in one shore')
print('PYTHON PASS: intersection multiset {0:64,2:8,3:48}; exchange component sizes 16x1, 2x8, 2x8, 2x8, 1x16')
