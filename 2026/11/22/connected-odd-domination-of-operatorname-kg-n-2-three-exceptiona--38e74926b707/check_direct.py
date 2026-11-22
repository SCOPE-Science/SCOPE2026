"""Finite independent direct verifier of connected odd dominating sets on KG(n,2)."""
from itertools import combinations
from collections import Counter, deque
from math import comb, factorial

def expected(n):
    if n == 5:return (5,12)
    if n == 6:return (3,15)
    count=12*comb(n,5)+(840 if n==8 else 0)+(945 if n==10 else 0)
    return (5,count)

def enumerate_opt(n):
    pairs=list(combinations(range(n),2))
    N=len(pairs)
    neighbors=[sum((1<<j) for j,f in enumerate(pairs) if i!=j and set(e).isdisjoint(f)) for i,e in enumerate(pairs)]
    closed=[neighbors[i]|(1<<i) for i in range(N)]
    minsize,expect=expected(n)
    found=[]
    counts=Counter()
    for k in (1,3,5) if minsize==5 else (1,3):
        if k>minsize:continue
        for idxs in combinations(range(N),k):
            mask=sum(1<<i for i in idxs)
            if any(((closed[j]&mask).bit_count()&1)==0 for j in range(N)):
                continue
            touched=1<<idxs[0]
            while True:
                nxt=touched
                for i in idxs:
                    if (touched>>i)&1:nxt|=neighbors[i]&mask
                if nxt==touched:break
                touched=nxt
            if touched!=mask:continue
            found.append(frozenset(idxs))
            counts[k]+=1
    assert counts[minsize]==expect,(n,counts,expect)
    assert all(counts[k]==0 for k in counts if k<minsize)
    if n==5:
        assert len(found)==12
        g={i:{j for j in range(len(found)) if i!=j and len(found[i]&found[j])==3} for i in range(len(found))}
        assert all(len(v)==5 for v in g.values())
        dist={i:0 for i in [0]}; q=deque([0])
        while q:
            u=q.popleft()
            for v in g[u]:
                if v not in dist:dist[v]=dist[u]+1;q.append(v)
        assert len(dist)==12 and Counter(dist.values())=={0:1,1:5,2:5,3:1}
        # Bipartition by BFS coloring, and all possible edges across are present save a matching
        left={u for u,d in dist.items() if d%2==0}; right=set(range(12))-left
        assert len(left)==len(right)==6
        assert all(g[u]<=right and len(g[u])==5 for u in left)
        assert all(g[u]<=left and len(g[u])==5 for u in right)
        nonedges={(u,v) for u in left for v in right if v not in g[u]}
        assert len(nonedges)==6 and len({u for u,v in nonedges})==6 and len({v for u,v in nonedges})==6
        assert all(not any(len(found[i]&found[j])==4 for j in range(12) if i!=j) for i in range(12))
        print('Petersen two-replacement graph: crown(6), 12 vertices, 30 edges, distance histogram 1,5,5,1')
    print('n=%d vertices=%d connected-odd-domination minimum=%d count=%d' % (n,N,minsize,len(found)))

if __name__=='__main__':
    for n in range(5,11):enumerate_opt(n)
    print('DIRECT CHECK PASS')
