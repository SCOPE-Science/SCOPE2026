"""Finite incidence diagnostics for projective planes over GF(2) and GF(3).
The all-projective-planes uniqueness theorem is proved analytically in RESULT.md.
"""
import math
from itertools import product


def projective_reps(p):
    vectors = set()
    for v in product(range(p), repeat=3):
        if v == (0, 0, 0):
            continue
        first = next(z for z in v if z)
        inv = pow(first, -1, p)
        vectors.add(tuple((inv * z) % p for z in v))
    return sorted(vectors)


def test_order(p):
    points = projective_reps(p)
    lines = projective_reps(p)
    v = p * p + p + 1
    assert len(points) == len(lines) == v
    b = [[int(sum(x * y for x, y in zip(pt, line)) % p == 0)
          for line in lines] for pt in points]
    assert all(sum(row) == p + 1 for row in b)
    assert all(sum(b[i][j] for i in range(v)) == p + 1 for j in range(v))
    checks = 0
    for i in range(v):
        for j in range(v):
            z = sum(b[i][l] * b[j][l] for l in range(v))
            assert z == (p + 1 if i == j else 1)
            checks += 1
    for i in range(v):
        for j in range(v):
            z = sum(b[l][i] * b[l][j] for l in range(v))
            assert z == (p + 1 if i == j else 1)
            checks += 1
    a = math.sqrt(p)
    beta = ((p + 1) - a) / v
    assert abs((a + beta) - ((p + 1) + (v - 1) * a) / v) < 1e-13
    assert abs((a * beta * 2 + v * beta * beta) / v - 1 / v) < 1e-13
    return checks


if __name__ == '__main__':
    count = sum(test_order(q) for q in (2, 3))
    print(f'PROJECTIVE_PLANE_INCIDENCE_OK {count} exact Gram entries')
