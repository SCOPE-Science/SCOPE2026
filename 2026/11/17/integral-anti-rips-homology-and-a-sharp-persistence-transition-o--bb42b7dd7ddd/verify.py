#!/usr/bin/env python3
"""Exact integral boundary certificates for finite Hamming packing complexes.

Python 3 standard library only. The output is a deterministic JSON certificate.
The two enumerators use independent constructions (combinations vs graph growth).
"""
from collections import Counter
from itertools import combinations
import json


def faces_by_combinations(n, threshold):
    N = 1 << n
    adjacent = [set() for _ in range(N)]
    for u in range(N):
        for v in range(u + 1, N):
            if (u ^ v).bit_count() >= threshold:
                adjacent[u].add(v)
                adjacent[v].add(u)
    out = {1: [(v,) for v in range(N)]}
    for size in range(2, 5):
        out[size] = [t for t in combinations(range(N), size)
                     if all(v in adjacent[u] for u, v in combinations(t, 2))]
    assert not any(all(v in adjacent[u] for u, v in combinations(t + (w,), 2))
                   for t in out[4] for w in range(N) if w > t[-1]), '5-clique found'
    return out, adjacent


def faces_by_growth(adjacent):
    N = len(adjacent)
    out = {1: [(v,) for v in range(N)]}
    for size in range(2, 5):
        out[size] = []
        for t in out[size - 1]:
            for v in range(t[-1] + 1, N):
                if all(v in adjacent[u] for u in t):
                    out[size].append(t + (v,))
    return out


def oriented_boundary_matrix_rows(sources, targets):
    """One row per oriented target, sparse integer columns for source faces."""
    loc = {face: i for i, face in enumerate(targets)}
    rows = [dict() for _ in targets]
    for col, simplex in enumerate(sources):
        for j in range(len(simplex)):
            face = simplex[:j] + simplex[j + 1:]
            rows[loc[face]][col] = (-1) ** j
    return rows


def integer_unit_elimination(initial_rows):
    """Integral Smith-like elimination; only ±1 pivots, hence primitive image.

    Each step uses invertible integer row and column operations to isolate a
    unit pivot. A zero residual matrix certifies the full rank and unit Smith
    factors without numerical approximation or modular-rank assumptions.
    """
    rows = {i: dict(row) for i, row in enumerate(initial_rows)}
    cols = {}
    for i, row in rows.items():
        for j, value in row.items():
            assert value != 0
            cols.setdefault(j, {})[i] = value
    count, maximum = 0, 1
    while True:
        pivots = [(len(rows[i]) * len(cols[j]), i, j)
                  for i, row in rows.items() for j, v in row.items()
                  if abs(v) == 1]
        if not pivots:
            break
        _, i, j = min(pivots)
        row = dict(rows[i]); column = dict(cols[j]); unit = rows[i][j]
        assert unit in (-1, 1)
        for other_i, coeff in column.items():
            if other_i == i:
                continue
            factor = coeff * unit
            for other_j, value in row.items():
                if other_j == j:
                    continue
                updated = rows[other_i].get(other_j, 0) - factor * value
                if updated:
                    rows[other_i][other_j] = updated
                    cols[other_j][other_i] = updated
                    maximum = max(maximum, abs(updated))
                else:
                    rows[other_i].pop(other_j, None)
                    cols[other_j].pop(other_i, None)
        for other_i in column:
            rows[other_i].pop(j, None)
        for other_j in row:
            cols[other_j].pop(i, None)
        del rows[i]
        del cols[j]
        count += 1
    assert not any(rows.values()), 'nonzero residual: unit certificate incomplete'
    assert not any(cols.values()), 'column map mismatch'
    return {'unit_pivots': count, 'residual_nonzero': 0,
            'largest_intermediate_absolute_entry': maximum}


def verify_case(n, threshold, expected):
    faces, adj = faces_by_combinations(n, threshold)
    independent = faces_by_growth(adj)
    assert faces == independent
    f = tuple(len(faces[s]) for s in range(1, 5))
    assert f == tuple(expected['face_counts'])
    old_edges = {e for e in faces[2] if (e[0] ^ e[1]).bit_count() >= n - 1}
    new_edges = [e for e in faces[2] if e not in old_edges]
    assert len(old_edges) == (1 << (n - 1)) * (n + 1)
    assert len(new_edges) == (1 << (n - 1)) * (n * (n - 1) // 2)
    incidence = Counter(t[:j] + t[j + 1:] for t in faces[4] for j in range(4))
    assert len(incidence) == len(faces[3])
    assert set(incidence.values()) == {1}
    full = oriented_boundary_matrix_rows(faces[3], faces[2])
    selected = {e: i for i, e in enumerate(faces[2]) if e in new_edges}
    rel = [full[i] for e, i in selected.items()]
    assert len(rel) == len(new_edges)
    full_result = integer_unit_elimination(full)
    relative_result = integer_unit_elimination(rel)
    assert full_result['unit_pivots'] == expected['boundary2_rank']
    assert relative_result['unit_pivots'] == expected['relative_boundary2_rank']
    rank2 = full_result['unit_pivots']; rankproj = relative_result['unit_pivots']
    rank3 = len(faces[4])
    b1 = f[1] - (f[0] - 1) - rank2
    b2 = f[2] - rank2 - rank3
    old_b1 = len(old_edges) - f[0] + 1
    kernel_rank = rank2 - rankproj
    image_rank = old_b1 - kernel_rank
    cokernel_rank = len(new_edges) - rankproj
    assert (b1, b2, old_b1, kernel_rank, image_rank, cokernel_rank) == tuple(expected['ranks'])
    assert image_rank + cokernel_rank == b1
    return {'n': n, 'threshold_new': threshold, 'threshold_old': threshold + 1,
            'face_counts_dim0_to_3': list(f), 'triangles_per_tetrahedron': 4,
            'triangles_in_exactly_one_tetrahedron': len(incidence),
            'full_boundary_2_certificate': full_result,
            'relative_boundary_2_certificate': relative_result,
            'boundary_3_rank': rank3,
            'old_edges': len(old_edges), 'new_edges': len(new_edges),
            'integral_betti_1': b1, 'integral_betti_2': b2,
            'old_integral_betti_1': old_b1,
            'integral_inclusion_H1_kernel_rank': kernel_rank,
            'integral_inclusion_H1_image_rank': image_rank,
            'integral_inclusion_H1_cokernel_rank': cokernel_rank,
            'all_relevant_cokernels_torsionfree': True,
            'independent_face_enumerators_agree': True}


def main():
    cases = [
        verify_case(5, 3, {'face_counts': [32, 256, 480, 120],
                           'boundary2_rank': 209, 'relative_boundary2_rank': 159,
                           'ranks': [16, 151, 65, 50, 15, 1]}),
        verify_case(6, 4, {'face_counts': [64, 704, 960, 240],
                           'boundary2_rank': 418, 'relative_boundary2_rank': 418,
                           'ranks': [223, 302, 161, 0, 161, 62]})]
    print(json.dumps({'result': 'PASS', 'finite_cases': cases,
                      'all_parameter_proof': 'see RESULT.md, Plotkin triple inequality'},
                     sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
