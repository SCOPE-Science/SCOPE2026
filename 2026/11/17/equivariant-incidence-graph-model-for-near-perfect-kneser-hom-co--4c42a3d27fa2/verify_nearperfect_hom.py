"""Exact finite checks for Hom(K_r, KG(2r+1,2)), r=2,3,4.

The code constructs all zero cells and all maximal two-cells directly
from the defining disjointness condition. A maximal two-cell is indexed by
one distinguished color with a 3-element support and 2-element supports
for the remaining colors.
"""
from itertools import combinations
from math import factorial
from collections import deque


def cells(r):
    n = 2*r + 1
    ground = tuple(range(n))
    def rec(remaining, current):
        if len(current) == r:
            yield tuple(current)
        else:
            for pair in combinations(remaining, 2):
                avail = tuple(q for q in remaining if q not in pair)
                yield from rec(avail, current + (pair,))
    zero = tuple(rec(ground, ()))
    assert len(set(zero)) == len(zero)
    id_of = {v: k for k, v in enumerate(zero)}
    # Each zero cell has exactly one spare point.
    triangles = {}
    for v in zero:
        spare = next(q for q in ground if all(q not in b for b in v))
        for color in range(r):
            triple = tuple(sorted(v[color] + (spare,)))
            key = (color, triple, tuple(v[j] if j != color else () for j in range(r)))
            if key not in triangles:
                corners = []
                for pair in combinations(triple, 2):
                    w = tuple(pair if j == color else v[j] for j in range(r))
                    corners.append(id_of[w])
                assert len(set(corners)) == 3
                triangles[key] = tuple(corners)
            assert id_of[v] in triangles[key]
    return zero, triangles


def check(r):
    n=2*r+1
    zero, triangles = cells(r)
    id_of = {v: k for k, v in enumerate(zero)}
    V = len(zero)
    T = len(triangles)
    incidence = sum(len(set(c)) for c in triangles.values())
    assert V == factorial(n)//(2**r)
    assert T == r*factorial(n)//(6*2**(r-1))
    assert incidence == 3*T
    # BFS in the bipartite incidence graph; vertices are 0-cells and triangles.
    v_triangles = [[] for _ in range(V)]
    for i, corners in enumerate(triangles.values()):
        for v in corners:
            v_triangles[v].append(i)
    tris = list(triangles.values())
    seen_v = {0}
    seen_t = set()
    q = deque([(0,0)])
    while q:
        side,k = q.popleft()
        if side == 0:
            for j in v_triangles[k]:
                if j not in seen_t:
                    seen_t.add(j)
                    q.append((1,j))
        else:
            for j in tris[k]:
                if j not in seen_v:
                    seen_v.add(j)
                    q.append((0,j))
    assert len(seen_v) == V and len(seen_t) == T
    betti = incidence - (V+T) + 1
    assert betti == 1 + (2*r - 3)*factorial(n)//(3*2**r)
    # Each 1-cell is contained in a unique 2-cell:
    edge_set = set()
    for corners in tris:
        for a,b in combinations(corners,2):
            e = tuple(sorted((a,b)))
            assert e not in edge_set
            edge_set.add(e)
    assert len(edge_set) == 3*T
    # Check the quotient under free color-label permutations S_r directly.
    vertex_orbits = {tuple(sorted(v)) for v in zero}
    triangle_orbits = set()
    incidence_orbits = set()
    for (special, triple, others), corners in triangles.items():
        non_special_pairs = tuple(sorted(p for p in others if p))
        t_orbit = (triple, non_special_pairs)
        triangle_orbits.add(t_orbit)
        for c in corners:
            v_orbit = tuple(sorted(zero[c]))
            incidence_orbits.add((v_orbit, t_orbit))
    assert len(vertex_orbits) == V//factorial(r)
    assert len(triangle_orbits) == T//factorial(r)
    assert len(incidence_orbits) == incidence//factorial(r)
    quotient_betti = len(incidence_orbits) - len(vertex_orbits) - len(triangle_orbits) + 1
    assert quotient_betti == 1 + (2*r-3)*factorial(n)//(3*2**r*factorial(r))
    assert (betti-1)//factorial(r) == quotient_betti-1
    print(f'r={r} n={n} zero_cells={V} triangles={T} incidence_edges={incidence} connected=YES betti1={betti} color_quotient_betti1={quotient_betti}')
    # Generators of S_n x S_r act simplicially and preserve the incidence graph.
    if r <= 3:
        triangle_vertex_sets = {frozenset(c) for c in tris}
        for gen in range(n-1):
            perm = list(range(n))
            perm[gen],perm[gen+1] = perm[gen+1],perm[gen]
            for corners in tris:
                mapped = frozenset(id_of[tuple(tuple(sorted(perm[q] for q in pair)) for pair in zero[k])] for k in corners)
                assert mapped in triangle_vertex_sets
        for gen in range(r-1):
            for corners in tris:
                mapped = []
                for k in corners:
                    b = list(zero[k]); b[gen],b[gen+1] = b[gen+1],b[gen]
                    mapped.append(id_of[tuple(b)])
                assert frozenset(mapped) in triangle_vertex_sets
                assert frozenset(mapped) != frozenset(corners)
    return V,T,incidence,betti


if __name__ == '__main__':
    for r in (2,3,4):
        check(r)
    print('NEAR_PERFECT_KNESER_HOM_EXACT_PASS')
