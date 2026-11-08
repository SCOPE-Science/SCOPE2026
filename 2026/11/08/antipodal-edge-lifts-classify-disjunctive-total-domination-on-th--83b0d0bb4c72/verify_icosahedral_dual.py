from itertools import combinations
from collections import Counter, deque
U=list(range(1,6));V=list(range(6,11));top=0;bottom=11
E=set()
def edge(a,b): E.add(tuple(sorted((a,b))))
for i in range(5):
 edge(top,U[i]);edge(bottom,V[i]);edge(U[i],U[(i+1)%5]);edge(V[i],V[(i+1)%5]);edge(U[i],V[i]);edge(U[i],V[(i-1)%5])
assert len(E)==30
F=[frozenset(t) for t in combinations(range(12),3) if all(tuple(sorted(e)) in E for e in combinations(t,2))]
assert len(F)==20
A=[set() for _ in F]
for i,f in enumerate(F):
 for j in range(i):
  if len(f&F[j])==2:A[i].add(j);A[j].add(i)
assert all(len(x)==3 for x in A)
D=[]
for v in range(20):
 dist=[-1]*20;dist[v]=0;q=deque([v]);
 while q:
  t=q.popleft()
  for w in A[t]:
   if dist[w]<0:dist[w]=dist[t]+1;q.append(w)
 assert sorted(dist).count(5)==1
 D.append(set(w for w in range(20) if dist[w]==2))
ant=[]
for v in range(20):
 dist=[-1]*20;dist[v]=0;q=deque([v]);
 while q:
  t=q.popleft()
  for w in A[t]:
   if dist[w]<0:dist[w]=dist[t]+1;q.append(w)
 ant.append(dist.index(5))
assert all(ant[ant[v]]==v for v in range(20))
def isdtd(S): return all((A[v]&S) or len(D[v]&S)>=2 for v in range(20))
sol=[frozenset(S) for S in combinations(range(20),4) if isdtd(set(S))]
assert len(sol)==15
pairsets=set()
for v in range(20):
 for w in A[v]:
  pairsets.add(frozenset((v,w,ant[v],ant[w])))
assert len(pairsets)==15 and set(sol)==pairsets
assert not any(len(s&t)==3 for s,t in combinations(sol,2))
for k in range(1,4): assert not any(isdtd(set(S)) for S in combinations(range(20),k))
print('DUAL_OK',len(E),len(F),len(sol),len(pairsets),'induced_edges',Counter(sum(int(w in A[v]) for v,w in combinations(s,2)) for s in sol),'intersections',Counter(len(x&y) for x,y in combinations(sol,2)))
# Quotient by distance-five involution and two-replacement state graph.
rep=lambda v:min(v,ant[v])
quot=set(tuple(sorted((rep(v),rep(w)))) for v in range(20) for w in A[v] if rep(v)!=rep(w))
assert len(quot)==15
assert len({rep(v) for v in range(20)})==10
assert all(sum(a in e for e in quot)==3 for a in {rep(v) for v in range(20)})
stateimage={s:next((e for e in quot if s==frozenset((*e,*map(lambda v:ant[v],e)))),None) for s in sol}
assert all(x is not None for x in stateimage.values())
assert len(set(stateimage.values()))==15
R={s:set() for s in sol}
for x,y in combinations(sol,2):
 if len(x&y)==2: R[x].add(y);R[y].add(x)
 assert (len(x&y)==2)==(len(set(stateimage[x])&set(stateimage[y]))==1)
assert all(len(R[s])==4 for s in R)
assert sum(map(len,R.values()))//2==30
# Unrelated construction: quotient has girth 5 and diameter 2, and thus is Petersen.
vertices=set(rep(v) for v in range(20));qa={v:set() for v in vertices}
for a,b in quot:qa[a].add(b);qa[b].add(a)
assert len(vertices)==10 and all(len(qa[v])==3 for v in vertices)
assert not any(a in qa[b] for v in vertices for a,b in combinations(qa[v],2))
assert not any(len(qa[a]&qa[b])==2 for a,b in combinations(vertices,2))
assert all(len(qa[a]&qa[b])==1 for a,b in combinations(vertices,2) if a!=b and b not in qa[a])
# The quotient is the (3,5)-Moore graph, uniquely the Petersen graph.
ecc=[]
for src in sol:
 dist={src:0};q=deque([src])
 while q:
  x=q.popleft()
  for y in R[x]:
   if y not in dist:dist[y]=dist[x]+1;q.append(y)
 assert len(dist)==15
 ecc.append(max(dist.values()))
assert set(ecc)=={3}
print('DUAL2_OK optima=15 radius=3 diameter=3 two_token_edges=30 one_token_edges=0 quotient_degree=3 quotient_5cycle_girth')
