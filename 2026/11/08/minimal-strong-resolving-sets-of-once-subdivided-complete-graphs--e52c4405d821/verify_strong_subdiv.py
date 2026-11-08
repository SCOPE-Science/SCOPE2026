"""Finite verification of minimal strong resolving sets for S(K_n).
Run with Python 3.9 or newer: python verify_strong_subdiv.py
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def construction(n):
    edges=list(combinations(range(n),2))
    verts=[('v',i) for i in range(n)]+[('e',i,j) for i,j in edges]
    adj={v:set() for v in verts}
    for i,j in edges:
        e=('e',i,j)
        for v in [('v',i),('v',j)]:
            adj[e].add(v)
            adj[v].add(e)
    return edges,verts,adj


def distances(verts,adj):
    all_d={}
    for root in verts:
        d={root:0};todo=deque([root])
        while todo:
            u=todo.popleft()
            for w in adj[u]:
                if w not in d:
                    d[w]=d[u]+1;todo.append(w)
        assert len(d)==len(verts)
        all_d[root]=d
    return all_d


def mmd(verts,adj,d):
    return {frozenset((u,v)) for u,v in combinations(verts,2)
            if all(d[w][v]<=d[u][v] for w in adj[u])
            and all(d[w][u]<=d[u][v] for w in adj[v])}


def min_strong_direct(verts,d):
    # Every candidate is checked against every vertex-pair witness, not via MMD.
    witness=[]
    for u,v in combinations(verts,2):
        witness.append(sum((1<<k) for k,w in enumerate(verts)
             if d[w][u]==d[w][v]+d[u][v]
             or d[w][v]==d[w][u]+d[u][v]))
    counts=Counter()
    for mask in range(1<<len(verts)):
        if any(not(mask&w) for w in witness):continue
        if all(any(not((mask^(1<<k))&w) for w in witness)
               for k in range(len(verts)) if mask>>k&1):
            counts[mask.bit_count()]+=1
    return counts


def maximal_intersecting(edges):
    # Exhaustively inspect all edge families for n <= 7, independent of the theorem.
    k=len(edges)
    conflict=[0]*k
    for i,e in enumerate(edges):
        conflict[i]=sum(1<<j for j,f in enumerate(edges)
                        if j!=i and not (set(e)&set(f)))
    counts=Counter()
    for mask in range(1<<k):
        if any(mask&conflict[i] for i in range(k) if mask>>i&1):continue
        if all(mask&conflict[i] for i in range(k) if not (mask>>i&1)):
            counts[k-mask.bit_count()]+=1
    return counts


def predicted(n):
    k=comb(n,2)
    out=Counter()
    out[k-n+1]+=n
    out[k-3]+=comb(n,3)
    return out


def main():
    total_graph_vertices=0
    subset_tests=0
    independent_family_tests=0
    total_sets=0
    for n in range(4,8):
        edges,V,A=construction(n);D=distances(V,A)
        observed=mmd(V,A,D)
        expected={frozenset((('e',i,j),('e',k,l)))
                 for (i,j),(k,l) in combinations(edges,2)
                 if len({i,j,k,l})==4}
        assert observed==expected,(n,'strong resolving graph mismatch')
        counts=maximal_intersecting(edges)
        assert counts==predicted(n),(n,counts,predicted(n))
        independent_family_tests+=1<<len(edges)
        total_sets+=sum(counts.values())
        if n<=5:
            direct=min_strong_direct(V,D)
            assert direct==predicted(n),(n,direct,predicted(n))
            subset_tests+=1<<len(V)
        total_graph_vertices+=len(V)
        print('n=',n,'vertices=',len(V),'maximal_sets=',dict(sorted(counts.items())))
    print('VERIFY_OK n=4..7 MMD=PASS maximal_intersecting=PASS',
          'family_masks=',independent_family_tests,
          'direct_strong_subsets=',subset_tests,
          'maximal_sets=',total_sets)

if __name__=='__main__':main()
