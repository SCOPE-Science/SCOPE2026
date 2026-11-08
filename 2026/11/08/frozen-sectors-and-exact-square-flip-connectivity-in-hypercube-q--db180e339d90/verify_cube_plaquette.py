"""Reproducible exhaustive checks of square-flip dimer sectors on binary cubes.
Only Python standard library is needed. The infinite-dimensional lower bound
is established by the separate constructive proof in RESULT.md.
"""
from collections import Counter, deque
from itertools import combinations

EXPECTED = {2:(2,0),3:(9,0),4:(272,8),5:(589185,120)}

def faces(d):
    N=1<<d
    return [(u,u^(1<<a),u^(1<<b),u^(1<<a)^(1<<b))
       for a in range(d) for b in range(a+1,d)
       for u in range(N) if not (u&(1<<a) or u&(1<<b))]

def canonical(d, keep=False):
    N=1<<d; partner=[-1]*N; F=faces(d)
    matchings=[]; degrees=Counter(); frozen=[]; total=0
    def rec(mask):
        nonlocal total
        if mask==0:
            total+=1
            deg=sum((partner[u]==v and partner[w]==z) or
                    (partner[u]==w and partner[v]==z) for u,v,w,z in F)
            degrees[deg]+=1
            if deg==0: frozen.append(tuple(partner))
            if keep: matchings.append(tuple(partner))
            return
        low=mask&-mask;u=low.bit_length()-1
        for a in range(d):
            v=u^(1<<a)
            if mask&(1<<v):
                partner[u]=v;partner[v]=u
                rec(mask^low^(1<<v))
                partner[u]=-1;partner[v]=-1
    rec((1<<N)-1)
    return total,degrees,frozen,matchings

def independent(d):
    """Second enumeration: match even vertices to odd neighbors, reverse ordering.
    Opposite-edge pair masks provide a separate flippability predicate.
    """
    N=1<<d
    even=[u for u in range(N) if u.bit_count()%2==0]
    odd=[u for u in range(N) if u.bit_count()%2==1]
    edge_id={}; edges=[]
    for u in even:
        for a in range(d):
            v=u^(1<<a);edge_id[u,v]=len(edges);edges.append((u,v))
    square_pairs=[]
    for u,v,w,z in faces(d):
        def eid(x,y):
            return edge_id[x,y] if x.bit_count()%2==0 else edge_id[y,x]
        square_pairs.append(((1<<eid(u,v))|(1<<eid(w,z)),
                             (1<<eid(u,w))|(1<<eid(v,z))))
    neighbors={u:[(1<<edge_id[u,v],v) for a in range(d) for v in [u^(1<<a)]] for u in even}
    total=0; frozen=0; degrees=Counter()
    def rec(k,used,bits):
        nonlocal total,frozen
        if k==len(even):
            total+=1
            deg=sum(1 for x,y in square_pairs if bits&x==x or bits&y==y)
            degrees[deg]+=1
            frozen+=(deg==0)
            return
        u=even[-k-1]
        for edge,v in reversed(neighbors[u]):
            if not (used&(1<<v)):
                rec(k+1,used|(1<<v),bits|edge)
    rec(0,0,0)
    return total,degrees,frozen

def transitions(d,matches):
    F=faces(d); idx={p:i for i,p in enumerate(matches)}
    adj=[set() for _ in matches]
    for i,p in enumerate(matches):
        for u,v,w,z in F:
            if p[u]==v and p[w]==z:
                t=list(p);t[u]=w;t[w]=u;t[v]=z;t[z]=v
            elif p[u]==w and p[v]==z:
                t=list(p);t[u]=v;t[v]=u;t[w]=z;t[z]=w
            else: continue
            j=idx[tuple(t)];adj[i].add(j);adj[j].add(i)
    visited=set();sizes=[]
    for u in range(len(matches)):
        if u in visited: continue
        stack=[u];visited.add(u);size=0
        while stack:
            v=stack.pop();size+=1
            for w in adj[v]:
                if w not in visited:visited.add(w);stack.append(w)
        sizes.append(size)
    return adj,Counter(sizes)

def run():
    stored={}
    for d in (2,3,4,5):
        a,da,frozen,matches=canonical(d,keep=(d==4))
        b,db,fb=independent(d)
        assert a==b==EXPECTED[d][0], (d,a,b)
        assert len(frozen)==fb==EXPECTED[d][1], (d,len(frozen),fb)
        assert da==db,(d,da,db)
        assert sum(da.values())==a
        print('Q',d,'matchings',a,'frozen',fb,'degree_histogram',sorted(da.items()))
        stored[d]=(frozen,matches)
        if d==4:
            adj,sizes=transitions(d,matches)
            assert sizes=={1:8,264:1},sizes
            assert sum(map(len,adj))//2==768
            assert all(len(adj[i])==sum((p[u]==v and p[w]==z) or (p[u]==w and p[v]==z) for u,v,w,z in faces(d)) for i,p in enumerate(matches))
            print('Q4 sector sizes',sorted(sizes.items()),'flip edges',sum(map(len,adj))//2)
    # Explicit four-way edge-disjoint frozen witness in Q4.
    witness = [
        (1,0,6,11,12,7,2,5,10,13,8,3,4,9,15,14),
        (2,9,0,7,5,4,14,3,12,1,11,10,8,15,6,13),
        (4,3,10,1,0,13,7,6,9,8,2,15,14,5,12,11),
        (8,5,3,2,6,1,4,15,0,11,14,9,13,12,10,7),
    ]
    assert all(p in stored[4][0] for p in witness)
    assert all(all(p[v] != q[v] for v in range(16))
               for i,p in enumerate(witness) for q in witness[i+1:])
    base=stored[4][0]
    def disjoint(p,q):return all(p[u]!=q[u] for u in range(16))
    adj={i: [j for j in range(8) if i!=j and disjoint(base[i],base[j])] for i in range(8)}
    assert sorted(map(len,adj.values()))==[3]*8
    assert all(set(adj[j]+[j])==set(adj[i]+[i]) for i in range(8) for j in adj[i])
    assert sum(len(x) for x in adj.values())//2==12
    print('Q4 frozen base disjointness: two disjoint K4', sorted(set(tuple(sorted([i]+adj[i])) for i in range(8))))
    print('VERIFY_OK')
if __name__=='__main__':run()
