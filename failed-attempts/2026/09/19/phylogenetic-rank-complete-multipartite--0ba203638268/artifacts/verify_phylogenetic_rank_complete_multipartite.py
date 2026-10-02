#!/usr/bin/env python3
"""Verify the explicit complete-multipartite tree embedding and four-point lower certificates."""

from itertools import combinations

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for k in range(lo, n + 1):
        for rest in partitions(n-k, k):
            yield (k,) + rest

def graph_distance(u, v):
    if u == v:
        return 0.0
    return 2.0 if u[0] == v[0] else 1.0

def formula(parts):
    q = sum(a >= 2 for a in parts)
    s = sum(a == 1 for a in parts)
    return q + int(s >= 2)

def coordinate_metrics(parts):
    coords = []
    for i, a in enumerate(parts):
        if a >= 2:
            def di(u, v, i=i):
                if u == v:
                    return 0.0
                ui, vi = (u[0] == i), (v[0] == i)
                if ui and vi:
                    return 2.0
                if ui != vi:
                    return 1.0
                return 0.0
            coords.append(di)
    singleton_parts = {i for i, a in enumerate(parts) if a == 1}
    if len(singleton_parts) >= 2:
        def d0(u, v):
            if u == v:
                return 0.0
            us, vs = u[0] in singleton_parts, v[0] in singleton_parts
            if us and vs:
                return 1.0
            if us != vs:
                return 0.5
            return 0.0
        coords.append(d0)
    return coords

def four_point_ok(d, vertices):
    for a, b, c, e in combinations(vertices, 4):
        sums = sorted([
            d(a,b) + d(c,e),
            d(a,c) + d(b,e),
            d(a,e) + d(b,c),
        ])
        if abs(sums[2] - sums[1]) > 1e-12:
            return False
    return True

def check(parts):
    V = [(i,j) for i,a in enumerate(parts) for j in range(a)]
    coords = coordinate_metrics(parts)
    assert len(coords) == formula(parts)
    for d in coords:
        assert four_point_ok(d, V)
    for u, v in combinations(V, 2):
        gd = graph_distance(u, v)
        vals = [d(u,v) for d in coords]
        assert all(x <= gd + 1e-12 for x in vals)
        assert abs(max(vals) - gd) <= 1e-12
    # Four-point certificates behind the lower bound.
    nontrivial = [i for i,a in enumerate(parts) if a >= 2]
    for i, j in combinations(nontrivial, 2):
        a, b = (i,0), (i,1)
        c, e = (j,0), (j,1)
        assert graph_distance(a,b) + graph_distance(c,e) == 4
        assert graph_distance(a,c) + graph_distance(b,e) == 2
        assert graph_distance(a,e) + graph_distance(b,c) == 2
    singletons = [i for i,a in enumerate(parts) if a == 1]
    if len(singletons) >= 2:
        x, y = (singletons[0],0), (singletons[1],0)
        for i in nontrivial:
            a, b = (i,0), (i,1)
            assert graph_distance(a,b) + graph_distance(x,y) == 3
            assert graph_distance(a,x) + graph_distance(b,y) == 2
            assert graph_distance(a,y) + graph_distance(b,x) == 2

checked = 0
by_n = []
for n in range(2, 11):
    local = 0
    for p in partitions(n):
        if len(p) < 2:
            continue
        check(p)
        checked += 1
        local += 1
    by_n.append((n, local))

print("complete multipartite types checked:", checked)
print("by order:", by_n)
print("all explicit embeddings and four-point certificates passed")
