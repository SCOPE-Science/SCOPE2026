from fractions import Fraction
from collections import deque,Counter
V=list(range(1,8))
lines=sorted(set(tuple(sorted((a,b,a^b))) for a in V for b in V if a!=b))
assert len(lines)==7
edge=[(i,7+j) for i,a in enumerate(V) for j,L in enumerate(lines) if a in L]
assert len(edge)==21
adj=[[] for _ in range(14)]
for u,v in edge:adj[u].append(v);adj[v].append(u)
assert all(len(z)==3 for z in adj)
all_d=[]
for root in range(14):
 dist={root:0};Q=deque([root])
 while Q:
  u=Q.popleft()
  for v in adj[u]:
   if v not in dist: dist[v]=dist[u]+1;Q.append(v)
 assert len(dist)==14 and Counter(dist.values())=={0:1,1:3,2:6,3:4}
 all_d.extend(dist.values())
metric=Fraction(sum(all_d),14*13)
assert metric==Fraction(27,13)
best=Fraction(0);winner=[];profile={}
for mask in range(1,(1<<14)-1):
 k=mask.bit_count(); b=sum(bool(mask&(1<<u))!=bool(mask&(1<<v)) for u,v in edge)
 if k>7: continue
 prof=profile.get(k,100)
 profile[k]=min(prof,b)
 ratio=Fraction(k*(14-k)*21,91*b)
 if ratio>best:best=ratio;winner=[mask]
 elif ratio==best:winner.append(mask)
assert best==Fraction(24,13)
assert len(winner)==28
assert all(x.bit_count()==6 for x in winner)
assert all(sum(bool(x&(1<<u)) and bool(x&(1<<v)) for u,v in edge)==6 for x in winner)
print('HEAWOOD_EXACT_OK metric',metric,'l1',best,'six_cycle_witnesses',len(winner),'min_boundary_by_k',profile)
