"""Independent triple-packing census and neighborhood generation on labelled triples."""
from itertools import combinations
from collections import Counter
from math import factorial

def states(n):
    k=n//3
    def rec(free,blocks):
        if len(blocks)==k:
            yield tuple(sorted(blocks));return
        anchor=free[0]
        for pair in combinations(free[1:],2):
            triple=(anchor,)+pair
            remainder=tuple(x for x in free if x not in triple)
            for center in triple:
                yield from rec(remainder, blocks+[(triple,center)])
        # This branch allows unused labels, but only when enough capacity remains.
        if len(free)>3*(k-len(blocks)):
            yield from rec(free[1:],blocks)
    yield from rec(tuple(range(n)),[])

def moves(n,s,sliding):
    used=set(x for triple,c in s for x in triple)
    spare=set(range(n))-used
    for idx,(triple,center) in enumerate(s):
        old_edges={frozenset((center,x)) for x in triple if x!=center}
        pool=tuple(sorted(set(triple)|spare))
        for t in combinations(pool,3):
            for c in t:
                if t==triple and c==center:continue
                if sliding:
                    new_edges={frozenset((c,x)) for x in t if x!=c}
                    if not old_edges.intersection(new_edges):continue
                a=list(s);a[idx]=(t,c)
                yield tuple(sorted(a))

def check(n):
    k=n//3;r=n%3
    ss=list(states(n)); S=set(ss)
    expected=factorial(n)//(factorial(r)*2**k*factorial(k))
    assert len(ss)==len(S)==expected,(n,len(ss),len(S),expected)
    comp_data=[]
    for sliding,d in [(True,{0:2,1:6,2:10}[r]),(False,{0:2,1:11,2:29}[r])]:
        G={s:set(moves(n,s,sliding)) for s in ss}
        assert all(G[s]<=S for s in ss),n
        assert all(len(G[s])==k*d for s in ss),(n,sliding,Counter(map(len,G.values())))
        assert all(s in G[t] for s in ss for t in G[s]),(n,sliding)
        seen=set(); comps=[]
        for s in ss:
            if s in seen:continue
            seen.add(s);q=[s]
            for t in q:
                for u in G[t]:
                    if u not in seen:seen.add(u);q.append(u)
            comps.append(len(q))
        if r==0:
            expected_comps=Counter({3**k:factorial(n)//(6**k*factorial(k))})
        else: expected_comps=Counter({len(ss):1})
        assert Counter(comps)==expected_comps,(n,sliding,Counter(comps),expected_comps)
        comp_data.append((sliding,k*d,expected_comps))
    print('PASS abstract',n,'optima',len(ss),'tests',comp_data,flush=True)

for n in range(3,10):check(n)
