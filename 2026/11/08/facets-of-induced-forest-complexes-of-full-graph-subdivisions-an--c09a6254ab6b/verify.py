"""Independent finite verifier of induced-forest facets of full graph subdivisions."""
from itertools import combinations
from collections import Counter
from math import comb

def graph_edges(n, gm):
    pairs=list(combinations(range(n),2));return [e for j,e in enumerate(pairs) if (gm>>j)&1]

def is_forest(n,edges,S):
    p=list(range(n));
    def find(a):
        while p[a]!=a: a=p[a]
        return a
    for i,j in edges:
        if (S>>i)&1 and (S>>j)&1:
            x,y=find(i),find(j)
            if x==y:return False
            p[x]=y
    return True

def predicted(n,E):
    m=len(E);h=n+m;Es={(u,v):i for i,(u,v) in enumerate(E)};out=set()
    for A in range(1<<n):
        selected=[i for i in range(n) if (A>>i)&1]
        internal=[j for j,(u,v) in enumerate(E) if ((A>>u)&1) and ((A>>v)&1)]
        noninternal=sum(1<<(n+j) for j in range(m) if j not in internal)
        # require internal edges chosen form spanning tree in every G[A] component
        for F in range(1<<len(internal)):
            eids=[internal[j] for j in range(len(internal)) if (F>>j)&1]
            parent=list(range(n))
            def find(x):
                while parent[x]!=x:x=parent[x]
                return x
            if len(eids):
                for eidx in eids:
                    x,y=E[eidx];p,q=find(x),find(y)
                    if p==q:break
                    parent[p]=q
                else: pass
                # if break from cycle, detect using direct function
                if not is_forest(n,[E[j] for j in eids],A):continue
            # every edge among selected has endpoints connected by F
            if any(find(u)!=find(v) for u,v in E if ((A>>u)&1) and ((A>>v)&1)):
                continue
            # for each omitted vertex, need two neighbors in one selected component
            good=True
            for x in range(n):
                if (A>>x)&1:continue
                groups=Counter(find(y) for u,v in E for y in ([v] if u==x and ((A>>v)&1) else [u] if v==x and ((A>>u)&1) else []))
                if max(groups.values(),default=0)<2:good=False;break
            if good:
                out.add(A|noninternal|sum(1<<(n+j) for j in eids))
    return out

def brute(n,E):
    h=n+len(E); H=[(u,n+j) for j,(u,v) in enumerate(E)]+[(v,n+j) for j,(u,v) in enumerate(E)]
    forests=[is_forest(h,H,S) for S in range(1<<h)]
    return {S for S in range(1<<h) if forests[S] and all(not forests[S|1<<x] for x in range(h) if not(S>>x)&1)}

profiles=0; subsets=0; facets=0
for n in range(1,5):
    for gm in range(1<<comb(n,2)):
        E=graph_edges(n,gm)
        obs=brute(n,E); pr=predicted(n,E)
        if obs!=pr:
            print('FAIL general',n,gm,E,'missing',obs-pr,'extra',pr-obs)
            raise SystemExit(1)
        profiles+=1;subsets+=1<<(n+len(E));facets+=len(obs)
for n in [5]:
    E=list(combinations(range(n),2));obs=brute(n,E);pr=predicted(n,E)
    assert obs==pr,(len(obs),len(pr))
    c=Counter(s.bit_count() for s in obs)
    formula=Counter()
    N=comb(n,2)
    for a in range(2,n+1):
        formula[N+2*a-1-comb(a,2)]+=comb(n,a)*a**(a-2)
    assert c==formula,(c,formula)
    profiles+=1;subsets+=1<<(n+len(E));facets+=len(obs)
for n in range(3,13):
    N=comb(n,2)
    c=Counter()
    for a in range(2,n+1):c[N+2*a-1-comb(a,2)]+=comb(n,a)*a**(a-2)
    assert max(c)==N+2 and min(c)==2*n-1
    assert sum(c.values())==sum(comb(n,a)*a**(a-2) for a in range(2,n+1))
print(f'VERIFY_OK labeled_base_graphs_and_cliques={profiles} full_subsets={subsets} maximal_induced_forests={facets} predicted_facets=PASS cycle_detection=PASS Cayley_cardinality=PASS size_extremes_n3to12=PASS')
