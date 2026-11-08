#!/usr/bin/env python3
"""Finite-field and formal-series checks for a contact-refined cusp Hilbert series.

No external modules are needed. The finite-field ideal enumeration is independent
of the normalization parametrization used in the general proof.
"""
from itertools import combinations, product


def rref_subspaces(q, n, dim):
    """All dim-subspaces of F_q^n, once each, in reduced row-echelon form."""
    for pivots in combinations(range(n), dim):
        positions = [(r, c) for r, p in enumerate(pivots)
                     for c in range(p + 1, n) if c not in pivots]
        for values in product(range(q), repeat=len(positions)):
            rows = [[int(c == p) for c in range(n)] for p in pivots]
            for (r, c), v in zip(positions, values):
                rows[r][c] = v
            yield pivots, rows


def in_subspace(v, pivots, rows, q):
    v = list(v)
    for p, row in zip(pivots, rows):
        a = v[p] % q
        if a:
            v = [(z - a * b) % q for z, b in zip(v, row)]
    return not any(v)


def rank(vectors, q):
    if not vectors:
        return 0
    m = [list(v) for v in vectors]
    n = len(m[0]); h = 0
    for c in range(n):
        v = next((i for i in range(h, len(m)) if m[i][c] % q), None)
        if v is None:
            continue
        m[h], m[v] = m[v], m[h]
        a = pow(m[h][c], -1, q)
        m[h] = [(z * a) % q for z in m[h]]
        for j in range(len(m)):
            if j != h:
                b = m[j][c]
                m[j] = [(z - b * w) % q for z, w in zip(m[j], m[h])]
        h += 1
        if h == len(m):
            break
    return h


def cusp_enum(q=2, trunc=7, max_n=4):
    exps = [0] + list(range(2, trunc))
    index = {p: i for i, p in enumerate(exps)}
    N = len(exps)
    basis = [[int(i == j) for i in range(N)] for j in range(N)]

    def times_power(v, d):
        out = [0] * N
        for i, e in enumerate(exps):
            if e + d in index:
                out[index[e + d]] = (out[index[e + d]] + v[i]) % q
        return out

    xspace = [times_power(v, 2) for v in basis]
    results = {}
    for n in range(1, max_n + 1):
        counts = {}
        for pivots, rows in rref_subspaces(q, N, N - n):
            if not all(in_subspace(times_power(row, d), pivots, rows, q)
                       for row in rows for d in (2, 3)):
                continue
            contact = N - rank(rows + xspace, q)
            counts[contact] = counts.get(contact, 0) + 1
        results[n] = counts
    return results


def plane_enum(q=2, max_n=3):
    # Polynomial ring modulo (x,y)^3, basis 1,x,y,x^2,xy,y^2.
    exps = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
    idx = {e: i for i, e in enumerate(exps)}
    N = len(exps)

    def times(v, dx, dy):
        out = [0] * N
        for i, (a, b) in enumerate(exps):
            if (a + dx, b + dy) in idx:
                out[idx[a + dx, b + dy]] = v[i]
        return out

    result = {}
    for n in range(1, max_n + 1):
        cnt = 0
        for pivots, rows in rref_subspaces(q, N, N - n):
            if all(in_subspace(times(row, dx, dy), pivots, rows, q)
                   for row in rows for dx, dy in [(1, 0), (0, 1)]):
                cnt += 1
        result[n] = cnt
    return result


def polynomial_series(q, u, max_n):
    # Evaluate H(Q,(Q q)^u z)/prod_{i=0}^{u-1}(1-Q^{i+1} q^i z)
    # as a dict (degree_Q, degree_z) -> integer.
    h = {(0, 0): 1, (1, 1): 1}
    for n in (2, 3):
        h[(n, 1)] = q
        h[(n, 2)] = 1
    for n in range(4, max_n + 1):
        h[(n, 2)] = q + 1
    s = {}
    for (n, k), c in h.items():
        if n + u * k <= max_n:
            key = (n + u * k, k)
            s[key] = s.get(key, 0) + c * q ** (u * k)
    for i in range(u):
        nxt = {}
        for (n, k), c in s.items():
            j = 0
            while n + j * (i + 1) <= max_n:
                key = (n + j * (i + 1), k + j)
                nxt[key] = nxt.get(key, 0) + c * q ** (i * j)
                j += 1
        s = nxt
    return s


def main():
    for q in (2, 3):
        counts = cusp_enum(q=q, trunc=7, max_n=4)
        expected = {1: {1: 1}, 2: {1: q, 2: 1},
                    3: {1: q, 2: 1}, 4: {2: q + 1}}
        assert counts == expected, (q, counts, expected)
        s = polynomial_series(q, 0, 8)
        for n, data in expected.items():
            assert {j: s.get((n, j), 0) for j in data} == data
        print('CUSP_INDEPENDENT_RREF_OK', q, counts)
    # For n<=3, x(y^2-x^3) belongs to (x,y)^3, so the
    # corresponding Hilbert schemes agree with the plane.
    plane = plane_enum(2, 3)
    s = polynomial_series(2, 1, 8)
    assert {n: sum(c for (d, k), c in s.items() if d == n)
            for n in range(1, 4)} == plane
    print('FAT_CUSP_PLANE_INITIAL_SEGMENT_OK', plane)
    for q in (2, 3, 5):
        for u in range(7):
            s = polynomial_series(q, u, 12)
            assert s.get((0, 0)) == 1
            assert all(k >= 0 and n >= k for n, k in s)
            assert all(c >= 0 for c in s.values())
            if u == 0:
                assert all(sum(c for (m, j), c in s.items() if m == n)
                           == q + 1 for n in range(2, 13))
    print('SERIES_SPECIALIZATIONS_OK', 21)
    print('CERTIFICATE_OK')


if __name__ == '__main__':
    main()
