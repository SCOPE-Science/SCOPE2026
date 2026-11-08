"""Standalone exact checks for facet-budget bounds in stacked polytopes.

Checks complement, rather than replace, the induction proof in RESULT.md.
"""
from collections import deque
from random import Random


def stack(facets, adj, facet):
    d = len(facet)
    v = len(adj)
    adj = [set(a) for a in adj] + [set(facet)]
    for u in facet:
        adj[u].add(v)
    fs = set(facets)
    fs.remove(facet)
    for u in facet:
        fs.add(frozenset((set(facet) - {u}) | {v}))
    assert len(fs) == len(facets) + d - 1
    return fs, adj


def make(d, choices):
    facets = set(frozenset(set(range(d+1))-{u}) for u in range(d+1))
    adj = [set(range(d+1))-{u} for u in range(d+1)]
    for ch in choices:
        f = sorted(facets, key=lambda z:tuple(sorted(z)))[ch % len(facets)]
        facets, adj = stack(facets, adj, f)
    return facets, adj


def components(adj, mask):
    n = len(adj)
    alive = set(range(n))-set(mask)
    k = 0
    while alive:
        k += 1
        start = next(iter(alive))
        q = [start]
        alive.remove(start)
        while q:
            u = q.pop()
            for v in adj[u] & alive:
                alive.remove(v)
                q.append(v)
    return k


def all_cuts(d, adj):
    n=len(adj)
    count=0
    best=None
    for mask in range(1, 1<<n):
        S={j for j in range(n) if mask>>j & 1}
        c=components(adj,S)
        assert c <= (d-1)*len(S)-(d-2), (d,n,S,c)
        count+=1
        if c>1:
            assert (d-1)*len(S)>c
            ratio=(len(S),c)
            if best is None or ratio[0]*best[1]<best[0]*ratio[1]:
                best=ratio
    return count,best


def kleetope(d, core_choices):
    facets,adj=make(d,core_choices)
    m=len(adj)
    old_facets=sorted(facets,key=lambda z:tuple(sorted(z)))
    nfac=len(old_facets)
    for f in old_facets:
        assert f in facets
        facets,adj=stack(facets,adj,f)
    c=components(adj,set(range(m)))
    assert c==nfac
    assert nfac==(d-1)*m-(d-2)*(d+1)
    return m,nfac


def main():
    rng=Random(6057)
    count=0
    for d in (3,4,5,6):
        for k in range(0,7 if d==3 else 5):
            for rep in range(4):
                choices=[rng.randrange(1000) for _ in range(k)]
                f,adj=make(d,choices)
                c,best=all_cuts(d,adj)
                count+=c
        for k in (0,1,2,5,12,25,50,100):
            choices=[rng.randrange(10**9) for _ in range(k)]
            m,nfac=kleetope(d,choices)
            assert m/nfac>1/(d-1)
    print(f'PASS: {count} complete cut checks; 32 exact Kleetope formulas; no failures.')


if __name__=='__main__':
    main()
