from collections import Counter,deque
from itertools import combinations,permutations
N=16
edges=tuple((v,v^(1<<i)) for v in range(N) for i in range(4) if v<(v^(1<<i)))
edge_index={e:j for j,e in enumerate(edges)}
adj={v:tuple(v^(1<<i) for i in range(4)) for v in range(N)}
C=set()
def dfs(path,mask):
 if len(path)==N:
  if 0 not in adj[path[-1]]:return
  es=(tuple(sorted(e)) for e in zip(path,path[1:]+[0]))
  C.add(sum(1<<edge_index[e] for e in es));return
 for y in adj[path[-1]]:
  if not mask>>y&1:dfs(path+[y],mask|1<<y)
dfs([0],1)
face_masks=set()
for i,j in combinations(range(4),2):
 for v in range(N):
  sq={v,v^(1<<i),v^(1<<j),v^(1<<i)^(1<<j)}
  mask=sum(1<<edge_index[e] for e in edges if set(e)<=sq)
  face_masks.add(mask)
G={x:set() for x in C}
for x in C:
 for face in face_masks:
  common=x&face
  if common.bit_count()!=2:continue
  e=[edges[i] for i in range(32) if common>>i&1]
  if set(e[0]).isdisjoint(e[1]):
   y=x^face
   if y in C:G[x].add(y)
assert all(x in G[y] for x in C for y in G[x])
components=[];seen=set()
for x in sorted(C):
 if x in seen:continue
 comp={x};queue=[x];seen.add(x)
 for v in queue:
  for w in G[v]:
   if w not in seen:seen.add(w);comp.add(w);queue.append(w)
 components.append(comp)
print('C',len(C),'faces',len(face_masks),'E',sum(map(len,G.values()))//2,'comps',Counter(map(len,components)))
print('deg',dict(sorted(Counter(map(len,G.values())).items())))
large=max(components,key=len)
Ecc=Counter();pairs=Counter();rad=1e9;diam=0
for i,v in enumerate(sorted(large)):
 dist={v:0};q=deque([v])
 while q:
  w=q.popleft()
  for u in G[w]:
   if u not in dist:dist[u]=dist[w]+1;q.append(u)
 assert len(dist)==len(large)
 ecc=max(dist.values());Ecc[ecc]+=1;rad=min(rad,ecc);diam=max(diam,ecc)
print('radius',rad,'diam',diam,'ecc spectrum',dict(sorted(Ecc.items())))
# sorted graph orbits
emaps=[]
for p in permutations(range(4)):
 for shift in range(16):
  trans=[]
  for a,b in edges:
   def m(v):return shift ^ sum(1<<p[i] for i in range(4) if v>>i&1)
   trans.append(edge_index[tuple(sorted((m(a),m(b))))])
  emaps.append(trans)
assert len(emaps)==384
seen=set();orbitsets=[]
for x in sorted(C):
 if x in seen:continue
 o=set(sum(1<<em[i] for i in range(32) if x>>i&1) for em in emaps)
 assert o.issubset(C)
 orbitsets.append(o);seen|=o
assert seen==C
orbitsets.sort(key=lambda o:(len(G[min(o)]),len(o),min(o)))
label={c:i for i,o in enumerate(orbitsets) for c in o}
for i,o in enumerate(orbitsets):
 rep=min(o);freq=[0]*4
 for e,b in enumerate(edges):
  if rep>>e&1:freq[(b[0]^b[1]).bit_length()-1]+=1
 q=Counter(label[v] for v in G[rep])
 assert all(Counter(label[v] for v in G[u])==q for u in o)
 print('orbit',i,'size',len(o),'degree',len(G[rep]),'profile',sorted(freq),'neighbor_orbits',[q[j] for j in range(9)],'rep_mask',f'{rep:08x}')
