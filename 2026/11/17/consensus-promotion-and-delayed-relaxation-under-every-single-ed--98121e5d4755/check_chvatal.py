#!/usr/bin/env python3
"""Exhaustive independently executable certificate for edge-deleted majority on Chvatal's graph."""
from collections import Counter

EDGES = ((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
         (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
         (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))
N = 12
STATES = 1 << N
EXPECT = {
    None: (234,136,7,32,2906),
    (0,1): (118,82,11,24,3164),
    (0,6): (130,106,8,2,3094),
    (2,3): (126,118,7,20,3032),
    (2,6): (106,78,7,8,2996),
    (2,8): (144,128,8,4,3080),
}

def adjacency(removed=None):
    a = [[0]*N for _ in range(N)]
    for u,v in EDGES:
        if (u,v) == removed: continue
        a[u][v] = a[v][u] = 1
    return a

def symmetries():
    a=adjacency()
    # Ordering grows a connected patch; nonedges are checked as well as edges.
    order = [0,1,4,6,9,2,5,7,3,8,10,11]
    morphisms=[]
    f={}
    used=set()
    def extend(k):
        if k==N:
            morphisms.append(tuple(f[i] for i in range(N)))
            return
        u=order[k]
        for v in range(N):
            if v in used: continue
            if all(a[u][p]==a[v][q] for p,q in f.items()):
                used.add(v); f[u]=v
                extend(k+1)
                used.remove(v); del f[u]
    extend(0)
    assert len(morphisms)==8
    return morphisms

def spectrum(removed):
    a=adjacency(removed)
    masks = [sum((1<<j)*a[i][j] for j in range(N)) for i in range(N)]
    degree = [sum(row) for row in a]
    def forward(x):
        y=0
        for i in range(N):
            k=(x & masks[i]).bit_count()
            if 2*k>degree[i] or (2*k==degree[i] and x & (1<<i)):
                y|=1<<i
        return y
    f=[forward(x) for x in range(STATES)]
    depth=[-1]*STATES
    period=[0]*STATES
    rep=[-1]*STATES
    for start in range(STATES):
        if depth[start]>=0: continue
        chain=[]; position={};cur=start
        while depth[cur]<0 and cur not in position:
            position[cur]=len(chain)
            chain.append(cur)
            cur=f[cur]
        if depth[cur]>=0:
            for x in reversed(chain):
                depth[x]=depth[f[x]]+1
                period[x]=period[f[x]]
                rep[x]=rep[f[x]]
        else:
            c=position[cur]
            cyc=chain[c:]
            p=len(cyc)
            r=min(cyc)
            for x in cyc:
                depth[x]=0; period[x]=p; rep[x]=r
            for x in reversed(chain[:c]):
                depth[x]=depth[f[x]]+1
                period[x]=p
                rep[x]=r
    assert all(p in (1,2) for p in period)
    assert all(d>=0 for d in depth)
    assert all(0<=r<STATES for r in rep)
    assert sum(Counter((depth[x],period[x]) for x in range(STATES)).values()) == STATES
    fix=sum(depth[x]==0 and period[x]==1 for x in range(STATES))
    cyc=sum(depth[x]==0 and period[x]==2 for x in range(STATES))//2
    dmax=max(depth)
    ndmax=depth.count(dmax)
    # The two unanimous states are distinct fixed points.
    assert f[0]==0 and f[STATES-1]==STATES-1
    consensus=sum(rep[x] in (0,STATES-1) for x in range(STATES))
    return (fix,cyc,dmax,ndmax,consensus),Counter((depth[x],period[x]) for x in range(STATES))

def main():
    assert len(EDGES)==24
    A=adjacency()
    assert all(sum(row)==4 for row in A)
    assert not any(A[i][j] and A[j][k] and A[k][i]
                   for i in range(N) for j in range(i+1,N) for k in range(j+1,N))
    # Full finite chromatic check identifies this standard extremal graph.
    def colorable(q):
        colors=[-1]*N
        order=sorted(range(N),key=lambda i: -sum(A[i]))
        def search(k):
            if k==N: return True
            i=order[k]
            for c in range(q):
                if all(not A[i][j] or colors[j]!=c for j in range(N)):
                    colors[i]=c
                    if search(k+1): return True
                    colors[i]=-1
            return False
        return search(0)
    assert not colorable(3) and colorable(4)
    group=symmetries()
    remaining=set(EDGES)
    classes=[]
    while remaining:
        e=min(remaining)
        orbit={tuple(sorted((p[e[0]],p[e[1]]))) for p in group}
        assert orbit<=set(EDGES)
        classes.append((e,len(orbit)))
        remaining-=orbit
    assert classes==[((0,1),4),((0,6),8),((2,3),4),((2,6),4),((2,8),4)]
    baseline,base_hist=spectrum(None)
    assert baseline==EXPECT[None]
    assert base_hist==Counter({(0,1):234,(0,2):272,(1,1):754,(1,2):80,
        (2,1):1764,(2,2):16,(3,1):640,(4,1):136,(5,1):136,(6,1):32,(7,1):32})
    print('baseline',baseline,'histogram',sorted(base_hist.items()))
    all_types=Counter()
    for e in EDGES:
        t,h=spectrum(e)
        all_types[t]+=1
        assert t[4]>baseline[4]
        print('deleted',e,'result',t)
    assert all_types==Counter({EXPECT[e]:s for e,s in classes})
    for e,s in classes:
        print('orbit_representative',e,'orbit_size',s,'result',EXPECT[e])
    print('PASS 25 exhaustive maps, 8 automorphisms, 5 edge orbits, all 4096 states each')

if __name__=='__main__':
    main()
