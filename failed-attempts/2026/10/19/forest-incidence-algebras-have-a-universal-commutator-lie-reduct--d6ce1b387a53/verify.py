#!/usr/bin/env python3
"""Check finite-field joint-centralizer ranks in height-two tree incidence algebras.

The program computes each commutator linear map directly in the ordinary
incidence-algebra basis, independently of the abstract Lie decomposition.
It requires only the Python standard library.
"""
from collections import Counter
from itertools import product
from math import comb


def matrix_rank(rows, p):
    if not rows:
        return 0
    a = [list(r) for r in rows]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col] % p, -1, p)
        a[rank] = [v * inv % p for v in a[rank]]
        for i in range(m):
            if i != rank and a[i][col] % p:
                z = a[i][col]
                a[i] = [(v - z * w) % p for v, w in zip(a[i], a[rank])]
        rank += 1
        if rank == min(m, n):
            break
    return rank


def direct_rank(tup, edges, n, p):
    m = len(edges)
    s = len(tup)
    # J^s rows; diagonal/idempotent and interval-basis columns.
    rows = [[0] * (n + m) for _ in range(s * m)]
    for i, vector in enumerate(tup):
        for e, (u, v) in enumerate(edges):
            row = rows[i * m + e]
            row[u] = -vector[n + e] % p
            row[v] = vector[n + e] % p
            row[n + e] = (vector[u] - vector[v]) % p
    return matrix_rank(rows, p)


def predicted(p, s, m):
    a0 = 1
    a1 = (p ** s - 1) * (p + 1)
    a2 = (p ** s - 1) * (p ** s - p)
    # Coefficients of p^s (a0+a1*t+a2*t^2)^m
    out = [1]
    for _ in range(m):
        nxt = [0] * (len(out) + 2)
        for i, val in enumerate(out):
            for j, a in enumerate((a0, a1, a2)):
                nxt[i + j] += a * val
        out = nxt
    return {i: p ** s * a for i, a in enumerate(out) if a}


def check_lie_splitting(edges, n, p):
    m = len(edges)
    z = [1] * n + [0] * m
    basis = [z]
    for target in range(m):
        d = [None] * n
        d[0] = 0
        while None in d:
            changed = False
            for e, (u, v) in enumerate(edges):
                delta = 1 if e == target else 0
                if d[u] is not None and d[v] is None:
                    d[v] = (d[u] - delta) % p
                    changed = True
                elif d[v] is not None and d[u] is None:
                    d[u] = (d[v] + delta) % p
                    changed = True
            assert changed, 'graph must be a tree'
        basis.append(d + [0] * m)
    for e in range(m):
        r = [0] * (n + m)
        r[n + e] = 1
        basis.append(r)
    assert matrix_rank(basis, p) == n + m
    for e in range(m):
        for f, (u, v) in enumerate(edges):
            h = basis[e + 1]
            bracket = (h[u] - h[v]) % p
            assert bracket == (e == f)
    print('LIE_SPLITTING_OK', f'q={p}', f'edges={edges}')


def count_ranks(edges, n, p, s):
    elems = tuple(product(range(p), repeat=n + len(edges)))
    ans = Counter()
    for tup in product(elems, repeat=s):
        ans[direct_rank(tup, edges, n, p)] += 1
    expected = predicted(p, s, len(edges))
    assert dict(ans) == expected, (p, s, edges, dict(ans), expected)
    print('CHECK', f'q={p}', f's={s}', f'n={n}', f'edges={edges}',
          'rank_counts=' + str(dict(sorted(ans.items()))))
    # The rank-one-or-zero conditions on all edge blocks are precisely
    # the pairwise commutativity conditions for a tuple.
    commuting = 0
    for tup in product(elems, repeat=s):
        valid = True
        for a in range(s):
            for b in range(a + 1, s):
                for e, (u, v) in enumerate(edges):
                    da = tup[a][u] - tup[a][v]
                    db = tup[b][u] - tup[b][v]
                    xa = tup[a][n + e]
                    xb = tup[b][n + e]
                    if (da * xb - db * xa) % p:
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                break
        commuting += valid
    rank01 = 1 + (p ** s - 1) * (p + 1)
    expected_commuting = p ** s * rank01 ** len(edges)
    assert commuting == expected_commuting, (commuting, expected_commuting)
    print('COMMUTING', commuting)


def main():
    # Two different Hasse trees on four vertices: a star and a fence.
    star = ((0, 1), (0, 2), (0, 3))
    fence = ((0, 1), (2, 1), (2, 3))
    fork = ((0, 1), (0, 2))
    for p in (2, 3, 5):
        for edges in (star, fence):
            check_lie_splitting(edges, 4, p)
    count_ranks(star, 4, 2, 1)
    count_ranks(fence, 4, 2, 1)
    count_ranks(star, 4, 2, 2)
    count_ranks(fence, 4, 2, 2)
    count_ranks(fork, 3, 3, 2)
    count_ranks(fork, 3, 2, 3)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
