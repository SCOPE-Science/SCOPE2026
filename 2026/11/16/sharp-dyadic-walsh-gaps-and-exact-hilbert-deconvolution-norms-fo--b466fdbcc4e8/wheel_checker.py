#!/usr/bin/env python3
"""Exact Walsh checks for spanning-tree indicators of wheel graphs.

Only Python's standard library is needed. All arithmetic is integral.
"""
from itertools import combinations
from math import comb
from random import Random


def wheel_edges(n):
    return [(i, (i + 1) % n) for i in range(n)] + [(i, n) for i in range(n)]


def is_tree(n, edges, mask):
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    count = 0
    for j, (u, v) in enumerate(edges):
        if mask & (1 << j):
            count += 1
            u, v = find(u), find(v)
            if u == v:
                return False
            parent[u] = v
    return count == n


def walsh_in_place(vec):
    n = len(vec)
    step = 1
    while step < n:
        for start in range(0, n, 2 * step):
            for j in range(start, start + step):
                a, b = vec[j], vec[j + step]
                vec[j] = a + b
                vec[j + step] = a - b
        step *= 2


def signed_minor(n, rim, spoke):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = spoke[i] + rim[i - 1] + rim[i]
        A[i][(i+1)%n] -= rim[i]
        A[(i+1)%n][i] -= rim[i]
    return A


def bareiss(A):
    A = [row[:] for row in A]
    n = len(A)
    sign, den = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((i for i in range(k+1, n) if A[i][k]), None)
            if p is None: return 0
            A[k], A[p] = A[p], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * pivot - A[i][k] * A[k][j]
                assert num % den == 0
                A[i][j] = num // den
            A[i][k] = 0
        den = pivot
    return sign * A[-1][-1]


def matmul(A,B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0],
             A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0],
             A[1][0]*B[0][1]+A[1][1]*B[1][1]]]


def transfer_det(n, rim, spoke):
    P = [[1, 0], [0, 1]]
    for i in range(n):
        r, prev = rim[i], rim[i-1]
        assert r in (-1,1) and prev in (-1,1)
        T = [[(spoke[i]+prev+r)*r, -prev*r],[1,0]]
        P = matmul(T,P)
    prod = 1
    for r in rim: prod *= r
    return prod * (P[0][0] + P[1][1] - 2)


def witness(n):
    if n % 3 == 0:
        if n % 6 == 3:
            return [1]*n, [-1]*n, -4
        return [1]*n, [1,1,1,-1,1,-1]+[-1]*(n-6), -4
    if n % 6 in (1,5):
        return [1]*n, [-1]*n, -1
    if n % 6 == 2:
        return [1]*n, [1]+[-1]*(n-1), -1
    if n % 6 == 4:
        return [1,-1,1]+[1]*(n-3), [-1,1,1,1]+[-1]*(n-4), -1
    raise AssertionError


def main():
    rng = Random(271828)
    coeff_total = 0
    for n in range(3, 10):
        size = 1 << (2*n)
        edges = wheel_edges(n)
        f = [0]*size
        trees = 0
        for inds in combinations(range(2*n), n):
            mask = sum(1 << i for i in inds)
            if is_tree(n, edges, mask):
                f[mask] = 1
                trees += 1
        walsh_in_place(f)
        assert f[0] == trees
        assert sum(z*z for z in f) == size*trees
        m = min(abs(z) for z in f if z)
        assert m == (4 if n%3 == 0 else 1)
        assert all(z % 4 == 0 for z in f) if n%3 == 0 else all(z%2 == 1 for z in f)
        assert (0 in f) == (n%3 == 0)
        zeros = f.count(0)
        coeff_total += size
        for mask in (0, size-1, *[rng.randrange(size) for _ in range(48)]):
            rim = [1-2*((mask>>j)&1) for j in range(n)]
            spoke = [1-2*((mask>>(n+j))&1) for j in range(n)]
            d1 = bareiss(signed_minor(n,rim,spoke))
            d2 = transfer_det(n,rim,spoke)
            assert d1 == d2 == f[mask], (n,mask,d1,d2,f[mask])
        print('n',n,'trees',trees,'coefficients',size,'zeros',zeros,'min_abs_nonzero',m)
    for n in range(3, 91):
        r,s,claimed = witness(n)
        got = transfer_det(n,r,s)
        assert got == claimed,(n,got)
        if n <= 20:
            assert bareiss(signed_minor(n,r,s)) == claimed
    assert coeff_total == sum(1<<(2*n) for n in range(3,10))
    print('WHEEL_SPANNING_TREE_WALSH_GAP_PASS coefficients=%d witnesses=88' % coeff_total)

if __name__=='__main__': main()
