"""Independent direct edge-distance signature and pairwise replacement enumerator."""
from itertools import combinations
from collections import Counter,deque
links={0:(1,4,6,9),1:(2,5,7),2:(3,6,8),3:(4,7,9),4:(5,8),5:(10,11),6:(10,11),7:(8,11),8:(10,),9:(10,11)}
edges=sorted((v,w) for v,nbr in links.items() for w in nbr)
assert len(edges)==24
adj=[[False]*12 for _ in range(12)]
for x,y in edges:adj[x][y]=adj[y][x]=True
inf=1000000
d=[[0 if u==v else 1 if adj[u][v] else inf for v in range(12)] for u in range(12)]
for k in range(12):
 for u in range(12):
  for v in range(12):d[u][v]=min(d[u][v],d[u][k]+d[k][v])
sig=[[min(d[v][u],d[v][w]) for u,w in edges] for v in range(12)]
def resolves(s):return len({tuple(sig[v][j] for v in s) for j in range(24)})==24
assert all(not resolves(s) for s in combinations(range(12),4))
B=[s for s in combinations(range(12),5) if resolves(s)];assert len(B)==192
J=[set() for _ in B];S=[set() for _ in B]
for i,a in enumerate(B):
 for j in range(i+1,len(B)):
  b=B[j];shared=set(a)&set(b)
  if len(shared)!=4:continue
  J[i].add(j);J[j].add(i)
  u=next(x for x in a if x not in shared);v=next(x for x in b if x not in shared)
  if adj[u][v]:S[i].add(j);S[j].add(i)
assert sum(map(len,J))//2==1152 and sum(map(len,S))//2==428
assert Counter(map(len,S))=={2:28,3:32,4:48,5:32,6:32,7:8,8:8,10:4}
def traversal(A):
 ec=Counter()
 for root in range(len(A)):
  seen={root:0};q=deque([root])
  while q:
   u=q.popleft()
   for v in A[u]:
    if v not in seen:seen[v]=seen[u]+1;q.append(v)
  assert len(seen)==len(A)
  ec[max(seen.values())]+=1
 return ec
assert traversal(J)=={5:192} and traversal(S)=={6:120,7:72}
print('basis_count=192 jump_edges=1152 slide_edges=428')
print('connected_both=True jump_radius_diameter=(5,5) slide_radius_diameter=(6,7)')
print('slide_degree='+str(dict(sorted(Counter(map(len,S)).items()))))
print('eccentricity_slide={6:120,7:72}')
print('PASS')
