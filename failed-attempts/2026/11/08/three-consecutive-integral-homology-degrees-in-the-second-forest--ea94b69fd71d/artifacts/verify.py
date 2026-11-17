#!/usr/bin/env python3
"""Standalone exhaustive certificate for the level-two forest complex of K2 x K3 x K3.

The empty simplex is included. Morse boundary coefficients are integral.
Requires Python 3.9+ (standard library only).
"""
import collections
import functools
import itertools
import json
import sys

sys.setrecursionlimit(300000)
VERTICES = list(itertools.product(range(2), range(3), range(3)))
N = len(VERTICES)
COUNT = 1 << N
ADJ = [0] * N
EDGES = []
for i in range(N):
    for j in range(i + 1, N):
        if all(x != y for x, y in zip(VERTICES[i], VERTICES[j])):
            ADJ[i] |= 1 << j
            ADJ[j] |= 1 << i
            EDGES.append((i, j))
assert (N, len(EDGES)) == (18, 36)

# Incremental valid-subset enumeration: adding one vertex to a forest cannot
# create a cycle unless two of its neighbors were already connected.
valid = bytearray(COUNT)
valid[0] = 1
for s in range(1, COUNT):
    bit = s & -s
    i = bit.bit_length() - 1
    t = s ^ bit
    if not valid[t]:
        continue
    neighbors = t & ADJ[i]
    degree = neighbors.bit_count()
    if degree > 2:
        continue
    if any((t & ADJ[j]).bit_count() == 2 for j in range(N)
           if (neighbors >> j) & 1):
        continue
    if degree == 2:
        first = neighbors & -neighbors
        second = neighbors ^ first
        seen, frontier = first, first
        while frontier and not (seen & second):
            one = frontier & -frontier
            frontier ^= one
            j = one.bit_length() - 1
            fresh = ADJ[j] & t & ~seen
            seen |= fresh
            frontier |= fresh
        if seen & second:
            continue
    valid[s] = 1

# Independent exhaustive predicate: computes all selected degrees and uses a
# component-edge test for acyclicity (each connected component of a finite
# undirected graph is a tree iff it has one fewer edge than vertices).
def independently_valid(s):
    bits = [i for i in range(N) if (s >> i) & 1]
    if any((ADJ[i] & s).bit_count() > 2 for i in bits):
        return False
    seen = 0
    for i in bits:
        if (seen >> i) & 1:
            continue
        stack = [i]
        seen |= 1 << i
        component_size = 0
        twice_edges = 0
        while stack:
            j = stack.pop()
            component_size += 1
            local = ADJ[j] & s
            twice_edges += local.bit_count()
            fresh = local & ~seen
            while fresh:
                bit = fresh & -fresh
                fresh ^= bit
                seen |= bit
                stack.append(bit.bit_length() - 1)
        if twice_edges != 2 * (component_size - 1):
            return False
    return True

assert all(bool(valid[s]) == independently_valid(s) for s in range(COUNT))
faces = [s for s in range(COUNT) if valid[s]]
fvector = {str(d): c for d, c in sorted(collections.Counter(
    s.bit_count() - 1 for s in faces).items())}
assert len(faces) == 49743
facet_counts = collections.Counter(
    s.bit_count()-1 for s in faces
    if all(not valid[s | (1 << v)] for v in range(N) if ((s >> v) & 1) == 0)
)
assert dict(facet_counts) == {7: 108, 8: 1202, 9: 252}
assert sum((-1) ** (int(d)) * c for d, c in fvector.items()) == 13


# Independent direct simplicial-boundary reduction over F_2; this does not
# use the discrete-Morse projection, matching or integral matrices.
by_size = collections.defaultdict(list)
for s in faces:
    by_size[s.bit_count()].append(s)

def original_mod2_boundary_rank(k):
    row_index = {s: i for i, s in enumerate(by_size[k])}
    pivot_columns = {}
    for upper in by_size[k + 1]:
        m, col = upper, 0
        while m:
            bit = m & -m
            m ^= bit
            col ^= 1 << row_index[upper ^ bit]
        while col:
            pivot = col.bit_length() - 1
            if pivot not in pivot_columns:
                pivot_columns[pivot] = col
                break
            col ^= pivot_columns[pivot]
    return len(pivot_columns)

direct_mod2_ranks = {str(k): original_mod2_boundary_rank(k)
                     for k in (5, 6, 7, 8, 9)}
assert direct_mod2_ranks == {'5': 5216, '6': 7570,
                            '7': 6326, '8': 2360, '9': 246}


def run_matching(order):
    remaining = bytearray(valid)
    lower_to_upper = {}
    for v in order:
        bit = 1 << v
        for s in faces:
            t = s | bit
            if (s & bit) == 0 and remaining[s] and remaining[t]:
                lower_to_upper[s] = t
                remaining[s] = remaining[t] = 0
    critical = [s for s in faces if remaining[s]]
    assert len(critical) == len(faces) - 2 * len(lower_to_upper)

    # Explicit directed-Hasse test, unmatched edges down and matched up.
    # This validates the acyclic matching independently of any chain algebra.
    indegree = [0] * COUNT
    incidences = 0
    for b in faces:
        m = b
        while m:
            bit = m & -m
            m ^= bit
            a = b ^ bit
            incidences += 1
            if lower_to_upper.get(a) == b:
                indegree[b] += 1
            else:
                indegree[a] += 1
    assert incidences == 322092
    queue = collections.deque(s for s in faces if indegree[s] == 0)
    reached = 0
    while queue:
        s = queue.popleft()
        reached += 1
        m = s
        while m:
            bit = m & -m
            m ^= bit
            a = s ^ bit
            if lower_to_upper.get(a) != s:
                indegree[a] -= 1
                if indegree[a] == 0:
                    queue.append(a)
        for v in order:
            bit = 1 << v
            t = s | bit
            if (s & bit) == 0 and lower_to_upper.get(s) == t:
                indegree[t] -= 1
                if indegree[t] == 0:
                    queue.append(t)
    assert reached == len(faces), (reached, len(faces))

    by_dim = collections.defaultdict(list)
    for s in critical:
        by_dim[s.bit_count() - 1].append(s)
    critical_counts = {str(d): len(v) for d, v in sorted(by_dim.items())}
    assert critical_counts == {'6': 16, '7': 33, '8': 36, '9': 6}
    upper = set(lower_to_upper.values())
    positions = {d: {s: j for j, s in enumerate(by_dim[d])}
                 for d in by_dim}

    @functools.lru_cache(None)
    def reduce_face(s):
        """Projection of an oriented face to critical faces of the same size."""
        d = s.bit_count() - 1
        if s in upper:
            return ()
        if s not in lower_to_upper:
            return ((positions[d][s], 1),)
        b = lower_to_upper[s]
        new_vertex = (b ^ s).bit_length() - 1
        matching_sign = (-1) ** (b & ((1 << new_vertex) - 1)).bit_count()
        acc = {}
        m = b
        position = 0
        while m:
            bit = m & -m
            m ^= bit
            f = b ^ bit
            if f != s:
                incidence_sign = (-1) ** position
                for j, coefficient in reduce_face(f):
                    acc[j] = acc.get(j, 0) - matching_sign * incidence_sign * coefficient
            position += 1
        return tuple((j, w) for j, w in acc.items() if w)

    matrix_checks = {}
    for degree in (7, 8, 9):
        rows = len(by_dim[degree - 1])
        cols = len(by_dim[degree])
        mat = [[0] * cols for _ in range(rows)]
        for j, simplex in enumerate(by_dim[degree]):
            m = simplex
            position = 0
            while m:
                bit = m & -m
                m ^= bit
                face = simplex ^ bit
                for i, w in reduce_face(face):
                    mat[i][j] += ((-1) ** position) * w
                position += 1
        nonzero = sum(bool(entry) for row in mat for entry in row)
        if degree == 7:
            assert nonzero == 19
            # Every row has a private unit pivot column. The resulting square
            # minor is a signed permutation matrix and has determinant +/-1.
            chosen = []
            for row in mat:
                i = next((i for i, w in enumerate(row) if abs(w) == 1), None)
                assert i is not None
                chosen.append(i)
            assert len(set(chosen)) == rows == 16
            assert all(sum(bool(mat[k][j]) for k in range(rows)) == 1
                       for j in chosen)
            assert all(abs(mat[i][j]) == 1
                       for i, j in enumerate(chosen))
            assert all(max(map(abs, row)) <= 1 for row in mat)
            matrix_checks['7'] = {'rows': rows, 'cols': cols,
                                  'nonzero': nonzero,
                                  'unit_minor_columns': chosen,
                                  'unimodular_minor': True}
        else:
            assert nonzero == 0
            matrix_checks[str(degree)] = {'rows': rows, 'cols': cols,
                                          'nonzero': nonzero}
    return {'matched_pairs': len(lower_to_upper), 'critical_cells': critical_counts,
            'directed_hasse_incidences': incidences,
            'topological_order_vertices': reached,
            'morse_boundaries': matrix_checks,
            'projection_cache_faces': reduce_face.cache_info().currsize}

asc = run_matching(range(N))
desc = run_matching(range(N - 1, -1, -1))
assert asc['matched_pairs'] == desc['matched_pairs'] == 24826
assert asc['critical_cells'] == desc['critical_cells']
assert asc['morse_boundaries']['7']['unimodular_minor']
assert desc['morse_boundaries']['7']['unimodular_minor']
print(json.dumps({
    'verification_marker': 'TRIPLE_PRODUCT_FOREST_LEVEL_TWO_INTEGRAL_HOMOLOGY_VERIFIED',
    'graph': 'K2 categorical K3 categorical K3',
    'vertices': N,
    'edges': len(EDGES),
    'subsets_checked_twice': COUNT,
    'faces_including_empty': len(faces),
    'facets_by_dimension': dict(sorted(facet_counts.items())),
    'face_vector_by_dimension': fvector,
    'reduced_euler_characteristic': 13,
    'ascending': asc,
    'descending': desc,
    'reduced_integral_homology': {'7': 'Z^17', '8': 'Z^36', '9': 'Z^6'},
    'direct_mod2_simplicial_boundary_ranks': direct_mod2_ranks,
    'all_other_reduced_integral_homology': '0'
}, sort_keys=True, indent=2))
