"""Finite exact homotopy and reflection-character certificate for a 3-by-4 grid.

No external dependencies; run with Python 3.10+.
"""
from collections import Counter, deque
from itertools import combinations

ROWS, COLS, N = 3, 4, 12
FULL = (1 << N) - 1


def neighbors(v):
    r, c = divmod(v, COLS)
    return {rr * COLS + cc for rr, cc in
            ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            if 0 <= rr < ROWS and 0 <= cc < COLS}


ADJ = [neighbors(v) for v in range(N)]


def independent_vertices(indices):
    return all(j not in ADJ[i] for i, j in combinations(indices, 2))


OBSTRUCTIONS = tuple(sum(1 << v for v in indices)
                     for indices in combinations(range(N), 4)
                     if independent_vertices(indices))


def complex_pair():
    # Membership in the robust complex means that no independent quartet is contained.
    K = {x for x in range(1, FULL + 1)
         if all((x & obstruction) != obstruction for obstruction in OBSTRUCTIONS)}
    # The Alexander dual is the union of simplices complementary to independent quartets.
    T = {x for x in range(1, FULL)
         if any((x & obstruction) == 0 for obstruction in OBSTRUCTIONS)}
    # Independent computation of dual membership via K (empty face belongs to K).
    assert T == {x for x in range(1, FULL) if FULL ^ x not in K}
    return K, T


def morse_certificate(faces, dimension, count):
    # First-available vertex-toggle matching, in vertex order 0,...,11.
    unmatched = set(faces)
    pairs = []
    for v in range(N):
        b = 1 << v
        for lo in sorted(unmatched):
            hi = lo | b
            if not (lo & b) and lo in unmatched and hi in unmatched:
                unmatched.remove(lo)
                unmatched.remove(hi)
                pairs.append((lo, hi))
    crit = Counter(face.bit_count() - 1 for face in unmatched)
    assert crit == {0: 1, dimension: count}, crit
    assert 2 * len(pairs) + len(unmatched) == len(faces)

    # Exhaustive acyclicity: for every codimension-one face incidence,
    # orient downwards except that matched incidences are reversed.
    pair_set = set(pairs)
    outgoing = {f: [] for f in faces}
    indegree = {f: 0 for f in faces}
    directed_edges = 0
    for high in faces:
        for v in range(N):
            if not (high >> v & 1):
                continue
            low = high ^ (1 << v)
            if not low:
                continue
            assert low in faces
            src, dst = (low, high) if (low, high) in pair_set else (high, low)
            outgoing[src].append(dst)
            indegree[dst] += 1
            directed_edges += 1
    queue = deque(f for f in faces if indegree[f] == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for w in outgoing[u]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    assert visited == len(faces), ('closed gradient path', visited, len(faces))
    return len(pairs), directed_edges, crit


def permutation(vertical, horizontal):
    out = []
    for i in range(N):
        row, col = divmod(i, COLS)
        if vertical:
            row = ROWS - 1 - row
        if horizontal:
            col = COLS - 1 - col
        out.append(row * COLS + col)
    assert len(set(out)) == N
    return out


def permutation_sign(image):
    inversions = sum(image[i] > image[j]
                     for i in range(len(image))
                     for j in range(i + 1, len(image)))
    return -1 if inversions % 2 else 1


def homology_trace_from_simplices(faces, homology_degree, vertical, horizontal):
    p = permutation(vertical, horizontal)
    # Reduced chain Lefschetz number: empty face contributes -1.
    reduced_lefschetz = -1
    for mask in faces:
        vertices = [v for v in range(N) if mask >> v & 1]
        images = [p[v] for v in vertices]
        if set(images) == set(vertices):
            reduced_lefschetz += ((-1) ** (len(vertices) - 1)
                                   * permutation_sign(images))
    return (-1) ** homology_degree * reduced_lefschetz


def fixed_square_triples(vertical, horizontal):
    # Six unit squares, arranged in two rows and three columns.
    mapping = {}
    for r in range(2):
        for c in range(3):
            rr = 1 - r if vertical else r
            cc = 2 - c if horizontal else c
            mapping[r * 3 + c] = rr * 3 + cc
    return sum({mapping[v] for v in triple} == set(triple)
               for triple in combinations(range(6), 3))


def main():
    K, T = complex_pair()
    assert len(K) == 1415 and len(T) == 2679
    print('INDEPENDENT_QUARTETS', len(OBSTRUCTIONS))
    for label, complex_faces, degree in [('ROBUST', K, 5), ('TOTAL_CUT', T, 4)]:
        f_vector = tuple(sum(face.bit_count() == j + 1 for face in complex_faces)
                         for j in range(8 if label == 'TOTAL_CUT' else 6))
        pairs, incidences, crit = morse_certificate(complex_faces, degree, 20)
        assert sum((-1)**j * count for j, count in enumerate(f_vector)) == 1 + (-1)**degree * 20
        print(label, 'f_vector', f_vector, 'pairs', pairs,
              'cover_relations', incidences, 'critical', dict(crit), 'acyclic', True)
        traces = []
        for vertical, horizontal in ((False, False), (True, False), (False, True), (True, True)):
            t = homology_trace_from_simplices(complex_faces, degree, vertical, horizontal)
            traces.append(t)
        assert traces == [20, 0, -4, 0], (label, traces)
        print(label, 'V4_character', tuple(traces))
    # A character comparison proves an isomorphism over Q: sign on horizontal
    # reflection, times the permutation module on triples of the six squares.
    model = [( (-1 if horizontal else 1) * fixed_square_triples(vertical, horizontal))
             for vertical, horizontal in ((False, False), (True, False), (False, True), (True, True))]
    assert model == [20, 0, -4, 0]
    mult = {(a, b): (20 - 4 * b)//4 for a in (-1, 1) for b in (-1, 1)}
    assert mult == {(-1, -1): 6, (-1, 1): 4, (1, -1): 6, (1, 1): 4}
    print('SQUARE_TRIPLES_TWISTED_CHARACTER', tuple(model), 'multiplicities', mult)
    print('ROBUST_3x4_EXACT_HOMOTOPY_AND_SYMMETRY_OK')


if __name__ == '__main__':
    main()
