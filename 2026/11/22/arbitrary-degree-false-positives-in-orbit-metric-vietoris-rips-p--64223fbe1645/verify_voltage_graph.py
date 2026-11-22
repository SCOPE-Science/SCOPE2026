#!/usr/bin/env python3
"""Finite checks for a family of cyclic graph covers and their orbit flag complexes.
Standard-library only; the separate all-order proof is in RESULT.md.
"""
from collections import defaultdict, deque
from itertools import combinations


def cover(q, m):
    assert q >= 3 and m >= 2
    verts = [(a, i, s) for a in range(q) for i in range(2) for s in range(m)]
    edges = set()
    for a, b in combinations(range(q), 2):
        for i in range(2):
            for j in range(2):
                for s in range(m):
                    u, v = (a, i, s), (b, j, (s+1) % m)
                    edges.add(frozenset((u, v)))
    return verts, edges


def components(verts, edges):
    adj = {v: set() for v in verts}
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    unseen = set(verts)
    result = []
    while unseen:
        start = next(iter(unseen))
        seen = {start}
        todo = deque([start])
        while todo:
            for w in adj[todo.popleft()]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        unseen -= seen
        result.append(seen)
    return result


def run():
    cases = ((3, 2), (3, 3), (3, 5), (4, 2), (4, 4), (5, 3), (6, 2))
    for q, m in cases:
        vs, es = cover(q, m)
        adj = {v: set() for v in vs}
        for edge in es:
            u, v = tuple(edge)
            adj[u].add(v)
            adj[v].add(u)
        assert len(vs) == 2*q*m
        assert len(es) == 4*(q*(q-1)//2)*m
        assert len(components(vs, es)) == 1
        # Every potential 3-cycle, including at m=2, is absent.
        assert not any((w in adj[u] and w in adj[v]) for u in vs for v in adj[u] for w in adj[v])
        # Rotation acts freely and preserves edge incidence.
        for delta in range(m):
            action = lambda v: (v[0], v[1], (v[2]+delta)%m)
            assert all(frozenset((action(u), action(v))) in es for u, v in (tuple(e) for e in es))
            if delta: assert not any(action(v) == v for v in vs)
        orbit_edges = {frozenset(((u[0], u[1]), (v[0], v[1]))) for u, v in (tuple(e) for e in es)}
        assert len(orbit_edges) == 4*(q*(q-1)//2)
        assert all(x != y for x, y in (tuple(e) for e in orbit_edges))
        base = [(a, i) for a in range(q) for i in range(2)]
        assert len(components(base, orbit_edges)) == 1
        assert (len(orbit_edges) - len(base) + 1) == 2*q*(q-2)+1
        # The orbit metric's flag complex is a join of q copies of S^0:
        # k-dimensional face counts: C(q,k+1)*2^(k+1).
        face_counts = [sum(1 for S in combinations(base, k+1) if len({a for a, i in S}) == k+1) for k in range(q)]
        assert face_counts == [2**(k+1)*__import__('math').comb(q, k+1) for k in range(q)]
        assert sum((-1)**k*f for k, f in enumerate(face_counts)) == 1 + (-1)**(q-1)
        print('PASS q=%d m=%d coverV=%d coverE=%d baseH1=%d flagEuler=%d' %
              (q,m,len(vs),len(es),2*q*(q-2)+1,1+(-1)**(q-1)))
    print('PASS: all %d finite cases; infinite proof is separate.' % len(cases))


if __name__ == '__main__':
    run()
