"""Checks for the composition-square-root spectrum in cubic jet algebras.

Only prime fields are enumerated. The general result is proved algebraically.
Run with Python 3 and no external dependencies.
"""
from itertools import product
from math import prod


def monomials(d):
    return [(i, j) for i in range(d) for j in range(i, d)]


def rank(a, p):
    if not a:
        return 0
    a = [[x % p for x in row] for row in a]
    n, m = len(a), len(a[0]); r = 0
    for col in range(m):
        t = next((i for i in range(r, n) if a[i][col]), None)
        if t is None:
            continue
        a[r], a[t] = a[t], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(n):
            if i != r and a[i][col]:
                z = a[i][col]
                a[i] = [(x - z * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def symmetric_square(B, p):
    d = len(B); mm = monomials(d); P = len(mm)
    out = [[0] * P for _ in range(P)]
    for index, (j, k) in enumerate(mm):
        for t, (a, b) in enumerate(mm):
            out[index][t] = (B[j][a] * B[k][b] if a == b
                             else B[j][a] * B[k][b] + B[j][b] * B[k][a]) % p
    return out


def actual_composition(B, Q, p):
    d = len(B); P = len(monomials(d)); R = symmetric_square(B, p)
    rows = []
    for i in range(d):
        linear = [sum(B[i][j] * B[j][k] for j in range(d)) % p for k in range(d)]
        quadratic = [(sum(B[i][j] * Q[j][k] for j in range(d)) +
                      sum(Q[i][j] * R[j][k] for j in range(P))) % p
                     for k in range(P)]
        rows.append(linear + quadratic)
    return rows


def radical_rank(B, Q, p):
    d = len(B); P = len(monomials(d)); R = symmetric_square(B, p)
    return rank([B[i] + Q[i] for i in range(d)] +
                [[0] * d + R[i] for i in range(P)], p)


def number_squarezero_linear(d, r, q):
    def gb(n, k):
        out = 1
        for i in range(k):
            out = out * (q ** (n - i) - 1) // (q ** (i + 1) - 1) if False else out
        num = prod(q ** (n - i) - 1 for i in range(k))
        den = prod(q ** (k - i) - 1 for i in range(k))
        return num // den
    gl = prod(q ** r - q ** i for i in range(r))
    return gb(d, r) * gb(d-r, r) * gl


def predict(d, r, q):
    s = d * (d + 1) // 2
    c = r * (r + 1) // 2
    a = d - 2 * r
    b = s - 2 * c
    H = (d-r) * s - a * c
    return number_squarezero_linear(d, r, q), H, (r+c, r+c+min(a,b))


def solve_constraint(d, q, B):
    P = len(monomials(d)); N = d * P
    columns = []
    for i in range(d):
        for j in range(P):
            Q = [[0] * P for _ in range(d)]
            Q[i][j] = 1
            columns.append([y for row in actual_composition(B, Q, q)
                            for y in row[d:]])
    return N - rank([list(x) for x in zip(*columns)], q)


def check_fiber_dimensions():
    for d in range(1, 7):
        for r in range(d // 2 + 1):
            B = [[0] * d for _ in range(d)]
            for j in range(r):
                B[j][r + j] = 1
            for p in (2, 3, 5):
                assert solve_constraint(d, p, B) == predict(d, r, p)[1]
    print('FIBER_RANKS_OK: d=1..6, prime fields 2,3,5')


def check_direct():
    for p in (2, 3):
        d = 2; P = len(monomials(d)); totals = {}; rank_counts = {}
        for entries in product(range(p), repeat=d*d+d*P):
            B = [list(entries[i*d:(i+1)*d]) for i in range(d)]
            off = d*d
            Q = [list(entries[off+i*P:off+(i+1)*P]) for i in range(d)]
            if any(any(v for v in row) for row in actual_composition(B, Q, p)):
                continue
            r = rank(B, p)
            totals[r] = totals.get(r, 0) + 1
            t = radical_rank(B, Q, p)
            rank_counts[t] = rank_counts.get(t, 0) + 1
        for r in range(2):
            N, H, _ = predict(d, r, p)
            assert totals.get(r, 0) == N * p**H, (p, r, totals)
        expected = {2: {0: 1, 1: 21, 2: 66},
                    3: {0: 1, 1: 104, 2: 840}}[p]
        assert rank_counts == expected, (p, rank_counts)
        print('DIRECT_OK: field=%d, fibers=%s, radical-ranks=%s' % (p, totals, rank_counts))


def rank_gaps():
    for d in range(2, 17):
        support = set()
        for r in range(d//2+1):
            _, _, (lo, hi) = predict(d, r, 2)
            support.update(range(lo, hi + 1))
        gaplist = [i for i in range(max(support)+1) if i not in support]
        predicted = []
        for r in range(d//2):
            high = d + r*(r-1)//2
            low_next = (r+1)*(r+4)//2
            predicted.extend(range(high+1, low_next))
        assert gaplist == predicted, (d, gaplist, predicted)
    print('GAP_INTERVALS_OK: d=2..16')


if __name__ == '__main__':
    check_fiber_dimensions()
    check_direct()
    rank_gaps()
    print('VERIFY_OK')
