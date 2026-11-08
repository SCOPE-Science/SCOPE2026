"""Independent incidence-model enumeration of secure configurations and exchanges."""
from itertools import combinations
from collections import Counter,deque
N=16;V=range(N)
E={frozenset((i,8+j)) for i in range(8) for j in range(8) if (i-j)%8 in (0,1,3)}
assert len(E)==24
# An explicit graph isomorphism from generalized-Petersen indexing to incidence indexing.
phi=(0,15,2,9,4,11,6,13,8,7,10,1,12,3,14,5)
GP={frozenset((a,b)) for i in range(8) for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8))}
assert {frozenset((phi[a],phi[b])) for a,b in (tuple(e) for e in GP)}==E
print('GP to incidence isomorphism verified')
adj=[{v for v in V if frozenset((u,v)) in E} for u in V]
Nclosed=[adj[u]|{u} for u in V]

def dominates(S):
 return all(S & Nclosed[v] for v in V)

def secure(S):
 return dominates(S) and all(any(dominates((S-{a})|{v}) for a in S&adj[v]) for v in V if v not in S)
solutions=set()
for k in range(8):
 layer={frozenset(xs) for xs in combinations(V,k) if secure(set(xs))}
 print('size',k,'secure',len(layer))
 if layer:solutions=layer;break
assert k==7 and len(solutions)==336
# No edge replacement in the second method: generate unordered pairs of candidates
# with six shared guard positions, then check whether the two changed positions are adjacent.
TJ={s:set() for s in solutions};TS={s:set() for s in solutions}
for s in solutions:
 for r in combinations(s,6):
  R=frozenset(r)
  old=next(iter(s-R))
  for add in V:
   if add in s:continue
   other=R|{add}
   if other in solutions:
    TJ[s].add(other)
    if add in adj[old]:TS[s].add(other)

def profile(g):
 unseen=set(g); components=[]
 while unseen:
  u=unseen.pop();q=deque([u]);C={u}
  while q:
   x=q.popleft()
   for y in g[x]:
    if y not in C:C.add(y);q.append(y);unseen.remove(y)
  components.append(C)
 ce=[]
 for C in components:
  for root in C:
   q=deque([root]);dist={root:0}
   while q:
    x=q.popleft()
    for y in g[x]:
     if y not in dist:dist[y]=dist[x]+1;q.append(y)
   assert len(dist)==len(C)
   ce.append((len(C),max(dist.values())))
 return (sum(map(len,g.values()))//2,sorted(Counter(len(C) for C in components).items()),sorted(Counter(map(len,g.values())).items()),sorted(Counter(ce).items()))
for name,G,expected in (
 ('TJ',TJ,(1392,[(336,1)],[(5,48),(6,96),(8,48),(11,144)], [((336,7),288),((336,8),48)])),
 ('TS',TS,(528,[(2,24),(288,1)],[(1,48),(3,240),(6,48)], [((2,1),48),((288,8),192),((288,9),96)]))):
 got=profile(G)
 print(name,'edges',got[0],'component_sizes',got[1],'degrees',got[2],'component_ecc',got[3])
 assert got==expected,(got,expected)
print('VERIFIED_INCIDENCE')
