#!/usr/bin/env python3
"""Reproducible finite checks for wheel general-position complexes.

All-order homotopy uses the cited cycle higher-independence theorem and
an explicit nullhomotopy; no finite experiment is used as an infinite proof.
"""
from collections import Counter
from itertools import combinations
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def bad_triples(n):
    return {frozenset((i % n, (i + 1) % n, (i + 2) % n)) for i in range(n)}


def rim_faces(n):
    bad = [sum(1 << x for x in t) for t in bad_triples(n)]
    return {mask for mask in range(1 << n) if all(mask & b != b for b in bad)}


def wheel_distances(n):
    # Rim labels 0,...,n-1 and hub n.
    v = n + 1
    adjacency = [set() for _ in range(v)]
    for i in range(n):
        for j in ((i + 1) % n, n):
            adjacency[i].add(j)
            adjacency[j].add(i)
    distances = []
    for start in range(v):
        dist = [None] * v
        dist[start] = 0
        todo = [start]
        for u in todo:
            for w in adjacency[u]:
                if dist[w] is None:
                    dist[w] = dist[u] + 1
                    todo.append(w)
        distances.append(dist)
    return distances


def wheel_faces(n):
    D = wheel_distances(n)
    bad = []
    for a, b, c in combinations(range(n + 1), 3):
        if (D[a][b] + D[b][c] == D[a][c] or
            D[a][c] + D[c][b] == D[a][b] or
            D[b][a] + D[a][c] == D[b][c]):
            bad.append((1 << a) | (1 << b) | (1 << c))
    return {mask for mask in range(1 << (n + 1)) if all(mask & b != b for b in bad)}


def model_faces(n):
    A = rim_faces(n)
    spoke = [0, *(1 << i for i in range(n))]
    rim_edges = [(1 << i) | (1 << ((i + 1) % n)) for i in range(n)]
    return A | {m | (1 << n) for m in spoke + rim_edges}


def check_mobius():
    n = 5
    faces = rim_faces(n)
    F = [tuple(i for i in range(n) if f >> i & 1)
         for f in faces if f.bit_count() == 3]
    assert len(F) == 5
    assert len([x for x in faces if x.bit_count() == 2]) == 10
    multiplicities = Counter(tuple(sorted(edge)) for tri in F for edge in combinations(tri, 2))
    boundary = {edge for edge, count in multiplicities.items() if count == 1}
    rim = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    assert boundary == rim
    assert all(count in (1, 2) for count in multiplicities.values())
    for v in range(n):
        links = [tuple(sorted(w for w in t if w != v)) for t in F if v in t]
        assert len(links) == 3
        deg = Counter(w for e in links for w in e)
        assert sorted(deg.values()) == [1, 1, 2, 2]
    # Integral first-homology computation for all GP(W6) simplices.
    full = wheel_faces(n)
    edges = sorted(tuple(i for i in range(n + 1) if mask >> i & 1)
                   for mask in full if mask.bit_count() == 2)
    triangles = sorted(tuple(i for i in range(n + 1) if mask >> i & 1)
                       for mask in full if mask.bit_count() == 3)
    assert len(edges) == 15 and len(triangles) == 10
    # Tree edges to hub form integral cycle basis (non-tree edges free coordinates).
    non_tree_edges = [e for e in edges if n not in e]
    assert len(non_tree_edges) == 10
    eindex = {e: i for i, e in enumerate(non_tree_edges)}
    M = sp.zeros(len(non_tree_edges), len(triangles))
    for j, (a,b,c) in enumerate(triangles):
        for edge, sign in [((b,c), 1), ((a,c),-1), ((a,b), 1)]:
            if edge in eindex:
                M[eindex[edge],j] = sign
    D = smith_normal_form(M, domain=ZZ)
    diag = sorted(abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i] != 0)
    assert diag == [1]*9 + [2], ('wrong RP2 torsion',diag)
    print('n=5: five-triangle Moebius surface, C5 boundary; GP(W6): H1=Z/2')


def critical_match(n):
    faces = rim_faces(n) - {0}
    rem = set(faces)
    pairs = []
    for v in range(n):
        for low in sorted(rem, key=lambda m: (m.bit_count(),m)):
            high = low | (1 << v)
            if not low >> v & 1 and low in rem and high in rem:
                rem.remove(low)
                rem.remove(high)
                pairs.append((low,high))
    return Counter(m.bit_count()-1 for m in rem), pairs


def main():
    assert wheel_faces(3) == set(range(1<<4)), 'W4 must be a simplex'
    for n in range(4,14):
        assert wheel_faces(n) == model_faces(n), ('model mismatch',n)
    print('n=3: simplex; n=4..13: all graph shortest-path faces equal hub-cone model')
    for n in range(6,81):
        forbidden = bad_triples(n)
        for i in range(n):
            v = (i+4)%n
            for a,b in combinations(((i+j)%n for j in (0,1,2)),2):
                assert frozenset((a,b,v)) not in forbidden, (n,i,a,b,v)
    print('n=6..80: each forbidden triangle bounds an explicit three-triangle cone')
    check_mobius()
    expected = {0: (0,0),1:(2,-1),2:(1,0),3:(1,1)}
    for n in range(6,17):
        crit,_ = critical_match(n)
        k,r = divmod(n,4)
        if r == 0:
            want = {0:1,2*k-1:3}
        elif r == 1:
            want = {0:1,2*k-1:1}
        elif r == 2:
            want = {0:1,2*k:1}
        else:
            want = {0:1,2*k+1:1}
        assert dict(crit) == want, (n,crit,want)
    print('n=6..16: lexicographic cycle Morse critical-cell counts agree with cited all-order formula')
    print('ALL CHECKS PASS')


if __name__=='__main__':
    main()
