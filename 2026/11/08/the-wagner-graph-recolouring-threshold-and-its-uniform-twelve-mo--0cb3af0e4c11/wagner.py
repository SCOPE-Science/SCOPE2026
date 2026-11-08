#!/usr/bin/env python3
"""Exact recoloring geometry of Wagner graph via direct labelled graph enumeration."""
from collections import Counter,deque
N=8
edges={(min(i,(i+1)%8),max(i,(i+1)%8)) for i in range(N)}|{(i,i+4) for i in range(4)}
adj=[set() for _ in range(N)]
for i,j in edges:adj[i].add(j);adj[j].add(i)

def compute(k):
 state=[];x=[-1]*N
 def dfs(pos):
  if pos==N:state.append(tuple(x));return
  forbidden={x[z] for z in adj[pos] if x[z]>=0}
  for c in range(k):
   if c not in forbidden:x[pos]=c;dfs(pos+1)
  x[pos]=-1
 dfs(0)
 d={s:i for i,s in enumerate(state)}
 g=[]
 for s in state:
  neighbor=[]
  for i in range(N):
   forbidden={s[z] for z in adj[i]}
   for c in range(k):
    if c!=s[i] and c not in forbidden:
     y=list(s);y[i]=c;neighbor.append(d[tuple(y)])
  g.append(neighbor)
 assert all(v in g[w] for w,ns in enumerate(g) for v in ns)
 print(k,'vertices',len(state),'edges',sum(map(len,g))//2,'degrees',Counter(map(len,g)))
 cid=[-1]*len(state);cs=[]
 for j in range(len(state)):
  if cid[j]>=0:continue
  Q=deque([j]);cid[j]=len(cs);q=0
  while Q:
   v=Q.popleft();q+=1
   for w in g[v]:
    if cid[w]<0:cid[w]=len(cs);Q.append(w)
  cs.append(q)
 print(k,'components',len(cs),Counter(cs))
 if len(state)<=20000:
  # dihedral plus palette swaps group
  transformations=[]
  for shift in range(1,2): transformations.append(([ (t+shift)%N for t in range(N)],list(range(k))))
  transformations.append(([(-t)%N for t in range(N)],list(range(k))))
  for a in range(k-1):
   p=list(range(k));p[a],p[a+1]=p[a+1],p[a]; transformations.append((list(range(N)),p))
  oid=[-1]*len(state);orbits=[]
  for z in range(len(state)):
   if oid[z]>=0:continue
   o=len(orbits);Q=deque([z]);oid[z]=o;vs=[]
   while Q:
    v=Q.popleft();vs.append(v)
    for vp,cp in transformations:
     y=d[tuple(cp[state[v][vp[t]]] for t in range(N))]
     if oid[y]<0:oid[y]=o;Q.append(y)
   orbits.append(vs)
  ecc=Counter();total=Counter();outs=[]
  for orbit in orbits:
   root=orbit[0];dis=[-1]*len(state);dis[root]=0;Q=deque([root]);hs=Counter({0:1})
   while Q:
    v=Q.popleft()
    for w in g[v]:
     if dis[w]<0: dis[w]=dis[v]+1;hs[dis[w]]+=1;Q.append(w)
   dmax=max(dis)
   ecc[dmax]+=len(orbit)
   for h,n in hs.items():total[h]+=n*len(orbit)
   outs.append((len(orbit),dmax,tuple(hs.get(i,0) for i in range(dmax+1)),''.join(map(str,state[root]))))
  print(k,'orbits',len(orbits),'ecc',ecc,'pairdist',{a:b//2 if a>0 else b for a,b in sorted(total.items())})
  print('orbits summary',outs)
 return state,g

if __name__=='__main__':
 order=(0,1,2,4,3,5,6,7)
 greedy={}
 for v in order:
  forbidden={greedy[u] for u in adj[v] if u in greedy}
  a=0
  while a in forbidden:a+=1
  greedy[v]=a
 assert tuple(greedy[v] for v in range(8))==(0,1,0,2,1,0,1,3)
 print('grundy_witness_order',order,'greedy_colors',tuple(greedy[v] for v in range(8)))
 for k in (3,4):compute(k)
