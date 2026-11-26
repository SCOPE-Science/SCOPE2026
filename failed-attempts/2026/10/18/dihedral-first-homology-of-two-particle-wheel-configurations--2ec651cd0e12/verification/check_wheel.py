"""Finite signed-cell and boundary checks for two-point wheel configurations.

The universal argument, rather than extrapolation from these checks, proves the theorem.
Run with Python 3.10 or later; no external packages are required.
"""
from itertools import combinations


def cells(n):
    vertices = tuple(range(n + 1))
    edges = tuple(sorted(
        {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
        | {(i, n) for i in range(n)}
    ))
    zeros = tuple(combinations(vertices, 2))
    ones = tuple((e, v) for e in edges for v in vertices if v not in e)
    twos = tuple((e, f) for e, f in combinations(edges, 2) if not set(e) & set(f))
    return zeros, ones, twos


def bit_rank(columns):
    pivots = {}
    for word in columns:
        while word:
            pos = word.bit_length() - 1
            if pos not in pivots:
                pivots[pos] = word
                break
            word ^= pivots[pos]
    return len(pivots)


def signed_boundaries(zeros, ones, twos):
    idx0 = {v: i for i, v in enumerate(zeros)}
    idx1 = {v: i for i, v in enumerate(ones)}
    d1 = []
    for (a, b), v in ones:
        d1.append({idx0[tuple(sorted((a, v)))]: -1,
                   idx0[tuple(sorted((b, v)))]: +1})
    d2 = []
    for (a, b), (c, d) in twos:
        terms = [(((c, d), b), +1), (((c, d), a), -1),
                 (((a, b), d), -1), (((a, b), c), +1)]
        col = {idx1[cell]: sign for cell, sign in terms}
        boundary2 = {}
        for row, sign in col.items():
            for vert, value in d1[row].items():
                boundary2[vert] = boundary2.get(vert, 0) + sign * value
        assert all(v == 0 for v in boundary2.values())
        d2.append(col)
    return d1, d2


def trace_action(n, a, reflected, zeros, ones, twos):
    p = {i: ((a - i) % n if reflected else (a + i) % n) for i in range(n)}
    p[n] = n
    def edge(e):
        return tuple(sorted((p[e[0]], p[e[1]])))
    def direction(e):
        return 1 if p[e[0]] < p[e[1]] else -1
    c0 = sum(1 for vs in zeros if tuple(sorted(p[v] for v in vs)) == vs)
    c1 = sum(direction(e) for e, v in ones if edge(e) == e and p[v] == v)
    c2 = sum(direction(e) * direction(f) *
             (1 if edge(e) < edge(f) else -1)
             for e, f in twos if tuple(sorted((edge(e), edge(f)))) == (e, f))
    return c0, c1, c2


def expected(n, a, reflected):
    if not reflected:
        return n + 1 if a == 0 else 1
    if n % 2:
        return -2
    return -1 if a % 2 == 0 else -3


def test(n):
    zeros, ones, twos = cells(n)
    assert (len(zeros), len(ones), len(twos)) == (
        n * (n + 1) // 2, 2 * n * (n - 1), n * (3 * n - 7) // 2)
    d1, d2 = signed_boundaries(zeros, ones, twos)
    mod2_columns = [sum(1 << row for row in col) for col in d2]
    assert bit_rank(mod2_columns) == len(twos), 'H2 is nonzero modulo 2'
    assert bit_rank([sum(1 << row for row in col) for col in d1]) == len(zeros)-1
    assert len(ones) - (len(zeros)-1) - len(twos) == n+1
    for reflected in (False, True):
        for a in range(n):
            c0, c1, c2 = trace_action(n, a, reflected, zeros, ones, twos)
            hom_trace = 1 - c0 + c1 - c2
            assert hom_trace == expected(n, a, reflected), (
                n, a, reflected, hom_trace, expected(n, a, reflected))
    print('CHECK_OK', n, 'cells', len(zeros), len(ones), len(twos),
          'rank_d2', len(twos), 'betti1', n+1,
          'dihedral_elements', 2*n)


if __name__ == '__main__':
    for n in range(4, 15):
        test(n)
    print('VERIFY_OK_WHEEL_TWO_POINT_DIHEDRAL')
