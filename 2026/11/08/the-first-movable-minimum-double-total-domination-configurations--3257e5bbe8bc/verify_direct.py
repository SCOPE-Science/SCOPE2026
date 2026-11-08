"""Complete direct verifier for minimum double-total domination of rook graphs.

No third-party dependencies. Run with Python 3.10+.
"""
from itertools import combinations
from collections import Counter, deque


def qualifies(rows, cols, mask, m):
    for r in range(len(rows)):
        for c in range(len(cols)):
            if rows[r]+cols[c]-2*((mask >> (r*m+c))&1) < 2:
                return False
    return True


def configurations(n, m, k):
    total=n*m
    result=[]
    for cells in combinations(range(total), k):
        rows=[0]*n; cols=[0]*m;mask=0
        for z in cells:
            mask |= 1<<z
            rows[z//m]+=1
            cols[z%m]+=1
        if qualifies(rows,cols,mask,m):
            result.append(mask)
    return result


def exchange_graph(sets, n, m):
    index={s:i for i,s in enumerate(sets)}
    adj=[set() for _ in sets]
    for i,s in enumerate(sets):
        for x in range(n*m):
            if not (s>>x)&1: continue
            deleted=s^(1<<x)
            for y in range(n*m):
                if (s>>y)&1:continue
                j=index.get(deleted|(1<<y))
                if j is not None:
                    adj[i].add(j)
                    assert x//m==y//m or x%m==y%m, ('jump is not a slide',n,m,x,y)
    assert all(i in adj[j] for j,v in enumerate(adj) for i in v)
    return adj


def components(adj):
    unseen=set(range(len(adj))); sizes=[];groups=[]
    while unseen:
        v=unseen.pop();queue=[v]
        for u in queue:
            for w in adj[u]:
                if w in unseen: unseen.remove(w);queue.append(w)
        sizes.append(len(queue));groups.append(queue)
    return sizes,groups


def ecc_diameter(adj, group):
    diam=0
    for source in group:
        distances={source:0};q=deque([source])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in distances:distances[v]=distances[u]+1;q.append(v)
        assert len(distances)==len(group)
        diam=max(diam,max(distances.values()))
    return diam


def verify_cutoff():
    for n in range(2,5):
        for m in range(n,25//n+1):
            if n*m>24:continue
            for k in range(1,n*m+1):
                opt=configurations(n,m,k)
                if opt:break
            adj=exchange_graph(opt,n,m)
            edges=sum(map(len,adj))//2
            if (n,m)==(4,6):
                assert k==8 and len(opt)==3189 and edges==2880
            else:
                assert edges==0,(n,m,k,edges)
            print('grid',n,m,'minimum',k,'optima',len(opt),'exchanges',edges)


def verify_main():
    n,m=4,6;sets=configurations(n,m,8)
    assert len(sets)==3189
    # Every configuration has its claimed degree-profile category.
    types=Counter()
    for s in sets:
        rows=tuple(sorted(sum((s>>(r*m+c))&1 for c in range(m)) for r in range(n)))
        cols=tuple(sorted(sum((s>>(r*m+c))&1 for r in range(n)) for c in range(m)))
        types[(rows,cols)]+=1
    expected={
        ((2,2,2,2),(0,0,0,0,4,4)):15,
        ((2,2,2,2),(0,0,0,2,2,4)):360,
        ((2,2,2,2),(0,0,0,2,3,3)):720,
        ((2,2,2,2),(0,0,2,2,2,2)):1350,
        ((1,1,3,3),(1,1,1,1,1,3)):720,
        ((1,1,1,5),(1,1,1,1,1,3)):24,
    }
    assert types==expected,(types,expected)
    adj=exchange_graph(sets,n,m)
    sizes,groups=components(adj)
    assert Counter(sizes)==Counter({1:2109,54:20})
    assert Counter(map(len,adj))==Counter({0:2109,4:360,6:720})
    assert sum(map(len,adj))//2==2880
    large=[g for g in groups if len(g)==54]
    assert all(sum(len(adj[u]) for u in g)//2==144 for g in large)
    assert all(ecc_diameter(adj,g)==5 for g in large)
    print('main optima',len(sets),'edges',2880,'components',len(groups))
    print('component sizes',sorted(Counter(sizes).items()))
    print('degrees',sorted(Counter(map(len,adj)).items()))
    print('every nontrivial component: 54 vertices, 144 edges, diameter 5')
    print('all exchanges obey token sliding')

if __name__=='__main__':
    verify_main()
    verify_cutoff()
    print('DIRECT CHECKS PASSED')
