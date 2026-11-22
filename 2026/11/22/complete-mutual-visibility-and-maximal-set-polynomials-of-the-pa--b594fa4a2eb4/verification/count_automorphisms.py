from collections import deque

# Independent exact automorphism count; distance-preserving bijections are exactly graph automorphisms.
n = 18
adj = [[] for _ in range(n)]
for x in range(3):
 for y in range(3):
  for m in range(3):
   for b in range(3):
    if y == (m*x+b) % 3:
     a, z = 3*x+y, 9+3*m+b
     adj[a].append(z)
     adj[z].append(a)
dist=[]
for s in range(n):
 d=[-1]*n;d[s]=0;q=deque([s])
 while q:
  v=q.popleft()
  for u in adj[v]:
   if d[u]<0:d[u]=d[v]+1;q.append(u)
 assert -1 not in d
 dist.append(d)

count=0

def rec(mapping, unused):
 global count
 if not unused:
  assert len(mapping)==n
  count+=1
  return
 best=None;bestcand=None
 for v in range(n):
  if v in mapping:continue
  cand=[j for j in unused if all(dist[v][u]==dist[j][w] for u,w in mapping.items())]
  if not cand:return
  if bestcand is None or len(cand)<len(bestcand):
   best,bestcand=v,cand
   if len(cand)==1:break
 for j in bestcand:
  mapping[best]=j
  rec(mapping, unused-{j})
  del mapping[best]

rec({},set(range(n)))
print('all distance-preserving bijections (graph automorphisms):',count)
assert count==216
