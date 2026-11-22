#!/usr/bin/env python3
"""Independent exact checks of ternary adjacent-sum spectra (standard Python 3)."""
from itertools import product
from math import comb
from random import Random


def compositions(total, bins=5):
    if bins == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for tail in compositions(total-a, bins-1):
                yield (a,) + tail


def observed(word, cyclic):
    pairs = zip(word, word[1:] + ((word[0],) if cyclic else ()))
    hist = [0]*5
    for a,b in pairs:
        hist[a+b] += 1
    return tuple(hist)


def lin_possible(a):
    a0,a1,a2,a3,a4 = a
    return not ((a2 == a3 == 0 and a1 > 0 and a4 > 0) or
                (a2 == a1 == 0 and a3 > 0 and a0 > 0) or
                (a1 == a2 == a3 == 0 and a0 > 0 and a4 > 0))


def cyc_possible(a):
    a0,a1,a2,a3,a4 = a
    if a1%2 != a3%2:
        return False
    if a1 and a3:
        return not (a1%2 and a2 == 0)
    if a1:
        return a4 == 0 or a2 >= 2
    if a3:
        return a0 == 0 or a2 >= 2
    if a2:
        return a2%2 == 0 or (a0 == 0 and a4 == 0)
    return (a0 > 0) != (a4 > 0)


def lin_formula(m):
    assert m >= 1
    return comb(m+4,4)-m*m+1


def cyc_formula(n):
    assert n >= 1
    return (n**4+8*n**3-28*n**2+136*n+27*(n%2))//48


def euler_witness(hist,cyclic):
    """Build a distinct Euler walk witness, independently using a split search."""
    a0,a1,a2,a3,a4=hist
    edges0=[(0,0,a0),(0,1,a1),(1,2,a3),(2,2,a4)]
    for k in range(a2+1):
        edges = edges0 + [(0,2,k),(1,1,a2-k)]
        deg=[0,0,0]
        g=[set() for _ in range(3)]
        for u,v,c in edges:
            deg[u]+=c
            deg[v]+=c
            if c and u!=v:
                g[u].add(v);g[v].add(u)
        active=[v for v,d in enumerate(deg) if d]
        odd=[v for v,d in enumerate(deg) if d%2]
        if cyclic and odd:continue
        if not cyclic and len(odd) not in (0,2):continue
        if not active:continue
        seen={active[0]}; stack=[active[0]]
        while stack:
            for v in g[stack.pop()]-seen:
                seen.add(v);stack.append(v)
        if seen!=set(active):continue
        # Hierholzer's algorithm, each edge assigned a unique ID
        adj=[[] for _ in range(3)]
        for u,v,c in edges:
            for _ in range(c):
                e=sum(len(t) for t in adj)
                adj[u].append((v,e)); adj[v].append((u,e))
        start=odd[0] if odd else active[0]
        walk=[];stk=[start];used=set()
        while stk:
            v=stk[-1]
            while adj[v] and adj[v][-1][1] in used:
                adj[v].pop()
            if adj[v]:
                u,e=adj[v].pop();used.add(e);stk.append(u)
            else:
                walk.append(stk.pop())
        walk=walk[::-1]
        if len(walk)!=sum(hist)+1:
            raise AssertionError(('bad euler length',hist,walk))
        word=tuple(walk[:-1] if cyclic else walk)
        if observed(word,cyclic)!=tuple(hist):
            raise AssertionError(('bad euler witness',hist,word))
        return word
    return None


def run():
    exact_words=0
    for m in range(1,10):
        cyc={observed(w,True) for w in product(range(3),repeat=m)}
        lin={observed(w,False) for w in product(range(3),repeat=m+1)}
        cyc_pred={a for a in compositions(m) if cyc_possible(a)}
        lin_pred={a for a in compositions(m) if lin_possible(a)}
        assert cyc==cyc_pred,('cyclic mismatch',m,cyc^cyc_pred)
        assert lin==lin_pred,('linear mismatch',m,lin^lin_pred)
        assert len(cyc)==cyc_formula(m),(m,len(cyc),cyc_formula(m))
        assert len(lin)==lin_formula(m),(m,len(lin),lin_formula(m))
        exact_words += 3**m + 3**(m+1)
    # Independent enumeration of *all* histogram vectors to 50 read positions.
    histchecks=0
    for n in range(1,51):
        totalcyc=totallin=0
        for a in compositions(n):
            histchecks+=1
            totalcyc+=cyc_possible(a)
            totallin+=lin_possible(a)
        assert totalcyc==cyc_formula(n),(n,totalcyc)
        assert totallin==lin_formula(n),(n,totallin)
    # Constructive check of graph criteria including large, boundary-heavy cases.
    witnesses=0
    rng=Random(3216547)
    for n in range(1,14):
        for a in compositions(n):
            for cyclic,pred in ((True,cyc_possible),(False,lin_possible)):
                witness=euler_witness(a,cyclic)
                assert (witness is not None)==pred(a),(n,a,cyclic)
                witnesses+=witness is not None
    for _ in range(1000):
        n=rng.randint(15,500)
        cuts=sorted(rng.sample(range(n+4),4)); a=[];previous=-1
        for cut in cuts:
            a.append(cut-previous-1);previous=cut
        a.append(n+3-previous)
        assert len(a)==5 and sum(a)==n
        for cyclic,pred in ((True,cyc_possible),(False,lin_possible)):
            witness=euler_witness(a,cyclic)
            assert (witness is not None)==pred(a),(n,a,cyclic)
            witnesses+=witness is not None
    print(f'SPECTRUM_VERIFY_OK word_instances={exact_words} histogram_vectors={histchecks} Euler_witnesses={witnesses} lengths=1..50')


if __name__=='__main__':
    run()
