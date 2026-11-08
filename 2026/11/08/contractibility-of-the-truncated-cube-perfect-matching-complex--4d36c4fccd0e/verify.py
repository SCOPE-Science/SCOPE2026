"""Standalone exact check for the perfect-matching complex of the truncated cube.

Python 3 standard library only. Graph vertices are directed edges of the three-cube.
The verifier enumerates graph matchings, simplices, two acyclic Morse
matchings, and their integral degree-three-to-four Morse boundaries.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
from itertools import combinations


def graph():
    neighbors = {u: sorted(u ^ b for b in (1, 2, 4)) for u in range(8)}
    darts = [(u, v) for u in range(8) for v in neighbors[u]]
    did = {d: i for i, d in enumerate(darts)}
    edges = []
    for u in range(8):
        for v in neighbors[u]:
            if u < v:
                edges.append(tuple(sorted((did[(u, v)], did[(v, u)]))))
        for v, w in combinations(neighbors[u], 2):
            edges.append(tuple(sorted((did[(u, v)], did[(u, w)]))))
    edges.sort()
    assert len(darts) == 24 and len(edges) == len(set(edges)) == 36
    return neighbors, did, edges


def graph_perfect_matchings(edges):
    incident = [[] for _ in range(24)]
    for i, (u, v) in enumerate(edges):
        incident[u].append((v, i))
        incident[v].append((u, i))
    facets = []

    def rec(remaining, selected):
        if not remaining:
            facets.append(selected)
            return
        u = (remaining & -remaining).bit_length() - 1
        for v, e in incident[u]:
            if remaining & (1 << v):
                rec(remaining ^ (1 << u) ^ (1 << v), selected | (1 << e))

    rec((1 << 24) - 1, 0)
    return facets, incident


def parity_perfect_matchings(neighbors, did, edges):
    index = {edge: i for i, edge in enumerate(edges)}
    old_edges = sorted({(min(u, v), max(u, v)) for u in range(8)
                        for v in neighbors[u]})
    assert len(old_edges) == 12
    facets = []
    for state in range(1 << 12):
        chosen = {u: [] for u in range(8)}
        for i, (u, v) in enumerate(old_edges):
            if state & (1 << i):
                chosen[u].append(v)
                chosen[v].append(u)
        if any(len(chosen[u]) not in (1, 3) for u in range(8)):
            continue
        selected = 0
        for i, (u, v) in enumerate(old_edges):
            if state & (1 << i):
                e = tuple(sorted((did[(u, v)], did[(v, u)])))
                selected |= (1 << index[e])
        for u in range(8):
            if len(chosen[u]) == 1:
                v, w = [z for z in neighbors[u] if z not in chosen[u]]
                e = tuple(sorted((did[(u, v)], did[(u, w)])))
                selected |= (1 << index[e])
        assert selected.bit_count() == 12
        facets.append(selected)
    return facets


def simplices(facets):
    faces = {0}
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub - 1) & facet
    return faces


def pairing(nonempty, vertex_order):
    pairs = {}
    for b in vertex_order:
        bit = 1 << b
        for lower in sorted(nonempty):
            if lower & bit or lower in pairs:
                continue
            upper = lower | bit
            if upper in nonempty and upper not in pairs:
                pairs[lower] = upper
                pairs[upper] = lower
    critical = sorted(nonempty - pairs.keys())
    assert all(a in nonempty and pairs[b] == a for a, b in pairs.items())
    assert all((a ^ b).bit_count() == 1 for a, b in pairs.items())
    return pairs, critical


def check_acyclic(nonempty, pairs):
    """Independent directed-Hasse topological-sort test."""
    indegree = {x: 0 for x in nonempty}
    incidences = 0
    for upper in nonempty:
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            if lower not in nonempty:
                continue
            incidences += 1
            if pairs.get(lower) == upper:
                indegree[upper] += 1
            else:
                indegree[lower] += 1
    ready = deque(x for x, d in indegree.items() if d == 0)
    removed = 0
    while ready:
        x = ready.popleft()
        removed += 1
        if pairs.get(x, 0).bit_count() == x.bit_count() + 1:
            y = pairs[x]
            indegree[y] -= 1
            if indegree[y] == 0:
                ready.append(y)
        bits = x
        while bits:
            bit = bits & -bits
            bits -= bit
            y = x ^ bit
            if y in nonempty and pairs.get(y) != x:
                indegree[y] -= 1
                if indegree[y] == 0:
                    ready.append(y)
    assert removed == len(nonempty)
    assert all(d == 0 for d in indegree.values())
    return incidences


def boundary_matrix(pairs, critical):
    """Integral Morse boundary from oriented four-to-three gradient paths."""
    c3 = sorted(x for x in critical if x.bit_count() == 4)
    c4 = sorted(x for x in critical if x.bit_count() == 5)
    assert all(x.bit_count() in (1, 4, 5) for x in critical)
    position = {face: i for i, face in enumerate(c3)}

    @lru_cache(None)
    def project(face):
        if face in position:
            return {position[face]: 1}
        mate = pairs[face]
        if mate.bit_count() == face.bit_count() - 1:
            return {}
        assert mate.bit_count() == face.bit_count() + 1
        vertices = [i for i in range(36) if mate & (1 << i)]
        missing = next(i for i, b in enumerate(vertices)
                       if (mate ^ (1 << b)) == face)
        result = defaultdict(int)
        for j, b in enumerate(vertices):
            if j == missing:
                continue
            for k, a in project(mate ^ (1 << b)).items():
                result[k] -= ((-1) ** (j + missing)) * a
        return {k: v for k, v in result.items() if v}

    rows = []
    for face in c4:
        row = [0] * len(c3)
        for j, b in enumerate(i for i in range(36) if face & (1 << i)):
            for k, a in project(face ^ (1 << b)).items():
                row[k] += ((-1) ** j) * a
        rows.append(row)
    return rows


def determinant(matrix):
    """Exact rational elimination; final result asserted integral."""
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        q = a[j][j]
        det *= q
        for i in range(j + 1, n):
            if a[i][j]:
                t = a[i][j] / q
                for k in range(j + 1, n):
                    a[i][k] -= t * a[j][k]
                a[i][j] = Fraction(0)
    assert det.denominator == 1
    return int(det)


def ordinary_matching_polynomial_at_minus_one(incident):
    @lru_cache(None)
    def rec(remaining):
        if not remaining:
            return 1
        u = (remaining & -remaining).bit_length() - 1
        total = rec(remaining ^ (1 << u))
        for v, _ in incident[u]:
            if remaining & (1 << v):
                total -= rec(remaining ^ (1 << u) ^ (1 << v))
        return total
    return rec((1 << 24) - 1)


def main():
    neighbors, did, edges = graph()
    perfect, incident = graph_perfect_matchings(edges)
    independent = parity_perfect_matchings(neighbors, did, edges)
    assert len(perfect) == len(set(perfect)) == 32
    assert set(perfect) == set(independent)
    faces = simplices(perfect)
    nonempty = faces - {0}
    fvec = [sum(x.bit_count() == k for x in nonempty) for k in range(1, 13)]
    assert len(faces) == 118096
    assert fvec == [36, 510, 3492, 11865, 22920, 28700,
                    25176, 15828, 7040, 2112, 384, 32]
    euler = sum((-1) ** (k - 1) * count for k, count in enumerate(fvec, 1))
    assert euler == 1
    print('vertices=24 edges=36 perfect_matchings=32 odd_degree_cube_subgraphs=32')
    print('faces_including_empty=118096 f_vector=' + repr(fvec))
    print('euler_characteristic=' + str(euler))
    for label, order, expected_critical, expected_pairs in [
        ('ascending', list(range(36)), 11, 59036),
        ('descending', list(reversed(range(36))), 23, 59024),
    ]:
        pairs, critical = pairing(nonempty, order)
        shape = Counter(x.bit_count() - 1 for x in critical)
        assert len(pairs) // 2 == expected_pairs
        assert dict(shape) == {0: 1, 3: expected_critical, 4: expected_critical}
        incidences = check_acyclic(nonempty, pairs)
        assert incidences == 737700
        mat = boundary_matrix(pairs, critical)
        det = determinant(mat)
        assert abs(det) == 1
        print('%s: pairs=%d critical=%s Hasse_incidences=%d determinant=%d'
              % (label, len(pairs)//2, dict(sorted(shape.items())), incidences, det))
    signed_total = ordinary_matching_polynomial_at_minus_one(incident)
    assert signed_total == 332
    print('ordinary_matching_complex_Euler_characteristic=' + str(1 - signed_total))
    print('TRUNCATED_CUBE_PM_COMPLEX_CONTRACTIBLE_VERIFIED')

if __name__ == '__main__':
    main()
