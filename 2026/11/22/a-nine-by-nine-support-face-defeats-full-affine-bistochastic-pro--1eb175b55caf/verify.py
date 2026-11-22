"""Exact rational certificate for a supported Birkhoff projection face."""
from fractions import Fraction as F

N = 9
ROW_SUPPORT = (
    (0, 1, 3, 5),
    (1, 4, 7, 8),
    (1, 2, 4, 5, 6, 8),
    (2, 3, 5, 6, 7),
    (0, 1, 7, 8),
    (0, 1, 4, 7),
    (1, 3, 5, 6, 8),
    (3, 8),
    (0, 2, 4, 6),
)
PERMUTATIONS = (
    (0, 1, 2, 3, 7, 4, 5, 8, 6),
    (1, 4, 5, 2, 8, 7, 6, 3, 0),
    (5, 7, 4, 6, 0, 1, 3, 8, 2),
    (3, 4, 6, 5, 7, 0, 1, 8, 2),
    (5, 8, 2, 7, 1, 0, 6, 3, 4),
    (5, 4, 1, 2, 0, 7, 8, 3, 6),
    (0, 1, 8, 2, 7, 4, 5, 3, 6),
)
E = [(i, j) for i, row in enumerate(ROW_SUPPORT) for j in row]
TARGET = (3, 7)


def solve(a, b):
    """Solve a nonsingular rational system using exact Gauss-Jordan elimination."""
    n = len(a)
    m = [[F(x) for x in row] + [F(y)] for row, y in zip(a, b)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if m[i][k] != 0)
        m[k], m[pivot] = m[pivot], m[k]
        f = m[k][k]
        m[k] = [v / f for v in m[k]]
        for i in range(n):
            if i != k:
                v = m[i][k]
                if v:
                    m[i] = [x - v * y for x, y in zip(m[i], m[k])]
    return [m[i][-1] for i in range(n)]


def signed_column(edge):
    i, j = edge
    b = [0] * (2 * N - 1)
    b[i] = 1
    if j < N - 1:
        b[N + j] = -1
    return b


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def main():
    assert len(E) == 38 and len(set(E)) == 38 and TARGET in E
    assert all(sorted(p) == list(range(N)) for p in PERMUTATIONS)
    assert {e for p in PERMUTATIONS for e in enumerate(p)} == set(E)
    columns = [signed_column(e) for e in E]
    d = 2 * N - 1
    gram = [[sum(u[i] * u[j] for u in columns) for j in range(d)]
            for i in range(d)]
    v = solve(gram, signed_column(TARGET))
    row = [(F(1) if e == TARGET else F(0)) - dot(v, b)
           for e, b in zip(E, columns)]
    row_norm = sum(map(abs, row), F(0))
    affine_norm = F(4 * (N - 1) ** 2, N ** 2)
    assert row_norm == F(13394263, 4220481)
    assert affine_norm == F(256, 81)
    assert row_norm - affine_norm == F(1497389, 113952987) > 0
    h = [F(1) if u > 0 else F(-1) if u < 0 else F(0) for u in row]
    bh = [sum(columns[e][i] * h[e] for e in range(len(E)))
          for i in range(d)]
    potentials = solve(gram, bh)
    qh = [h[e] - dot(potentials, columns[e]) for e in range(len(E))]
    assert qh[E.index(TARGET)] == row_norm
    assert all(sum(columns[e][i] * qh[e] for e in range(len(E))) == 0
               for i in range(d))
    x0 = [[F(0) for _ in range(N)] for _ in range(N)]
    for p in PERMUTATIONS:
        for i, j in enumerate(p):
            x0[i][j] += F(1, len(PERMUTATIONS))
    assert all(x0[i][j] > 0 for i, j in E)
    assert all(x0[i][j] == 0 for i in range(N) for j in range(N)
               if (i, j) not in E)
    eps = F(1, 1_000_000)
    x1 = [row[:] for row in x0]
    for e, (i, j) in enumerate(E):
        x1[i][j] += eps * qh[e]
    assert all(x1[i][j] > 0 for i, j in E)
    assert all(sum(x1[i][j] for j in range(N)) == 1 for i in range(N))
    assert all(sum(x1[i][j] for i in range(N)) == 1 for j in range(N))
    # KKT: G0-X0 = -1 off support; G1-X1 has row/column potentials
    # on support and negative normal slack off support.
    assert all(F(1) + eps * dot(potentials, signed_column((i, j))) > 0
               for i in range(N) for j in range(N) if (i, j) not in E)
    assert max(abs(t) for t in h) == 1
    assert (x1[TARGET[0]][TARGET[1]] - x0[TARGET[0]][TARGET[1]]) / eps == row_norm
    print('PASS: support coverage by seven permutations; exact rational Green solve;')
    print('PASS: strict primal positivity and strict dual slack for two finite inputs;')
    print('FACE_ROW_NORM', row_norm)
    print('FULL_AFFINE_NORM', affine_norm)
    print('STRICT_EXCESS', row_norm - affine_norm)


if __name__ == '__main__':
    main()
