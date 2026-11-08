"""Exact finite checks for cyclic-prism three-cut homology characters.

Standard Python 3; no third-party dependencies.
The infinite family theorem is proved separately by face classification,
Hopf traces, and equivariant combinatorial Alexander duality.
"""
from itertools import combinations, product


def graph_data(n):
    N = 2 * n
    edges = set()
    for i in range(n):
        j = (i + 1) % n
        for x, y in ((i, j), (n + i, n + j), (i, n + i)):
            edges.add(tuple(sorted((x, y))))
    neighbors = [set() for _ in range(N)]
    for x, y in edges:
        neighbors[x].add(y)
        neighbors[y].add(x)
    triangles = {
        tuple(sorted((x, m, y)))
        for m in range(N)
        for x, y in combinations(sorted(neighbors[m]), 2)
    }
    tetrahedra = {
        tuple(sorted((i, (i + 1) % n, i + n, ((i + 1) % n) + n)))
        for i in range(n)
    }
    assert len(edges) == 3 * n
    assert len(triangles) == 6 * n
    assert len(tetrahedra) == n
    return edges, triangles, tetrahedra


def vertex_permutation(n, a, reflection, swap):
    return [((a - i if reflection else a + i) % n) +
            n * (((x // n) + swap) % 2)
            for x in range(2 * n) for i in (x % n,)]


def orientation_sign(mapped):
    return -1 if sum(mapped[i] > mapped[j]
                     for i in range(len(mapped))
                     for j in range(i + 1, len(mapped))) % 2 else 1


def fixed_trace(faces, perm):
    return sum(orientation_sign([perm[v] for v in f])
               for f in faces if {perm[v] for v in f} == set(f))


def predicted(n, a, b, c):
    beta = 2 * n * n - 8 * n + 1
    if n % 2:
        if not b and not c:
            return beta if a == 0 else 1
        if not b and c:
            return -1
        if b and not c:
            return 4 - n
        return n - 2
    if not b and not c:
        return beta if a == 0 else (1 - n if a == n // 2 else 1)
    if not b and c:
        return 1 - n if a == n // 2 else 1
    if b and not c:
        return 9 - n if a % 2 == 0 else 3 - n
    return 1 - n if a % 2 == 0 else 3 - n


def verify_collapse(n, triangles, tetrahedra):
    """Rebuild the entire dual face set; perform 6n elementary collapses."""
    face_set = {(v,) for v in range(2 * n)}
    face_set.update(combinations(range(2 * n), 2))
    face_set.update(triangles)
    face_set.update(tetrahedra)
    initial = len(face_set)
    count = 0

    def collapse(free, coface):
        nonlocal count
        free, coface = tuple(sorted(free)), tuple(sorted(coface))
        assert free in face_set and coface in face_set
        assert len(coface) == len(free) + 1
        assert set(free).issubset(coface)
        containing = [x for x in face_set if set(free).issubset(x)]
        assert containing == [free, coface] or set(containing) == {free, coface}, (
            n, free, coface, containing)
        face_set.remove(free)
        face_set.remove(coface)
        count += 1

    for i in range(n):
        j = (i + 1) % n
        A, B, C, D = i, j, n + i, n + j
        collapse((A, B, C), (A, B, C, D))
    for layer in range(2):
        for i in range(n):
            a = layer * n + (i - 1) % n
            b = layer * n + i
            c = layer * n + (i + 1) % n
            collapse((a, c), (a, b, c))
    for i in range(n):
        j = (i + 1) % n
        A, B, C, D = i, j, n + i, n + j
        collapse((A, B), (A, B, D))
        collapse((A, D), (A, C, D))
        collapse((B, C), (B, C, D))
    assert count == 6 * n
    assert len(face_set) == initial - 12 * n
    assert max(map(len, face_set)) == 2
    remaining_edges = sum(len(f) == 2 for f in face_set)
    assert remaining_edges == (2 * n) * (2 * n - 1) // 2 - 5 * n
    neighbors = [set() for _ in range(2*n)]
    for e in face_set:
        if len(e) == 2:
            x, y = e
            neighbors[x].add(y)
            neighbors[y].add(x)
    reached = {0}
    stack = [0]
    while stack:
        for v in neighbors[stack.pop()]:
            if v not in reached:
                reached.add(v)
                stack.append(v)
    assert len(reached) == 2*n
    return count


def direct_cut_faces(n, edges):
    """Independently build every nonempty face of the ordinary cut complex."""
    V = set(range(2 * n))
    faces = set()
    for triple in combinations(range(2 * n), 3):
        edge_count = sum(tuple(sorted(e)) in edges for e in combinations(triple, 2))
        if edge_count <= 1:
            complement = sorted(V - set(triple))
            for k in range(1, len(complement) + 1):
                faces.update(combinations(complement, k))
    return faces


def run():
    total = 0
    collapses = 0
    direct_tests = 0
    for n in range(5, 17):
        N = 2 * n
        edges, triangles, tetrahedra = graph_data(n)
        faces = (
            [(j,) for j in range(N)],
            list(combinations(range(N), 2)),
            sorted(triangles),
            sorted(tetrahedra),
        )
        count = verify_collapse(n, triangles, tetrahedra)
        collapses += count
        cut_faces = direct_cut_faces(n, edges) if n <= 8 else None
        for a, b, c in product(range(n), (0, 1), (0, 1)):
            p = vertex_permutation(n, a, b, c)
            assert len(set(p)) == N
            traces = [fixed_trace(faces[j], p) for j in range(4)]
            sign = orientation_sign(p)
            computed = sign * (1 - traces[0] + traces[1] - traces[2] + traces[3])
            assert computed == predicted(n, a, b, c), (
                n, a, b, c, computed, predicted(n, a, b, c), traces)
            if cut_faces is not None:
                direct_euler = sum(
                    (-1) ** (len(f) - 1) * orientation_sign([p[v] for v in f])
                    for f in cut_faces if {p[v] for v in f} == set(f)
                )
                assert direct_euler - 1 == computed, (
                    n, a, b, c, direct_euler - 1, computed)
                direct_tests += 1
            total += 1
        avg = sum(predicted(n, a, b, c) for a, b, c in
                  product(range(n), (0, 1), (0, 1))) // (4 * n)
        assert avg == ((n - 3) // 2 if n % 2 else 0)
        print('n={}: group={} collapse_pairs={} dual_faces={} direct_faces={} invariants={}'.format(
            n, 4 * n, count, sum(map(len, faces)),
            len(cut_faces) if cut_faces is not None else 'not_enumerated', avg))
    print('group_element_checks={}'.format(total))
    print('elementary_collapse_pairs={}'.format(collapses))
    print('direct_cut_lefschetz_checks={}'.format(direct_tests))
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
