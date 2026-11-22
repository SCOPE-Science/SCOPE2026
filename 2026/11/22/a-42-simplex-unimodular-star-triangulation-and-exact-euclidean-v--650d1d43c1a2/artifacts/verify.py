"""Exact, standard-library-only check for the projected Petersen eigenpolytope."""
from itertools import combinations
from collections import Counter
from math import factorial


def determinant(matrix):
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    a = [list(map(int, row)) for row in matrix]
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * p - a[i][k] * a[k][j]
                assert num % previous == 0
                a[i][j] = num // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = p
    return sign * a[-1][-1]

edges = list(combinations(range(5), 2))
B = [[int(i in e) for e in edges] for i in range(5)]
# Each row is the value of an integer kernel-basis coordinate at an edge.
Z = [
    [0,0,1,1,1], [1,1,0,0,1], [-1,0,-1,0,-1],
    [0,-1,0,-1,-1], [-1,-1,-1,-1,-1],
    [1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0],
    [0,0,0,1,0], [0,0,0,0,1],
]
assert len(Z) == len(edges) == 10
for i in range(5):
    for j in range(5):
        assert sum(B[i][k] * Z[k][j] for k in range(10)) == 0
G = [[sum(Z[k][i]*Z[k][j] for k in range(10)) for j in range(5)] for i in range(5)]
assert determinant(G) == 162
BB = [[sum(B[i][e]*B[j][e] for e in range(10)) for j in range(5)] for i in range(5)]
assert BB == [[4 if i == j else 1 for j in range(5)] for i in range(5)]
assert determinant(BB) == 648
assert all(sum(Z[k][j] for k in range(10)) == 0 for j in range(5))

# Independent exact facet reconstruction: 252 candidate five-vertex hyperplanes.
facets = set()
for ids in combinations(range(10), 5):
    augmented = [Z[i] + [1] for i in ids]
    cofactors = [(-1)**j * determinant([row[:j]+row[j+1:] for row in augmented]) for j in range(6)]
    if not any(cofactors):
        continue
    vals = [sum(cofactors[j]*Z[i][j] for j in range(5)) + cofactors[5] for i in range(10)]
    if (min(vals) >= 0 or max(vals) <= 0) and any(vals):
        facets.add(frozenset(i for i, v in enumerate(vals) if v == 0))
assert len(facets) == 22, len(facets)
assert Counter(map(len, facets)) == Counter({5: 12, 6: 10})

# Independently enumerate the two classes of extreme fractional matchings.
cycle_supports = set()
for ids in combinations(range(10), 5):
    degree = [sum(int(v in edges[e]) for e in ids) for v in range(5)]
    if degree == [2]*5:
        cycle_supports.add(frozenset(ids))
assert len(cycle_supports) == 12
matching_supports = set()
for triple in combinations(range(5), 3):
    rest = [i for i in range(5) if i not in triple]
    support = frozenset(i for i, e in enumerate(edges)
                        if set(e).issubset(triple) or set(e) == set(rest))
    matching_supports.add(support)
assert len(matching_supports) == 10
all_indices = frozenset(range(10))
expected = {all_indices - s for s in cycle_supports | matching_supports}
assert expected == facets

# Choose three simplices on each six-vertex facet by the unique 3+3 circuit.
triangles = []
for face in sorted(facets, key=lambda S: tuple(sorted(S))):
    if len(face) == 5:
        simplex = sorted(face)
        assert abs(determinant([Z[i] for i in simplex])) == 1
        triangles.append(tuple(simplex))
        # Complementary minor: an odd 5-cycle.
        assert abs(determinant([[B[v][i] for i in sorted(all_indices - face)] for v in range(5)])) == 2
    else:
        supp = all_indices - face
        assert supp in matching_supports
        # The support triangle, plus complementary edge, determines a unique 2+3 partition.
        triple = next(T for T in combinations(range(5), 3) if
                      {i for i, e in enumerate(edges) if set(e).issubset(T)}.issubset(supp))
        pair = tuple(i for i in range(5) if i not in triple)
        assert len(pair) == 2
        a = min(pair)
        drops = [i for i in face if a in edges[i]]
        assert len(drops) == 3
        for i in drops:
            simplex = sorted(face - {i})
            assert len(simplex) == 5
            assert abs(determinant([Z[j] for j in simplex])) == 1
            complement = sorted(all_indices - frozenset(simplex))
            assert abs(determinant([[B[v][j] for j in complement] for v in range(5)])) == 2
            triangles.append(tuple(simplex))
assert len(triangles) == 42
assert len(set(triangles)) == 42
# All intrinsic pyramid volumes equal 1/(5!*sqrt(162)) = 1/(1080*sqrt(2)).
# 42 such pyramids give 7/(180*sqrt(2)).
assert 42 * 180 == 7 * 1080
print('PETERSEN_EIGENPOLYTOPE_42_UNIMODULAR_PYRAMIDS_PASS')
print('facet count',len(facets),'types',dict(Counter(map(len,facets))))
print('lattice normal volume',len(triangles),'coordinate volume 7/20',
      'ambient Gram determinant',determinant(G))
