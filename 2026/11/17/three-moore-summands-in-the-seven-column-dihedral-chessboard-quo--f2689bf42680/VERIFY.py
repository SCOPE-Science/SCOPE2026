"""Exact quotient-chain verifier for a four-row seven-column rook complex.

Usage: python3 verify.py
Only the Python standard library is needed. All incidence coefficients are
integers; no floating-point computations or precomputed input tables are used.
"""
from collections import defaultdict
from itertools import combinations, permutations
from math import gcd

ROWS, COLS = 4, 7
TRANSFORMS = [(sgn, shift) for sgn in (1, -1) for shift in range(COLS)]


def transform(face, operation):
    sign, shift = operation
    return tuple(sorted((v // COLS) * COLS +
                        (sign * (v % COLS) + shift) % COLS for v in face))


def canonical_chain(chain):
    return min(tuple(transform(face, g) for face in chain) for g in TRANSFORMS)


def build_complex():
    # Exhausts every nonempty rook placement, hence every nonempty face.
    faces = []
    for k in range(1, ROWS + 1):
        for chosen_rows in combinations(range(ROWS), k):
            for chosen_cols in permutations(range(COLS), k):
                faces.append(tuple(sorted(r * COLS + c
                                          for r, c in zip(chosen_rows, chosen_cols))))
    assert [sum(len(f) == k for f in faces) for k in range(1, 5)] == [28, 252, 840, 840]

    orbits = [set() for _ in range(ROWS)]
    # Every barycentric simplex is a strict inclusion chain whose top face
    # appears as the 'face' of one iteration. Ordered prefixes exhaust all
    # subfaces of that top face, including every possible rank pattern.
    for face in faces:
        k = len(face)
        for length in range(1, k + 1):
            for ranks in combinations(range(1, k + 1), length):
                if ranks[-1] != k:
                    continue
                for perm in permutations(face):
                    chain = tuple(tuple(sorted(perm[:r])) for r in ranks)
                    orbits[length - 1].add(canonical_chain(chain))
    orbits = [sorted(level) for level in orbits]
    assert list(map(len, orbits)) == [142, 1236, 2520, 1440]
    ids = [{simplex: i for i, simplex in enumerate(level)}
           for level in orbits]

    # Boundaries of the regular orbit-of-flags cell structure: group
    # transformations preserve face cardinalities and hence flag order.
    boundary = {}
    for dimension in range(1, 4):
        D = {}
        for j, chain in enumerate(orbits[dimension]):
            column = defaultdict(int)
            for i in range(dimension + 1):
                facet = chain[:i] + chain[i + 1:]
                row = ids[dimension - 1][canonical_chain(facet)]
                column[row] += (-1) ** i
            D[j] = {r: v for r, v in column.items() if v}
        boundary[dimension] = D
    return orbits, boundary


def check_d2(D, dimensions):
    for k in (2, 3):
        for col in D[k].values():
            result = defaultdict(int)
            for middle, value in col.items():
                for row, coefficient in D[k-1][middle].items():
                    result[row] += value * coefficient
            assert all(x == 0 for x in result.values()), 'boundary squared is nonzero'


def cancel_units(D, sizes):
    # Unit-pivot cancellation of free consecutive chain generators. Each
    # Schur complement is an integral chain isomorphism plus a contractible
    # length-two complex; this preserves all integral homology groups.
    C = {k: {j: dict(v) for j, v in D[k].items()} for k in (1, 2, 3)}
    R = {k: defaultdict(dict) for k in C}
    for k in C:
        for j, col in C[k].items():
            for i, v in col.items():
                R[k][i][j] = v
    live = {k: set(range(sizes[k])) for k in range(4)}

    def erase(k, i, j):
        old = C[k][j].pop(i, None)
        if old is not None:
            R[k][i].pop(j)
            if not R[k][i]:
                R[k].pop(i)

    def alter(k, i, j, delta):
        if delta == 0:
            return
        value = C[k][j].get(i, 0) + delta
        if value:
            C[k][j][i] = value
            R[k][i][j] = value
        else:
            erase(k, i, j)

    def find_unit(k):
        best = None
        for i, row in R[k].items():
            for j, pivot in row.items():
                if abs(pivot) == 1:
                    cost = (len(row) - 1) * (len(C[k][j]) - 1)
                    if best is None or cost < best[0]:
                        best = (cost, i, j)
                    if cost == 0:
                        return i, j
        return None if best is None else (best[1], best[2])

    counts = {1: 0, 2: 0, 3: 0}
    for k in (3, 2, 1, 3, 2, 1):
        while True:
            pair = find_unit(k)
            if pair is None:
                break
            i, j = pair
            pivot = C[k][j][i]
            assert abs(pivot) == 1
            column, row = dict(C[k][j]), dict(R[k][i])
            for l, a in row.items():
                if l != j:
                    for h, b in column.items():
                        if h != i:
                            alter(k, h, l, -pivot * a * b)
            for l in row:
                if l != j:
                    erase(k, i, l)
            for h in column:
                erase(k, h, j)
            del C[k][j]
            live[k].remove(j)
            live[k - 1].remove(i)
            if k > 1:
                for h in list(C[k - 1][i]):
                    erase(k - 1, h, i)
                del C[k - 1][i]
            if k < 3:
                for l in list(R[k + 1].get(j, {})):
                    erase(k + 1, j, l)
            counts[k] += 1
    return C, live, counts


def smith_three_by_many(C, live):
    indices = sorted(live[2])
    columns = sorted(live[3])
    assert len(indices) == 3
    A = [[C[3][j].get(i, 0) for j in columns] for i in indices]
    d1 = 0
    for row in A:
        for entry in row:
            d1 = gcd(d1, abs(entry))
    d12 = 0
    for i, j in combinations(range(3), 2):
        for a, b in combinations(range(len(columns)), 2):
            d12 = gcd(d12, abs(A[i][a] * A[j][b] - A[i][b] * A[j][a]))
    d123 = 0
    for a, b, c in combinations(range(len(columns)), 3):
        determinant = (A[0][a] * (A[1][b] * A[2][c] - A[1][c] * A[2][b])
                     - A[0][b] * (A[1][a] * A[2][c] - A[1][c] * A[2][a])
                     + A[0][c] * (A[1][a] * A[2][b] - A[1][b] * A[2][a]))
        d123 = gcd(d123, abs(determinant))
    assert d1 and d12 and d123
    return (d1, d12 // d1, d123 // d12), (d1, d12, d123), A


def run():
    orbits, boundaries = build_complex()
    sizes = list(map(len, orbits))
    check_d2(boundaries, sizes)
    C, live, counts = cancel_units(boundaries, sizes)
    check_d2(C, [len(live[k]) for k in range(4)])
    remaining = [len(live[k]) for k in range(4)]
    smith, gcd_minors, A = smith_three_by_many(C, live)
    assert remaining == [1, 0, 3, 18]
    assert counts == {1: 141, 2: 1095, 3: 1422}
    assert smith == (2, 2, 2)
    assert all(not C[1][j] for j in C[1])
    assert all(not C[2][j] for j in C[2])
    print('face_counts', [28, 252, 840, 840])
    print('orbit_chain_counts', sizes)
    print('boundary_squared_zero', True)
    print('unit_cancellations', [counts[k] for k in (1, 2, 3)])
    print('remaining_cells', remaining)
    print('gcd_minors', gcd_minors)
    print('nonzero_smith_factors', smith)
    print('integral_homology', 'H0=Z, H1=0, H2=(Z/2)^3, H3=Z^15')
    print('PASS')


if __name__ == '__main__':
    run()
