#!/usr/bin/env python3
"""Exact finite certificate for quadrangle cycles in the rank-three PG(2,3) matroid.

Requires Python >=3.10 and sympy. All incidence data are derived from GF(3)^3.
"""
from itertools import combinations, product
from collections import Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def normalized(v):
    a = next(x for x in v if x)
    inv = pow(a, -1, 3)
    return tuple(x * inv % 3 for x in v)


def determinant(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0])) % 3


def rank_mod(A, p):
    """Full row elimination over the prime field, without sympy rank machinery."""
    a = [[int(x) % p for x in row] for row in A]
    rows, cols = len(a), len(a[0])
    rank, pivot_columns = 0, []
    for j in range(cols):
        k = next((i for i in range(rank, rows) if a[i][j]), None)
        if k is None:
            continue
        a[k], a[rank] = a[rank], a[k]
        inv = pow(a[rank][j], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(rows):
            if i == rank or a[i][j] == 0:
                continue
            q = a[i][j]
            a[i] = [(x - q * y) % p for x, y in zip(a[i], a[rank])]
        pivot_columns.append(j)
        rank += 1
        if rank == rows:
            break
    return rank, pivot_columns


def main():
    points = sorted({normalized(v) for v in product(range(3), repeat=3) if any(v)})
    assert len(points) == 13
    triples = list(combinations(range(13), 3))
    triangles = [t for t in triples if determinant(*(points[i] for i in t))]
    triangle_set = set(triangles)
    triangle_index = {t: i for i, t in enumerate(triangles)}
    arcs = [a for a in combinations(range(13), 4)
            if all(t in triangle_set for t in combinations(a, 3))]
    assert len(triangles) == len(arcs) == 234
    assert sum(0 in a for a in arcs) == 72
    assert len([t for t in triples if t not in triangle_set]) == 52

    # Every column is the oriented tetrahedral boundary supported on a 4-arc.
    arc_matrix = [[0] * len(arcs) for _ in triangles]
    for j, a in enumerate(arcs):
        for i, t in enumerate(combinations(a, 3)):
            arc_matrix[triangle_index[t]][j] = (-1) ** i

    # A split integral section of the boundary onto the cycle lattice of K_13:
    # non-root edges form canonical coordinates for that lattice.
    edges = list(combinations(range(1, 13), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    selected = []
    for i, j in edges:
        if (0, i, j) in triangle_set:
            selected.append((0, i, j))
        else:
            k = next(k for k in range(1, 13) if k not in (i, j)
                     and tuple(sorted((0, i, k))) in triangle_set
                     and tuple(sorted((0, j, k))) in triangle_set
                     and tuple(sorted((i, j, k))) in triangle_set)
            selected.append(tuple(sorted((i, j, k))))
    assert len(set(selected)) == 66
    section = [[0] * 66 for _ in edges]
    for j, t in enumerate(selected):
        for k, e in enumerate(combinations(t, 2)):
            if e in edge_index:
                section[edge_index[e]][j] = (-1) ** k
    det_section = Matrix(section).det(method='domain-ge')
    assert abs(det_section) == 1
    # Image of the simplicial boundary on the root-free edges has determinant 1,
    # giving the 168 integral coordinates indexed by all unselected triangles.
    missing = [t for t in triangles if t not in set(selected)]
    assert len(missing) == 168
    R = [arc_matrix[triangle_index[t]] for t in missing]

    # Independent exact evidence: rank over F_3 and a maximal determinant.
    rank_three, _ = rank_mod(R, 3)
    rank_two, columns = rank_mod(R, 2)
    assert rank_three == 165 and rank_two == 168 and len(columns) == 168
    maximal_minor = Matrix([[row[j] for j in columns] for row in R])
    determinant_minor = maximal_minor.det(method='domain-ge')
    assert determinant_minor == -27

    # A second exact implementation checks the entire Smith invariant list.
    smith = smith_normal_form(Matrix(R), domain=ZZ)
    invariants = Counter(abs(int(smith[i, i])) for i in range(168))
    assert invariants == {1: 165, 3: 3}
    # Boundary composition check for each 4-arc and each of 78 oriented edges.
    all_edges = list(combinations(range(13), 2))
    edge_idx = {e: i for i, e in enumerate(all_edges)}
    boundary = [[0] * len(triangles) for _ in all_edges]
    for j, t in enumerate(triangles):
        for k, edge in enumerate(combinations(t, 2)):
            boundary[edge_idx[edge]][j] = (-1) ** k
    for j in range(len(arcs)):
        for i in range(len(all_edges)):
            assert sum(boundary[i][t] * arc_matrix[t][j] for t in range(len(triangles))) == 0
    print('PG23_QUADRANGLE_LATTICE_EXACT_PASS')
    print('points=13 lines=13 independent_triangles=234 quadrangles=234')
    print('chosen_boundary_section=66 determinant=' + str(det_section))
    print('top_integral_homology_rank=168')
    print('rank_mod_2=168 rank_mod_3=165')
    print('maximal_minor_columns=' + ','.join(str(j) for j in columns))
    print('maximal_minor_determinant=' + str(determinant_minor))
    print('smith_invariants=1^165,3^3')
    print('circuit_boundary_lattice_quotient=(Z/3Z)^3')
    print('signed_boundary_squared_zero=verified_234_columns_78_edges')

if __name__ == '__main__':
    main()
