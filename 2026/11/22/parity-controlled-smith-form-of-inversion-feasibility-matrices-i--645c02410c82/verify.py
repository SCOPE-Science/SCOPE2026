#!/usr/bin/env python3
"""Exact finite checks for inversion feasibility of one-types in two dense orders.

Requires sympy (tested with version 1.14). Run: python verify.py
The universal theorem is proved algebraically in RESULT.md, not inferred from tests.
"""
import itertools
import json
from collections import Counter
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def entry(p, q):
    i, j = p
    k, ell = q
    return 1 if (i - k) * (j - ell) <= 0 else 0


def matrix(n):
    m = n + 1
    return Matrix(m * m, m * m, lambda a, b:
                  entry(divmod(a, m), divmod(b, m)))


def expansions(base_order):
    n = len(base_order)
    for a in range(n + 1):
        first = list(base_order[:a]) + ['x'] + list(base_order[a:])
        for b in range(n + 2):
            full = first[:b] + ['y'] + first[b:]
            gx = sum(not isinstance(z, str) for z in full[:full.index('x')])
            gy = sum(not isinstance(z, str) for z in full[:full.index('y')])
            yield gx, gy, full.index('x') < full.index('y')


def brute_feasibility(n, base_order2):
    m = n + 1
    a = list(expansions(tuple(range(n))))
    b = list(expansions(base_order2))
    feasible = [[0] * (m * m) for _ in range(m * m)]
    for i, k, xy in a:
        for j, ell, uv in b:
            if xy != uv:
                feasible[i * m + j][k * m + ell] = 1
    return feasible


def test_integer_relation_differences(n):
    m = n + 1
    N = m * m
    eye = Matrix.eye(N)
    def col(i, j):
        return eye[:, i*m+j]
    transformed = [col(n, 0)]
    transformed += [col(k, 0)-col(k-1, 0) for k in range(1, m)]
    transformed += [col(0, k)-col(0, k-1) for k in range(1, m)]
    transformed += [col(k, ell)-col(k-1, ell)-col(k, ell-1)+col(k-1, ell-1)
                    for k in range(1, m) for ell in range(1, m)]
    W = Matrix.hstack(*transformed)
    assert abs(W.det()) == 1
    actual = matrix(n)*W
    expect = [Matrix.ones(N, 1)]
    expect += [Matrix(N, 1, lambda a, b: 1 if divmod(a, m)[0] == k
                       and divmod(a, m)[1] >= 1 else 0) for k in range(1, m)]
    expect += [Matrix(N, 1, lambda a, b: 1 if divmod(a, m)[1] == k
                       and divmod(a, m)[0] >= 1 else 0) for k in range(1, m)]
    expect += [-col(k-1, ell-1)-col(k, ell)
               for k in range(1, m) for ell in range(1, m)]
    assert actual == Matrix.hstack(*expect)


def test():
    for n in range(1, 6):
        test_integer_relation_differences(n)
    base_structures = 0
    compared_entries = 0
    for n in range(1, 5):
        m = n + 1
        expected = [[entry(divmod(a, m), divmod(b, m))
                     for b in range(m*m)] for a in range(m*m)]
        for perm in itertools.permutations(range(n)):
            actual = brute_feasibility(n, perm)
            assert actual == expected, (n, perm)
            base_structures += 1
            compared_entries += (m*m) ** 2
    smith_sizes = []
    for n in range(1, 10):
        N = (n + 1) ** 2
        M = matrix(n)
        D = smith_normal_form(M, domain=ZZ)
        diag = Counter(abs(int(D[i, i])) for i in range(N))
        predicted = {1: n*n + n + 1,
                     2: n-1 if n % 2 else 1,
                     0: 1 if n % 2 else n-1}
        for v in (0, 1, 2):
            assert diag[v] == predicted[v], (n, diag, predicted)
        assert set(diag) <= {0, 1, 2}
        smith_sizes.append(n)
    print(json.dumps({"status": "VERIFY_OK", "base_permutations": base_structures,
                      "feasibility_cells_checked": compared_entries,
                      "smith_parameters_checked": smith_sizes}, sort_keys=True))


if __name__ == '__main__':
    test()
