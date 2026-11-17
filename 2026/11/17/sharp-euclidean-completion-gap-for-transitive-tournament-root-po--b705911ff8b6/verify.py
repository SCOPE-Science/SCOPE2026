#!/usr/bin/env python3
"""Exact rational, standalone checks of root-polytope projection certificates."""
from fractions import Fraction as F


def root(n, i, j):
    x = [F(0)] * n
    x[i] = F(1)
    x[j] = F(-1)
    return tuple(x)


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(x, c):
    return tuple(c * a for a in x)


def positive_roots(n):
    return [root(n, i, j) for i in range(n) for j in range(i + 1, n)]


def pos_combination(n, terms):
    z = tuple(F(0) for _ in range(n))
    assert sum((weight for _, _, weight in terms), F(0)) == 1
    for i, j, weight in terms:
        assert weight >= 0
        z = add(z, scale(root(n, i, j), weight))
    return z


def positive_min_norm(n, omission):
    positions = [i for i in range(n) if i not in omission]
    m = len(positions)
    assert m >= 2
    c = F(6, m * (m * m - 1))
    weights = [(positions[h], positions[h + 1], c * (h + 1) * (m - h - 1))
               for h in range(m - 1)]
    point = pos_combination(n, weights)
    expected = [F(0)] * n
    for h, i in enumerate(positions):
        expected[i] = c * (m - 1 - 2 * h)
    assert point == tuple(expected)
    s = F(12, m * (m * m - 1))
    assert dot(point, point) == s
    for i, j in zip(positions[:-1], positions[1:]):
        assert dot(point, root(n, i, j)) == s
    for h in range(m):
        for k in range(h + 1, m):
            assert dot(point, root(n, positions[h], positions[k])) == s * (k - h)
    return point, s


def kkt_projection(n, x, point):
    # Equivalence for projection onto conv{roots}:
    # (x-point) dot (r-point) <=0 for each extreme root r.
    residue = sub(x, point)
    return all(dot(residue, sub(r, point)) <= 0 for r in positive_roots(n))


def check_small():
    # n=2 is a segment-versus-point problem.
    assert dot(sub(scale(root(2, 0, 1), F(-1)), root(2, 0, 1)),
               sub(scale(root(2, 0, 1), F(-1)), root(2, 0, 1))) == 8
    # n=3: the antipodal longest root projects to its positive half.
    n = 3
    x = scale(root(n, 0, n - 1), F(-1))
    p = pos_combination(n, [(0, 1, F(1, 2)), (1, 2, F(1, 2))])
    assert kkt_projection(n, x, p)
    assert dot(sub(x, p), sub(x, p)) == F(9, 2)
    for i, j in [(0, 1), (1, 2)]:
        x = scale(root(n, i, j), F(-1))
        r = root(n, 1, 2) if i == 0 else root(n, 0, 1)
        assert dot(sub(x, r), sub(x, r)) == 2
    # n=4: all three adjacent-root weights are positive in the projection.
    n = 4
    x = scale(root(n, 0, n - 1), F(-1))
    p = pos_combination(n, [(0, 1, F(1, 5)), (1, 2, F(3, 5)), (2, 3, F(1, 5))])
    assert kkt_projection(n, x, p)
    assert dot(sub(x, p), sub(x, p)) == F(16, 5)
    others = {
        (0, 1): [(1, 2, F(2, 3)), (2, 3, F(1, 3))],
        (0, 2): [(1, 2, F(1, 6)), (2, 3, F(5, 6))],
        (1, 2): [(0, 1, F(1, 2)), (2, 3, F(1, 2))],
        (1, 3): [(0, 1, F(5, 6)), (1, 2, F(1, 6))],
        (2, 3): [(0, 1, F(1, 3)), (1, 2, F(2, 3))],
    }
    for (i, j), terms in others.items():
        q = pos_combination(n, terms)
        y = scale(root(n, i, j), F(-1))
        assert dot(sub(y, q), sub(y, q)) < F(16, 5)


def check_general(n):
    m = n - 2
    assert n >= 5
    p, s = positive_min_norm(n, {0, n - 1})
    x = scale(root(n, 0, n - 1), F(-1))
    assert dot(x, p) == 0
    assert kkt_projection(n, x, p)
    assert dot(sub(x, p), sub(x, p)) == 2 + s
    assert s == F(12, (n - 3) * (n - 2) * (n - 1))
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) == (0, n - 1):
                continue
            q, t = positive_min_norm(n, {i, j})
            y = scale(root(n, i, j), F(-1))
            assert t == s and dot(y, q) == 0
            assert dot(sub(y, q), sub(y, q)) == 2 + s
            a, b = (j, j + 1) if j < n - 1 else (i - 1, i)
            r = root(n, a, b)
            assert dot(sub(y, q), sub(r, q)) > 0


def main():
    check_small()
    for n in range(5, 17):
        check_general(n)
    for n in (30, 61, 103):
        p, s = positive_min_norm(n, {0, n - 1})
        x = scale(root(n, 0, n - 1), F(-1))
        assert kkt_projection(n, x, p)
        assert dot(sub(x, p), sub(x, p)) == 2 + s
    print('POSITIVE_ROOT_HAUSDORFF_PASS small=2,3,4 all_negative_certificates=5..16 large_highest_KKT=30,61,103')


if __name__ == '__main__':
    main()
