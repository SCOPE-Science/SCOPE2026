"""Self-contained verification for cubic fibers in two-pole graph path algebras.
Work over prime fields F_2 and F_3. Arrow-level computations directly implement
concatenation of three arrows; higher-path coordinates are free q^(3|E|)."""
from itertools import product, combinations
from collections import Counter


def independent_number(n, edges):
    return max(sum(mask >> i & 1 for i in range(n))
               for mask in range(1 << n)
               if all(not ((mask >> u & 1) and (mask >> v & 1)) for u,v in edges))


def matching_number(a,b,edges):
    result=0
    for size in range(len(edges)+1):
        for es in combinations(edges,size):
            if len(set(u for u,v in es))==size and len(set(v for u,v in es))==size:
                result=max(result,size)
    return result


def expected(q,a,b,edges,target):
    n=a+b; e=len(edges)
    forced={v for i,edge in enumerate(edges) if target[i] != 0 for v in edge}
    value=0
    for mask in range(1<<n):
        if any(not (mask>>v & 1) for v in forced):
            continue
        s=mask.bit_count()
        active_edges=sum((mask>>u & 1) and (mask>>v & 1) for u,v in edges)
        value+=(q-1)**s * q**(e-active_edges)
    return value


def direct(q,a,b,edges):
    n=a+b; e=len(edges)
    hist=Counter()
    for ac in product(range(q),repeat=n):
        for bs in product(range(q),repeat=e):
            target=tuple(ac[u]*bs[i]*ac[v]%q for i,(u,v) in enumerate(edges))
            hist[target]+=1
    return hist

cases=[
 (1,1,[(0,1)]),
 (1,2,[(0,1),(0,2)]),
 (2,2,[(0,2),(1,3)]),
 (2,2,[(0,2),(0,3),(1,2),(1,3)]),
 (2,3,[(0,2),(0,3),(1,3),(1,4)]),
 (3,3,[(0,3),(0,4),(1,4),(2,5)]),
]
for q in (2,3):
 for a,b,edges in cases:
    if q==3 and a+b+len(edges)>9: continue
    hist=direct(q,a,b,edges)
    assert len(hist)==q**len(edges), (q,a,b,edges,len(hist))
    for target in product(range(q),repeat=len(edges)):
        assert hist[target]==expected(q,a,b,edges,target), (q,a,b,edges,target)
    assert sum(hist.values())==q**(a+b+len(edges))
    nu=matching_number(a,b,edges)
    alpha=independent_number(a+b,edges)
    assert alpha+nu==a+b
    maxexpr=max(mask.bit_count()-sum((mask>>u&1)and(mask>>v&1) for u,v in edges) for mask in range(1<<(a+b)))
    assert maxexpr==alpha
    topcoeff=sum(mask.bit_count()-sum((mask>>u&1)and(mask>>v&1) for u,v in edges)==alpha for mask in range(1<<(a+b)))
    assert topcoeff>=1
    # Check direct cubic values of nonzero full-support target have exactly (q-1)^V roots.
    full=tuple([1]*len(edges))
    assert hist[full]==(q-1)**(a+b)
    print('PASS',q,a,b,len(edges),'targets',len(hist),'matching',nu,'leading_coefficient',topcoeff)
print('ALL PASS')

def full_path_replay(q,a,b,edges):
    """Independent complete path-basis multiplication, not merely monomial formula."""
    source=0; uids=list(range(1,a+1)); vids=list(range(a+1,a+b+1)); sink=a+b+1
    epaths=[(source,u) for u in uids]+[(uids[u],vids[v-a]) for u,v in edges]+[(v,sink) for v in vids]
    two=[(source,uids[u],vids[v-a]) for u,v in edges]+[(uids[u],vids[v-a],sink) for u,v in edges]
    three=[(source,uids[u],vids[v-a],sink) for u,v in edges]
    paths=epaths+two+three; d=len(paths)
    ix={p:i for i,p in enumerate(paths)}
    def multiply(f,g):
        z=[0]*d
        for i,p in enumerate(paths):
            if not f[i]: continue
            for j,r in enumerate(paths):
                if g[j] and p[-1]==r[0]:
                    z[ix[p+r[1:]]]=(z[ix[p+r[1:]]]+f[i]*g[j])%q
        return z
    for coords in product(range(q),repeat=d):
        sq=multiply(coords,coords)
        cu=multiply(sq,coords)
        assert all(v==0 for v in cu[:len(epaths)+len(two)])
        acoeff=coords[:a]; bcoeff=coords[a:a+len(edges)]; ccoeff=coords[a+len(edges):a+len(edges)+b]
        expected=tuple(acoeff[u]*bcoeff[i]*ccoeff[v-a]%q for i,(u,v) in enumerate(edges))
        assert tuple(cu[-len(edges):])==expected, (q,a,b,edges,coords,cu,expected)
    print('PASS full-path-multiplication',q,a,b,len(edges),'elements',q**d)

for q,a,b,ee in [(2,1,1,[(0,1)]),(3,1,1,[(0,1)]),(2,1,2,[(0,1),(0,2)])]:
    full_path_replay(q,a,b,ee)
print('ALL INDEPENDENT PATH CHECKS PASS')
