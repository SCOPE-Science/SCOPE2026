import numpy as np, json
from collections import deque

G1=json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/G1.json"))
E1=[tuple(e) for e in G1["E1"]]; s1=G1["s1"]
s2=json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/s2_charpoly.json"))["s2"]
E0=[(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(1,6),(2,7),(3,8),(4,9),(5,7),(6,8),(7,9),(8,5),(9,6)]
# G2: lift of G1 by s2
def lift(E,sg,n):
    LE=[]
    for (u,v),s in zip(E,sg):
        if s==1: LE.extend([(u,v),(u+n,v+n)])
        else: LE.extend([(u,v+n),(u+n,v)])
    return LE
E2=lift(E1,s2,20)
N2=40
A2=np.zeros((N2,N2))
for u,v in E2: A2[u,v]+=1; A2[v,u]+=1
ev=np.linalg.eigvalsh(A2)
print("G2 spectrum:",np.round(ev,6))
triv=np.abs(np.abs(ev)-3)<1e-6
lam=float(max(abs(e) for e,t in zip(ev,triv) if not t))
print("lambda(G2)=",lam, " Ramanujan?", lam<=2*np.sqrt(2))
adj=[[] for _ in range(N2)]
for u,v in E2: adj[u].append(v); adj[v].append(u)
vis=[False]*N2; dq=deque([0]); vis[0]=True
while dq:
    u=dq.popleft()
    for w in adj[u]:
        if not vis[w]: vis[w]=True; dq.append(w)
print("connected:",all(vis))
col=[-1]*N2; col[0]=0; dq=deque([0]); bip=True
odd=None
while dq:
    u=dq.popleft()
    for w in adj[u]:
        if col[w]==-1: col[w]=1-col[u]; dq.append(w)
        elif col[w]==col[u]: bip=False
print("bipartite:",bip, "(no -3 eigenvalue:",float(min(ev))>-3+1e-6,")")
def girth(N,adj):
    best=10**9;wit=None
    for s in range(N):
        dist=[-1]*N;par=[-1]*N;dist[s]=0;dq=deque([s])
        while dq:
            u=dq.popleft()
            for w in adj[u]:
                if dist[w]==-1: dist[w]=dist[u]+1;par[w]=u;dq.append(w)
                elif par[u]!=w and par[w]!=u:
                    if dist[u]+dist[w]+1<best: best=dist[u]+dist[w]+1
    return best
def diam(N,adj):
    d=0
    for s in range(N):
        dist=[-1]*N;dist[s]=0;dq=deque([s])
        while dq:
            u=dq.popleft()
            for w in adj[u]:
                if dist[w]==-1: dist[w]=dist[u]+1;dq.append(w)
        d=max(d,max(dist))
    return d
print("girth:",girth(N2,adj),"diam:",diam(N2,adj))
print("min ev:",min(ev))
json.dump({"E2":E2},open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/G2.json","w"))
