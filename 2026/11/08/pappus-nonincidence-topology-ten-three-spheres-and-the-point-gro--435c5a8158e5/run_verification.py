"""Exact finite verification for the Pappus nonincidence neighborhood complex.

Uses only the Python standard library. All checks use integer bit masks.
Run: python run_verification.py
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

N = 18
# Explicit 18-cycle plus nine chords: the canonical Pappus graph.
EDGES = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
EDGES |= {tuple(sorted(e)) for e in [
    (0, 5), (1, 8), (2, 13), (3, 10), (4, 15),
    (6, 11), (7, 14), (9, 16), (12, 17),
]}
ADJ = [set() for _ in range(N)]
for a, b in EDGES:
    ADJ[a].add(b)
    ADJ[b].add(a)
assert len(EDGES) == 27
assert all(len(v) == 3 for v in ADJ)
assert all((a + b) % 2 == 1 for a, b in EDGES)
SIDE = (list(range(0, 18, 2)), list(range(1, 18, 2)))


def compute_faces(vertices, witnesses):
    """Two independent definitions: facet down-closure and direct witness test."""
    facets = [sum(1 << i for i, v in enumerate(vertices) if v not in ADJ[w])
              for w in witnesses]
    a = {0}
    for facet in facets:
        subset = facet
        while subset:
            a.add(subset)
            subset = (subset - 1) & facet
    b = set()
    for mask in range(1 << len(vertices)):
        if any(all((not (mask >> i & 1)) or (v not in ADJ[w])
                   for i, v in enumerate(vertices)) for w in witnesses):
            b.add(mask)
    assert a == b, "independent face definitions disagreed"
    assert len(set(facets)) == 9
    assert all(f.bit_count() == 6 for f in facets)
    return a, facets


def matching(faces, number_of_vertices, vertex_order):
    """Repeated matching by one-vertex toggles; empty face remains unmatched."""
    unused = set(faces)
    pairs = []
    for vertex in vertex_order:
        bit = 1 << vertex
        for low in sorted(unused, key=lambda x: (x.bit_count(), x)):
            high = low | bit
            if low and not (low & bit) and low in unused and high in unused:
                unused.remove(low)
                unused.remove(high)
                pairs.append((low, high))
    # Exhaustively check the reversed matched Hasse orientation is a DAG.
    matched = set(pairs)
    indegree = {face: 0 for face in faces}
    directed = defaultdict(list)
    incidences = 0
    for low in faces:
        for j in range(number_of_vertices):
            bit = 1 << j
            if low & bit:
                continue
            high = low | bit
            if high not in faces:
                continue
            incidences += 1
            source, target = (low, high) if (low, high) in matched else (high, low)
            directed[source].append(target)
            indegree[target] += 1
    queue = deque(f for f in faces if indegree[f] == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in directed[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert visited == len(faces), "Morse gradient graph contains a cycle"
    assert 2 * len(pairs) + len(unused) == len(faces)
    return Counter(x.bit_count() - 1 for x in unused), len(pairs), incidences


def f2_rank(columns):
    basis = {}
    for value in columns:
        while value:
            pivot = value.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis)


def direct_boundary_ranks(faces):
    by_dimension = {k: sorted(s for s in faces if s.bit_count() == k + 1)
                    for k in range(6)}
    ranks = []
    for k in range(1, 6):
        rows = {s: j for j, s in enumerate(by_dimension[k - 1])}
        columns = []
        for s in by_dimension[k]:
            boundary = 0
            for j in range(9):
                if s >> j & 1:
                    boundary ^= 1 << rows[s & ~(1 << j)]
            columns.append(boundary)
        ranks.append(f2_rank(columns))
    assert f2_rank([1 for _ in by_dimension[0]]) == 1
    return ranks


def cycle_type(pi):
    seen = set()
    lengths = []
    for i in range(len(pi)):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            j = pi[j]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def character(pi, faces):
    """Hopf trace: L = tr H_0 - tr H_3 = 1 - chi_3."""
    lef = 0
    for face in faces:
        if not face:
            continue
        indices = [j for j in range(9) if face >> j & 1]
        images = [pi[j] for j in indices]
        if set(indices) != set(images):
            continue
        parity = sum(images[i] > images[j]
                     for i in range(len(images)) for j in range(i + 1, len(images))) % 2
        lef += (-1) ** (len(indices) - 1 + parity)
    return 1 - lef


def check_point_group(faces):
    """All point permutations preserving the nine incidence triples."""
    point_side, line_side = SIDE
    triple_masks = {sum(1 << i for i, v in enumerate(point_side) if v in ADJ[w])
                    for w in line_side}
    assert len(triple_masks) == 9
    table = Counter()
    count = 0
    for pi in permutations(range(9)):
        mapped = {sum(1 << pi[i] for i in range(9) if triple >> i & 1)
                  for triple in triple_masks}
        if mapped != triple_masks:
            continue
        count += 1
        table[(cycle_type(pi), character(pi, faces))] += 1
    assert count == 108
    assert sum(value * multiplicity for (_, value), multiplicity in table.items()) == 0
    expected = Counter({
        ((1, 1, 1, 1, 1, 1, 1, 1, 1), 10): 1,
        ((2, 2, 2, 1, 1, 1), -2): 9,
        ((2, 2, 2, 1, 1, 1), 2): 9,
        ((2, 2, 2, 2, 1), 2): 9,
        ((3, 3, 1, 1, 1), 1): 6,
        ((3, 3, 3), -2): 12,
        ((3, 3, 3), 1): 8,
        ((6, 2, 1), -1): 18,
        ((6, 3), -1): 18,
        ((6, 3), 1): 18,
    })
    assert table == expected
    return table


def main():
    # A published model of the same nine-line Pappus configuration,
    # in a different point labelling (Abdallah--Schenck, Example 3.5).
    published = {frozenset(int(c) for c in triple) for triple in
                 ("127", "135", "148", "239", "246", "368", "459", "567", "789")}
    relabelling = (1, 2, 3, 5, 7, 9, 4, 6, 8)
    ours = {frozenset(SIDE[0].index(p) + 1 for p in ADJ[line])
            for line in SIDE[1]}
    assert {frozenset(relabelling[j - 1] for j in triple)
            for triple in ours} == published
    # An explicit incidence-preserving point/line interchange.
    duality = [1, 0, 5, 6, 7, 8, 9, 16, 17, 12, 11, 10, 3, 4, 15, 14, 13, 2]
    assert sorted(duality) == list(range(18))
    assert all(duality[a] % 2 != a % 2 for a in range(18))
    assert {tuple(sorted((duality[a], duality[b]))) for a, b in EDGES} == EDGES
    all_faces = []
    for vertices, witnesses in (SIDE, SIDE[::-1]):
        faces, facets = compute_faces(vertices, witnesses)
        all_faces.append(faces)
        face_vector = [sum(face.bit_count() == k for face in faces) for k in range(7)]
        assert face_vector == [1, 9, 36, 81, 108, 54, 9]
        assert len(faces) == 298
        ranks = direct_boundary_ranks(faces)
        betti = [9 - ranks[0] - 1]
        for dim in range(1, 5):
            betti.append(face_vector[dim+1] - ranks[dim-1] - ranks[dim])
        betti.append(face_vector[6] - ranks[4])
        assert betti == [0, 0, 0, 10, 0, 0], (ranks, betti)
        for order in (range(9), range(8, -1, -1)):
            critical, pairs, incidences = matching(faces, 9, order)
            assert critical == Counter({-1: 1, 0: 1, 3: 10})
            assert pairs == 143
            print('COMPONENT', vertices[0], 'FACES', len(faces),
                  'MORSE_PAIRS', pairs, 'HASSE_INCIDENCES', incidences,
                  'CRITICAL', dict(sorted(critical.items())))
        print('FACE_VECTOR', face_vector, 'BOUNDARY_RANKS_F2', ranks,
              'BETTI_REDUCED_F2', betti)
    table = check_point_group(all_faces[0])
    print('POINT_PRESERVING_GROUP', sum(table.values()), 'CHARACTER_TABLE', sorted(table.items()))
    print('INVARIANT_H3_DIMENSION', sum(value*n for (_,value),n in table.items())//108)
    print('PAPPUS_NONINCIDENCE_NEIGHBORHOOD_HOMOTOPY_AND_CHARACTER_VERIFIED')

if __name__ == '__main__':
    main()
