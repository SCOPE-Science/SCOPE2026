"""Exact verification of two Petersen general-position fault homotopy types.

Run with Python 3.9+ (standard library only): python verify.py
The directed face-incidence graph is checked for acyclicity, and all
integral Morse differentials are computed by signed gradient expansion.
"""

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations


VERTICES = tuple(combinations(range(5), 2))
EDGES = tuple(
    (i, j) for i, j in combinations(range(10), 2)
    if set(VERTICES[i]).isdisjoint(VERTICES[j])
)
assert len(EDGES) == 15


def complex_data(edge_fault=None, vertex_fault=None):
    retained = tuple(i for i in range(10) if i != vertex_fault)
    index = {v: i for i, v in enumerate(retained)}
    order = len(retained)
    neighbors = [set() for _ in retained]
    for u, v in EDGES:
        if (u, v) == edge_fault or u == vertex_fault or v == vertex_fault:
            continue
        a, b = index[u], index[v]
        neighbors[a].add(b)
        neighbors[b].add(a)

    distances = []
    for root in range(order):
        dist = [-1] * order
        dist[root] = 0
        queue = deque([root])
        while queue:
            a = queue.popleft()
            for b in neighbors[a]:
                if dist[b] == -1:
                    dist[b] = dist[a] + 1
                    queue.append(b)
        assert all(d >= 0 for d in dist), 'Graph must be connected'
        distances.append(dist)

    forbidden = []
    for a, b, c in combinations(range(order), 3):
        d = distances
        if (d[a][b] + d[b][c] == d[a][c]
                or d[a][c] + d[c][b] == d[a][b]
                or d[b][a] + d[a][c] == d[b][c]):
            forbidden.append((1 << a) | (1 << b) | (1 << c))
    faces = {
        face for face in range(1, 1 << order)
        if not any(face & t == t for t in forbidden)
    }
    return order, len(forbidden), faces


def facets(face, order):
    """Boundary of an oriented increasing-vertex simplex over the integers."""
    vertices = [i for i in range(order) if (face >> i) & 1]
    return tuple((face ^ (1 << i), (-1) ** j)
                 for j, i in enumerate(vertices))


def exact_morse_data(order, faces):
    """Acyclic sequential vertex-toggle matching, plus signed Morse boundary."""
    unmatched = set(faces)
    pairs = []
    for bit in range(order):
        matched_here = [
            (f, f | (1 << bit)) for f in sorted(unmatched)
            if not ((f >> bit) & 1) and f | (1 << bit) in unmatched
        ]
        for lower, upper in matched_here:
            unmatched.remove(lower)
            unmatched.remove(upper)
        pairs.extend(matched_here)
    critical = set(unmatched)
    lower_to_upper = dict(pairs)
    upper_to_lower = {b: a for a, b in pairs}
    assert len(lower_to_upper) == len(upper_to_lower) == len(pairs)
    assert set(lower_to_upper).isdisjoint(critical)
    assert set(upper_to_lower).isdisjoint(critical)

    # Full Hasse orientation: matched incidences upward, all others downward.
    indegree = {f: 0 for f in faces}
    outgoing = defaultdict(list)
    incidences = 0
    for f in faces:
        for t, _ in facets(f, order):
            if t == 0:
                continue
            assert t in faces
            if lower_to_upper.get(t) == f:
                source, target = t, f
            else:
                source, target = f, t
            outgoing[source].append(target)
            indegree[target] += 1
            incidences += 1
    ready = deque(v for v, d in indegree.items() if d == 0)
    visited = 0
    while ready:
        vertex = ready.popleft()
        visited += 1
        for target in outgoing[vertex]:
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
    assert visited == len(faces), 'Directed Hasse cycle detected'

    # Integral algebraic Morse projection, using unit incidence coefficients.
    @lru_cache(maxsize=None)
    def project(face):
        if face in critical:
            return {face: 1}
        if face in upper_to_lower:
            return {}
        upper = lower_to_upper[face]
        boundary = dict(facets(upper, order))
        incidence = boundary[face]
        assert incidence in (-1, 1)
        result = Counter()
        for other, coefficient in boundary.items():
            if other == face:
                continue
            for retained, value in project(other).items():
                result[retained] -= incidence * coefficient * value
        return {f: c for f, c in result.items() if c}

    differentials = {}
    for cell in critical:
        if cell.bit_count() == 1:
            continue
        differential = Counter()
        for face, coefficient in facets(cell, order):
            for other, value in project(face).items():
                differential[other] += coefficient * value
        differentials[cell] = {other: v for other, v in differential.items() if v}
    return Counter(f.bit_count() - 1 for f in critical), incidences, len(pairs), differentials


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                pivots[p] = x
                break
            x ^= pivots[p]
    return len(pivots)


def check_mod2_betti(order, faces):
    """Independent full-boundary check over the field of two elements."""
    by_dim = {d: sorted(f for f in faces if f.bit_count() - 1 == d)
              for d in range(order)}
    ranks = {}
    for d in range(1, order):
        rows = {f: j for j, f in enumerate(by_dim[d - 1])}
        cols = []
        for cell in by_dim[d]:
            mask = 0
            for face, _ in facets(cell, order):
                mask ^= 1 << rows[face]
            cols.append(mask)
        ranks[d] = gf2_rank(cols)
    return {
        d: len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
        for d in range(order) if by_dim[d]
    }


def check_orbits():
    images_vertex = set()
    images_edge = set()
    chosen = EDGES[0]
    for sigma in permutations(range(5)):
        perm = [VERTICES.index(tuple(sorted((sigma[a], sigma[b]))))
                for a, b in VERTICES]
        images_vertex.add(perm[0])
        images_edge.add(tuple(sorted((perm[chosen[0]], perm[chosen[1]]))))
    assert images_vertex == set(range(10))
    assert images_edge == set(EDGES)


def run():
    check_orbits()
    expected = (
        ('intact', None, None, 30, {0: 10, 1: 45, 2: 90, 3: 80, 4: 30, 5: 5},
         {0: 1, 3: 1}, 260, 860, 129, {0: 1, 3: 1}),
        ('one_edge', EDGES[0], None, 50, {0: 10, 1: 45, 2: 70, 3: 38, 4: 6},
         {0: 1, 1: 1, 2: 3}, 169, 482, 82, {0: 1, 1: 1, 2: 3}),
        ('one_vertex', None, 0, 33, {0: 9, 1: 36, 2: 51, 3: 24, 4: 3},
         {0: 1, 2: 2}, 123, 336, 60, {0: 1, 2: 2}),
    )
    for (name, edge_fault, vertex_fault, count_bad, fvector,
         expected_critical, face_total, arrows, pairs_expected, betti_expected) in expected:
        order, forbidden_count, faces = complex_data(edge_fault, vertex_fault)
        actual_f = dict(Counter(f.bit_count() - 1 for f in faces))
        critical, incidences, pairs, differentials = exact_morse_data(order, faces)
        betti = check_mod2_betti(order, faces)
        betti = {d: b for d, b in betti.items() if b}
        assert forbidden_count == count_bad, (name, forbidden_count)
        assert actual_f == fvector, (name, actual_f)
        assert len(faces) == face_total
        assert dict(critical) == expected_critical, (name, dict(critical))
        assert incidences == arrows and pairs == pairs_expected
        assert all(not diff for diff in differentials.values()), (name, differentials)
        assert betti == betti_expected, (name, betti)
        print(name, 'faces', face_total, 'forbidden_triples', count_bad,
              'pairs', pairs, 'critical', dict(sorted(critical.items())),
              'Hasse_arrows', arrows, 'integral_Morse_boundaries_zero', True,
              'GF2_Betti', dict(sorted(betti.items())))
    print('PASS: both one-fault homotopy types and transitive fault orbits')


if __name__ == '__main__':
    run()
