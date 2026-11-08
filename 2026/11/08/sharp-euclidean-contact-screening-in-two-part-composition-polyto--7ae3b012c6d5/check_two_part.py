"""Exact, standalone checks of the two-block composition-polytope circumball formulas.

No nonstandard modules are needed.  The theorem is proved in the accompanying
mathematical text; finite checks are independent corroboration, not its proof.
"""
from fractions import Fraction as F
from itertools import combinations


def vertices(p, q):
    n = p + q
    z = (0,) * n
    result = {z}
    for i in range(p):
        v = [0] * n
        v[i] = p
        result.add(tuple(v))
    for j in range(q):
        v = [0] * n
        v[p + j] = n
        result.add(tuple(v))
    for i in range(p):
        for j in range(q):
            v = [0] * n
            v[i], v[p + j] = p, q
            result.add(tuple(v))
    return result


def solve_linear(rows, rhs):
    n = len(rhs)
    mat = [[F(z) for z in row] + [F(v)] for row, v in zip(rows, rhs)]
    for col in range(n):
        pivot = next((k for k in range(col, n) if mat[k][col] != 0), None)
        if pivot is None:
            return None
        mat[col], mat[pivot] = mat[pivot], mat[col]
        r = mat[col][col]
        mat[col] = [x / r for x in mat[col]]
        for k in range(n):
            if k != col:
                r = mat[k][col]
                mat[k] = [mat[k][j] - r * mat[col][j] for j in range(n + 1)]
    return tuple(row[-1] for row in mat)


def halfspace_vertices(p, q):
    n = p + q
    rows = []
    limits = []
    for i in range(n):
        row = [0] * n
        row[i] = -1
        rows.append(row)
        limits.append(0)
    rows.append([1] * p + [0] * q)
    limits.append(p)
    rows.append([1] * n)
    limits.append(n)
    got = set()
    for inds in combinations(range(n + 2), n):
        v = solve_linear([rows[i] for i in inds], [limits[i] for i in inds])
        if v is not None and all(sum(a * b for a, b in zip(row, v)) <= lim
                                 for row, lim in zip(rows, limits)):
            got.add(v)
    return got


def formula(p, q):
    n = p + q
    K = p * p + 3 * p * q + q * q
    Fdiscr = (q - 2) * n * n - q * p * p
    a = max(F(0), F(-Fdiscr, 2 * K))
    b = F(n, q) * (1 - a)
    rr = F(n * n * (q - 1), q) + F(K, q) * a * a
    return a, b, rr, Fdiscr


def run():
    assertions = 0
    checked_vertices = 0
    phase_counts = {'two_orbit': 0, 'terminal_only': 0}
    # Recover vertices without relying on a precomputed list: independent H-systems.
    for p in range(1, 7):
        for q in range(1, 7):
            if p + q > 8:
                continue
            vs = halfspace_vertices(p, q)
            assert vs == vertices(p, q), (p, q, vs ^ vertices(p, q))
            assertions += 1
    # Confirm exact rational squared distances, all claimed contacts,
    # and the convex-hull barycentric minimum-radius certificate.
    for p in range(1, 81):
        for q in range(1, 81):
            n = p + q
            a, b, rr, discr = formula(p, q)
            assert discr != 0
            assertions += 1
            assert 0 <= a < 1 and b > 0
            assertions += 1
            center_sq = p * a * a + q * b * b
            d0 = center_sq
            da = center_sq + p * p - 2 * p * a
            db = center_sq + n * n - 2 * n * b
            dc = center_sq + p * p + q * q - 2 * p * a - 2 * q * b
            assert db == rr and max(d0, da, db, dc) == rr
            assertions += 1
            assert dc < rr and (d0 == rr) == (p == q == 1)
            assertions += 1
            assert (da == rr) == (discr < 0)
            assertions += 1
            if discr < 0:
                assert 0 < a < 1
                # Uniform mixture of A_i with total mass a and B_j with mass 1-a.
                assert (a, b) == (a * F(p, p), (1 - a) * F(n, q))
                phase_counts['two_orbit'] += 1
            else:
                assert a == 0 and q >= 3 and da < rr
                phase_counts['terminal_only'] += 1
            assertions += 1
            if n <= 12:
                center = (a,) * p + (b,) * q
                observed = set()
                for x in vertices(p, q):
                    dsq = sum((F(z) - c) ** 2 for z, c in zip(x, center))
                    assert dsq <= rr
                    assertions += 1
                    checked_vertices += 1
                    if dsq == rr:
                        observed.add(x)
                expected = set()
                for j in range(q):
                    v = [0] * n
                    v[p + j] = n
                    expected.add(tuple(v))
                if discr < 0:
                    for i in range(p):
                        v = [0] * n
                        v[i] = p
                        expected.add(tuple(v))
                if p == q == 1:
                    expected.add((0, 0))
                assert observed == expected
                assertions += 1
    assert phase_counts['two_orbit'] and phase_counts['terminal_only']
    print('PASS: exact-rational independent facet-vertex reconstruction and distance certificates')
    print(f'parameter_pairs=6400; assertions={assertions}; small_vertex_distance_tests={checked_vertices}')
    print(f'phase_counts={phase_counts}')
    for p, q in [(1, 1), (1, 3), (3, 2), (10, 4), (10, 5)]:
        print(f'example ({p},{q}): center+radius={formula(p,q)}')


if __name__ == '__main__':
    run()
