#!/usr/bin/env python3
"""Exact finite tests for the conjugation-fixed partition-transfer clique complex.
No third-party packages or downloaded data are required.
"""
from functools import lru_cache
from itertools import zip_longest

@lru_cache(None)
def partitions(n, cap):
    if n == 0:
        return ((),)
    out = []
    for first in range(min(n, cap), 0, -1):
        out.extend((first,) + rest for rest in partitions(n - first, first))
    return tuple(out)

def conjugate(p):
    return tuple(sum(a >= col for a in p) for col in range(1, p[0] + 1))

def transfer_neighbors(p):
    out = set()
    for donor in range(len(p)):
        for recipient in range(len(p) + 1):
            if donor == recipient:
                continue
            q = list(p) + [0]
            q[donor] -= 1
            q[recipient] += 1
            q = tuple(sorted((a for a in q if a > 0), reverse=True))
            if q != p:
                out.add(q)
    return out

def ferrers_distance(p, q):
    return sum(abs(a - b) for a, b in zip_longest(p, q, fillvalue=0))

def components(graph):
    remaining = set(graph)
    sizes = []
    while remaining:
        start = next(iter(remaining))
        front = [start]
        remaining.remove(start)
        size = 0
        while front:
            x = front.pop()
            size += 1
            for y in graph[x] & remaining:
                remaining.remove(y)
                front.append(y)
        sizes.append(size)
    return sorted(sizes)

def fixed_orbit_graph(n):
    ps = partitions(n, n)
    universe = set(ps)
    assert all(p == tuple(sorted(p, reverse=True)) and sum(p) == n for p in ps)
    assert len(universe) == len(ps)
    neighbor = {p: transfer_neighbors(p) for p in ps}
    # Independent exhaustive graph construction via Ferrers symmetric difference.
    direct = {p: set() for p in ps}
    for i, p in enumerate(ps):
        for q in ps[i+1:]:
            if ferrers_distance(p, q) == 2:
                direct[p].add(q)
                direct[q].add(p)
    assert all(neighbor[p] == direct[p] for p in ps)
    assert all(conjugate(q) in neighbor[conjugate(p)] for p in ps for q in neighbor[p])
    orbits = {tuple(sorted({p, conjugate(p)})) for p in ps}
    admissible = sorted(o for o in orbits if len(o) == 1 or o[1] in neighbor[o[0]])
    graph = {i: set() for i in range(len(admissible))}
    for i, a in enumerate(admissible):
        for j in range(i + 1, len(admissible)):
            b = admissible[j]
            if all(y in neighbor[x] for x in a for y in b):
                graph[i].add(j)
                graph[j].add(i)
    return len(ps), admissible, graph

def local_near_square_check(m):
    p = (m,) * (m-1) + (m-1,)
    A = (m+1,) + (m,) * (m-3) + (m-1, m-1)
    B = (m,) * (m-2) + (m-1, m-1, 1)
    C = (m+1,) + (m,) * (m-2) + (m-2,)
    D = (m,) * (m-1) + (m-2, 1)
    assert conjugate(p) == p
    assert transfer_neighbors(p) == {A, B, C, D}
    assert conjugate(A) == D and conjugate(B) == C
    assert ferrers_distance(A, D) == ferrers_distance(B, C) == 4
    assert all(conjugate(x) != x for x in (A, B, C, D))

if __name__ == '__main__':
    count = []
    for n in range(1, 25):
        pnum, orbits, graph = fixed_orbit_graph(n)
        sizes = components(graph)
        count.append(len(sizes))
        if n in (8, 15, 24):
            print(f'n={n}; partitions={pnum}; orbit vertices={len(orbits)}; components={sizes}')
        assert len(sizes) <= 2 if n < 24 else sizes == [1, 2, 29]
    assert count == [1,1,1,1,1,1,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,3]
    assert len(partitions(24,24)) == 1575
    pnum, vs, gg = fixed_orbit_graph(24)
    target = ((5, 5, 5, 5, 4),)
    assert target in vs and not gg[vs.index(target)]
    for m in range(3, 31):
        local_near_square_check(m)
    print('PASS: complete 1..24 orbit-graph component census, independent adjacency routes, and 28 finite local tests')
