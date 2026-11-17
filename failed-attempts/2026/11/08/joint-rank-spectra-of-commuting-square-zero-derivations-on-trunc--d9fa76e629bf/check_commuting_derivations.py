#!/usr/bin/env python3
"""Independent direct-multiplication checks for commuting square-zero derivations.

Usage: python3 check_commuting_witt_char2.py. Only Python stdlib required.
All matrices use the actual truncated-polynomial basis 1,t,...,t^(N-1).
"""
from itertools import product

IRREDUCIBLE = {2: 0b11, 4: 0b111, 8: 0b1011}


def mul(x, y, q):
    p = IRREDUCIBLE[q]
    e = q.bit_length() - 1
    z = 0
    while y:
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & q:
            x ^= p
    return z & (q - 1)


def derivation_matrix(f, q):
    n = len(f)
    # row-major; D(t^j) = (j modulo 2) t^(j-1) f(t)
    return tuple(tuple(f[i - j + 1] if j % 2 and 0 <= i - j + 1 < n else 0
                       for j in range(n)) for i in range(n))


def mat_product(a, b, q):
    n = len(a)
    return tuple(tuple(_dot(a[i], [b[h][j] for h in range(n)], q)
                       for j in range(n)) for i in range(n))


def _dot(row, col, q):
    s = 0
    for x, y in zip(row, col):
        if x and y:
            s ^= mul(x, y, q)
    return s


def zero_matrix(a):
    return not any(any(row) for row in a)


def census(n, q, arities):
    # For N odd, d(t^N)=t^(N-1)d(t) imposes f_0=0.
    polys = ((0,) + coeff for coeff in product(range(q), repeat=n-1)) if n % 2 else product(range(q), repeat=n)
    mats = []
    coeffs = []
    for f in polys:
        a = derivation_matrix(f, q)
        if zero_matrix(mat_product(a, a, q)):
            mats.append(a)
            coeffs.append(f)
    ell = m = n // 2
    c = (m + 1) // 2
    membership = []
    for f in coeffs:
        a = [f[2*h] for h in range(m)] if n % 2 == 0 else [f[2*h+2] for h in range(m)]
        b = [f[2*h+1] for h in range(m)]
        membership.append(sum(1 << (j-c) for j in range(c, m+1)
                              if all(x == 0 for x in a[:m-j])
                              and all(x == 0 for x in b[:j])))
    assert all(membership), (n, q, "no component")
    adjacency = []
    for a in mats:
        mask = 0
        for j, b in enumerate(mats):
            commutes = mat_product(a, b, q) == mat_product(b, a, q)
            assert commutes == bool(membership[len(adjacency)] & membership[j]), (n, q, "component rigidity", len(adjacency), j)
            if commutes:
                mask |= 1 << j
        adjacency.append(mask)
    # The k-tuples include repeats and zero, as the mathematical formula does.
    observed = {0: 1, 1: len(mats)}
    if max(arities) >= 2:
        observed[2] = sum(mask.bit_count() for mask in adjacency)
    if max(arities) >= 3:
        observed[3] = sum((adjacency[i] & adjacency[j]).bit_count()
                          for i, mask in enumerate(adjacency)
                          for j in range(len(mats)) if mask >> j & 1)
    if max(arities) >= 4:
        observed[4] = sum((adjacency[i] & adjacency[j] & adjacency[k]).bit_count()
                          for i, mask in enumerate(adjacency)
                          for j in range(len(mats)) if mask >> j & 1
                          for k in range(len(mats)) if ((mask & adjacency[j]) >> k) & 1)
    m = n // 2
    ell = m // 2
    expected = {r: q**(m*r) + ell*(q**r-1)*q**((m-1)*r) for r in arities}
    for r in arities:
        assert observed[r] == expected[r], (n, q, r, observed[r], expected[r])
    return observed


def main():
    test_cases = [
        (2, 2, 4), (3, 2, 4), (4, 2, 4), (5, 2, 4),
        (6, 2, 4), (7, 2, 4), (8, 2, 3), (9, 2, 3),
        (4, 4, 3), (5, 4, 3), (6, 4, 2), (7, 4, 2),
        (4, 8, 2), (5, 8, 2),
    ]
    for n, q, rmax in test_cases:
        got = census(n, q, list(range(rmax + 1)))
        print('N=%d q=%d tuple_counts=%s' %
              (n, q, ','.join('%d:%d' % (r, got[r]) for r in sorted(got))))
    print('COMMUTING_SQUARE_ZERO_DERIVATIONS_DIRECT_MATRIX_CHECKS_OK')


if __name__ == '__main__':
    main()


def matrix_rank(matrix, q):
    a = [list(row) for row in matrix]
    nr = len(a)
    h = 0
    for col in range(nr):
        pivot = next((i for i in range(h, nr) if a[i][col]), None)
        if pivot is None:
            continue
        a[h], a[pivot] = a[pivot], a[h]
        scale = a[h][col]
        inv = 1
        for _ in range(q - 2):
            inv = mul(inv, scale, q)
        a[h] = [mul(inv, x, q) for x in a[h]]
        for i in range(nr):
            if i != h and a[i][col]:
                s = a[i][col]
                a[i] = [u ^ mul(s, v, q) for u, v in zip(a[i], a[h])]
        h += 1
        if h == nr:
            break
    return h


def profile_test(n, q, arity):
    m = n//2
    c = (m+1)//2
    polys = ((0,)+x for x in product(range(q), repeat=n-1)) if n%2 else product(range(q), repeat=n)
    mats = []
    for f in polys:
        d = derivation_matrix(f, q)
        if zero_matrix(mat_product(d,d,q)):
            mats.append(d)
    ranks = [matrix_rank(d, q) for d in mats]
    adj = [[mat_product(d,e,q)==mat_product(e,d,q) for e in mats] for d in mats]
    from collections import Counter
    actual = Counter()
    for t in product(range(len(mats)), repeat=arity):
        if all(adj[t[i]][t[j]] for i in range(arity) for j in range(i)):
            actual[tuple(ranks[i] for i in t)] += 1
    formula = Counter()
    for j in range(c, m+1):
        ps = []
        for intersect in (False, True):
            if intersect and j==c:
                ps.append(None)
                continue
            a_len = j-int(intersect)
            b_len = m-j
            bounds = [q**(min(a_len, r)+min(b_len,r)) for r in range(m+1)]
            coeff = [1]+[bounds[r]-bounds[r-1] for r in range(1,m+1)]
            ps.append(coeff)
        for tup in product(range(m+1), repeat=arity):
            val = 1
            for r in tup:
                val *= ps[0][r]
            if j>c:
                neg = 1
                for r in tup:
                    neg *= ps[1][r]
                val -= neg
            formula[tup] += val
    assert {k:v for k,v in actual.items() if v} == {k:v for k,v in formula.items() if v}, (n,q,arity,actual,formula)
    print('PROFILE_N=%d q=%d arity=%d tuples=%d rank_profiles=%d' %
          (n,q,arity,sum(actual.values()),len(actual)))


if __name__ == '__main__':
    for cfg in [(4,2,3),(6,2,3),(8,2,3),(6,4,2),(4,8,2)]:
        profile_test(*cfg)
    print('COMPLETE_MULTIVARIATE_RANK_PROFILE_CHECKS_OK')
