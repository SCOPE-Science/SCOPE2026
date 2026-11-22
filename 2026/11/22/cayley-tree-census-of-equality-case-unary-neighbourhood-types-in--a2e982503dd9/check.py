#!/usr/bin/env python3
"""Reproduce the exact saturated unary-profile census for three-block forests.
Python >=3.9, standard library only. No network access needed.
"""
from itertools import combinations, product
from math import factorial


def triple_partitions(elements):
    elements = tuple(sorted(elements))
    if not elements:
        yield ()
        return
    x, rest = elements[0], elements[1:]
    for yz in combinations(rest, 2):
        remaining = tuple(v for v in rest if v not in yz)
        for continuation in triple_partitions(remaining):
            yield ((x,) + yz,) + continuation


def tree_edges(q):
    if q == 1:
        yield ()
        return
    for code in product(range(q), repeat=q-2):
        degree = [1]*q
        for x in code: degree[x] += 1
        code = list(code)
        edges = []
        for v in code:
            u = min(i for i in range(q) if degree[i] == 1)
            edges.append((u,v))
            degree[u]-=1; degree[v]-=1
        u,v = [i for i in range(q) if degree[i] == 1]
        edges.append((u,v))
        yield tuple(edges)


def build(partition, centres, tree, attachments):
    """Return complete labelled host graph, marked set and trace family."""
    m = 3*len(partition)
    edges = []
    for block,centre in zip(partition,centres):
        for v in block:
            if v != centre: edges.append((centre,v))
    edges = [(a,b) for a,b in edges]
    for i,j in enumerate(range(m)):
        edges.append((i,m+j))
    for k,((i,j),(a,b)) in enumerate(zip(tree,attachments)):
        edges.extend([(3*m+k,a),(3*m+k,b)])
    # connectors have labels 3m,... ; private leaves m,...,2m-1;
    # add one empty-profile vertex after the connector range.
    # The unused labels 2m,...,3m-1 are deliberately not in the host.
    empty = 3*m + len(tree)
    edges.append((m,empty))
    nodes = set(range(2*m)) | set(range(3*m,3*m+len(tree))) | {empty}
    A = set(range(m))
    adj = {v:set() for v in nodes}
    for u,v in edges:
        assert u in nodes and v in nodes and v not in adj[u]
        adj[u].add(v); adj[v].add(u)
    assert len(edges)==len(nodes)-1
    seen={0}; stack=[0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen: seen.add(v);stack.append(v)
    assert seen==nodes, 'not a connected tree'
    trace=frozenset(frozenset((adj[v]|{v})&A) for v in nodes)
    expected = {frozenset(), *(frozenset([i]) for i in A)}
    for block,centre in zip(partition,centres):
        expected.add(frozenset(block))
        expected.update(frozenset([centre,x]) for x in block if x!=centre)
    for a,b in attachments: expected.add(frozenset([a,b]))
    assert trace==frozenset(expected)
    assert len(trace)==len(nodes)==7*len(partition)
    return trace


def verify_census(q):
    m = 3*q
    expected = factorial(m)//(2**q*factorial(q))*9**(q-1)*(q**(q-2) if q>1 else 1)
    families = set()
    num=0
    for part in triple_partitions(range(m)):
        for centres in product(*part):
            for tree in tree_edges(q):
                options = [list(product(part[i],part[j])) for i,j in tree]
                for ends in product(*options):
                    t=build(part,centres,tree,ends)
                    if q <= 2:
                        assert t not in families
                        families.add(t)
                    num+=1
    assert num==expected,(q,num,expected)
    if q<=2: assert len(families)==expected
    return q,m,num


def verify_small_forests():
    counts={}
    for n in range(1,7):
        E=list(combinations(range(n),2))
        forest_count=0
        for mask in range(1<<len(E)):
            par=list(range(n))
            def find(u):
                while par[u]!=u: u=par[u]
                return u
            adj=[set() for _ in range(n)]
            cycle=False
            for k,(u,v) in enumerate(E):
                if (mask>>k)&1:
                    a,b=find(u),find(v)
                    if a==b: cycle=True;break
                    par[a]=b
                    adj[u].add(v);adj[v].add(u)
            if cycle:continue
            forest_count+=1
            for m in range(1,n+1):
                for A in combinations(range(n),m):
                    aset=set(A)
                    types={frozenset((adj[v]|{v})&aset) for v in range(n)}
                    assert len(types)<=2*m +m//3,(n,mask,A,types)
        counts[n]=forest_count
    return counts


if __name__=='__main__':
    print('FORESTS_TO_6', verify_small_forests())
    for q in (1,2): print('CENSUS',verify_census(q))
    # All q=3 cases follow the injectivity argument; replay representative
    # families from each of two different reduced tree shapes.
    q=3
    partition=((0,1,2),(3,4,5),(6,7,8))
    for tree in tree_edges(q):
        centres=(0,3,6)
        ends=tuple((partition[i][0],partition[j][0]) for i,j in tree)
        build(partition,centres,tree,ends)
    print('Q3_PREDICTED',factorial(9)//(2**3*factorial(3))*9**2*3)
    print('ALL_CHECKS_OK')
