#!/usr/bin/env python3
"""Reproducible finite checks for McGee graph-metric Rips homotopy types.

Python 3 stdlib only. The mathematical deductions appear in RESULT.md.
"""
from collections import Counter, deque
from itertools import combinations

N = 24
LCF = (-12, 7, -7) * 8


def graph():
    a = [set() for _ in range(N)]
    def edge(i, j):
        assert i != j
        a[i].add(j)
        a[j].add(i)
    for v in range(N):
        edge(v, (v + 1) % N)
        edge(v, (v + LCF[v]) % N)
    assert all(len(a[v]) == 3 for v in range(N))
    assert sum(map(len, a)) // 2 == 36
    assert all(v in a[w] for v in range(N) for w in a[v])
    return a


def distances_bfs(a):
    d = []
    for root in range(N):
        row = [-1] * N
        row[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in a[u]:
                if row[v] < 0:
                    row[v] = row[u] + 1
                    q.append(v)
        assert all(x >= 0 for x in row)
        d.append(row)
    return d


def distances_fw(a):
    inf = N + 1
    d = [[0 if i == j else 1 if j in a[i] else inf
          for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def girth(a):
    # Shortest cycle by BFS and non-parent back edges in a simple graph.
    ans = N + 1
    for s in range(N):
        dist = {s: 0}
        parent = {s: -1}
        q = deque([s])
        while q:
            u = q.popleft()
            for v in a[u]:
                if v not in dist:
                    parent[v] = u
                    dist[v] = dist[u] + 1
                    q.append(v)
                elif parent[u] != v:
                    ans = min(ans, dist[u] + dist[v] + 1)
    return ans


def rips_faces(d, r):
    # Every clique is enumerated precisely once using strictly increasing labels.
    mask = [sum(1 << w for w in range(N) if w != v and d[v][w] <= r)
            for v in range(N)]
    out = set()
    def add(s, avail):
        while avail:
            b = avail & -avail
            avail ^= b
            i = b.bit_length() - 1
            q = s | b
            assert q not in out
            out.add(q)
            add(q, avail & mask[i])
    add(0, (1 << N) - 1)
    return out


def collapse_r2(faces, a):
    f = set(faces)
    collapsed = 0
    def elementary(simplex, freeface):
        nonlocal collapsed
        assert simplex in f and freeface in f
        assert simplex.bit_count() == freeface.bit_count() + 1
        assert freeface & simplex == freeface
        # Check no other strict superface at all: a free simplicial face.
        supers = [x for x in f if (x & freeface) == freeface]
        assert supers == [simplex, freeface] or set(supers) == {simplex,freeface}, (simplex, freeface, supers)
        f.remove(freeface)
        f.remove(simplex)
        collapsed += 1
    for v in range(N):
        nb = sorted(a[v])
        b = sum(1 << x for x in nb)
        elementary(b | (1 << v), b)
        for x, y in combinations(nb, 2):
            pair = (1 << x) | (1 << y)
            elementary(pair | (1 << v), pair)
    assert collapsed == 96
    graph_faces = {(1 << v) for v in range(N)}
    graph_faces |= {(1 << v) | (1 << w)
                    for v in range(N) for w in a[v] if v < w}
    assert f == graph_faces
    return collapsed


def components(dist4):
    unseen = set(range(N)); out = []
    while unseen:
        start = min(unseen)
        q = [start]; unseen.remove(start); component = []
        while q:
            v = q.pop()
            component.append(v)
            for w in dist4[v]:
                if w in unseen:
                    unseen.remove(w)
                    q.append(w)
        out.append(sorted(component))
    return sorted(out)


def main():
    a = graph()
    d = distances_bfs(a)
    assert d == distances_fw(a)
    assert girth(a) == 7
    assert Counter(x for row in d for x in row) == {0: 24, 1: 72, 2: 144, 3: 288, 4: 48}
    assert all(Counter(row) == {0: 1, 1: 3, 2: 6, 3: 12, 4: 2} for row in d)
    print('GRAPH 24 vertices, 36 edges, girth=7, diameter=4; BFS=Floyd')
    f1 = rips_faces(d, 1)
    f2 = rips_faces(d, 2)
    assert len(f1) == 60 and len(f2) == 252
    c2 = collapse_r2(f2, a)
    print('R2 252 nonempty faces, 96 elementary collapses onto the original graph')
    f3 = rips_faces(d, 3)
    fv3 = tuple(sum(x.bit_count() == k for x in f3) for k in range(1, 13))
    # Coefficients of (1+4t+2t^2)^6, omitting constant term.
    poly = [1]
    for _ in range(6):
        new = [0] * (len(poly) + 2)
        for i, x in enumerate(poly):
            for j, y in enumerate((1, 4, 2)):
                new[i+j] += x*y
        poly = new
    assert fv3 == tuple(poly[1:])
    assert len(f3) == 117648
    dist4 = [{j for j in range(N) if d[i][j] == 4} for i in range(N)]
    assert all(len(x) == 2 for x in dist4)
    cp = components(dist4)
    expected = [[0, 6, 12, 18], [1, 5, 13, 17], [2, 10, 14, 22],
                [3, 9, 15, 21], [4, 8, 16, 20], [7, 11, 19, 23]]
    assert cp == expected
    assert all(sum(w in dist4[v] for w in comp) == 2
               for comp in cp for v in comp)
    # Each 4-vertex component is connected 2-regular, hence C4.
    # An independent subset of a disjoint union is the union of independent subsets.
    # At radius 3, missing pairs are exactly distance-4 edges.
    print('R3 117648 faces; distance-four complement exactly six disjoint C4')
    print('DISTANCE_FOUR_COMPONENTS', cp)
    print('R3_FACE_VECTOR', fv3)
    print('R3 = join of six Ind(C4) = join of six S0 = S5')
    assert max(max(row) for row in d) == 4
    print('R4 full simplex (contractible)')
    print('BARCODE reduced H0 23x[0,1), H1 13x[1,3), H5 1x[3,4)')
    print('MCGEE_RIPS_COMPLETE_TOPOLOGY_PASS')


if __name__ == '__main__':
    main()
