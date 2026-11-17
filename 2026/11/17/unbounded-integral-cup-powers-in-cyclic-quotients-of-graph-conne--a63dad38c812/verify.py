"""Finite reproducibility checks for cyclic graph-connectivity complexes.

Python 3 standard library only. Finite checks corroborate, but do not replace,
the infinite-family proof or its classifying-space cohomology argument.
"""
from itertools import combinations
from collections import defaultdict
from math import gcd


def connected_after_deleting(n, edge_set, omitted):
    remain = set(range(n)) - set(omitted)
    if len(remain) <= 1:
        return True
    start = next(iter(remain))
    seen = {start}
    frontier = [start]
    adj = {v: [] for v in remain}
    for a, b in edge_set:
        if a in remain and b in remain:
            adj[a].append(b)
            adj[b].append(a)
    while frontier:
        for v in adj[frontier.pop()]:
            if v not in seen:
                seen.add(v)
                frontier.append(v)
    return seen == remain


def k_connected(n, edge_set, k):
    return all(connected_after_deleting(n, edge_set, omitted)
               for j in range(k) for omitted in combinations(range(n), j))


def rotate_edges(n, edge_set, amount=1):
    return frozenset(tuple(sorted(((a + amount) % n, (b + amount) % n)))
                     for a, b in edge_set)


def expected_free(n, k):
    return n in (3, 5, 7, 11, 13) and k <= 2


def verify_orbit_obstructions():
    prime_tests = 0
    for p in (3, 5, 7, 11, 13):
        for a, b in combinations(range(p), 2):
            orbit = frozenset(tuple(sorted(((a + t) % p, (b + t) % p)))
                              for t in range(p))
            assert len(orbit) == p
            assert k_connected(p, orbit, 2)
            if p >= 5:
                assert not k_connected(p, orbit, 3)
            prime_tests += 1
    composite_tests = 0
    for n in (4, 6, 8, 9, 10, 12):
        d = next(x for x in range(2, n) if n % x == 0)
        order = n // d
        edge_orbit = frozenset(tuple(sorted(((j * d) % n, ((j + 1) * d) % n)))
                               for j in range(order))
        assert not k_connected(n, edge_orbit, 1)
        assert rotate_edges(n, edge_orbit, d) == edge_orbit
        composite_tests += 1
    return prime_tests, composite_tests


def n5_orbit_chain():
    n = 5
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}
    m = len(edges)
    edge_shift = [idx[tuple(sorted(((a + 1) % n, (b + 1) % n)))]
                  for a, b in edges]

    def mask_edges(mask):
        return frozenset(edges[i] for i in range(m) if mask >> i & 1)

    def rotate(mask):
        y = 0
        for i in range(m):
            if mask >> i & 1:
                y |= 1 << edge_shift[i]
        return y

    faces = {mask for mask in range(1, 1 << m)
             if not k_connected(n, mask_edges(mask), 2)}
    assert len(faces) == 785
    orbit_rep = {}
    reps = defaultdict(list)
    for mask in sorted(faces):
        if mask in orbit_rep:
            continue
        orb, x = [], mask
        for _ in range(n):
            orb.append(x)
            x = rotate(x)
        assert x == mask and len(set(orb)) == n
        rep = min(orb)
        reps[mask.bit_count() - 1].append(rep)
        for x in orb:
            orbit_rep[x] = rep
    for d in reps:
        reps[d].sort()
    sizes = {d: len(reps[d]) for d in reps}
    assert sizes == {0: 2, 1: 9, 2: 24, 3: 42, 4: 48, 5: 28, 6: 4}, sizes
    ix = {d: {r: i for i, r in enumerate(reps[d])} for d in reps}

    def parity(arr):
        return -1 if sum(arr[i] > arr[j] for i in range(len(arr))
                         for j in range(i + 1, len(arr))) % 2 else 1

    def orbit_orientation(mask, rep):
        a = [i for i in range(m) if mask >> i & 1]
        for _ in range(n):
            if mask == rep:
                return parity(a)
            mask = rotate(mask)
            a = [edge_shift[i] for i in a]
        raise AssertionError('missing orbit')

    maxd = max(reps)
    c = {d: len(reps[d]) for d in reps}
    boundaries = {d: [[0] * c[d] for _ in range(c[d - 1])]
                  for d in range(1, maxd + 1)}
    for d in range(1, maxd + 1):
        for j, rep in enumerate(reps[d]):
            es = [i for i in range(m) if rep >> i & 1]
            for pos, edge in enumerate(es):
                face = rep ^ (1 << edge)
                target = orbit_rep[face]
                boundaries[d][ix[d - 1][target]][j] += (-1) ** pos * orbit_orientation(face, target)

    def compositions_zero():
        for d in range(2, maxd + 1):
            for row in boundaries[d - 1]:
                for j in range(c[d]):
                    assert sum(row[k] * boundaries[d][k][j]
                               for k in range(c[d - 1])) == 0, d

    compositions_zero()
    cancels = 0
    while True:
        pivot = None
        for d in sorted(boundaries, reverse=True):
            for i, row in enumerate(boundaries[d]):
                for j, v in enumerate(row):
                    if abs(v) == 1:
                        pivot = (d, i, j)
                        break
                if pivot is not None:
                    break
            if pivot is not None:
                break
        if pivot is None:
            break
        d, i, j = pivot
        mat = boundaries[d]
        unit = mat[i][j]
        # Unimodular column changes in degree d, with inverse changes
        # to adjacent boundary in degree d+1.
        for k in range(c[d]):
            if k == j:
                continue
            factor = mat[i][k] // unit
            if factor:
                for row in mat:
                    row[k] -= factor * row[j]
                if d + 1 in boundaries:
                    for l in range(c[d + 1]):
                        boundaries[d + 1][j][l] += factor * boundaries[d + 1][k][l]
        # Unimodular row changes, with inverse changes in degree d-1.
        for l in range(c[d - 1]):
            if l == i:
                continue
            factor = mat[l][j] // unit
            if factor:
                for k in range(c[d]):
                    mat[l][k] -= factor * mat[i][k]
                if d - 1 in boundaries:
                    for row in boundaries[d - 1]:
                        row[i] += factor * row[l]
        assert mat[i][j] == unit
        assert all(mat[i][k] == 0 for k in range(c[d]) if k != j)
        assert all(mat[l][j] == 0 for l in range(c[d - 1]) if l != i)
        mat.pop(i)
        for row in mat:
            row.pop(j)
        if d + 1 in boundaries:
            assert all(x == 0 for x in boundaries[d + 1][j])
            boundaries[d + 1].pop(j)
        if d - 1 in boundaries:
            assert all(row[i] == 0 for row in boundaries[d - 1])
            for row in boundaries[d - 1]:
                row.pop(i)
        c[d] -= 1
        c[d - 1] -= 1
        cancels += 1
        compositions_zero()
    assert cancels == 74, cancels
    assert c == {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 0}, c
    assert abs(boundaries[2][0][0]) == 5, boundaries[2]
    four = boundaries[4]
    assert len(four) == 2 and len(four[0]) == 2
    det = four[0][0] * four[1][1] - four[0][1] * four[1][0]
    assert abs(det) == 5
    assert gcd(*(abs(x) for row in four for x in row)) == 1
    assert all(v == 0 for d in (1, 3, 5) for row in boundaries[d] for v in row)
    return len(faces), sum(sizes.values()), cancels, c, det


def main():
    p, c = verify_orbit_obstructions()
    f, o, u, counts, det = n5_orbit_chain()
    print('PRIME_EDGE_ORBITS_2CONNECTED', p)
    print('COMPOSITE_INVARIANT_DISCONNECTED_WITNESSES', c)
    print('FIVE_VERTEX_NOT_2_CONNECTED_FACES', f)
    print('FIVE_VERTEX_CYCLIC_FACE_ORBITS', o)
    print('EXACT_UNIT_CANCELLATIONS', u)
    print('RESIDUAL_CELLS_BY_DEGREE', counts)
    print('RESIDUAL_DEGREE_FOUR_DETERMINANT', det)
    print('HOMOLOGY_Q5 H1=Z/5 H3=Z/5 H5=Z^2; other positive H=0')
    print('ALL_FINITE_CHECKS_PASS')


if __name__ == '__main__':
    main()
