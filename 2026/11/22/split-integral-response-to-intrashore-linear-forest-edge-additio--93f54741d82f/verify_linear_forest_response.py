#!/usr/bin/env python3
"""Standalone finite checks for induced-linear-forest response in graph joins.

The universal statement rests on a topological attaching-map proof; these
bounded tests independently enumerate induced subgraphs, boundary matrices,
and integral null-homotopy discs for the missing triangular faces.
"""
from collections import deque
from itertools import combinations
from math import comb


def linear_forest(a, edges):
    edges = {tuple(sorted(e)) for e in edges}
    degree = [0] * a
    parent = list(range(a))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        if max(degree) > 2 or root(u) == root(v):
            return False
        parent[root(u)] = root(v)
    return True


def graph_faces(a, b, edges):
    """Enumerate the definition, without using the predicted face formula."""
    n = a + b
    graph_edges = set(edges) | {(i, j) for i in range(a) for j in range(a, n)}
    faces = [[] for _ in range(n + 1)]
    for k in range(n + 1):
        for s in combinations(range(n), k):
            S = set(s)
            degree = {i: 0 for i in s}
            parent = {i: i for i in s}
            def root(i):
                while parent[i] != i:
                    i = parent[i]
                return i
            valid = True
            for u, v in graph_edges:
                if u not in S or v not in S:
                    continue
                degree[u] += 1
                degree[v] += 1
                if degree[u] > 2 or degree[v] > 2:
                    valid = False
                    break
                x, y = root(u), root(v)
                if x == y:
                    valid = False
                    break
                parent[x] = y
            if valid:
                faces[k].append(s)
    return faces


def predicted_faces(a, b, edges):
    out = [[] for _ in range(a + b + 1)]
    for k in range(a + b + 1):
        for s in combinations(range(a + b), k):
            aa = [x for x in s if x < a]
            bb = [x for x in s if x >= a]
            valid = (not aa or not bb or
                     (len(aa) == 1 and len(bb) <= 2) or
                     (len(bb) == 1 and len(aa) == 2 and tuple(aa) not in edges))
            if valid:
                out[k].append(s)
    return out


def gf_rank(columns, p):
    pivots = {}
    for column in columns:
        v = dict(column)
        while v:
            k = max(v)
            if v[k] % p == 0:
                del v[k]
                continue
            if k not in pivots:
                inv = pow(v[k], -1, p)
                pivots[k] = {i: (x * inv) % p for i, x in v.items() if (x * inv) % p}
                break
            multiplier = v[k] % p
            for i, x in pivots[k].items():
                y = (v.get(i, 0) - multiplier * x) % p
                if y:
                    v[i] = y
                elif i in v:
                    del v[i]
    return len(pivots)


def ranks(faces, p):
    boundary_rank = [0]
    for k in range(1, len(faces)):
        index = {face: i for i, face in enumerate(faces[k - 1])}
        columns = []
        for s in faces[k]:
            columns.append({index[s[:j] + s[j+1:]]: (-1)**j for j in range(k)})
        boundary_rank.append(gf_rank(columns, p))
    boundary_rank.append(0)
    return {k-1: len(faces[k])-boundary_rank[k]-boundary_rank[k+1]
            for k in range(len(faces))
            if len(faces[k])-boundary_rank[k]-boundary_rank[k+1] != 0}


def oriented_boundary(triangle):
    return [(triangle[:j] + triangle[j+1:], (-1)**j) for j in range(3)]


def canonical_edge(x, y):
    return ((x, y), 1) if x < y else ((y, x), -1)


def boundary_of_chain(chain):
    out = {}
    for triangle, coefficient in chain:
        for edge, sign in oriented_boundary(triangle):
            e, orientation = canonical_edge(*edge)
            out[e] = out.get(e, 0) + coefficient * sign * orientation
    return {x: y for x, y in out.items() if y}


def complement_path(a, edges, source, target):
    pending = deque([source])
    previous = {source: None}
    while pending:
        u = pending.popleft()
        for v in range(a):
            if u == v or tuple(sorted((u,v))) in edges or v in previous:
                continue
            previous[v] = u
            pending.append(v)
    if target not in previous:
        raise AssertionError('complement disconnected')
    path = []
    x = target
    while x is not None:
        path.append(x)
        x = previous[x]
    return list(reversed(path))


def signed_null_disc(a, edges, u, v, b_vertex, face_set):
    path = complement_path(a, edges, u, v)
    chain = [((path[i], path[i+1], b_vertex), 1) for i in range(len(path)-1)]
    chain.extend([((u, path[i], path[i+1]), -1) for i in range(1,len(path)-1)])
    assert all(tuple(sorted(tri)) in face_set for tri,_ in chain)
    assert boundary_of_chain(chain) == boundary_of_chain([((u,v,b_vertex), 1)])


def check(a,b,edges,do_homology=True):
    edges = {tuple(sorted(x)) for x in edges}
    assert linear_forest(a,edges)
    faces = graph_faces(a,b,edges)
    expected_faces = predicted_faces(a,b,edges)
    assert faces == expected_faces, (a,b,edges,'faces')
    triangles = set(faces[3])
    for u,v in edges:
        for x in range(a,a+b):
            signed_null_disc(a,edges,u,v,x,triangles)
    if do_homology:
        R = 1-a*b+a*comb(b,2)+b*comb(a,2)
        expected = {2:R-b*len(edges)} if R-b*len(edges) else {}
        for p in (2,3):
            actual = ranks(faces,p)
            assert actual == expected,(a,b,edges,p,actual,expected)
    return 1


def run():
    cases=0;homology_cases=0
    # All labeled linear forests on four A-vertices.
    for a,b in ((4,2),(4,3)):
        all_edges=list(combinations(range(a),2))
        for mask in range(1<<len(all_edges)):
            edges={e for i,e in enumerate(all_edges) if mask & (1<<i)}
            if linear_forest(a,edges):
                cases+=check(a,b,edges,do_homology=True)
                homology_cases+=1
    # A broader class, including long paths, matchings and disconnected paths.
    examples = []
    for a in (5,6,7):
        examples.extend((a,es) for es in [
            set(), {(i,i+1) for i in range(a-1)},
            {(2*i,2*i+1) for i in range(a//2)},
            {(0,1),(1,2)}, {(0,1),(1,2),(3,4)}])
    for a,edges in examples:
        for b in (2,3):
            cases+=check(a,b,edges,do_homology=True)
            homology_cases+=1
    print('PASS: exact induced-forest face classification and signed integral filling disks')
    print('PASS: reduced homology over GF(2) and GF(3) in all tested cases')
    print(f'Tested graph instances: {cases}; independently calculated homology instances: {homology_cases}')
    print('Small exceptional boundary (a=3, internal path P3):')
    exceptional=ranks(graph_faces(3,3,{(0,1),(1,2)}),2)
    assert exceptional == {1:1,2:5}
    print('  GF(2) reduced ranks:', exceptional, '(shows connected-complement assumption matters)')
    print('Finite checks do not prove any all-parameter or torsion statement.')

if __name__=='__main__':
    run()
