#!/usr/bin/env python3
"""Independent hole/side model; full distances and explicit routes for crown bases."""
from collections import deque
from itertools import product


def all_states(n):
    for h in range(n):
        for bits in range(1<<(n-1)):
            colors=[-1]*n
            k=0
            for i in range(n):
                if i!=h:
                    colors[i]=(bits>>k)&1
                    k+=1
            yield (h,tuple(colors))


def step(state,i):
    h,x=state
    assert i!=h and x[h]==-1
    y=list(x)
    y[h]=1-y[i]
    y[i]=-1
    return (i,tuple(y))


def legal_path(start,holes):
    curr=start
    assert holes[0]==start[0]
    for h in holes[1:]:
        curr=step(curr,h)
    return curr


def graph(n):
    states=list(all_states(n))
    idx={s:i for i,s in enumerate(states)}
    assert len(states)==len(idx)==n*2**(n-1)
    adj=[tuple(idx[step(s,j)] for j in range(n) if j!=s[0]) for s in states]
    for v,nb in enumerate(adj):
        assert len(set(nb))==n-1
        assert all(v in adj[w] for w in nb)
    return states,adj


def diameter(n,full):
    states,adj=graph(n)
    if full:
        starts=range(len(states))
    else:
        starts=[i for i,s in enumerate(states) if s[0]==0 and s[1].count(1) in range(n)][:3]
        starts+=list(range(0,len(states),max(1,len(states)//11)))
    diam=0
    for j in starts:
        dist=[-1]*len(states)
        dist[j]=0
        q=deque([j])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dist[v]<0:
                    dist[v]=dist[u]+1
                    q.append(v)
        assert all(d>=0 for d in dist), (n,j)
        diam=max(diam,max(dist))
        assert max(dist)==n+3,(n,j,max(dist))
    assert diam==n+3
    return len(states),len(starts),diam


def test_explicit(n):
    for bits in product((0,1),repeat=n-1):
        X=(0,tuple([-1]+list(bits)))
        if n>=4:
            # All sides inverted, hole unchanged. Find two equal colors.
            p,q=next((p,q) for p in range(1,n) for q in range(p+1,n) if X[1][p]==X[1][q])
            c=X[1][p]
            opp=[i for i in range(1,n) if X[1][i]!=c]
            same=[i for i in range(1,n) if X[1][i]==c and i not in (p,q)]
            path=[0,p,q,0]+opp+[p,q]+same+[0]
            Y=(0,tuple([-1]+[1-a for a in bits]))
            assert len(path)-1==n+3
            assert legal_path(X,path)==Y,(n,bits,path)
        # Hole changes, all source sides same: n+2-step constructive path.
    for c in (0,1):
        X=(0,tuple([-1]+[c]*(n-1)))
        target=[1-c]*n
        target[0]=c
        target[1]=-1
        path=[0,2,1,0,2]+list(range(3,n))+[1]
        assert len(path)-1==n+2,(n,path)
        assert legal_path(X,path)==(1,tuple(target)),(n,c,path,legal_path(X,path))
    return 2**(n-1)+2

if __name__=='__main__':
    for n in range(3,9):
        states,starts,diam=diameter(n,True)
        print(f'n={n} states={states} bfs_starts={starts} exact_diameter={diam} PASS')
    for n in range(9,12):
        states,starts,diam=diameter(n,False)
        print(f'n={n} states={states} bfs_starts={starts} tested_eccentricity={diam} PASS')
    for n in range(4,12):
        count=test_explicit(n)
        print(f'explicit_routes_n={n} checked={count} PASS')
    print('STATE_VERIFY_PASS full n=3..8 sampled n=9..11 explicit n=4..11')
