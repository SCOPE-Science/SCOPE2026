#!/usr/bin/env python3
"""Alternate shortest-path multiplicity and full-set enumerator; Python 3 stdlib only.

Run: python3 verify_meg_independent.py
"""
from array import array
from collections import Counter, deque
from itertools import combinations


def graph(kind):
    if kind == 'P':
        names=list(combinations(range(5),2))
        ed=[(i,j) for i in range(10) for j in range(i+1,10) if not(set(names[i])&set(names[j]))]
        return names,ed
    if kind == 'S':
        pairs=list(combinations(range(5),2))
        triples=list(combinations(range(5),3))
        names=pairs+triples
        ed=[(i,10+j) for i,a in enumerate(pairs) for j,b in enumerate(triples) if set(a)<=set(b)]
        return names,ed
    if kind == 'D':
        names=[('outer',i) for i in range(10)]+[('inner',i) for i in range(10)]
        ed=set()
        def add(a,b):ed.add(tuple(sorted((a,b))))
        for i in range(10):
            add(i,(i+1)%10)
            add(i,10+i)
            add(10+i,10+(i+2)%10)
        return names,sorted(ed)
    raise ValueError(kind)

def path_info(n,ed):
    adj=[[] for _ in range(n)]
    for a,b in ed:adj[a].append(b);adj[b].append(a)
    ds=[];ws=[]
    for s in range(n):
        dist=[-1]*n;ways=[0]*n;dist[s]=0;ways[s]=1;q=deque([s])
        while q:
            v=q.popleft()
            for u in adj[v]:
                if dist[u]==-1:dist[u]=dist[v]+1;q.append(u)
                if dist[u]==dist[v]+1:ways[u]+=ways[v]
        assert -1 not in dist
        ds.append(dist);ws.append(ways)
    return ds,ws

def inspect(kind,expect,mu,expect_min,components_expected):
    names,ed=graph(kind);n=len(names);N=1<<n
    assert len(ed)==3*n//2 and len(set(tuple(sorted(e)) for e in ed))==len(ed)
    d,w=path_info(n,ed)
    paircover=[[0]*n for _ in range(n)]
    for s in range(n):
        for t in range(s+1,n):
            bits=0
            for z,(a,b) in enumerate(ed):
                uses=0
                if d[s][a]+1+d[b][t]==d[s][t]:uses += w[s][a]*w[b][t]
                if d[s][b]+1+d[a][t]==d[s][t]:uses += w[s][b]*w[a][t]
                assert uses<=w[s][t]
                if uses==w[s][t]:bits|=1<<z
            paircover[s][t]=paircover[t][s]=bits
    cover=array('Q',[0])*N
    valid=bytearray(N)
    hist=[0]*(n+1);minima=[]
    all_edges=(1<<len(ed))-1
    for mask in range(1,N):
        v=mask.bit_length()-1
        r=mask^(1<<v)
        x=cover[r]
        tail=r
        while tail:
            b=tail&-tail;u=b.bit_length()-1;tail-=b
            x|=paircover[v][u]
        cover[mask]=x
        if x==all_edges:
            valid[mask]=1;k=mask.bit_count();hist[k]+=1
            if k==mu:minima.append(mask)
    assert hist==expect,(kind,hist,expect)
    assert len(minima)==expect[mu]
    minhist=[0]*(n+1)
    for m in range(1,N):
        if not valid[m]:continue
        r=m;minimal=True
        while r:
            b=r&-r;r-=b
            if valid[m^b]:minimal=False;break
        if minimal:minhist[m.bit_count()]+=1
    assert minhist==expect_min,(kind,minhist,expect_min)
    isets=[]
    maxind=0
    for mask in range(N):
        if not any((mask>>a&1) and (mask>>b&1) for a,b in ed):
            k=mask.bit_count()
            if k>maxind:maxind=k;isets=[]
            if k==maxind:isets.append(mask)
    assert (maxind,len(isets))=={'P':(4,5),'D':(8,5),'S':(10,2)}[kind]
    if kind=='P':assert set(((N-1)^m for m in minima))==set(isets)
    if kind=='D':assert set(isets).issubset(minima)
    if kind=='S':assert set(isets)==set(minima)
    if kind=='D':
        geometry=Counter()
        for m in minima:
            induced=[(a,b) for a,b in ed if m>>a&1 and m>>b&1]
            mx=max((sum(1 for a,b in induced if v in (a,b)) for v in range(n)),default=0)
            geometry[(len(induced),mx)]+=1
        assert geometry==Counter({(0,0):5,(3,1):20}),geometry
    if kind=='S':
        shores={sum(1<<i for i in range(10)),sum(1<<(i+10) for i in range(10))}
        assert set(minima)==shores,(kind,minima)
    if kind=='P':
        assert all(not any(m>>a&1==0 and m>>b&1==0 for a,b in ed) for m in minima)
    for budget,counts in components_expected.items():
        seen=bytearray(N);pieces=Counter();total=0
        for root in range(N):
            if not valid[root] or root.bit_count()>budget or seen[root]:continue
            seen[root]=1;q=deque([root]);sz=0
            while q:
                m=q.popleft();sz+=1
                for i in range(n):
                    v=m^(1<<i)
                    if valid[v] and not seen[v] and v.bit_count()<=budget:
                        seen[v]=1;q.append(v)
            total+=sz;pieces[sz]+=1
        assert pieces==counts,(kind,budget,pieces,counts)
        assert total==sum(hist[:budget+1])
    print(kind,'number of vertices',n,'minimum',mu,'optimal',len(minima),'MEG total',sum(hist),'confirmed')

inspect('P',[0,0,0,0,0,0,5,30,30,10,1],6,
        [0,0,0,0,0,0,5,10,0,0,0],{6:{1:5},7:{1:10,5:5},8:{65:1}})
inspect('D',[0,0,0,0,0,0,0,0,25,1840,13686,37020,54000,49880,31650,14392,4765,1140,190,20,1],8,
        [0,0,0,0,0,0,0,0,25,1540,2006,0,0,0,0,0,0,0,0,0,0],
        {8:{1:25},9:{1:1540,13:25},10:{1:2006,13545:1},11:{52571:1}})
inspect('S',[0,0,0,0,0,0,0,0,0,0,2,20,115,480,1320,1924,1510,660,160,20,1],10,
        [0,0,0,0,0,0,0,0,0,0,2,0,25,60,100,0,0,0,0,0,0],
        {10:{1:2},11:{11:2},12:{1:25,56:2},13:{1:60,9:5,256:2},14:{1:100,1837:1},15:{3861:1}})
print('MEG_INDEPENDENT_ALL_CHECKS_OK')
