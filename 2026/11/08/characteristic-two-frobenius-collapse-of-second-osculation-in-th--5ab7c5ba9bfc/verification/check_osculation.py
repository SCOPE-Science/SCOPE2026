#!/usr/bin/env python3
"""Independent Hasse-jet rank checks for the truncated-simplex monomial embedding.

No symbolic derivative division is used: all entries are integer binomial products,
reduced modulo the indicated characteristic where appropriate.
"""
from itertools import combinations_with_replacement
from math import comb
from fractions import Fraction


def monomial_exponents(n):
    out = []
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                continue
            ex = [0] * n
            if i > 0:
                ex[i - 1] += 2
            if j > 0:
                ex[j - 1] += 1
            out.append(tuple(ex))
    assert len(out) == n * (n + 1)
    assert len(set(out)) == len(out)
    return out


def multiindices(n, order):
    rows = [tuple([0] * n)]
    for degree in range(1, order + 1):
        for indices in combinations_with_replacement(range(n), degree):
            row = [0] * n
            for i in indices:
                row[i] += 1
            rows.append(tuple(row))
    return rows


def jets(n, order):
    exps = monomial_exponents(n)
    return [[__import__('math').prod(comb(e, a) for e, a in zip(exp, alpha))
             for exp in exps] for alpha in multiindices(n, order)]


def rank_modp(matrix, p):
    a = [[value % p for value in row] for row in matrix]
    m, n = len(a), len(a[0])
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot], a[r] = a[r], a[pivot]
        scale = pow(a[r][col], -1, p)
        a[r] = [scale * v % p for v in a[r]]
        for i in range(m):
            if i == r or a[i][col] == 0:
                continue
            c = a[i][col]
            a[i] = [(x - c*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def rank_q(matrix):
    a = [[Fraction(value) for value in row] for row in matrix]
    m, n = len(a), len(a[0])
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot], a[r] = a[r], a[pivot]
        scale = a[r][col]
        a[r] = [v/scale for v in a[r]]
        for i in range(r + 1, m):
            if a[i][col]:
                c = a[i][col]
                a[i] = [x - c*y for x,y in zip(a[i],a[r])]
        r += 1
        if r == m:
            break
    return r


def expected(n, p, order):
    if order == 0:
        return 1
    if order == 1:
        return n + 1
    if order == 2:
        return 2*n + (1 if p == 2 else comb(n, 2))
    if order == 3:
        return n*(n + 1)
    raise ValueError(order)


def main():
    checks = 0
    for n in range(2, 9):
        rows = [jets(n, order) for order in range(4)]
        for p in (2, 3, 5, 7):
            actual = tuple(rank_modp(x, p) for x in rows)
            wanted = tuple(expected(n, p, order) for order in range(4))
            assert actual == wanted, (n, p, actual, wanted)
            checks += 1
        print(f'n={n} char2-second-rank={expected(n,2,2)} odd-second-rank={expected(n,3,2)} third-rank={n*(n+1)}')
    for n in range(2, 6):
        rows = [jets(n, order) for order in range(4)]
        actual = tuple(rank_q(x) for x in rows)
        wanted = tuple(expected(n, 3, order) for order in range(4))
        assert actual == wanted, (n, actual, wanted)
        checks += 1
    for n in range(2, 9):
        exps = monomial_exponents(n)
        squares = [tuple(2 if j == i else 0 for j in range(n)) for i in range(n)]
        square_row_indices = [multiindices(n, 2).index(alpha) for alpha in squares]
        M = jets(n, 2)
        for i in range(n):
            # section t_i^2 is obtained from x_i^2 x_0.
            section_index = next(j for j, pair in enumerate(exps) if pair == squares[i])
            assert M[square_row_indices[i]][section_index] % 2 == 1
            for other in range(n):
                if other != i:
                    assert M[square_row_indices[other]][section_index] % 2 == 0
        for alpha, row in zip(multiindices(n, 2), M):
            if sum(alpha) == 2 and max(alpha) == 1:
                assert all(value % 2 == 0 for value in row)
    print(f'EXACT_RANK_TESTS={checks}')
    print('CHARACTERISTIC_TWO_QUADRATIC_FORMS_ARE_INDEPENDENT_SQUARES')
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
