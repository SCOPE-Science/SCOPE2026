"""Complete labelled J_5 synchronous strict-majority census, indegree peeling."""
from collections import Counter, deque
import json
n=5; N=4*n; L=1<<N
adj=[0]*N
def edge(i,j):
 assert i!=j and not (adj[i]>>j)&1
 adj[i]|=1<<j;adj[j]|=1<<i
for i in range(n):
 for j in (n+i,2*n+i,3*n+i): edge(i,j)
 edge(n+i,n+(i+1)%n)
cyc=[2*n+i for i in range(n)]+[3*n+i for i in range(n)]
for i in range(2*n):edge(cyc[i],cyc[(i+1)%(2*n)])
assert all(m.bit_count()==3 for m in adj)
F=[0]*L
for x in range(L):
 y=0
 for i,m in enumerate(adj):
  if (x&m).bit_count()>=2:y|=1<<i
 F[x]=y
# indegree stripping and dynamic programming toward attractors
ind=[0]*L
for y in F:ind[y]+=1
q=deque(i for i,k in enumerate(ind) if k==0)
removed=[]
while q:
 x=q.popleft();removed.append(x);y=F[x];ind[y]-=1
 if ind[y]==0:q.append(y)
root=[-1]*L;depth=[-1]*L;period={};rstates=set();cycles=[]
for i in range(L):
 if ind[i]<=0 or root[i]>=0:continue
 cyc=[];y=i
 while root[y]<0:
  root[y]=i;depth[y]=0;cyc.append(y);y=F[y]
 assert y==i
 r=min(cyc)
 for x in cyc:root[x]=r
 period[r]=len(cyc);cycles.append(cyc)
for x in reversed(removed):
 y=F[x];root[x]=root[y];depth[x]=depth[y]+1
assert all(k>=0 for k in depth)
by_entry=Counter((depth[i],period[root[i]]) for i in range(L))
basin=Counter(root)
basin_spectrum=Counter((period[r],c) for r,c in basin.items())
maxd=max(depth)
sumconsensus=basin[0]+basin[L-1]
summary={"vertices":N,"edges":sum(a.bit_count() for a in adj)//2,"states":L,"orbit_period_counts":sorted(Counter(period.values()).items()),"entry_period":sorted((d,p,c) for (d,p),c in by_entry.items()),"maximum_entry":maxd,"maximum_entry_population":sum(d==maxd for d in depth),"basin_spectrum":sorted((p,size,mul) for (p,size),mul in basin_spectrum.items()),"unanimous_basins":[basin[0],basin[L-1]],"oscillatory_basin_total":sum(c for r,c in basin.items() if period[r]==2),"sample_max_depth_state":next(i for i,d in enumerate(depth) if d==maxd),"adjacency_masks":adj}
assert sum(p*k for p,k in summary['orbit_period_counts'])==sum(d==0 for d in depth)
assert sum(size*mul for p,size,mul in summary['basin_spectrum'])==L
assert sum(c for d,p,c in summary['entry_period'])==L
print(json.dumps(summary,sort_keys=True,indent=2))
