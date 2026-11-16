"""Exact, self-contained checks for the complete-graph tree Walsh multiplier theorem.

Run: python3 VERIFY.py  (Python 3, standard library only).
The infinite claims rely on the accompanying proof; this file supplies finite tests.
"""
from itertools import product, combinations
from math import comb
from random import Random


def edges(n):
    return list(combinations(range(n), 2))


def prufer_tree(code, n):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    out = []
    for v in code:
        u = min(i for i, d in enumerate(degree) if d == 1)
        out.append((min(u, v), max(u, v)))
        degree[u] -= 1
        degree[v] -= 1
    a, b = [i for i, d in enumerate(degree) if d == 1]
    out.append((a, b))
    return out


def full_walsh(n):
    ed = edges(n)
    index = {e: j for j, e in enumerate(ed)}
    m = len(ed)
    data = [0] * (1 << m)
    for code in product(range(n), repeat=n-2):
        mask = 0
        for e in prufer_tree(code, n):
            mask |= 1 << index[e]
        data[mask] += 1
    size = len(data)
    step = 1
    while step < size:
        for start in range(0, size, 2 * step):
            for j in range(start, start + step):
                a, b = data[j], data[j + step]
                data[j], data[j + step] = a+b, a-b
        step *= 2
    return data, ed


def signed_tree_det(n, sign):
    # Reduced weighted Laplacian with final vertex deleted.
    L = [[0] * (n-1) for _ in range(n-1)]
    for (i, j), val in sign.items():
        if i < n-1:
            L[i][i] += val
        if j < n-1:
            L[j][j] += val
        if i < n-1 and j < n-1:
            L[i][j] -= val
            L[j][i] -= val
    return det_bareiss(L)


def det_bareiss(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n-1):
        if A[k][k] == 0:
            pivot = next((i for i in range(k+1, n) if A[i][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        v = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = A[i][j]*v - A[i][k]*A[k][j]
                assert num % prev == 0
                A[i][j] = num // prev
        for i in range(k+1, n):
            A[i][k] = 0
        prev = v
    return sign*A[n-1][n-1]


def balanced_signs(n):
    assert n % 2 == 0 and n >= 4
    return [1]* (n//2) + [-1]*(n//2)


def edge_signs(x):
    return {(i,j): x[i]*x[j] for i,j in edges(len(x))}


def sharp_even_signs(n):
    x = balanced_signs(n)
    s = edge_signs(x)
    # A star on vertices 1..n-1, isolated vertex 0.
    for v in range(2, n):
        s[1,v] *= -1
    return s


def check():
    # Full independent Walsh enumeration, not determinant enumeration.
    for n in range(3, 7):
        coeff, ed = full_walsh(n)
        assert len(coeff) == 1 << len(ed)
        assert coeff[0] == n ** (n-2)
        nonzero = [abs(z) for z in coeff if z]
        wanted = 1 if n % 2 else (1 << (n-2))
        assert min(nonzero) == wanted, (n, min(nonzero), wanted)
        if n % 2:
            assert not any(z == 0 for z in coeff)
        else:
            assert any(z == 0 for z in coeff)
            assert all(z % wanted == 0 for z in coeff)
            assert coeff.count(0) >= comb(n, n//2)
        # Explicit sharp witnesses in the independently computed transform.
        if n % 2:
            x = [1]*((n+1)//2)+[-1]*((n-1)//2)
            signed = edge_signs(x)
            expected = 1
        else:
            signed = sharp_even_signs(n)
            expected = 1 << (n-2)
        mask = sum(1 << k for k, e in enumerate(ed) if signed[e] == -1)
        assert abs(coeff[mask]) == expected
        print('FULL_WALSH_OK', n, 'frequencies', len(coeff), 'min_nonzero', wanted,
              'zeros', coeff.count(0))
    # Exact determinant verification, independent of character-space enumeration.
    rng = Random(271828)
    for n in range(3, 14):
        for _ in range(50):
            s = {e: rng.choice([-1, 1]) for e in edges(n)}
            v = signed_tree_det(n, s)
            assert abs(v) <= n ** (n-2)
            if n % 2:
                assert v % 2 != 0
            else:
                assert v % (1 << (n-2)) == 0
        if n % 2:
            x = [1]*((n+1)//2)+[-1]*((n-1)//2)
            v = signed_tree_det(n, edge_signs(x))
            assert abs(v) == 1
        else:
            x = balanced_signs(n)
            assert signed_tree_det(n, edge_signs(x)) == 0
            v = signed_tree_det(n, sharp_even_signs(n))
            assert abs(v) == 1 << (n-2), (n, v)
        print('EXACT_LAPLACIAN_OK', n)
    print('COMPLETE_GRAPH_TREE_WALSH_SHARP_CHECKS_PASS')


if __name__ == '__main__':
    check()
