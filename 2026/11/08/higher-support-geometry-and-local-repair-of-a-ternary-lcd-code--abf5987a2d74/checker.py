#!/usr/bin/env python3
"""Exact, standard-library-only check of the printed ternary [25,5,14] code.
Run: python3 checker.py
"""
from collections import Counter
from itertools import combinations, product

Q = 3
GENERATOR_ROWS = (
    '1000022000110211122121020',
    '0100000222100112111112121',
    '0010021220202220021120200',
    '0001020211122201101002100',
    '0000111102112001011121222',
)
G = tuple(tuple(int(c) for c in row) for row in GENERATOR_ROWS)
assert len(G) == 5 and all(len(row) == 25 for row in G)
COLS = tuple(tuple(G[i][j] for i in range(5)) for j in range(25))


def rank_mod3(a):
    a = [list(row) for row in a]
    if not a:
        return 0
    k, n, r = len(a), len(a[0]), 0
    for j in range(n):
        pivot = next((i for i in range(r, k) if a[i][j] % Q), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = 1 if a[r][j] % Q == 1 else 2
        a[r] = [(x * inv) % Q for x in a[r]]
        for i in range(k):
            if i != r and a[i][j] % Q:
                z = a[i][j] % Q
                a[i] = [(a[i][u] - z * a[r][u]) % Q for u in range(n)]
        r += 1
        if r == k:
            break
    return r


def image(v):
    return tuple(sum(v[i] * G[i][j] for i in range(5)) % Q for j in range(25))


def normalized(col):
    pivot = next(x for x in col if x)
    inv = 1 if pivot == 1 else 2
    return tuple(inv * x % Q for x in col)


def rref_subspaces(k, r):
    # Every r-plane in F_3^k has precisely one reduced row-echelon basis.
    for pivots in combinations(range(k), r):
        free = [(i, j) for i, p in enumerate(pivots)
                for j in range(p + 1, k) if j not in pivots]
        for vals in product(range(Q), repeat=len(free)):
            B = [[0] * k for _ in range(r)]
            for i, p in enumerate(pivots):
                B[i][p] = 1
            for (i, j), value in zip(free, vals):
                B[i][j] = value
            yield B


def support_size(B):
    # All possible codewords in this subcode are spanned by rows BG.
    return sum(any(sum(row[i] * G[i][j] for i in range(5)) % Q
                   for row in B) for j in range(25))


def verify():
    assert rank_mod3(G) == 5
    gram = [[sum(G[i][u] * G[j][u] for u in range(25)) % Q
             for j in range(5)] for i in range(5)]
    assert rank_mod3(gram) == 5
    projective = [normalized(col) for col in COLS]
    assert len(set(projective)) == 25

    weights = Counter(sum(x != 0 for x in image(v))
                      for v in product(range(Q), repeat=5))
    expected_weights = {0: 1, 14: 22, 15: 56, 16: 62, 17: 32,
                        18: 20, 19: 24, 20: 12, 21: 4, 22: 4, 23: 6}
    assert dict(weights) == expected_weights and sum(weights.values()) == 243

    expected_supports = {
        1: {14:11, 15:28, 16:31, 17:16, 18:10, 19:12,
            20:6, 21:2, 22:2, 23:3},
        2: {19:6, 20:87, 21:291, 22:326, 23:216, 24:205, 25:79},
        3: {22:15, 23:255, 24:445, 25:495},
        4: {24:25, 25:96},
        5: {25:1},
    }
    for r, target in expected_supports.items():
        actual = Counter(support_size(B) for B in rref_subspaces(5, r))
        assert dict(actual) == target, (r, actual)
        assert sum(actual.values()) == {1:121, 2:1210, 3:1210, 4:121, 5:1}[r]
        if r == 1:
            assert all(weights[wt] == 2*number for wt, number in target.items())
    assert [min(d) for d in expected_supports.values()] == [14,19,22,24,25]

    # Independent low-weight dual test using explicit nonzero relations.
    # Any dual word supported on J has coefficient vector c with
    # sum(c_j G[:,j])=0; all coefficients are in {1,2} over F_3.
    def dependent_full(J):
        for tail in product((1, 2), repeat=len(J) - 1):
            coefs = (1,) + tail
            if all(sum(coefs[u] * COLS[J[u]][i]
                       for u in range(len(J))) % 3 == 0
                   for i in range(5)):
                return True
        return False

    assert not any(dependent_full((j,)) for j in range(25))
    assert not any(dependent_full(J) for J in combinations(range(25), 2))
    triples = [J for J in combinations(range(25), 3) if dependent_full(J)]
    assert len(triples) == 15
    triple_degree = Counter(j for J in triples for j in J)
    assert [j+1 for j in range(25) if not triple_degree[j]] == [1,7,9,10]
    assert dict(Counter(triple_degree[j] for j in range(25))) == {0:4,1:5,2:10,3:4,4:2}
    quads = [J for J in combinations(range(25), 4) if dependent_full(J)]
    assert len(quads) == 486
    quad_degree = Counter(j for J in quads for j in J)
    assert all(quad_degree[j] > 0 for j in range(25))
    assert sorted(quad_degree[j] for j in (0, 6, 8, 9)) == [83,85,87,87]
    # No four points lie on a projective line, by the r=3 support bound.
    # Therefore every four-support dual vector is unique up to scaling.
    assert sum(quad_degree.values()) == 4 * 486
    assert sum(triple_degree.values()) == 3 * 15
    # 15 collinear triples give exactly 30 weight-3 dual words;
    # 486 four-point circuits give exactly 972 weight-4 dual words.
    print('PASS: generator dimension 5; LCD Gram invertible; 25 distinct projective columns')
    print('PASS: all 243 codewords, all 2663 nonzero subcodes and exact support census')
    print('PASS: weights (14,19,22,24,25); exactly 15 triple and 486 quadruple dual supports')
    print('PASS: localities 2 for 21 coordinates, 3 for coordinates 1,7,9,10')


if __name__ == '__main__':
    verify()
