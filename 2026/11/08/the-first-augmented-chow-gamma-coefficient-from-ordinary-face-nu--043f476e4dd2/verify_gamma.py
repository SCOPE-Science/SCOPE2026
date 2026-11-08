#!/usr/bin/env python3
"""Independent exact checks for low-degree augmented-Chow gamma statements.

Only Python's standard library is used. Source-defined gamma evaluations are
compared with simplex flag-chain enumeration and ab/cd conversion.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
from itertools import product


def add(*polys):
    z = {}
    for p in polys:
        for k, v in p.items():
            z[k] = z.get(k, 0) + v
    return {k: v for k, v in z.items() if v}


def scale(p, c):
    return {k: v * c for k, v in p.items() if v * c}


def multiply(p, q):
    z = {}
    for a, u in p.items():
        for b, v in q.items():
            z[a + b] = z.get(a + b, 0) + u * v
    return {k: v for k, v in z.items() if v}


def power_t(k):
    return {k: 1}


def T(k):
    if k % 2 == 0:
        return {}
    q = (k - 1) // 2
    catalan = comb(2 * q, q) // (q + 1)
    return {q: ((-1) ** q) * catalan}


def little_s(k):
    return add({0: 1}, multiply({1: 1}, add(*(T(j) for j in range(1, k + 1)))))


def gamma_word(w):
    k = [len(x) for x in w.split('d')]
    r = len(k) - 1
    result = {}
    for ell in range(r + 1):
        p = little_s(k[ell])
        for j in range(ell + 1, r + 1):
            p = multiply(p, T(k[j] + 1))
        result = add(result, scale(p, 2 ** ell))
    return multiply(power_t(r), result)


@lru_cache(None)
def cd_words(n):
    if n == 0:
        return ('',)
    words = ['c' + w for w in cd_words(n-1)]
    if n >= 2:
        words.extend('d' + w for w in cd_words(n-2))
    return tuple(words)


def ab_expansion(w):
    v = {'': 1}
    for letter in w:
        expansions = ('a', 'b') if letter == 'c' else ('ab', 'ba')
        q = {}
        for prefix, count in v.items():
            for suffix in expansions:
                q[prefix+suffix] = q.get(prefix+suffix, 0) + count
        v = q
    return v


def simplex_flag_f(n, mask):
    ranks = [j + 1 for j in range(n) if (mask >> j) & 1]
    boundaries = [0] + ranks + [n + 1]
    parts = [boundaries[i+1]-boundaries[i] for i in range(len(boundaries)-1)]
    return factorial(n+1) // __import__('math').prod(factorial(p) for p in parts)


def solve(A, b):
    # Overdetermined exact rational linear system, with independent equations.
    m, k = len(A), len(A[0])
    matrix = [[Fraction(x) for x in row] + [Fraction(rhs)] for row, rhs in zip(A, b)]
    pivot_rows = []
    rr = 0
    for cc in range(k):
        pivot = next((z for z in range(rr, m) if matrix[z][cc]), None)
        assert pivot is not None, 'dependent cd-monomials'
        matrix[rr], matrix[pivot] = matrix[pivot], matrix[rr]
        den = matrix[rr][cc]
        matrix[rr] = [v / den for v in matrix[rr]]
        for i in range(m):
            if i != rr and matrix[i][cc]:
                mul = matrix[i][cc]
                matrix[i] = [x - mul*y for x, y in zip(matrix[i], matrix[rr])]
        pivot_rows.append(rr)
        rr += 1
    for row in matrix:
        if all(v == 0 for v in row[:k]):
            assert row[k] == 0, 'inconsistent ab-to-cd expansion'
    return [matrix[rr][k] for rr in pivot_rows]


def simplex_cd_index(n):
    words = [''.join(t) for t in product('ab', repeat=n)]
    basis = cd_words(n)
    f = {mask: simplex_flag_f(n, mask) for mask in range(1 << n)}
    h = {mask: sum((-1) ** (mask.bit_count()-subset.bit_count()) * f[subset]
                   for subset in f if (subset & mask) == subset) for mask in f}
    b = [h[sum(1 << i for i, letter in enumerate(w) if letter == 'b')]
         for w in words]
    exps = [ab_expansion(w) for w in basis]
    A = [[e.get(w, 0) for e in exps] for w in words]
    vals = solve(A, b)
    assert all(v.denominator == 1 for v in vals)
    return dict(zip(basis, (int(v) for v in vals)))


def run():
    expected_cd = {
        1: {'c': 1},
        2: {'cc': 1, 'd': 1},
        3: {'ccc': 1, 'cd': 2, 'dc': 2},
        4: {'cccc': 1, 'ccd': 3, 'cdc': 5, 'dcc': 3, 'dd': 4},
    }
    expected_gamma = {
        1: {0: 1, 1: 1},
        2: {0: 1, 1: 4},
        3: {0: 1, 1: 11, 2: 5},
        4: {0: 1, 1: 26, 2: 43},
    }
    checks = 0
    for n in range(1, 5):
        cd = simplex_cd_index(n)
        assert cd == expected_cd[n], (n, cd)
        checks += 1
        gamma = add(*(scale(gamma_word(w), a) for w, a in cd.items()))
        assert gamma == expected_gamma[n], (n, gamma)
        checks += 1
        for w in cd_words(n):
            gw = gamma_word(w)
            assert gw.get(0, 0) == (1 if w == 'c'*n else 0)
            assert (w == 'c'*n or all(v >= 0 for v in gw.values()))
            checks += 2
    for n in range(2, 30):
        assert gamma_word('c' * n).get(1, 0) == 1
        checks += 1
        for j in range(n-1):
            w = 'c'*j + 'd' + 'c'*(n-j-2)
            assert gamma_word(w).get(1,0) == (3 if j == n-2 else 2), (n,j)
            checks += 1
        g_simplex = 2 ** (n+1) - n - 2
        assert sum(comb(n+1,j+1) for j in range(n)) + (n+1) - 2*n - 1 == g_simplex
        checks += 1
    for m in range(3, 31):
        polygon_gamma = add(gamma_word('cc'), scale(gamma_word('d'),m-2))
        assert polygon_gamma == {0:1,1:3*m-5}
        checks += 1
    cube_right = add(gamma_word('ccc'), scale(gamma_word('dc'), 6),
                     scale(gamma_word('cd'), 4))
    cube_left = add(gamma_word('ccc'), scale(gamma_word('dc'), 4),
                    scale(gamma_word('cd'), 6))
    assert cube_right == {0: 1, 1: 25, 2: 15}
    assert cube_left == {0: 1, 1: 27, 2: 13}
    assert cube_right[1] - cube_left[1] == 6 - 8
    checks += 3
    assert gamma_word('cccd').get(3,0) < 0
    print('PASS', checks, 'exact checks; simplexes 1..4;',
          'all one-d first-gamma word coefficients through degree 29;',
          'polygons with 3..30 vertices; negative gamma degree-3 word in degree 5')


if __name__ == '__main__':
    run()
