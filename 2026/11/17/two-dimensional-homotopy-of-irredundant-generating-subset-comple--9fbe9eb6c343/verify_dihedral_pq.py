#!/usr/bin/env python3
"""Finite independent reconstruction of irredundant-subset complexes in dihedral groups.

No external packages are required. The all-subsets group-membership oracle uses gcd
subgroup structure, not the theorem's predicted cell decomposition.
"""
from itertools import combinations
from math import gcd


def subgroup(n, subset):
    rotations = [x for k, x in subset if k == 0]
    reflections = [x for k, x in subset if k == 1]
    d = n
    for x in rotations:
        d = gcd(d, x)
    for x in reflections[1:]:
        d = gcd(d, x - reflections[0])
    return d, (reflections[0] % d if reflections else None)


def belongs(n, subset, element):
    d, reflection_residue = subgroup(n, subset)
    kind, exponent = element
    if kind == 0:
        return exponent % d == 0
    return reflection_residue is not None and exponent % d == reflection_residue


def independent(n, subset):
    return all(not belongs(n, subset[:j] + subset[j+1:], x)
               for j, x in enumerate(subset))


def predicted_faces(p, q):
    n = p*q
    refl = [(1, j) for j in range(n)]
    group_p = [(0, j) for j in range(1, n) if gcd(n, j) == q]
    group_q = [(0, j) for j in range(1, n) if gcd(n, j) == p]
    generators = [(0, j) for j in range(1, n) if gcd(n, j) == 1]
    vertices = refl + group_p + group_q + generators
    E = set()
    T = set()
    def add_edge(x, y):
        E.add(tuple(sorted((x, y))))
    def add_triangle(x, y, z):
        triangle = tuple(sorted((x,y,z)))
        T.add(triangle)
        for a,b in combinations(triangle, 2):
            add_edge(a,b)
    for a, b in combinations(refl, 2):
        add_edge(a,b)
    for r in refl:
        for x in group_p + group_q + generators:
            add_edge(r,x)
    for x in group_p:
        for y in group_q:
            add_edge(x,y)
            for r in refl:
                add_triangle(x,y,r)
    for r,s in combinations(refl, 2):
        if (r[1]-s[1])%p == 0:
            for x in group_p:
                add_triangle(r,s,x)
        if (r[1]-s[1])%q == 0:
            for x in group_q:
                add_triangle(r,s,x)
    return vertices, E, T


def rank_mod2_triangles(edges, triangles):
    edge_index = {edge:j for j,edge in enumerate(sorted(edges))}
    pivot = {}
    for triangle in triangles:
        x = 0
        for e in combinations(triangle, 2):
            x ^= 1 << edge_index[e]
        while x:
            high = x.bit_length() - 1
            if high not in pivot:
                pivot[high] = x
                break
            x ^= pivot[high]
    return len(pivot)


def expected_betti(p, q):
    n=p*q
    a=p-1; b=q-1; h=a*b
    b1=h*(3*n-2)//2
    b2=2*n*h - (3*n*(a+b))//2 - h+n+a+b-1
    return b1,b2


def check(p, q):
    n=p*q
    vertices,E,T=predicted_faces(p,q)
    all_vertices = [(0,j) for j in range(1,n)] + [(1,j) for j in range(n)]
    assert set(vertices)==set(all_vertices)
    oracle_edges={tuple(sorted(s)) for s in combinations(all_vertices,2)
                  if independent(n,s)}
    oracle_triangles={tuple(sorted(s)) for s in combinations(all_vertices,3)
                      if independent(n,s)}
    assert E == oracle_edges, (p,q,'wrong edges')
    assert T == oracle_triangles, (p,q,'wrong triangles')
    assert not any(independent(n,s) for s in combinations(all_vertices,4)), (p,q,'4-face')
    z2=rank_mod2_triangles(E,T)
    betti1=len(E)-len(vertices)+1-z2
    betti2=len(T)-z2
    assert (betti1,betti2)==expected_betti(p,q)
    # Independent f-vector: the first Betti number is the cycle count after
    # adjoining diagonal reflection edges and generator spokes to core.
    n_diag=n*(p-1)*(q-1)//2
    n_generator_spokes=(p-1)*(q-1)*(n-1)
    assert betti1 == n_diag+n_generator_spokes
    print(f"p={p},q={q},vertices={len(vertices)},edges={len(E)},triangles={len(T)},"
          f"betti1_mod2={betti1},betti2_mod2={betti2},classification=PASS")


def main():
    for p,q in [(2,3),(2,5),(3,5),(3,7)]:
        check(p,q)
    print('DIHEDRAL_PQ_IRREDUNDANT_COMPLEX_CHECK_PASS')

if __name__ == '__main__':
    main()
