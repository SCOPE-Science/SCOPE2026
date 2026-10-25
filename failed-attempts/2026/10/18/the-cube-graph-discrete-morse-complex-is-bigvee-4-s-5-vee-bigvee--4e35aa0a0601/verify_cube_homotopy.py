#!/usr/bin/env python3
"""Exact finite verification for the ordinary Morse complex of the cube graph.

No external dependencies. Run: python verify_cube_homotopy.py

The graph is the one-skeleton of the three-dimensional cube. A vertex in
its Morse complex is a graph-vertex/incident-edge incidence, represented
by an oriented edge u -> v; faces are acyclic partial outdegree-one
orientations. The second matching is on the FACE POSET of this Morse
complex, not on the cube graph itself.
"""
from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import prod

V = tuple(range(8))
NEIGHBORS = tuple(tuple(v ^ (1 << j) for j in range(3)) for v in V)
ARCS = tuple((u, v) for u in V for v in NEIGHBORS[u])
ARC_ID = {arc: j for j, arc in enumerate(ARCS)}
assert len(ARCS) == 24
EDGES = tuple((u, v) for u in V for v in NEIGHBORS[u] if u < v)
assert len(EDGES) == 12


def has_cycle(next_vertex):
    for origin in V:
        seen = set()
        u = origin
        while u != -1 and u not in seen:
            seen.add(u)
            u = next_vertex[u]
        if u != -1:
            return True
    return False


def enumerate_by_tails():
    faces = set()
    for indices in product(range(4), repeat=8):
        target = tuple(NEIGHBORS[u][k - 1] if k else -1
                       for u, k in enumerate(indices))
        if not has_cycle(target):
            faces.add(sum(1 << ARC_ID[(u, v)] for u, v in enumerate(target)
                          if v != -1))
    return faces


def enumerate_by_edges():
    faces = set()
    for choices in product(range(3), repeat=12):
        target = [-1] * 8
        mask = 0
        possible = True
        for (u, v), ch in zip(EDGES, choices):
            if ch == 0:
                continue
            tail, head = (u, v) if ch == 1 else (v, u)
            if target[tail] != -1:
                possible = False
                break
            target[tail] = head
            mask |= 1 << ARC_ID[(tail, head)]
        if possible and not has_cycle(target):
            faces.add(mask)
    return faces


def signed_facets(mask):
    sign = 1
    bits = mask
    while bits:
        bit = bits & -bits
        yield mask ^ bit, sign
        bits ^= bit
        sign = -sign


def matching_by_arc_toggles(faces):
    remaining = set(faces)
    partners = {}
    for j in range(len(ARCS)):
        bit = 1 << j
        pairs = [(f, f | bit) for f in remaining
                 if not f & bit and (f | bit) in remaining]
        for lower, upper in pairs:
            assert lower in remaining and upper in remaining
            partners[lower] = upper
            partners[upper] = lower
            remaining.remove(lower)
            remaining.remove(upper)
    return partners, remaining


def directed_hasse_is_acyclic(faces, partners):
    # All upper-to-lower Hasse arrows are reversed exactly for matched pairs.
    indegree = {f: 0 for f in faces}
    next_nodes = {f: [] for f in faces}
    incidences = 0
    for upper in faces:
        for lower, sign in signed_facets(upper):
            assert lower in faces and sign in (-1, 1)
            incidences += 1
            if partners.get(lower) == upper:
                source, target = lower, upper
            else:
                source, target = upper, lower
            next_nodes[source].append(target)
            indegree[target] += 1
    queue = deque(f for f, deg in indegree.items() if deg == 0)
    processed = 0
    while queue:
        f = queue.popleft()
        processed += 1
        for target in next_nodes[f]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    assert processed == len(faces), 'the discrete-Morse matching is cyclic'
    return incidences


def two_skeleton_face_topological_order(faces, partners):
    # Exchange arrows on 5-cells. For a matched 5<->6 pair, the lower
    # 5-cell points to every other boundary 5-cell of its matched 6-cell.
    level5 = sorted(f for f in faces if f.bit_count() == 6)
    successors = {f: [] for f in level5}
    indegree = {f: 0 for f in level5}
    for lower in level5:
        upper = partners.get(lower)
        if upper is None or upper.bit_count() != 7:
            continue
        for other, _ in signed_facets(upper):
            if other != lower:
                successors[lower].append(other)
                indegree[other] += 1
    queue = deque(f for f in level5 if indegree[f] == 0)
    order = []
    while queue:
        f = queue.popleft()
        order.append(f)
        for other in successors[f]:
            indegree[other] -= 1
            if indegree[other] == 0:
                queue.append(other)
    assert len(order) == len(level5)
    return order


def gradient_matrix_recursive(crit5, crit6, partners):
    row_index = {f: i for i, f in enumerate(crit5)}

    @lru_cache(maxsize=None)
    def project(face):
        if face in row_index:
            return {row_index[face]: 1}
        upper = partners.get(face)
        if upper is None or upper.bit_count() != 7:
            # An upper member of a 4<->5 pair maps to zero.
            return {}
        facets = dict(signed_facets(upper))
        pivot = facets[face]
        assert abs(pivot) == 1
        ans = Counter()
        for other, sign in facets.items():
            if other != face:
                for i, coefficient in project(other).items():
                    ans[i] -= pivot * sign * coefficient
        return {i: c for i, c in ans.items() if c}

    matrix = [[0] * len(crit6) for _ in crit5]
    for j, top in enumerate(crit6):
        for face, sign in signed_facets(top):
            for i, coefficient in project(face).items():
                matrix[i][j] += sign * coefficient
    return matrix


def gradient_matrix_propagation(crit5, crit6, partners, order):
    # Independently sum all signed gradient paths in forward topological
    # order; this does not use recursive memoisation or the matrix above.
    row_index = {f: i for i, f in enumerate(crit5)}
    matrix = [[0] * len(crit6) for _ in crit5]
    for j, top in enumerate(crit6):
        current = Counter()
        for face, sign in signed_facets(top):
            current[face] += sign
        for face in order:
            coefficient = current.pop(face, 0)
            if not coefficient:
                continue
            if face in row_index:
                matrix[row_index[face]][j] += coefficient
                continue
            upper = partners.get(face)
            if upper is None or upper.bit_count() != 7:
                continue
            facets = dict(signed_facets(upper))
            pivot = facets[face]
            assert abs(pivot) == 1
            for other, sign in facets.items():
                if other != face:
                    current[other] -= coefficient * pivot * sign
        assert not any(current.values())
    return matrix


def unit_pivot_smith_reduction(matrix):
    # Integral row and column operations with unit pivots prove the Smith
    # invariants without a floating-point calculation or symbolic library.
    a = [row.copy() for row in matrix]
    num_rows, num_cols = len(a), len(a[0])
    k = 0
    max_abs = 0
    while k < min(num_rows, num_cols):
        pivot = next(((i, j) for i in range(k, num_rows)
                      for j in range(k, num_cols) if abs(a[i][j]) == 1), None)
        if pivot is None:
            break
        i, j = pivot
        a[i], a[k] = a[k], a[i]
        for row in a:
            row[j], row[k] = row[k], row[j]
        sign = a[k][k]
        for i in range(k + 1, num_rows):
            factor = a[i][k] * sign
            if factor:
                for j in range(k, num_cols):
                    a[i][j] -= factor * a[k][j]
        for j in range(k + 1, num_cols):
            factor = a[k][j] * sign
            if factor:
                for i in range(k, num_rows):
                    a[i][j] -= factor * a[i][k]
        assert all(a[i][k] == 0 for i in range(k + 1, num_rows))
        assert all(a[k][j] == 0 for j in range(k + 1, num_cols))
        max_abs = max(max_abs, max(abs(v) for row in a for v in row))
        k += 1
    tail_nonzero = sum(a[i][j] != 0 for i in range(k, num_rows)
                       for j in range(k, num_cols))
    assert tail_nonzero == 0
    return k, max_abs


def main():
    faces = enumerate_by_tails()
    independent = enumerate_by_edges()
    assert faces == independent
    counts = Counter(f.bit_count() - 1 for f in faces)
    assert [counts[k] for k in range(-1, 7)] == [
        1, 24, 240, 1296, 4080, 7488, 7424, 3072]
    assert len(faces) == 23625
    # The matrix-forest check follows from the Q3 Laplacian spectrum
    # 0, 2,2,2, 4,4,4, 6. Coefficient of t^(k+1) counts k-faces.
    coefficients = [1]
    for eigenvalue in (0, 2, 2, 2, 4, 4, 4, 6):
        newer = [0] * (len(coefficients) + 1)
        for i, c in enumerate(coefficients):
            newer[i] += eigenvalue * c
            newer[i + 1] += c
        coefficients = newer
    assert coefficients == [0, 3072, 7424, 7488, 4080,
                            1296, 240, 24, 1]
    partners, remaining = matching_by_arc_toggles(faces)
    assert len(partners) == 2 * 11698
    assert Counter(f.bit_count() - 1 for f in remaining) == {5: 47, 6: 182}
    arcs = directed_hasse_is_acyclic(faces, partners)
    assert arcs == 124200
    crit5 = sorted(f for f in remaining if f.bit_count() == 6)
    crit6 = sorted(f for f in remaining if f.bit_count() == 7)
    order = two_skeleton_face_topological_order(faces, partners)
    a = gradient_matrix_recursive(crit5, crit6, partners)
    b = gradient_matrix_propagation(crit5, crit6, partners, order)
    assert a == b
    assert len(a) == 47 and all(len(row) == 182 for row in a)
    nonzero = sum(v != 0 for row in a for v in row)
    assert nonzero == 334
    assert max(abs(v) for row in a for v in row) == 1
    rank, max_abs = unit_pivot_smith_reduction(a)
    assert rank == 43, (rank, max_abs)
    assert len(crit5) - rank == 4
    assert len(crit6) - rank == 139
    # Encode each signed entry as 0 (minus), 1 (zero), or 2 (plus).
    digest = sha256(bytes(v + 1 for row in a for v in row)).hexdigest()
    print('VERIFY_OK',
          'faces=23625', 'hasse_incidences=124200',
          'matching_pairs=11698', 'critical5=47', 'critical6=182',
          'morse_shape=47x182', 'morse_nonzero=334',
          'unit_smith_factors=43', 'smith_zeros=4',
          'H5_rank=4', 'H6_rank=139',
          'matrix_sha256=' + digest)


if __name__ == '__main__':
    main()
