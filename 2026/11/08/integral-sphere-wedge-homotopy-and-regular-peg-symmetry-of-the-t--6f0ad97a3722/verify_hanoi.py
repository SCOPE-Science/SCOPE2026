#!/usr/bin/env python3
"""Exact integral cellular and symmetry checks for a three-disk Hanoi independence complex.

Run with Python 3.10 or later; uses only the standard library.
"""
from collections import Counter, defaultdict, deque
from itertools import product, permutations

VERTICES = list(product(range(3), repeat=3))
POSITION = {word: index for index, word in enumerate(VERTICES)}


def adjacent(x, y):
    for h in range(3):
        if (x[:h] == y[:h] and x[h] != y[h]
                and all(x[t] == y[h] and y[t] == x[h] for t in range(h + 1, 3))):
            return True
    return False


EDGES = [(i, j) for i, x in enumerate(VERTICES)
         for j, y in enumerate(VERTICES) if i < j and adjacent(x, y)]
NEIGHBORS = [0] * len(VERTICES)
for a, b in EDGES:
    NEIGHBORS[a] |= 1 << b
    NEIGHBORS[b] |= 1 << a


def check_physical_hanoi_isomorphism():
    """Certify Sierpinski-swap and physical single-move graphs equivariantly coincide.

    The distance triples to the three corner vertices give a complete, canonical
    coordinate system in both 27-vertex graphs, so no graph-isomorphism library
    or reliance on geometric drawings is involved.
    """
    physical_edges = set()
    physical_neighbors = [0] * len(VERTICES)
    for i, x in enumerate(VERTICES):
        for j in range(i + 1, len(VERTICES)):
            y = VERTICES[j]
            changed = [k for k in range(3) if x[k] != y[k]]
            if len(changed) != 1:
                continue
            h = changed[0]
            if all(x[t] == y[t] and x[t] not in (x[h], y[h])
                   for t in range(h + 1, 3)):
                physical_edges.add((i, j))
                physical_neighbors[i] |= 1 << j
                physical_neighbors[j] |= 1 << i
    assert len(physical_edges) == 39

    corners = (POSITION[(0, 0, 0)], POSITION[(1, 1, 1)], POSITION[(2, 2, 2)])

    def distance_array(adjacency, source):
        lengths = [-1] * len(VERTICES)
        lengths[source] = 0
        todo = deque([source])
        while todo:
            v = todo.popleft()
            remaining = adjacency[v]
            while remaining:
                bit = remaining & -remaining
                remaining -= bit
                w = bit.bit_length() - 1
                if lengths[w] == -1:
                    lengths[w] = lengths[v] + 1
                    todo.append(w)
        assert all(d >= 0 for d in lengths)
        return lengths

    triple_sets = []
    for adjacency in (NEIGHBORS, physical_neighbors):
        distances = [distance_array(adjacency, c) for c in corners]
        keys = {tuple(length[v] for length in distances): v
                for v in range(len(VERTICES))}
        assert len(keys) == 27  # injectivity; all 27 vertices indexed
        triple_sets.append(keys)
    assert set(triple_sets[0]) == set(triple_sets[1])
    mapping = [0] * len(VERTICES)
    for fingerprint, source in triple_sets[0].items():
        mapping[source] = triple_sets[1][fingerprint]
    assert all(mapping[c] == c for c in corners)
    for u, v in EDGES:
        a, b = sorted((mapping[u], mapping[v]))
        assert (a, b) in physical_edges
    # Each peg relabeling commutes with the distance-coordinate isomorphism.
    for p in permutations(range(3)):
        act = [POSITION[tuple(p[d] for d in word)] for word in VERTICES]
        for v in range(27):
            assert mapping[act[v]] == act[mapping[v]]
    print('PHYSICAL_HANOI_EQUIVARIANT_ISOMORPHISM_PASS',len(physical_edges),len(mapping))


def independent_faces():
    out = []

    def search(mask, candidates):
        out.append(mask)
        while candidates:
            bit = candidates & -candidates
            candidates -= bit
            i = bit.bit_length() - 1
            search(mask | bit, candidates & ~NEIGHBORS[i])

    search(0, (1 << len(VERTICES)) - 1)
    return out


def faces_with_sign(upper):
    index = 0
    while upper:
        bit = upper & -upper
        yield bit, 1 if index % 2 == 0 else -1
        upper -= bit
        index += 1


def matching(nonempty_faces):
    remaining = set(nonempty_faces)
    lower_upper, upper_lower = {}, {}
    for i in range(len(VERTICES)):
        bit = 1 << i
        for lower in list(remaining):
            upper = lower | bit
            if not lower & bit and upper in remaining:
                lower_upper[lower] = upper
                upper_lower[upper] = lower
                remaining.remove(lower)
                remaining.remove(upper)
    return remaining, lower_upper, upper_lower


def check_acyclic(faces, lower_upper):
    indegree = {face: 0 for face in faces}
    directed = defaultdict(list)
    covers = 0
    for upper in faces:
        if upper == 0:
            continue
        for bit, _ in faces_with_sign(upper):
            lower = upper ^ bit
            if lower == 0:
                continue  # ordinary (not augmented) CW chain complex
            covers += 1
            if lower_upper.get(lower) == upper:
                directed[lower].append(upper)
                indegree[upper] += 1
            else:
                directed[upper].append(lower)
                indegree[lower] += 1
    ready = deque(face for face in faces if indegree[face] == 0)
    processed = 0
    while ready:
        face = ready.popleft()
        processed += 1
        for target in directed[face]:
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
    assert processed == len(faces), (processed, len(faces))
    return covers


def projection(critical, lower_upper, upper_lower, size):
    basis = sorted(face for face in critical if face.bit_count() == size)
    lookup = {face: i for i, face in enumerate(basis)}
    memo, active = {}, set()

    def project(face):
        if face in memo:
            return memo[face]
        assert face not in active, 'closed gradient path'
        output = [0] * len(basis)
        if face in lookup:
            output[lookup[face]] = 1
        elif face in upper_lower:
            pass
        else:
            assert face in lower_upper
            active.add(face)
            upper = lower_upper[face]
            inserted = upper ^ face
            inserted_position = (upper & (inserted - 1)).bit_count()
            lower_coeff = 1 if inserted_position % 2 == 0 else -1
            for bit, sign in faces_with_sign(upper):
                other = upper ^ bit
                if other == face:
                    continue
                factor = -sign * lower_coeff
                term = project(other)
                for i, coefficient in enumerate(term):
                    output[i] += factor * coefficient
            active.remove(face)
        memo[face] = tuple(output)
        return memo[face]

    return basis, project


def boundary(chain):
    result = defaultdict(int)
    for face, coefficient in chain.items():
        for bit, sign in faces_with_sign(face):
            result[face ^ bit] += coefficient * sign
    return {face: coefficient for face, coefficient in result.items() if coefficient}


def matched_lower_order(lower_upper, size):
    lows = [face for face in lower_upper if face.bit_count() == size]
    subset = set(lows)
    degree = {face: 0 for face in lows}
    dependencies = defaultdict(list)
    for face in lows:
        upper = lower_upper[face]
        for bit, _ in faces_with_sign(upper):
            next_face = upper ^ bit
            if next_face != face and next_face in subset:
                dependencies[face].append(next_face)
                degree[next_face] += 1
    ready = deque(face for face in lows if degree[face] == 0)
    ordered = []
    while ready:
        face = ready.popleft()
        ordered.append(face)
        for nxt in dependencies[face]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                ready.append(nxt)
    assert len(ordered) == len(lows)
    return ordered


def lift_cycle(critical_face, order, lower_upper):
    chain = {critical_face: 1}
    residual = boundary(chain)
    for lower in order:
        coeff = residual.get(lower, 0)
        if not coeff:
            continue
        upper = lower_upper[lower]
        inserted = upper ^ lower
        position = (upper & (inserted - 1)).bit_count()
        lower_sign = 1 if position % 2 == 0 else -1
        correction = -coeff * lower_sign
        chain[upper] = chain.get(upper, 0) + correction
        for bit, sign in faces_with_sign(upper):
            target = upper ^ bit
            residual[target] = residual.get(target, 0) + correction * sign
            if residual[target] == 0:
                del residual[target]
    assert residual == {}, 'cycle has a nonzero boundary'
    assert boundary(chain) == {}, 'independently reconstructed cycle boundary nonzero'
    return {face: coefficient for face, coefficient in chain.items() if coefficient}


def relabel_face(face, coordinate_permutation):
    result = 0
    while face:
        bit = face & -face
        face -= bit
        index = bit.bit_length() - 1
        result |= 1 << coordinate_permutation[index]
    return result


def orientation_sign(face, coordinate_permutation):
    permuted_vertices = []
    while face:
        bit = face & -face
        face -= bit
        permuted_vertices.append(coordinate_permutation[bit.bit_length() - 1])
    parity = sum(a > b for i, a in enumerate(permuted_vertices)
                 for b in permuted_vertices[i + 1:]) % 2
    return -1 if parity else 1


def det_integer(a):
    # Fraction-free Bareiss determinant.
    a = [row[:] for row in a]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign, pivot_prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            nonzero = next((j for j in range(k + 1, n) if a[j][k]), None)
            if nonzero is None:
                return 0
            a[k], a[nonzero] = a[nonzero], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % pivot_prev == 0
                a[i][j] = numerator // pivot_prev
            a[i][k] = 0
        pivot_prev = pivot
    return sign * a[n - 1][n - 1]


def main():
    check_physical_hanoi_isomorphism()
    all_faces = independent_faces()
    counts = Counter(face.bit_count() for face in all_faces)
    assert len(VERTICES) == 27 and len(EDGES) == 39
    assert counts == {0: 1, 1: 27, 2: 312, 3: 2016, 4: 7983,
                      5: 19953, 6: 31211, 7: 29151, 8: 14565, 9: 2925}
    nonempty = [face for face in all_faces if face]
    critical, lower_upper, upper_lower = matching(nonempty)
    assert len(lower_upper) == len(upper_lower) == 54065
    assert Counter(face.bit_count() - 1 for face in critical) == {0: 1, 6: 6, 7: 6}
    covers = check_acyclic(nonempty, lower_upper)
    assert covers == 672537  # 27 singleton-to-empty incidences excluded
    print('FACES_AND_MORSE_PASS', len(nonempty), covers, len(lower_upper))

    basis6, project6 = projection(critical, lower_upper, upper_lower, 7)
    basis7, project7 = projection(critical, lower_upper, upper_lower, 8)
    # Full integral Morse boundary from critical 7-cells to critical 6-cells.
    coefficients = []
    for face in basis7:
        vector = [0] * len(basis6)
        for bit, sign in faces_with_sign(face):
            for i, value in enumerate(project6(face ^ bit)):
                vector[i] += sign * value
        coefficients.append(vector)
    assert all(value == 0 for row in coefficients for value in row)
    print('INTEGRAL_MORSE_BOUNDARY_PASS', len(basis6), len(basis7))

    group_actions = []
    for peg_permutation in permutations(range(3)):
        action = [POSITION[tuple(peg_permutation[j] for j in word)] for word in VERTICES]
        for a, b in EDGES:
            assert tuple(sorted((action[a], action[b]))) in EDGESET
        group_actions.append((peg_permutation, action))

    for size, basis, projector, representative in [
        (7, basis6, project6, 18911508),
        (8, basis7, project7, 72370452),
    ]:
        assert representative in basis
        order = matched_lower_order(lower_upper, size - 1)
        cycle = lift_cycle(representative, order, lower_upper)
        orbit = []
        for peg_permutation, action in group_actions:
            result = [0] * len(basis)
            for face, coefficient in cycle.items():
                image = relabel_face(face, action)
                coeff = coefficient * orientation_sign(face, action)
                for i, x in enumerate(projector(image)):
                    result[i] += coeff * x
            orbit.append(result)
        det = det_integer(orbit)
        assert abs(det) == 1, (size, det)
        print('INTEGRAL_REGULAR_ORBIT_PASS', 'degree', size - 1,
              'generator', representative, 'cycle_terms', len(cycle), 'det', det)

    for peg_permutation, action in group_actions:
        trace = 0
        for face in nonempty:
            if relabel_face(face, action) == face:
                trace += (-1) ** (face.bit_count() - 1) * orientation_sign(face, action)
        assert trace == 1, (peg_permutation, trace)
    print('SIGNED_LEFSCHETZ_PASS', len(group_actions))
    print('HANOI_INTEGRAL_HOMOTOPY_AND_REGULAR_MODULES_PASS')


EDGESET = set(EDGES)
if __name__ == '__main__':
    main()
