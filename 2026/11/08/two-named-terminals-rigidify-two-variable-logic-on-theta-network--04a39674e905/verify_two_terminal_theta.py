"""Finite corroboration for two-terminal theta networks, no third-party dependencies.

Not an exhaustive proof for unbounded path lengths or unrestricted logic.
"""
from collections import deque, Counter, defaultdict
from itertools import combinations_with_replacement, product


def theta(lengths):
    assert len(lengths) == 3 and min(lengths) >= 2
    G = [set(), set()]
    branches = []
    for L in lengths:
        path = [0]
        for _ in range(L - 1):
            path.append(len(G)); G.append(set())
        path.append(1)
        for u,v in zip(path,path[1:]):
            G[u].add(v); G[v].add(u)
        branches.append(path)
    return G, branches


def distances(G, source):
    d = [-1] * len(G); d[source] = 0
    q = deque([source])
    while q:
        v = q.popleft()
        for w in G[v]:
            if d[w] == -1:
                d[w] = d[v]+1; q.append(w)
    assert -1 not in d
    return d


def center_hist(G):
    ds,dt=distances(G,0),distances(G,1)
    maxL = max(ds)+max(dt)+2
    return {L:sum(ds[v]==L//2 and dt[v]==(L+1)//2 for v in range(len(G)))
            for L in range(2,maxL+1)}


def two_pebble_classes(G,H,constants=False):
    # Full fixed-point FO^2 refinement on ordered partial assignments.
    graphs=[G,H]; colors=[]; states=[]; indexes=[]
    for g in graphs:
        n=len(g); ts=list(product(range(-1,n),repeat=2))
        states.append(ts);indexes.append({t:i for i,t in enumerate(ts)})
    atoms={}
    for g,ts in zip(graphs,states):
        c=[]
        for x,y in ts:
            signature=(x>=0,y>=0,x==y if x>=0 and y>=0 else None,
                y in g[x] if x>=0 and y>=0 else None)
            if constants:
                signature+=(x==0 if x>=0 else None,x==1 if x>=0 else None,
                    y==0 if y>=0 else None,y==1 if y>=0 else None,
                    x in g[0] if x>=0 else None,x in g[1] if x>=0 else None,
                    y in g[0] if y>=0 else None,y in g[1] if y>=0 else None,
                    1 in g[0])
            if signature not in atoms: atoms[signature]=len(atoms)
            c.append(atoms[signature])
        colors.append(c)
    for _ in range(120):
        ids={}; nxt=[]
        for g,ts,idx,c in zip(graphs,states,indexes,colors):
            nc=[]
            for x,y in ts:
                a=c[idx[(x,y)]]
                sig=(a, frozenset(c[idx[(z,y)]] for z in range(len(g))),
                       frozenset(c[idx[(x,z)]] for z in range(len(g))))
                if sig not in ids:ids[sig]=len(ids)
                nc.append(ids[sig])
            nxt.append(nc)
        if nxt==colors:break
        colors=nxt
    else:
        raise AssertionError('Refinement did not stabilize')
    return colors[0][indexes[0][(-1,-1)]]==colors[1][indexes[1][(-1,-1)]]


def partition_le3(n):
    return sum(1 for a in range(n+1) for b in range(a,n+1)
               if b<=n-a-b)


def main():
    triples=list(combinations_with_replacement(range(2,9),3))
    witnesses=0; local=0
    for t in triples:
        G,paths=theta(t)
        h=center_hist(G)
        for L,count in h.items():
            assert count==t.count(L),(t,L,count,t.count(L))
            witnesses +=1
        assert all(len(G[v])>=1 and len(G[v])<len(G)-1 for v in range(len(G)))
        local+=len(G)
        seen=[L for L,m in h.items() if m>=1]
        doubled=[L for L,m in h.items() if m>=2]
        # Reconstruct a length multiset from only two-variable properties.
        rec=[]
        for L in seen:
            rec.extend([L]* (2 if L in doubled else 1))
        if len(rec)<3:
            assert len(rec)==2 and len(seen)==1
            rec.append(seen[0])
        assert tuple(sorted(rec))==t,(t,rec)
    for n in range(0,22):
        exact=partition_le3(n)
        formula=(n*n+6*n+12)//12
        assert exact==formula,(n,exact,formula)
    tests=[(2,2,2),(2,2,3),(2,2,4),(2,3,3),(2,3,4),
           (3,3,3),(3,3,4),(3,4,4),(4,4,4),(4,4,5),
           (5,5,5),(5,5,6)]
    games=0
    for i,a in enumerate(tests):
        for j,b in enumerate(tests):
            if j<i:continue
            G,_=theta(a);H,_=theta(b)
            assert two_pebble_classes(G,H,False)
            assert two_pebble_classes(G,H,True)==(a==b), (a,b)
            games+=2
    print('PASS theta triples tested:',len(triples))
    print('PASS middle-distance multiplicity witnesses:',witnesses)
    print('PASS local nonneighbor/neighbor cases:',local)
    print('PASS exact two-variable reconstruction:',len(triples))
    print('PASS independent partition enumeration:',22)
    print('PASS independent two-pebble refinement comparisons:',games)

if __name__=='__main__':main()
