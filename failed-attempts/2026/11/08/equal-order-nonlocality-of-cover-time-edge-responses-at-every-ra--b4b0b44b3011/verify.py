#!/usr/bin/env python3
"""Independent finite checks for an equal-order cover-time response construction.

Uses only Python's standard library. Finite tests support, but do not replace,
the quantified analytic argument in RESULT.md.
"""
from fractions import Fraction as F
from collections import deque
from math import ceil, log2


def graphs(h, M):
    assert h >= 1 and M >= 3
    # A common vertex label set: 0=c, 1=s, 2=u, 3=v, 4=w,
    # 5,...,4+h are the common stem, and the remaining M-1 are extra.
    n = M + h + 4
    c, s, u, v, w = range(5)
    stem = list(range(5, h + 5))
    remaining = list(range(h + 5, n))
    common = [(c, s), (c, u), (c, v), (c, w), (c, stem[0])]
    common += list(zip(stem, stem[1:]))
    clique = [stem[-1]] + remaining
    neg = common + [(a, b) for k, a in enumerate(clique) for b in clique[k+1:]]
    pos = common + list(zip([stem[-1]] + remaining[:-1], remaining))
    # The positive path runs through all h+M-1 noncentral path vertices.
    assert len(pos) == h + M + 3
    return n, neg, pos, (s, u, v)


def adjacency(n, edges):
    a = [set() for _ in range(n)]
    for x, y in edges:
        assert x != y and y not in a[x]
        a[x].add(y)
        a[y].add(x)
    return a


def marked_ball(n, edges, marked, radius):
    a = adjacency(n, edges)
    dist = {x: 0 for x in marked}
    todo = deque(marked)
    while todo:
        x = todo.popleft()
        if dist[x] == radius:
            continue
        for y in a[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                todo.append(y)
    verts = sorted(dist)
    included = {(min(x, y), max(x, y)) for x in verts for y in a[x] if y in dist}
    degree_labels = {x: len(a[x]) for x in verts}
    return verts, included, degree_labels


def solve_fraction(A, b):
    n = len(b)
    # Gaussian elimination with partial row pivoting (exact rational).
    for col in range(n):
        p = next((i for i in range(col, n) if A[i][col]), None)
        assert p is not None
        A[col], A[p] = A[p], A[col]
        b[col], b[p] = b[p], b[col]
        piv = A[col][col]
        for j in range(col, n):
            A[col][j] /= piv
        b[col] /= piv
        for i in range(n):
            if i == col or not A[i][col]:
                continue
            scale = A[i][col]
            for j in range(col, n):
                A[i][j] -= scale * A[col][j]
            b[i] -= scale * b[col]
    return b


def cover_expectation(n, edges, start):
    """Solve exact visited-set Markov equations over rationals."""
    adj = adjacency(n, edges)
    full = (1 << n) - 1
    known = {(full, v): F(0) for v in range(n)}
    for mask in range(full - 1, 0, -1):
        vs = [i for i in range(n) if (mask >> i) & 1]
        ix = {v: j for j, v in enumerate(vs)}
        k = len(vs)
        A = [[F(int(i == j)) for j in range(k)] for i in range(k)]
        b = [F(1) for _ in vs]
        for i, v in enumerate(vs):
            for u in adj[v]:
                if (mask >> u) & 1:
                    A[i][ix[u]] -= F(1, len(adj[v]))
                else:
                    b[i] += known[(mask | (1 << u), u)] / len(adj[v])
        solution = solve_fraction(A, b)
        for v, val in zip(vs, solution):
            known[(mask, v)] = val
    return known[(1 << start, start)]


def poly(L):
    return 345*L**5 + 676*L**4 - 489*L**3 - 887*L**2 - 336*L - 44


def positive_exact(L):
    return F(2 * poly(L), 15*(L+1)*(2*L+1)*(3*L+2)*(5*L+2))


def positive_excursion(L):
    def A(k):
        return 1/(1+k*L) - 1/(L+1+k*L)
    def B(k):
        return 1/(1+k) - L/(L+1+k*L)
    a = A(F(1)) + B(F(1))
    b = A(F(3, 2)) + B(F(3, 2))
    j = L**2*(A(F(1))-A(F(3, 2))) + B(F(1))-B(F(3, 2))
    ET = F(L) + F(1, L+1)
    return 2*(ET-(2*L+7)*(a-F(2, 3)*b)-j)


def check():
    nassert = 0
    for h in range(1, 11):
        M = 16*(h+1)
        n, neg, pos, marks = graphs(h, M)
        assert n == 17*h+20
        assert marked_ball(n, neg, marks, h) == marked_ball(n, pos, marks, h)
        assert [len(adjacency(n, neg)[i]) for i in marks] == [1, 1, 1]
        assert len(adjacency(n, neg)[0]) == len(adjacency(n, pos)[0]) == 5
        # Graph bridge topology supplies R_uv=2 (each marked leaf is a bridge).
        assert all((0, i) in neg and (0, i) in pos for i in marks)
        assert len(neg)*2-1 == M*(M-1)+2*h+7
        assert len(pos) == (h+M-1)+4
        assert M >= 32
        k0 = ceil(log2(M-1))
        assert k0+2 <= F(M-1, 2)
        assert M*(M-1) > 3*(4*h+2)*(2*h+1)
        assert F(2*h+1) - F(M*(M-1)+2*h+7, 3*(4*h+2)) < 0
        assert positive_exact(h+M-1) > 0
        nassert += 11
    for L in range(1, 101):
        assert positive_excursion(L) == positive_exact(L)
        assert (positive_exact(L) > 0) == (L >= 2)
        nassert += 2
    # Exact rational first-passage equations at two eight-vertex cases.
    h, M = 1, 3
    n, neg, pos, marks = graphs(h, M)
    s, u, v = marks
    assert n == 8
    assert marked_ball(n, neg, marks, h) == marked_ball(n, pos, marks, h)
    dn = cover_expectation(n, neg + [(u, v)], s) - cover_expectation(n, neg, s)
    dp = cover_expectation(n, pos + [(u, v)], s) - cover_expectation(n, pos, s)
    assert dn < 0
    assert dp == positive_exact(h+M-1) == F(116353, 39270)
    nassert += 5
    print('PASS:', nassert, 'exact integer and rational checks')
    print('small equal-order witness: h=1, M=3, n=8')
    print('negative response:', dn, 'positive response:', dp)
    print('analytic all-radius construction: M=16(h+1), order=17h+20')


if __name__ == '__main__':
    check()
