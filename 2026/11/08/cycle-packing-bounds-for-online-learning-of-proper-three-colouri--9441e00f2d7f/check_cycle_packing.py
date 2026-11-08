#!/usr/bin/env python3
"""Exact finite checks of 3-colouring online dimensions; standard library only."""
import itertools
from functools import lru_cache


def components(n, es):
    adj=[set() for _ in range(n)]
    for i,j in es: adj[i].add(j);adj[j].add(i)
    unseen=set(range(n)); out=[]
    while unseen:
        stack=[unseen.pop()]; nodes=set(stack)
        while stack:
            for w in adj[stack.pop()]:
                if w in unseen:unseen.remove(w);nodes.add(w);stack.append(w)
        out.append(nodes)
    return out

def cycle_packing(n, edges):
    es=set(tuple(sorted(e)) for e in edges)
    masks=set()
    for k in range(3,n+1):
        for v in itertools.combinations(range(n),k):
            a=v[0]
            for z in itertools.permutations(v[1:]):
                p=(a,)+z
                if p[1]>p[-1]: continue
                if all(tuple(sorted((p[i],p[(i+1)%k]))) in es for i in range(k)):
                    masks.add(sum(1<<i for i in v))
                    break
    @lru_cache(None)
    def best(remaining):
        return max([0]+[1+best(remaining&~cyc) for cyc in masks if (remaining&cyc)==cyc])
    return best((1<<n)-1)

def is_pseudoforest(n,edges):
    C=components(n,edges)
    return all(sum(u in comp and v in comp for u,v in edges)<=len(comp) for comp in C)

def unicyclic_count(n,edges):
    return sum(sum(u in c and v in c for u,v in edges)==len(c) for c in components(n,edges))

def ldim(n,edges):
    es=list(edges)
    colorings=[c for c in itertools.product(range(3),repeat=n) if all(c[u]!=c[v] for u,v in es)]
    m=len(colorings)
    if m<=1:return 0
    cuts=[sum((1<<i) for i,c in enumerate(colorings) if c[v]==a)
          for v in range(n) for a in range(3)]
    @lru_cache(None)
    def d(S):
        if S.bit_count()<=1:return 0
        ans=0
        for cut in cuts:
            pos=S&cut; neg=S&~cut
            if pos and neg:
                ans=max(ans,1+min(d(pos),d(neg)))
        return ans
    return d((1<<m)-1)

def run():
    seen=0; pseudo=0; maxn=5
    for n in range(maxn+1):
        edgelist=list(itertools.combinations(range(n),2))
        for edgeflags in range(1<<len(edgelist)):
            if n>=5 and edgeflags.bit_count()<n-1: continue
            edges=[e for i,e in enumerate(edgelist) if edgeflags>>i&1]
            nu=cycle_packing(n,edges)
            L=ldim(n,edges)
            assert L<=n-nu,(n,edges,nu,L)
            if is_pseudoforest(n,edges):
                pseudo+=1
                assert L==n-unicyclic_count(n,edges),(n,edges,L)
            assert (L==n)==(nu==0),(n,edges,L,nu)
            seen+=1
    print('EXHAUSTIVE_ALL_GRAPHS_PASS', seen, 'pseudoforests',pseudo)
    # Extended unicyclic and tree examples for lengths 6 through 9.
    extended=0
    for length in range(3,8):
        # cycle and cycle plus one pendant vertex
        edges=[(i,(i+1)%length) for i in range(length)]
        assert ldim(length,edges)==length-1
        extended+=1
        if length<=6:
            assert ldim(length+1,edges+[(0,length)])==length
            extended+=1
    for n in range(2,8):
        assert ldim(n,[(i,i+1) for i in range(n-1)])==n
        assert ldim(n,[(0,i) for i in range(1,n)])==n
        extended+=2
    # Two four-cycles joined at one vertex: n=7, two cycles, packing number 1.
    bowtie=[(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(5,6),(6,0)]
    assert cycle_packing(7,bowtie)==1
    assert ldim(7,bowtie)==6
    print('EXTENDED_PASS',extended,'BOWTIE_4_4_LDIM_6_PASS')

if __name__=='__main__':run()
