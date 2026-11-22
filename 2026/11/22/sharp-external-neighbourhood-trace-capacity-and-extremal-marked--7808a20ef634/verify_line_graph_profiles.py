#!/usr/bin/env python3
"""Finite tests for marked-edge external adjacency traces.

Only Python's standard library is used.  An input graph is represented by
its marked edges; placing it inside a sufficiently large complete graph
realizes every possible external trace.
"""
from itertools import combinations
from math import comb


def exact_profiles(edges):
    edges = [tuple(sorted(e)) for e in edges]
    assert len(edges) == len(set(edges)) and all(u != v for u,v in edges)
    m = len(edges)
    vertices = sorted({x for e in edges for x in e})
    st = {v: 0 for v in vertices}
    for i, (u,v) in enumerate(edges):
        st[u] |= 1 << i
        st[v] |= 1 << i
    # Two genuinely unmarked vertices also realize the empty trace.
    a, b = max(vertices) + 1, max(vertices) + 2
    st[a] = st[b] = 0
    marked = set(edges)
    return {st[u] | st[v] for u, v in combinations(st, 2)
            if tuple(sorted((u,v))) not in marked}


def bound(m):
    assert m >= 1
    if m % 2 == 0:
        k=m//2
        return 1 + comb(3*k, 2)
    k=(m-1)//2
    return 2 if k == 0 else 2 + comb(3*k+1, 2)


def component_types(edges):
    vertices={x for e in edges for x in e}
    adj={x:set() for x in vertices}
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    ans=[]
    while vertices:
        root=min(vertices)
        todo=[root]; vertices.remove(root); part={root}
        while todo:
            for y in adj[todo.pop()]:
                if y in vertices:
                    vertices.remove(y);part.add(y);todo.append(y)
        deg=sorted(len(adj[x]) for x in part)
        e=sum(deg)//2
        if e == 1: typ='K2'
        elif e == 2: typ='P3'
        elif e == 3 and deg == [1,1,1,3]: typ='K13'
        elif e == 3 and deg == [1,1,2,2]: typ='P4'
        else: typ='other'
        ans.append(typ)
    return sorted(ans)


def expected_equality(edges):
    m=len(edges); types=component_types(edges)
    if m==1: return types==['K2']
    if m==2: return types in (['P3'], ['K2','K2'])
    if m%2==0: return types==['P3']*(m//2)
    k=(m-1)//2
    return types in (sorted(['P3']*k+['K2']),
                     sorted(['P3']*(k-1)+['K13']))


def paths_of_two(k):
    out=[]
    for j in range(k):
        a=3*j
        out.extend([(a,a+1),(a+1,a+2)])
    return out


def test():
    checks=0
    for n in range(2,8):
        choices=list(combinations(range(n),2))
        for m in range(1,min(7,len(choices))+1):
            for edges in combinations(choices,m):
                fam=exact_profiles(edges)
                value=len(fam)
                target=bound(m)
                assert value <= target, (n,m,edges,value,target)
                assert (value==target)==expected_equality(edges), (n,m,edges,value,target,component_types(edges))
                checks+=1
    # Explicit equality patterns whose vertex counts exceed seven.
    for k in range(1,13):
        even=paths_of_two(k)
        assert len(exact_profiles(even))==bound(2*k)
        odd_a=even+[(3*k,3*k+1)]
        assert len(exact_profiles(odd_a))==bound(2*k+1)
        odd_b=paths_of_two(k-1)
        a=3*(k-1)
        odd_b.extend([(a,a+1),(a,a+2),(a,a+3)])
        assert len(exact_profiles(odd_b))==bound(2*k+1)
        checks+=3
    print('VERIFY_OK', checks)

if __name__ == '__main__':
    test()
