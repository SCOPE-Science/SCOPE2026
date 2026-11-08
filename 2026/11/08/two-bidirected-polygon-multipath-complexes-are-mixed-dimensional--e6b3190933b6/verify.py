#!/usr/bin/env python3
"""Exact finite certificates for bidirected polygon multipath complexes on 5 and 6 vertices.

Requires only Python 3 standard library.  Checks the full face posets, explicit
acyclic discrete-Morse matchings, a primitive integral 2-cocycle and its zero
Alexander-Whitney cup square.
"""
from itertools import combinations, product
from collections import Counter, deque


def graph_arcs(L):
    return ([(i, (i + 1) % L) for i in range(L)]
            + [((i + 1) % L, i) for i in range(L)])


def valid_arc_set(ids, arcs):
    """Independently apply the graph-theoretic disjoint-directed-path definition."""
    edges = [arcs[i] for i in ids]
    sources = [a for a, _ in edges]
    targets = [b for _, b in edges]
    if len(set(sources)) != len(edges) or len(set(targets)) != len(edges):
        return False
    next_vertex = dict(edges)
    for start in next_vertex:
        visited = set()
        vertex = start
        while vertex in next_vertex:
            if vertex in visited:
                return False
            visited.add(vertex)
            vertex = next_vertex[vertex]
    return True


def all_faces(L):
    arcs = graph_arcs(L)
    faces = {}
    for r in range(1, 2 * L + 1):
        for ids in combinations(range(2 * L), r):
            if valid_arc_set(ids, arcs):
                faces[sum(1 << i for i in ids)] = ids
    return faces


def h_width(face):
    return face.bit_count() - 1


def matching_and_acyclicity(L, faces):
    """Prioritized vertex toggles; verify every cover of the full face poset."""
    still = set(faces)
    pairs = []
    for i in range(2 * L):
        toggle = 1 << i
        for f in sorted(still):
            g = f | toggle
            if f in still and not (f & toggle) and g in still:
                assert h_width(g) == h_width(f) + 1
                still.remove(f)
                still.remove(g)
                pairs.append((f, g))
    paired = set(pairs)
    edges_out = {f: [] for f in faces}
    indegree = {f: 0 for f in faces}
    incidence_count = 0
    for g in faces:
        for i in faces[g]:
            f = g & ~(1 << i)
            if f not in faces:
                # The empty face is not an actual Morse cell.
                assert f == 0
                continue
            a, b = (f, g) if (f, g) in paired else (g, f)
            edges_out[a].append(b)
            indegree[b] += 1
            incidence_count += 1
    queue = deque(f for f in faces if indegree[f] == 0)
    visited = 0
    while queue:
        f = queue.popleft()
        visited += 1
        for g in edges_out[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
    assert visited == len(faces), 'Directed reversed Hasse graph is cyclic'
    assert 2 * len(pairs) + len(still) == len(faces)
    return Counter(h_width(f) for f in still), len(pairs), incidence_count, still


def oriented_boundary(chain):
    output = {}
    for simplex, coefficient in chain.items():
        for j in range(len(simplex)):
            face = simplex[:j] + simplex[j + 1:]
            output[face] = output.get(face, 0) + (-1) ** j * coefficient
    return {face: coefficient for face, coefficient in output.items()
            if coefficient}


def permutation_sign(indices):
    return (-1) ** sum(indices[i] > indices[j]
                        for i in range(len(indices))
                        for j in range(i + 1, len(indices)))


def verify_cup(L, faces):
    assert L == 6
    # Coefficients are on increasing oriented three-vertex simplices.
    supporting = [
        (0, 1, 3), (0, 2, 3), (0, 2, 4), (0, 2, 5),
        (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)
    ]
    alpha = {s: 1 for s in supporting}
    assert all(sum(1 << i for i in s) in faces for s in supporting)
    tetrahedra = [v for v in faces.values() if len(v) == 4]
    top_faces = [v for v in faces.values() if len(v) == 5]
    assert len(tetrahedra) == 48 and len(top_faces) == 12
    for s in tetrahedra:
        assert sum((-1)**j * alpha.get(s[:j] + s[j+1:], 0)
                   for j in range(4)) == 0, ('Not a cocycle', s)
    for s in top_faces:
        assert alpha.get(s[:3], 0) * alpha.get(s[2:], 0) == 0, (
            'Nonzero Alexander-Whitney cup-square coefficient', s)
    # Embedded octahedron = join of pairs of opposite arcs on three disjoint edges.
    z = {}
    for choices in product((0, 1), repeat=3):
        ordered = tuple(k if bit == 0 else L + k
                        for k, bit in zip((0, 2, 4), choices))
        simplex = tuple(sorted(ordered))
        assert sum(1 << i for i in simplex) in faces
        coefficient = (-1)**sum(choices) * permutation_sign(ordered)
        z[simplex] = coefficient
    assert len(z) == 8
    assert not oriented_boundary(z), 'Octahedral 2-cycle has nonzero boundary'
    pairing = sum(alpha.get(s, 0) * coeff for s, coeff in z.items())
    assert pairing == 1, 'Cocycle is not shown primitive'
    return len(supporting), len(tetrahedra), len(top_faces), pairing



def exact_rational_rank(rows):
    """Gauss elimination over the rationals: no floating-point assumptions."""
    from fractions import Fraction
    a = [[Fraction(v) for v in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        d = a[rank][col]
        for j in range(col, n):
            a[rank][j] /= d
        for i in range(rank + 1, m):
            c = a[i][col]
            if c:
                for j in range(col, n):
                    a[i][j] -= c * a[rank][j]
        rank += 1
        if rank == m:
            break
    return rank


def exact_boundary_rank(faces, dim):
    lower = sorted((s for s in faces.values() if len(s) == dim))
    upper = sorted((s for s in faces.values() if len(s) == dim + 1))
    idx = {s: i for i, s in enumerate(lower)}
    rows = [[0] * len(upper) for _ in lower]
    for j, simplex in enumerate(upper):
        for k in range(len(simplex)):
            rows[idx[simplex[:k] + simplex[k+1:]]][j] = (-1)**k
    return exact_rational_rank(rows)


def run():
    totals = []
    for L, expected_fvec, expected_critical, expected_pairs in [
        (5, [10, 30, 30, 10], {0: 1, 2: 1, 3: 2}, 38),
        (6, [12, 48, 76, 48, 12], {0: 1, 2: 1, 4: 2}, 96),
    ]:
        faces = all_faces(L)
        fvec = [sum(len(s) == r for s in faces.values())
                for r in range(1, max(len(s) for s in faces.values()) + 1)]
        assert fvec == expected_fvec, (L, fvec)
        # A separate observation: each selected arc has distinct source/target,
        # so at most L arcs occur; an L-arc face would be a directed Hamilton cycle.
        assert max(map(len, faces.values())) == L - 1
        crit, npairs, ninc, crit_faces = matching_and_acyclicity(L, faces)
        assert dict(crit) == expected_critical, (L, crit)
        assert npairs == expected_pairs
        totals.append((L, fvec, npairs, ninc, dict(crit)))
        if L == 5:
            ranks = (exact_boundary_rank(faces, 2), exact_boundary_rank(faces, 3))
            assert ranks == (21, 8), ranks
        if L == 6:
            evidence = verify_cup(L, faces)
    for L, fv, m, incidences, cc in totals:
        print(f'L={L} f_vector={fv} matched_pairs={m} '
              f'hasse_incidences={incidences} critical_cells={cc} acyclic=YES')
    print(f'L=5 exact_rational_boundary_ranks_d2_d3={ranks}')
    print(f'integral_cocycle_support={evidence[0]} '
          f'tetrahedra={evidence[1]} four_faces={evidence[2]} '
          f'octahedral_pairing={evidence[3]} cup_square=ZERO')
    print('ALL_VERIFY_OK')


if __name__ == '__main__':
    run()
