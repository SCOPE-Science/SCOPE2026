"""Finite independent checks for a maximal-line-graph-clique incidence theorem."""
from itertools import combinations
from functools import lru_cache
from math import comb

def max_intersecting_families(n, edges):
    # Exhaustively enumerate all subsets of edges for small input graphs.
    m=len(edges)
    out=[]
    for mask in range(1,1<<m):
        support=[i for i in range(m) if mask>>i&1]
        if any(not (set(edges[i])&set(edges[j])) for i,j in combinations(support,2)):
            continue
        if any(all(set(edges[j])&set(edges[i]) for i in support) for j in range(m) if not(mask>>j&1)):
            continue
        out.append(mask)
    return out

def vcdim_and_counts(m, concepts):
    counts=[1]
    d=0
    for k in range(1,m+1):
        c=0
        for S in combinations(range(m),k):
            seen=set()
            for H in concepts:
                pat=sum(((H>>i)&1)<<j for j,i in enumerate(S))
                seen.add(pat)
            c+=len(seen)==1<<k
        if not c: break
        counts.append(c);d=k
    return d,counts

def ldim(m, concepts):
    # state is a bitset of indices of distinct maximal cliques.
    masks=[]
    for i in range(m):
        masks.append(sum(((h>>i)&1)<<j for j,h in enumerate(concepts)))
    @lru_cache(None)
    def rank(state):
        v=0
        for q in masks:
            a=state&q; b=state&~q
            if a and b:
                v=max(v,1+min(rank(a),rank(b)))
        return v
    return rank((1<<len(concepts))-1)

def check_kn(n):
    edges=list(combinations(range(n),2))
    cliques=max_intersecting_families(n,edges)
    vc,co=vcdim_and_counts(len(edges),cliques)
    li=ldim(len(edges),cliques)
    assert vc==li==3, (n,vc,li)
    assert co==[1,comb(n,2),3*comb(n,3),comb(n,3)+n*comb(n-1,3)],(n,co)
    assert len(cliques)==n+comb(n,3)
    print(f'K_{n}: {len(cliques)} maximal cliques, VC={vc}, Ldim={li}, polynomial={co}')

if __name__=='__main__':
    for n in range(4,7):check_kn(n)
    # All graphs on at most 5 vertices, independently enumerating all maximal intersecting edge families.
    num=0
    for n in range(2,6):
        all_edges=list(combinations(range(n),2))
        for g in range(1,1<<len(all_edges)):
            edges=[e for i,e in enumerate(all_edges) if g>>i&1]
            cliques=max_intersecting_families(n,edges)
            vc,_=vcdim_and_counts(len(edges),cliques)
            li=ldim(len(edges),cliques)
            assert 0<=vc<=li<=3,(n,edges,cliques,vc,li)
            num+=1
    print(f'UNIVERSAL_SMALL_GRAPH_PASS graphs={num}')
