"""Independent incidence-formula verification of edge resolving bases.

Run: python3 heawood_edge_bases_verify_alt.py
"""
from itertools import combinations
from collections import Counter, deque

P=set(range(7)); L=set(range(7,14)); V=P|L
inc=lambda p,j: (p-(j-7))%7 in {0,1,3}
flags=[(p,j) for p in range(7) for j in range(7,14) if inc(p,j)]
A={v:set() for v in V}
for p,j in flags:A[p].add(j);A[j].add(p)
assert len(flags)==21

def signature(vertex,edge):
 p,j=edge
 if vertex<7: return 0 if vertex==p else 1 if inc(vertex,j) else 2
 return 0 if vertex==j else 1 if inc(p,vertex) else 2

def resolves(S):
 return len({tuple(signature(w,e) for w in S) for e in flags})==21

triples=[p for p in combinations(P,3) if not any(all(inc(x,j) for x in p) for j in L)]
assert len(triples)==28
B=set()
for T in triples:
 tangent=[j for j in L if sum(inc(p,j) for p in T)==1]
 assert len(tangent)==3
 for U in combinations(tangent,2): B.add(frozenset(T+U))
for T in combinations(L,3):
 if any(all(inc(p,j) for j in T) for p in P): continue
 tangents=[p for p in P if sum(inc(p,j) for j in T)==1]
 assert len(tangents)==3
 for U in combinations(tangents,2): B.add(frozenset(T+U))
assert len(B)==168
for size in range(0,5):
 assert not any(resolves(S) for S in combinations(V,size)),size
all5={frozenset(S) for S in combinations(V,5) if resolves(S)}
assert B==all5

# The minimum state graphs, calculated directly from geometric configurations.
R={mode:{b:set() for b in B} for mode in ('jump','slide')}
for b in B:
 for u in b:
  for v in V-b:
   nb=frozenset((b-{u})|{v})
   if nb in B:
    R['jump'][b].add(nb)
    if v in A[u]: R['slide'][b].add(nb)
assert Counter(len(R['jump'][b]) for b in B)=={5:168}
assert Counter(len(R['slide'][b]) for b in B)=={2:168}
assert sum(len(a) for a in R['jump'].values())//2==420
assert sum(len(a) for a in R['slide'].values())//2==168

def components(graph):
 remaining=set(graph);groups=[]
 while remaining:
  s=next(iter(remaining));visit={s};queue=[s]
  while queue:
   for t in graph[queue.pop()]:
    if t not in visit: visit.add(t);queue.append(t)
  groups.append(visit);remaining-=visit
 return groups
J=components(R['jump']);S=components(R['slide'])
assert list(map(len,J))==[168]
assert Counter(map(len,S))=={8:21}
# A connected 2-regular graph on eight vertices is exactly C8.
for source in B:
 d={source:0};Q=deque([source])
 while Q:
  x=Q.popleft()
  for y in R['jump'][x]:
   if y not in d:d[y]=d[x]+1;Q.append(y)
 assert len(d)==168
 assert max(d.values())==5

# Enumerate each undirected simple 8-cycle exactly once using its smallest vertex.
cyc=set()
for root in V:
 def dfs(path):
  if len(path)==8:
   if root in A[path[-1]]:
    f=tuple(path)
    cyc.add(min(f, (root,)+tuple(reversed(f[1:]))))
   return
  for q in A[path[-1]]:
   if q>root and q not in path:dfs(path+[q])
 dfs([root])
assert len(cyc)==21,len(cyc)
cycle_sets={frozenset(c) for c in cyc}
union_sets={frozenset().union(*C) for C in S}
assert union_sets==cycle_sets
print('PASS 28 point triangles and 28 line triangles; three tangents, two selected')
print('PASS minimum edge metric dimension 5; 168 bases; all smaller subsets fail')
print('PASS jumping 168 vertices, 420 edges, 5-regular connected, diameter 5')
print('PASS sliding 168 vertices, 168 edges, 21 disjoint 8-cycles')
print('PASS slide components correspond bijectively to all 21 eight-cycles of graph')
