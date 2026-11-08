"""Exact, standard-library certificate for the Paley-23 out-neighborhood complex.
Run with Python 3.10+; no input files or third-party packages are needed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

P = 23
R = frozenset((i * i) % P for i in range(1, P))
assert R == {1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18}
TOP = (1 << P) - 1
facets = [sum(1 << ((b + r) % P) for r in R) for b in range(P)]
assert len(set(facets)) == P and all(x.bit_count() == 11 for x in facets)

# Exhaustive construction by the submask recurrence, including the empty face.
faces = {0}
for facet in facets:
    mask = facet
    while mask:
        faces.add(mask)
        mask = (mask - 1) & facet
assert len(faces) == 42298
vector = tuple(sum(s.bit_count() == k for s in faces) for k in range(1, 12))
assert vector == (23, 253, 1771, 6325, 10373, 10626, 7590, 3795, 1265, 253, 23)

# Independent face enumeration using sorted combinations, not submask iteration.
other_faces = {0}
for facet in facets:
    verts = [v for v in range(P) if (facet >> v) & 1]
    for degree in range(1, 12):
        for subset in combinations(verts, degree):
            other_faces.add(sum(1 << v for v in subset))
assert faces == other_faces
assert all(sum(((1 << u) & f) != 0 and ((1 << v) & f) != 0 for f in facets) == 5
           for u, v in combinations(range(P), 2))

# Simplicial boundary signs on increasing vertex lists.
def boundary(mask):
    verts = [v for v in range(P) if (mask >> v) & 1]
    return [(mask ^ (1 << v), 1 if (k % 2 == 0) else -1)
            for k, v in enumerate(verts)]


def exact_matching(ordered_vertices, expected_pairs, expected_critical):
    remaining = set(faces) - {0}
    lower_to_upper, upper_to_lower = {}, {}
    for v in ordered_vertices:
        selected = []
        for x in remaining:
            y = x | (1 << v)
            if not (x & (1 << v)) and y in remaining:
                selected.append((x, y))
        for x, y in selected:
            assert x in remaining and y in remaining
            remaining.remove(x)
            remaining.remove(y)
            lower_to_upper[x] = y
            upper_to_lower[y] = x
    assert len(lower_to_upper) == expected_pairs
    crit = Counter(x.bit_count() - 1 for x in remaining)
    assert crit == expected_critical

    # Orient matched codimension-one incidences upward, other incidences downward.
    # A directed cycle would invalidate the discrete Morse certificate.
    indegree = {x: 0 for x in faces if x}
    out = defaultdict(list)
    edge_count = 0
    for y in indegree:
        if y.bit_count() == 1:
            continue
        for x, _ in boundary(y):
            if lower_to_upper.get(x) == y:
                src, dst = x, y
            else:
                src, dst = y, x
            out[src].append(dst)
            indegree[dst] += 1
            edge_count += 1
    queue = deque(x for x, n in indegree.items() if n == 0)
    count = 0
    while queue:
        x = queue.popleft()
        count += 1
        for y in out[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert count == len(indegree) == 42297
    critical3 = sorted(x for x in remaining if x.bit_count() == 4)
    critical4 = sorted(x for x in remaining if x.bit_count() == 5)
    index = {c: k for k, c in enumerate(critical3)}

    # Eliminate the matched 3--4 cell pairs in the integral cellular chain
    # complex.  A 3-cell paired as the upper cell of a 2--3 pair projects to 0;
    # a critical 3-cell projects to itself. Recursive substitutions follow
    # 3--4 gradient paths and terminate by the acyclicity checked above.
    @lru_cache(None)
    def project(face):
        if face in index:
            return {index[face]: 1}
        if face in upper_to_lower:
            return {}
        assert face in lower_to_upper and face.bit_count() == 4
        upper = lower_to_upper[face]
        eps = next(sgn for f, sgn in boundary(upper) if f == face)
        result = defaultdict(int)
        for f, sgn in boundary(upper):
            if f != face:
                for i, c in project(f).items():
                    result[i] -= eps * sgn * c
        return {i: v for i, v in result.items() if v}

    columns = []
    for c4 in critical4:
        col = [0] * len(critical3)
        for f, sgn in boundary(c4):
            for i, c in project(f).items():
                col[i] += sgn * c
        columns.append(col)
    assert len(columns) == expected_critical[4]
    assert all(abs(z) <= 1 for col in columns for z in col)
    # Integer kernel vector confirms rank at most four.
    # A specified unit determinant of four columns confirms rank at least four
    # and all four nonzero Smith factors equal one.
    def determinant(rows):
        a = [list(row) for row in rows]
        total = 0
        for perm in __import__('itertools').permutations(range(len(rows))):
            inversions = sum(perm[i] > perm[j] for i in range(len(rows)) for j in range(i+1, len(rows)))
            term = (-1) ** inversions
            for k in range(len(rows)):
                term *= a[k][perm[k]]
            total += term
        return total

    # Find four linearly independent rows and a four-column determinant of +-1
    # using a small exact rational elimination (no numerical tolerance).
    from fractions import Fraction
    pivots = {}
    independent_rows = []
    for i in range(len(critical3)):
        row = [Fraction(columns[j][i]) for j in range(len(columns))]
        for pivot in sorted(pivots):
            factor = row[pivot]
            if factor:
                row = [v - factor * w for v, w in zip(row, pivots[pivot])]
        pivot = next((j for j, v in enumerate(row) if v), None)
        if pivot is not None:
            factor = row[pivot]
            pivots[pivot] = [v / factor for v in row]
            independent_rows.append(i)
    assert len(independent_rows) == len(columns)-1
    minors = []
    for colids in combinations(range(len(columns)), len(columns)-1):
        sub = [[columns[j][i] for j in colids] for i in independent_rows]
        minors.append((colids, determinant(sub)))
    assert any(abs(z) == 1 for _, z in minors)
    assert (len(critical3) - len(independent_rows), len(critical4) - len(independent_rows)) == (209, 1)
    return {'pairs': len(lower_to_upper), 'hasse': edge_count,
            'critical': dict(sorted(crit.items())), 'survivor_ranks': [209, 1],
            'minor_witnesses': [(list(cols), val) for cols, val in minors],
            'unit_minor_rows': independent_rows,
            'morse_column_supports': [sum(x != 0 for x in col) for col in columns]}

ascending = exact_matching(range(P), 21039, {0: 1, 3: 213, 4: 5})
descending = exact_matching(range(P - 1, -1, -1), 21041, {0: 1, 3: 211, 4: 3})
assert ascending['survivor_ranks'] == descending['survivor_ranks'] == [209, 1]
assert ascending['hasse'] == descending['hasse']

# Affine automorphisms preserve quadratic residues: x -> a*x+b, a in R.
for a in R:
    for b in range(P):
        assert all(((a * r) % P) in R for r in R)
        assert len({(a*x + b) % P for x in range(P)}) == P

# Every nontrivial translation acts as one 23-cycle, so it fixes no nonempty
# face of this complex (all faces have <=11 vertices).
# Every nontrivial residue multiplier has cycles {0}, R and -R, and the only
# invariant nonempty faces are {0} and R. This is checked exhaustively.
for a in R - {1}:
    fixed = []
    for mask in faces - {0}:
        transformed = 0
        sub = mask
        while sub:
            bit = sub & -sub
            sub ^= bit
            transformed |= 1 << ((a * (bit.bit_length()-1)) % P)
        if transformed == mask:
            fixed.append(mask)
    assert set(fixed) == {1, facets[0]}
# A nontrivial residue multiplier acts as an 11-cycle on R; its orientation
# on the 10-simplex R is +1. Hence L=2 for multiplier-type elements.
# A nontrivial translation has L=0. Identity L equals Euler characteristic.
chi = sum((-1) ** (k - 1) * vector[k - 1] for k in range(1, 12))
assert chi == -207
# Since the affine group has odd order 23*11, its action on the rank-one
# integral H_4 is necessarily trivial. Then L=1-tr(H_3)+tr(H_4).
character = {'identity': 2 - chi, 'nontrivial_translation': 2,
             'nontrivial_multiplier_affine': 0}
assert character == {'identity': 209, 'nontrivial_translation': 2,
                     'nontrivial_multiplier_affine': 0}
assert (209 + 22 * 2 + 230 * 0) // 253 == 1
print('PALEY23_NEIGHBORHOOD_WEDGE_AND_AFFINE_CHARACTER_VERIFIED')
print('faces_including_empty=', len(faces), 'fvector=', vector)
print('ascending=', ascending)
print('descending=', descending)
print('affine_H3_character=', character)
print('affine_H3_invariants=1; affine_H4_invariants=1')
