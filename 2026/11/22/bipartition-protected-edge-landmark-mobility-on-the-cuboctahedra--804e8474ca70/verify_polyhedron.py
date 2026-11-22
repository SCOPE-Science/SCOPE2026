#!/usr/bin/env python3
"""Independent Cartesian-coordinate and witness-set verification of cuboctahedron."""
from itertools import product,combinations
from collections import defaultdict,Counter,deque
import json

P=sorted({tuple(v) for v in product((-1,0,1),repeat=3)
          if sum(x==0 for x in v)==1 and sum(abs(x) for x in v)==2})
assert len(P)==12
n=len(P)
def norm2(a,b):return sum((x-y)**2 for x,y in zip(a,b))
A=[[i!=j and norm2(P[i],P[j])==2 for j in range(n)] for i in range(n)]
assert all(sum(row)==4 for row in A)
G_edges=[(i,j) for i in range(n) for j in range(i+1,n) if A[i][j]]
assert len(G_edges)==24

dist=[]
for s in range(n):
    d=[-1]*n;d[s]=0;to=[s]
    for x in to:
        for y in range(n):
            if A[x][y] and d[y]==-1:d[y]=d[x]+1;to.append(y)
    assert all(z>=0 for z in d)
    dist.append(d)

def optima(columns):
    p=len(columns[0]);witness=[]
    for x in range(p):
        for y in range(x+1,p):
            witness.append(sum((1<<s) for s in range(n) if columns[s][x]!=columns[s][y]))
    assert all(witness)
    allgood=[m for m in range(1<<n) if all(m&z for z in witness)]
    k=min(map(int.bit_count,allgood))
    return k, sorted(m for m in allgood if m.bit_count()==k)

edge_columns=[[min(dist[v][a],dist[v][b]) for a,b in G_edges] for v in range(n)]
edge_k,edge_sets=optima(edge_columns)
node_k,node_sets=optima(dist)
assert (edge_k,len(edge_sets))==(5,168)
assert (node_k,len(node_sets))==(3,96)

def stats(states):
    mp={a:i for i,a in enumerate(states)}
    jumps=[[] for _ in states];slides=[[] for _ in states]
    for i,s in enumerate(states):
        for j,t in enumerate(states):
            if i>=j:continue
            removed=s&~t;added=t&~s
            if removed.bit_count()==1 and added.bit_count()==1:
                jumps[i].append(j);jumps[j].append(i)
                u=removed.bit_length()-1;v=added.bit_length()-1
                if A[u][v]:slides[i].append(j);slides[j].append(i)
    def scan(adj):
        unseen=set(range(len(states)));comps=[];ec=Counter();dc=Counter();ecc=Counter()
        while unseen:
            start=next(iter(unseen));seen={start};front=[start];unseen.remove(start)
            while front:
                nxt=[]
                for u in front:
                    for v in adj[u]:
                        if v in unseen:unseen.remove(v);seen.add(v);nxt.append(v)
                front=nxt
            radius=len(states);diam=0
            for start in seen:
                d=[-1]*len(states);d[start]=0;queue=[start]
                for x in queue:
                    for y in adj[x]:
                        if d[y]<0:d[y]=d[x]+1;queue.append(y)
                assert len(queue)==len(seen)
                md=max(d);radius=min(radius,md);diam=max(diam,md);ecc[md]+=1
                for y in seen:
                    if y>start:dc[d[y]]+=1
            comps.append((len(seen),radius,diam))
        ec.update({v:sum(len(a) for a in adj)//2 for v in ["edges"]})
        return dict(n=len(states),edges=ec['edges'],components=sorted(comps),
                    distance_counts=dict(sorted(dc.items())),
                    degree_counts=dict(sorted(Counter(map(len,adj)).items())),
                    eccentricity_counts=dict(sorted(ecc.items())))
    return scan(jumps),scan(slides),slides

ej,es,slide=stats(edge_sets)
nj,ns,_=stats(node_sets)

# Every chosen cuboctahedral vertex has a unique representation as an edge of the 3-cube.
def endpoints(p):
    z=p.index(0)
    a=sum(((1 if p[i]==1 else 0)<<i) for i in range(3) if i!=z)
    return a,a|(1<<z)
edge_end=[endpoints(p) for p in P]
miss={};groups=defaultdict(set)
for i,mask in enumerate(edge_sets):
    covered={v for j,(a,b) in enumerate(edge_end) if mask>>j&1 for v in (a,b)}
    absent=set(range(8))-covered
    assert len(absent)==1
    m=next(iter(absent));miss[i]=m;groups[m.bit_count()%2].add(i)
assert sorted(map(len,groups.values()))==[84,84]
assert Counter(miss.values())==Counter({i:21 for i in range(8)})
for i in range(len(slide)):
    assert all(miss[i].bit_count()%2==miss[j].bit_count()%2 for j in slide[i])
assert es['components']==[(84,6,6),(84,6,6)]
assert ej['components']==[(168,5,5)]
assert ns['components']==[(96,7,8)]
assert ej['distance_counts']=={1:948,2:2688,3:4704,4:5160,5:528}
assert es['distance_counts']=={1:360,2:840,3:1512,4:1992,5:1740,6:528}
assert es['degree_counts']=={3:48,4:48,5:48,6:24}
print(json.dumps(dict(edge_dim=edge_k,edge_bases=len(edge_sets),metric_dim=node_k,
    metric_bases=len(node_sets),edge_jump=ej,edge_slide=es,vertex_jump=nj,
    vertex_slide=ns,missing_counts=dict(sorted(Counter(miss.values()).items()))),sort_keys=True))
