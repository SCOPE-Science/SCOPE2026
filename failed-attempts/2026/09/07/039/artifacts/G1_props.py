import numpy as np
from collections import deque

def petersen_edges():
    E=[]
    for i in range(5):
        E.append((i,(i+1)%5))
    for i in range(5):
        E.append((i,5+i))
    for i in range(5):
        E.append((5+i,5+((i+2)%5)))
    return E
E0=petersen_edges()
s1=[1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,-1]

# Build G1: 20 vertices, lift of Petersen by s1
# edge (u,v) sign +1: (u,0)-(v,0),(u,1)-(v,1); -1: cross
def lift_edges(E, signs, n):
    LE=[]
    for (u,v),s in zip(E,signs):
        if s==1:
            LE.append((u,v)); LE.append((u+n,v+n))
        else:
            LE.append((u,v+n)); LE.append((u+n,v))
    return LE
E1=lift_edges(E0,s1,10)
print("G1 edges:",len(E1))
N1=20
A1=np.zeros((N1,N1))
for u,v in E1:
    A1[u,v]+=1; A1[v,u]+=1
ev1=np.linalg.eigvalsh(A1)
print("G1 spectrum:",np.round(ev1,6))
print("lambda:",max(abs(ev1[np.abs(np.abs(ev1)-3)>1e-6])))
# connectivity
adj=[[] for _ in range(N1)]
for u,v in E1:
    adj[u].append(v); adj[v].append(u)
vis=[False]*N1; dq=deque([0]); vis[0]=True
while dq:
    u=dq.popleft()
    for w in adj[u]:
        if not vis[w]: vis[w]=True; dq.append(w)
print("connected:",all(vis))
# bipartite?
col=[-1]*N1; col[0]=0; dq=deque([0]); bip=True
while dq:
    u=dq.popleft()
    for w in adj[u]:
        if col[w]==-1: col[w]=1-col[u]; dq.append(w)
        elif col[w]==col[u]: bip=False
print("bipartite:",bip)
# girth
def girth(N,adj):
    best=10**9
    for s in range(N):
        dist=[-1]*N; par=[-1]*N
        dist[s]=0; dq=deque([s])
        while dq:
            u=dq.popleft()
            for w in adj[u]:
                if dist[w]==-1:
                    dist[w]=dist[u]+1; par[w]=u; dq.append(w)
                elif par[u]!=w and par[w]!=u:
                    best=min(best,dist[u]+dist[w]+1)
    return best
print("girth G1:",girth(N1,adj))
# diameter
def diam(N,adj):
    d=0
    for s in range(N):
        dist=[-1]*N; dist[s]=0; dq=deque([s])
        while dq:
            u=dq.popleft()
            for w in adj[u]:
                if dist[w]==-1: dist[w]=dist[u]+1; dq.append(w)
        d=max(d,max(dist))
    return d
print("diam G1:",diam(N1,adj))
# save edge list
import json
json.dump({"E1":E1,"s1":s1},open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/G1.json","w"))
