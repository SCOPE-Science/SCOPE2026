#!/usr/bin/env python3
"""Exact integer verification for cyclic generic-line generalized Jacobians.
No external dependencies. Proves finite-range integral matrices only; the
unbounded theorem has a separate symbolic proof in RESULT.md.
"""
from itertools import combinations
from math import gcd


def determinant_bareiss(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    divisor = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((i for i in range(k + 1, n) if a[i][k]), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                t = a[i][j] * pivot - a[i][k] * a[k][j]
                assert t % divisor == 0
                a[i][j] = t // divisor
            a[i][k] = 0
        divisor = pivot
    return sign * a[-1][-1]


def test_integral_lattice(n):
    edges = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    chords = list(combinations(range(1, n), 2))
    g = len(chords)
    def oriented_edge(i, j):
        i %= n; j %= n
        sign = 1 if i < j else -1
        return (index[tuple(sorted((i, j)))], sign)
    def path_cycle(i, d):
        v = [0] * len(edges)
        for j in range(d):
            ix, sg = oriented_edge(i + j, i + j + 1)
            v[ix] += sg
        ix, sg = oriented_edge(i, i + d)
        v[ix] -= sg
        return v
    def perimeter():
        v = [0] * len(edges)
        for i in range(n):
            ix, sg = oriented_edge(i, i + 1)
            v[ix] += sg
        return v
    def rotate(v):
        w = [0] * len(edges)
        for a, (i, j) in enumerate(edges):
            ix, sg = oriented_edge(i + 1, j + 1)
            w[ix] += sg * v[a]
        return w
    def coords(v):
        return [v[index[e]] for e in chords]
    def boundary(v):
        b = [0] * n
        for t, (i, j) in enumerate(edges):
            b[i] -= v[t]
            b[j] += v[t]
        return b
    base = []
    for i, j in chords:
        v = [0] * len(edges)
        for x, y, sg in ((0, i, 1), (i, j, 1), (0, j, -1)):
            ix, sign = oriented_edge(x, y)
            v[ix] += sg * sign
        base.append(v)
    P = [[coords(rotate(base[j]))[i] for j in range(g)] for i in range(g)]
    basis = [perimeter()]
    dmax = (n-1)//2 if n%2 else n//2-1
    regular_blocks = []
    for d in range(2, dmax + 1):
        start = len(basis)
        basis += [path_cycle(i, d) for i in range(n)]
        regular_blocks.append(list(range(start, start+n)))
    special = []
    if n % 2 == 0:
        h = n//2
        start = len(basis)
        basis += [path_cycle(i,h) for i in range(h)]
        special = list(range(start, start+h))
    assert len(basis) == g
    assert all(boundary(v) == [0]*n for v in basis)
    B = [[coords(basis[j])[i] for j in range(g)] for i in range(g)]
    assert abs(determinant_bareiss(B)) == 1
    Q = [[0]*g for _ in range(g)]
    Q[0][0] = 1
    for block in regular_blocks:
        for i in range(len(block)):
            Q[block[(i+1)%len(block)]][block[i]] = 1
    for i in range(len(special)-1):
        Q[special[i+1]][special[i]] = 1
    if special:
        Q[0][special[-1]] = 1
        Q[special[0]][special[-1]] = -1
    for i in range(g):
        for j in range(g):
            lhs = sum(P[i][k]*B[k][j] for k in range(g))
            rhs = sum(B[i][k]*Q[k][j] for k in range(g))
            assert lhs == rhs, (n,i,j)
    return g


def count_direct(n,q,r):
    # Normalization components, nodes, and individual node branches
    verts = list(range(n))
    pairs = list(combinations(verts,2))
    f = lambda i: (i+r)%n
    fixed_edges = sum(1 for i,j in pairs if {f(i),f(j)} == {i,j})
    fixed_branches = sum(1 for i,j in pairs for k in (i,j)
                         if {f(i),f(j)} == {i,j} and f(k)==k)
    fixed_components = n if r % n == 0 else 0
    return fixed_components*(q**r+1) - fixed_branches + fixed_edges


def count_formula(n,q,r):
    if n%2:
        return n*(q**r-(n-3)//2) if r%n == 0 else 0
    h=n//2
    if r%n==0:
        return n*q**r - n*(h-2) - h
    if r%h==0:
        return h
    return 0


def main():
    for n in range(4,12):
        genus = test_integral_lattice(n)
        assert genus == (n-1)*(n-2)//2
        for q in (2,3,4,5,7,9):
            for r in range(1,2*n+1):
                assert count_direct(n,q,r)==count_formula(n,q,r), (n,q,r)
    print('CYCLIC_GENERIC_LINE_PICARD_INTEGRAL_LATTICES_AND_ZETA_OK')
    print('tested n=4..11; q=2,3,4,5,7,9; r=1..2n')

if __name__=='__main__':
    main()
