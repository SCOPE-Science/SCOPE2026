#!/usr/bin/env python3
"""Exact finite checks for two-token double-star independence and matching."""
from itertools import combinations, product
from functools import lru_cache
from collections import deque


def token_graph(a, b):
    assert a >= 1 and b >= 1
    x, y = a+b, a+b+1
    U, V = set(range(a)), set(range(a, a+b))
    edges = {frozenset((x,y))}
    edges.update(frozenset((x,u)) for u in U)
    edges.update(frozenset((y,v)) for v in V)
    tokens = list(combinations(range(a+b+2),2))
    ids = {t:i for i,t in enumerate(tokens)}
    nbr=[set() for _ in tokens]
    for i,t in enumerate(tokens):
        for e in edges:
            if len(set(t).intersection(e)) != 1:
                continue
            p=(set(t)^e)
            j=ids[tuple(sorted(p))]
            nbr[i].add(j)
    assert all(i in nbr[j] for i in range(len(tokens)) for j in nbr[i])
    left=[i for i,t in enumerate(tokens) if sum(v in V or v == x for v in t) % 2 == 0]
    right=set(range(len(tokens)))-set(left)
    assert all(j in right for i in left for j in nbr[i])
    return tokens,nbr,left,right,U,V,x,y


def max_matching(nbr,left,right):
    match_R = {}
    def augment(i,seen):
        for j in nbr[i]:
            if j in seen: continue
            seen.add(j)
            if j not in match_R or augment(match_R[j],seen):
                match_R[j]=i
                return True
        return False
    return sum(augment(i,set()) for i in left)


def predicted_configs(a,b, tokens, U,V,x,y):
    universal={frozenset((u,v)) for u in U for v in V}|{frozenset((x,y))}
    def opts(leaves,center):
        t=len(leaves)
        uu={frozenset(p) for p in combinations(leaves,2)}
        z={frozenset((center,i)) for i in leaves}
        if t<=2: return [z]
        if t==3: return [uu,z]
        return [uu]
    return [{i for i,t in enumerate(tokens) if frozenset(t) in universal|p|q}
            for p,q in product(opts(U,x),opts(V,y))]


def max_independent_exact(nbr):
    masks=[sum(1 <<j for j in ns) for ns in nbr]
    @lru_cache(None)
    def solve(mask):
        if not mask: return 0,1
        v=max((i for i in range(len(nbr)) if mask>>i&1),key=lambda i:(masks[i]&mask).bit_count())
        no,cno=solve(mask & ~(1<<v))
        yes,cyes=solve(mask & ~(masks[v]|(1<<v)))
        yes+=1
        if no>yes:return no,cno
        if yes>no:return yes,cyes
        return yes,cno+cyes
    out=solve((1<<len(nbr))-1)
    return out,solve.cache_info().currsize


def run():
    match_checks=0; independent_checks=0; exact_checks=0
    for a in range(1,9):
        for b in range(1,9):
            ts,nbr,L,R,U,V,x,y=token_graph(a,b)
            observed=max_matching(nbr,L,R)
            want=2*(a+b)-(a<=2)-(b<=2)
            assert observed==want,(a,b,observed,want)
            match_checks+=1
            configurations=predicted_configs(a,b,ts,U,V,x,y)
            expected_count=2**((a==3)+(b==3))
            target=len(ts)-want
            assert len(configurations)==expected_count
            assert len({frozenset(c) for c in configurations})==expected_count
            for c in configurations:
                assert len(c)==target and all(j not in c for i in c for j in nbr[i]),(a,b)
                independent_checks+=1
            if a<=3 and b<=3:
                (mx,cnt),states=max_independent_exact(nbr)
                assert (mx,cnt)==(target,expected_count),(a,b,mx,cnt,target,expected_count)
                print('EXACT_MAXIMUM_SETS',a,b,'number',cnt,'states',states)
                exact_checks+=1
    print('MATCHING_COUNTS',match_checks,'PASS')
    print('CONSTRUCTED_MAXIMUM_INDEPENDENT_SETS',independent_checks,'PASS')
    print('EXACT_OPTIMIZER_ENUMERATIONS',exact_checks,'PASS')
    print('VERIFY_OK')
if __name__=='__main__': run()
