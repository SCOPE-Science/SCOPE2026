"""Exact integral chain verification for the multipath complex of the bidirected 3-cube.

Run with Python 3.10+ (standard library only). No precomputed matrix is trusted.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

V = range(8)
ARCS = [(a, b) for a in V for b in V if (a ^ b).bit_count() == 1]
assert len(ARCS) == 24


def is_multipath_indices(indices):
    successor = [-1] * 8
    incoming = [-1] * 8
    for j in indices:
        a, b = ARCS[j]
        if successor[a] != -1 or incoming[b] != -1:
            return False
        successor[a] = b
        incoming[b] = a
    for start in V:
        seen = set()
        cur = start
        while cur != -1:
            if cur in seen:
                return False
            seen.add(cur)
            cur = successor[cur]
    return True


def faces_by_successor_recursion():
    faces = []
    successor = [-1] * 8

    def recurse(j, used_out, used_in, mask):
        if j == len(ARCS):
            faces.append(mask)
            return
        recurse(j + 1, used_out, used_in, mask)
        a, b = ARCS[j]
        if (used_out >> a) & 1 or (used_in >> b) & 1:
            return
        cur = b
        while cur != -1:
            if cur == a:
                return
            cur = successor[cur]
        assert successor[a] == -1
        successor[a] = b
        recurse(j + 1, used_out | (1 << a), used_in | (1 << b), mask | (1 << j))
        successor[a] = -1

    recurse(0, 0, 0, 0)
    return set(faces)


def faces_by_independent_combinations():
    faces = set()
    for k in range(8):
        for indices in combinations(range(24), k):
            if is_multipath_indices(indices):
                faces.add(sum(1 << j for j in indices))
    return faces


def greedy_matching(faces, order):
    free = set(faces)
    pairs = []
    for j in order:
        for low in list(free):
            upper = low | (1 << j)
            if not (low & (1 << j)) and upper in free:
                free.remove(low)
                free.remove(upper)
                pairs.append((low, upper))
    return pairs, free


def confirm_acyclic_matching(faces, pairs):
    matched = set(pairs)
    indegree = {s: 0 for s in faces}
    adjacency = {s: [] for s in faces}
    incidence_count = 0
    for upper in faces:
        remains = upper
        while remains:
            bit = remains & -remains
            remains -= bit
            low = upper ^ bit
            incidence_count += 1
            if (low, upper) in matched:
                adjacency[low].append(upper)
                indegree[upper] += 1
            else:
                adjacency[upper].append(low)
                indegree[low] += 1
    q = deque(s for s in faces if indegree[s] == 0)
    reached = 0
    while q:
        x = q.popleft()
        reached += 1
        for y in adjacency[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert reached == len(faces), (reached, len(faces))
    return incidence_count


def integral_morse_boundary(faces, pairs):
    columns = {}
    parents = defaultdict(set)
    for simplex in faces:
        boundary = {}
        k = 0
        bits = simplex
        while bits:
            bit = bits & -bits
            bits -= bit
            low = simplex ^ bit
            boundary[low] = (-1) ** k
            parents[low].add(simplex)
            k += 1
        columns[simplex] = boundary

    for lower, upper in pairs:
        pivot = columns[upper].get(lower, 0)
        assert abs(pivot) == 1, (lower, upper, pivot)
        upper_boundary = columns[upper]
        for other in tuple(parents[lower]):
            if other == upper:
                continue
            boundary = columns[other]
            scalar = boundary[lower] // pivot
            for row, value in upper_boundary.items():
                new_value = boundary.get(row, 0) - scalar * value
                if new_value:
                    boundary[row] = new_value
                    parents[row].add(other)
                else:
                    boundary.pop(row, None)
                    parents[row].discard(other)
        for row in tuple(upper_boundary):
            parents[row].discard(upper)
        for coface in tuple(parents[upper]):
            columns[coface].pop(upper, None)
        parents.pop(upper, None)
        del columns[upper]
        for row in tuple(columns[lower]):
            parents[row].discard(lower)
        del columns[lower]
        parents.pop(lower, None)

    for s, boundary in columns.items():
        squared = defaultdict(int)
        for row, coeff in boundary.items():
            assert row in columns
            assert row.bit_count() == s.bit_count() - 1
            for target, value in columns[row].items():
                squared[target] += coeff * value
        assert all(value == 0 for value in squared.values()), ('d^2 nonzero', s)
    return columns


def unit_diagonalization(array):
    """Elementary unimodular elimination. Reject if nonzero residual lacks a unit."""
    if not array:
        return 0
    M = [list(row) for row in array]
    rows, cols = len(M), len(M[0])
    pivot_no = 0
    while pivot_no < min(rows, cols):
        chosen = next(((i, j) for i in range(pivot_no, rows)
                       for j in range(pivot_no, cols) if abs(M[i][j]) == 1), None)
        if chosen is None:
            assert all(M[i][j] == 0 for i in range(pivot_no, rows)
                       for j in range(pivot_no, cols)), 'unresolved nonunit invariant'
            break
        i, j = chosen
        M[pivot_no], M[i] = M[i], M[pivot_no]
        for row in M:
            row[pivot_no], row[j] = row[j], row[pivot_no]
        pivot = M[pivot_no][pivot_no]
        assert abs(pivot) == 1
        for i in range(pivot_no + 1, rows):
            factor = M[i][pivot_no] // pivot
            if factor:
                for k in range(pivot_no, cols):
                    M[i][k] -= factor * M[pivot_no][k]
        for j in range(pivot_no + 1, cols):
            factor = M[pivot_no][j] // pivot
            if factor:
                for i in range(pivot_no, rows):
                    M[i][j] -= factor * M[i][pivot_no]
        assert all(M[i][pivot_no] == 0 for i in range(pivot_no + 1, rows))
        assert all(M[pivot_no][j] == 0 for j in range(pivot_no + 1, cols))
        pivot_no += 1
    return pivot_no


def verify_integral_morse(faces, pairs):
    remaining = integral_morse_boundary(faces, pairs)
    dimensions = Counter(s.bit_count() - 1 for s in remaining)
    ranks = {}
    for k in sorted(dimensions):
        lows = sorted(s for s in remaining if s.bit_count() - 1 == k - 1)
        highs = sorted(s for s in remaining if s.bit_count() - 1 == k)
        loc = {s: j for j, s in enumerate(lows)}
        matrix = [[0] * len(highs) for _ in lows]
        for j, simplex in enumerate(highs):
            for row, coeff in remaining[simplex].items():
                matrix[loc[row]][j] = coeff
        ranks[k] = unit_diagonalization(matrix)
    betti = {k: dimensions[k] - ranks[k] - ranks.get(k + 1, 0)
             for k in dimensions}
    assert all(b >= 0 for b in betti.values())
    return dimensions, ranks, betti


def direct_field_ranks(faces, prime):
    """Separate original simplicial-chain computation, without discrete Morse."""
    degree_faces = {k: sorted(s for s in faces if s.bit_count() - 1 == k)
                    for k in range(-1, 7)}
    rank = {}
    for k in range(0, 7):
        bases = {}
        labels = {s: i for i, s in enumerate(degree_faces[k - 1])}
        for simplex in degree_faces[k]:
            v = {}
            bits = simplex
            sign = 1
            while bits:
                bit = bits & -bits
                bits -= bit
                index = labels[simplex ^ bit]
                v[index] = (v.get(index, 0) + sign) % prime
                sign = -sign
            v = {a: b for a, b in v.items() if b}
            while v:
                idx = max(v)
                if idx not in bases:
                    inverse = pow(v[idx], -1, prime)
                    bases[idx] = {r: (c * inverse) % prime for r, c in v.items()}
                    break
                mult = v[idx]
                for r, c in bases[idx].items():
                    new = (v.get(r, 0) - mult * c) % prime
                    if new:
                        v[r] = new
                    else:
                        v.pop(r, None)
        rank[k] = len(bases)
    return rank


def main():
    faces = faces_by_successor_recursion()
    independent = faces_by_independent_combinations()
    assert faces == independent
    f = {k: sum(s.bit_count() - 1 == k for s in faces) for k in range(-1, 7)}
    assert [f[k] for k in range(-1, 7)] == [1, 24, 216, 928, 2016, 2160, 1008, 144]
    print('arcs=24 vertices=8 faces_total=6497')
    print('face_counts_minus1_to_6=' + ','.join(map(str, (f[k] for k in range(-1, 7)))))
    facets = [s for s in faces if not any((s | (1 << j)) in faces
                                               for j in range(24) if not (s >> j) & 1)]
    facet_profile = Counter(s.bit_count() - 1 for s in facets)
    assert facet_profile == {3: 6, 4: 48, 5: 336, 6: 144}
    print('facets_total=534 facet_dimensions=3:6,4:48,5:336,6:144')
    cycles = sum(all((path[i] ^ path[(i + 1) % 8]).bit_count() == 1
                     for i in range(8))
                 for p in permutations(range(1, 8))
                 for path in [(0,) + p])
    assert cycles == 12
    print('directed_Hamiltonian_cycles=12')
    expected_betti = {3: 6, 4: 45, 5: 36, 6: 12}
    for label, order in [('forward', range(24)), ('reverse', range(23, -1, -1))]:
        pairs, critical = greedy_matching(faces, order)
        incidences = confirm_acyclic_matching(faces, pairs)
        dims, ranks, betti = verify_integral_morse(faces, pairs)
        assert len(pairs) == 3193
        assert incidences == 29160
        assert len(critical) == 111
        assert dims == {3: 8, 4: 51, 5: 40, 6: 12}
        assert ranks == {3: 0, 4: 2, 5: 4, 6: 0}
        assert betti == expected_betti
        print(f'{label}: pairs=3193 critical_dims=3:8,4:51,5:40,6:12 incidences=29160')
        print(f'{label}: unit_smith_ranks=4:2,5:4; all_other_boundaries_zero')
    for prime in (2, 3):
        ranks = direct_field_ranks(faces, prime)
        assert ranks == {0: 1, 1: 23, 2: 193, 3: 735, 4: 1275, 5: 840, 6: 132}, (prime, ranks)
        print(f'direct_F{prime}_ranks=0:1,1:23,2:193,3:735,4:1275,5:840,6:132')
    print('INTEGRAL_CUBE_MULTIPATH_HOMOLOGY_VERIFIED')

if __name__ == '__main__':
    main()
