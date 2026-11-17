"""Finite independent checks of punctured halved-cube clique complexes.

Standard-library only. Run: python3 verify_halfcube.py
Exact mod-two ranks verify small cases; the general integral theorem uses proof.
"""
from itertools import combinations
from math import comb


def faces_by_adjacency(n, deleted):
    vertices = tuple(x for x in range(1 << n)
                     if x.bit_count() % 2 == 0 and (not deleted or x))
    neighbors = {v: {w for w in vertices if w > v and (v ^ w).bit_count() == 2}
                 for v in vertices}
    result = {}

    def grow(prefix, candidates):
        if prefix:
            result.setdefault(len(prefix), set()).add(prefix)
        for v in sorted(candidates):
            grow(prefix + (v,), candidates.intersection(neighbors[v]))

    grow((), set(vertices))
    return result


def faces_from_classification(n, deleted):
    result = {}
    def insert(simplex):
        if deleted and 0 in simplex:
            return
        result.setdefault(len(simplex), set()).add(tuple(sorted(simplex)))

    for odd in range(1 << n):
        if odd.bit_count() % 2 == 0:
            continue
        near = tuple(sorted(odd ^ (1 << j) for j in range(n)))
        for k in range(1, n + 1):
            for sub in combinations(near, k):
                insert(sub)

    for coords in combinations(range(n), 3):
        mask = sum(1 << j for j in coords)
        for base in range(1 << n):
            if base & mask:
                continue
            even = [base ^ s for s in (0, 1 << coords[0] | 1 << coords[1],
                                      1 << coords[0] | 1 << coords[2],
                                      1 << coords[1] | 1 << coords[2])]
            if base.bit_count() % 2:
                # If the fixed complement has odd parity, even vertices
                # are the singletons and the all-three-coordinate flip.
                even = [base ^ s for s in (1 << coords[0], 1 << coords[1],
                                          1 << coords[2], mask)]
            for k in range(1, 5):
                for sub in combinations(even, k):
                    insert(sub)
    return result


def mod2_ranks(faces):
    ordered = {k: sorted(rows) for k, rows in faces.items()}
    ranks = {}
    for k in range(2, max(ordered) + 1):
        index = {s: i for i, s in enumerate(ordered[k - 1])}
        pivots = {}
        for face in ordered[k]:
            bits = 0
            for subset in combinations(face, k - 1):
                bits ^= 1 << index[subset]
            while bits:
                high = bits.bit_length() - 1
                if high in pivots:
                    bits ^= pivots[high]
                else:
                    pivots[high] = bits
                    break
        ranks[k] = len(pivots)
    bettis = {k - 1: len(rows) - ranks.get(k, 0) - ranks.get(k + 1, 0)
              for k, rows in ordered.items()}
    bettis[0] -= 1
    return ranks, {k: v for k, v in bettis.items() if v}


def check_link_sphere_cones(n, deleted_faces):
    two_subsets = {tuple(sorted((i, j))): (1 << i) | (1 << j)
                   for i, j in combinations(range(n), 2)}
    for coords in combinations(range(n), 4):
        six = [two_subsets[p] for p in combinations(coords, 2)]
        w = sum(1 << j for j in coords)
        assert w != 0
        assert all((w ^ x).bit_count() == 2 for x in six)
        # The six pair labels form the octahedron graph; its 8 triangular
        # faces are the 4 coordinate stars and 4 coordinate triangles.
        triangles = [tuple(sorted(t)) for t in combinations(six, 3)
                     if all((x ^ y).bit_count() == 2
                            for x, y in combinations(t, 2))]
        assert len(triangles) == 8
        edge_occurrences = {}
        for tri in triangles:
            for edge in combinations(tri, 2):
                edge_occurrences[edge] = edge_occurrences.get(edge, 0) + 1
            assert tuple(sorted((w,) + tri)) in deleted_faces[4]
        assert len(edge_occurrences) == 12
        assert set(edge_occurrences.values()) == {2}
    return comb(n, 4)


def green_rank(n):
    return sum((-1) ** (i - 4) * (1 << (n-i)) * comb(n, i)
               for i in range(4, n + 1))


def verify():
    for n in range(4, 8):
        full = faces_by_adjacency(n, False)
        deleted = faces_by_adjacency(n, True)
        assert full == faces_from_classification(n, False)
        assert deleted == faces_from_classification(n, True)
        full_ranks, full_betti = mod2_ranks(full)
        del_ranks, del_betti = mod2_ranks(deleted)
        b = green_rank(n)
        loss = comb(n - 1, 3)
        assert full_betti == ({3: b} if b else {})
        assert del_betti == ({3: b - loss} if b != loss else {})
        assert check_link_sphere_cones(n, deleted) == comb(n, 4)
        count_full = sum(map(len, full.values()))
        count_del = sum(map(len, deleted.values()))
        print(f'n={n}: full_faces={count_full}; punctured_faces={count_del}; '
              f'full_beta3={b}; punctured_beta3={b-loss}; '
              f'link_beta2={loss}; cone_spheres={comb(n, 4)}; '
              f'mod2_boundary_ranks_full={full_ranks}; '
              f'mod2_boundary_ranks_punctured={del_ranks}')
    print('PUNCTURED_HALFCUBE_FINITE_CHECKS_PASS')


if __name__ == '__main__':
    verify()
