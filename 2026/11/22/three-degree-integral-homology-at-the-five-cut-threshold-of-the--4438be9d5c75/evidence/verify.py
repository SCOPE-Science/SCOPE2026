"""Standalone integral certificate for the ordinary five-cut complex of K_3 square K_4.

Run: python3 verify.py
Uses only the Python standard library. Vertices are encoded as 4*row+column.
"""
from itertools import combinations
from collections import defaultdict, Counter, deque
from functools import lru_cache

ROWS, COLS, K = 3, 4, 5
N = ROWS * COLS
FULL = (1 << N) - 1
ORDER = (8, 7, 0, 10, 5, 1, 6, 9, 3, 2, 11, 4)


def induced_components(vertices):
    remaining = set(vertices)
    count = 0
    while remaining:
        count += 1
        stack = [remaining.pop()]
        while stack:
            v = stack.pop()
            joined = [u for u in remaining if u // COLS == v // COLS or u % COLS == v % COLS]
            remaining.difference_update(joined)
            stack.extend(joined)
    return count


def compute_complex():
    disconnected = []
    for vertices in combinations(range(N), K):
        if induced_components(vertices) > 1:
            disconnected.append(sum(1 << i for i in vertices))
    facets = [FULL ^ s for s in disconnected]
    faces = {0}
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub - 1) & facet
    return disconnected, faces


def matching(faces):
    available = set(faces) - {0}
    pairs = []
    for v in ORDER:
        bit = 1 << v
        for face in sorted(tuple(available), key=lambda x: (x.bit_count(), x)):
            cover = face | bit
            if cover != face and face in available and cover in available:
                pairs.append((face, cover))
                available.remove(face)
                available.remove(cover)
    return available, pairs


def verify_acyclicity(faces, pairs):
    vertices = set(faces) - {0}
    # Ordinary downward Hasse arrows; reverse exactly the matched arrows.
    adjacency = {v: [] for v in vertices}
    indegree = {v: 0 for v in vertices}
    pairset = set(pairs)
    for upper in vertices:
        for bit_index in range(N):
            bit = 1 << bit_index
            if not upper & bit:
                continue
            lower = upper ^ bit
            if lower not in vertices:
                continue
            if (lower, upper) in pairset:
                source, destination = lower, upper
            else:
                source, destination = upper, lower
            adjacency[source].append(destination)
            indegree[destination] += 1
    queue = deque(v for v in vertices if indegree[v] == 0)
    visited = 0
    while queue:
        v = queue.popleft()
        visited += 1
        for u in adjacency[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                queue.append(u)
    assert visited == len(vertices), 'Matching is cyclic'
    return visited


@lru_cache(maxsize=None)
def oriented_boundary(face):
    indices = [i for i in range(N) if face & (1 << i)]
    return tuple((face ^ (1 << i), -1 if j % 2 else 1)
                 for j, i in enumerate(indices))


def morse_complex(critical, pairs):
    lower_to_upper = dict(pairs)
    upper_to_lower = {b: a for a, b in pairs}
    by_dim = defaultdict(list)
    for face in sorted(critical):
        by_dim[face.bit_count() - 1].append(face)

    @lru_cache(maxsize=None)
    def reduce_same_dim(face):
        if face in critical:
            return {face: 1}
        if face in upper_to_lower:
            return {}
        upper = lower_to_upper[face]
        sign = next(s for lower, s in oriented_boundary(upper) if lower == face)
        coefficients = defaultdict(int)
        for other, incidence in oriented_boundary(upper):
            if other == face:
                continue
            for target, coeff in reduce_same_dim(other).items():
                coefficients[target] -= sign * incidence * coeff
        return {target: coeff for target, coeff in coefficients.items() if coeff}

    boundaries = {}
    for dimension in (4, 5, 6):
        domain = by_dim[dimension]
        target = by_dim[dimension - 1]
        matrix = [[0 for _ in domain] for _ in target]
        target_index = {face: j for j, face in enumerate(target)}
        for column, face in enumerate(domain):
            for facet, sign in oriented_boundary(face):
                for generator, coeff in reduce_same_dim(facet).items():
                    matrix[target_index[generator]][column] += sign * coeff
        boundaries[dimension] = matrix
    return by_dim, boundaries


def mod2_rank(columns):
    pivots = {}
    for bits in columns:
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in pivots:
                bits ^= pivots[pivot]
            else:
                pivots[pivot] = bits
                break
    return len(pivots)


def check_direct_mod2(faces):
    by_dim = {d: sorted(x for x in faces if x.bit_count() - 1 == d)
              for d in range(0, 7)}
    ranks = {}
    for d in range(1, 7):
        index = {s: i for i, s in enumerate(by_dim[d - 1])}
        columns = []
        for face in by_dim[d]:
            bits = 0
            for i in range(N):
                if face & (1 << i):
                    bits ^= 1 << index[face ^ (1 << i)]
            columns.append(bits)
        ranks[d] = mod2_rank(columns)
    assert ranks == {1: 11, 2: 55, 3: 165, 4: 327, 5: 433, 6: 228}
    betti = {d: len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d in range(1, 7)}
    assert betti == {1: 0, 2: 0, 3: 0, 4: 8, 5: 5, 6: 36}
    return ranks, betti


def main():
    disconnected, faces = compute_complex()
    assert len(disconnected) == 264
    sizes = Counter(face.bit_count() for face in faces)
    assert [sizes[j] for j in range(8)] == [1, 12, 66, 220, 492, 768, 666, 264]
    critical, pairs = matching(faces)
    assert len(pairs) == 1218
    dimensions = Counter(face.bit_count() - 1 for face in critical)
    assert dimensions == {0: 1, 4: 9, 5: 6, 6: 36}
    dag_count = verify_acyclicity(faces, pairs)
    by_dim, boundaries = morse_complex(critical, pairs)
    assert not any(any(row) for row in boundaries[4])
    assert not any(any(row) for row in boundaries[6])
    b5 = boundaries[5]
    # Exactly two identical nonzero columns and a primitive column vector.
    assert len(b5) == 9 and all(len(row) == 6 for row in b5)
    assert b5 == [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, -1, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0],
        [0, -1, 0, -1, 0, 0],
        [0, -1, 0, -1, 0, 0],
    ]
    ranks, betti = check_direct_mod2(faces)
    print('Disconnected induced five-sets:', len(disconnected))
    print('Face counts by cardinality:', [sizes[j] for j in range(8)])
    print('Acyclic matching pairs:', len(pairs), '; poset vertices:', dag_count)
    print('Critical cells by dimension:', sorted(dimensions.items()))
    print('Integral Morse boundary B5: rank 1, single Smith invariant 1')
    print('Integral Morse boundaries B4 and B6: zero')
    print('Independent mod-2 boundary ranks:', sorted(ranks.items()))
    print('Reduced integral homology: H4=Z^8; H5=Z^5; H6=Z^36; others zero')
    print('PASS')


if __name__ == '__main__':
    main()
