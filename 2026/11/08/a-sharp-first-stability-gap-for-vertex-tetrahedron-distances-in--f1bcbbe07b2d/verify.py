"""Exact-rational exhaustive certificate for 4-dimensional Boolean simplices.

Requires Python 3.10+ standard library only. Run: python verify.py
All subsets, face projections, and coordinate-permutation orbits are checked.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from functools import lru_cache
from collections import Counter

DIM = 4
CUBE = tuple(product((0, 1), repeat=DIM))
ORIGIN = (0,) * DIM
OTHER = CUBE[1:]


def solve(a, b):
    """Return exact rational solution of a square system or None if singular."""
    n = len(b)
    aug = [[F(a[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if aug[i][j]), None)
        if pivot is None:
            return None
        aug[j], aug[pivot] = aug[pivot], aug[j]
        row_scale = aug[j][j]
        aug[j] = [x / row_scale for x in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                multiplier = aug[i][j]
                aug[i] = [aug[i][k] - multiplier * aug[j][k]
                          for k in range(n + 1)]
    return [row[-1] for row in aug]


@lru_cache(None)
def squared_projection(face):
    """Squared distance origin-to-affine-hull if projection lies in face."""
    v = face[0]
    k = len(face) - 1
    columns = [[face[i][j] - v[j] for j in range(DIM)]
               for i in range(1, len(face))]
    if k:
        gram = [[sum(columns[i][q] * columns[j][q]
                     for q in range(DIM)) for j in range(k)] for i in range(k)]
        rhs = [-sum(columns[i][q] * v[q] for q in range(DIM)) for i in range(k)]
        coords = solve(gram, rhs)
        if coords is None:
            return None
        barycentric = [1 - sum(coords), *coords]
    else:
        barycentric = [F(1)]
    if any(weight < 0 for weight in barycentric):
        return None
    point = [sum(barycentric[i] * face[i][j]
                 for i in range(len(face))) for j in range(DIM)]
    return sum(x * x for x in point)


def full_simplex(tetrahedron):
    # The marked vertex is the origin. Four difference columns span R^4.
    gram = [[sum(tetrahedron[i][q] * tetrahedron[j][q]
                 for q in range(DIM)) for j in range(DIM)] for i in range(DIM)]
    return solve(gram, [0] * DIM) is not None


def squared_distance(tetrahedron):
    # The closest point is the projection onto the relative interior of a
    # unique smallest face. Every nonempty face is examined, exactly.
    projections = [squared_projection(face)
                   for size in range(1, DIM + 1)
                   for face in combinations(tetrahedron, size)]
    feasible = [x for x in projections if x is not None]
    assert feasible
    return min(feasible)


def coord_orbits(configurations):
    remaining = set(configurations)
    group = tuple(permutations(range(DIM)))
    orbits = []
    while remaining:
        representative = min(remaining)
        orbit = {tuple(sorted(tuple(v[perm[i]] for i in range(DIM))
                              for v in representative)) for perm in group}
        assert orbit <= remaining
        orbits.append((representative, len(orbit)))
        remaining -= orbit
    return sorted(orbits)


def format_tetrahedron(tet):
    return '(' + ', '.join(''.join(map(str, v)) for v in tet) + ')'


def main():
    histogram = Counter()
    witnesses = {F(1, 4): [], F(1, 3): []}
    total = 0
    for tetrahedron in combinations(OTHER, DIM):
        if not full_simplex(tetrahedron):
            continue
        value = squared_distance(tetrahedron)
        total += 1
        histogram[value] += 1
        if value in witnesses:
            witnesses[value].append(tetrahedron)
    assert len(list(combinations(OTHER, DIM))) == 1365
    assert total == 940
    assert histogram[F(1, 4)] == 1
    assert histogram[F(1, 3)] == 28
    assert all(value >= F(1, 3) for value in histogram if value != F(1, 4))
    assert sorted(histogram)[:3] == [F(1, 4), F(1, 3), F(2, 5)]
    mini_orbits = coord_orbits(witnesses[F(1, 4)])
    assert [size for _, size in mini_orbits] == [1]
    near_orbits = coord_orbits(witnesses[F(1, 3)])
    assert sorted(size for _, size in near_orbits) == [4, 12, 12]
    reps = {format_tetrahedron(tet): size for tet, size in near_orbits}
    assert reps == {
        '(0001, 0010, 0100, 1001)': 12,
        '(0001, 0010, 0100, 1011)': 12,
        '(0001, 0010, 0100, 1111)': 4,
    }
    assert 16 * sum(size for _, size in near_orbits) == 448
    print('PASS: 1365 fixed-origin candidates; 940 full-dimensional simplices')
    print('PASS: unique fixed-origin 1/4 minimum; next value 1/3 (28 cases)')
    print('PASS: 16 global minimizers, 448 second-level cases')
    print('PASS: three full-cube symmetry orbits, sizes 192, 192, 64')
    print('First 10 exact squared-distance shells:', sorted(histogram.items())[:10])
    for tet, size in near_orbits:
        print(format_tetrahedron(tet), 'fixed-origin orbit:', size)


if __name__ == '__main__':
    main()
