"""Standalone finite-field checks for rank rigidity of quadratic augmentation symbols.
Python 3 standard library. Run: python verify.py
"""
from itertools import combinations, product
from collections import Counter
import random


def field_mul(a, b, q):
    if q == 2: return a & b
    if q != 4: raise ValueError('only GF(2), GF(4) in the verifier')
    p = 0
    while b:
        if b & 1: p ^= a
        b >>= 1
        a <<= 1
        if a & 4: a ^= 7
    return p


def rank(rows, ncols, q):
    rows = [list(x) for x in rows]
    pivot_row = 0
    for j in range(ncols):
        z = next((i for i in range(pivot_row, len(rows)) if rows[i][j]), None)
        if z is None: continue
        rows[z], rows[pivot_row] = rows[pivot_row], rows[z]
        u = rows[pivot_row][j]
        if q == 4:
            inv = next(a for a in (1, 2, 3) if field_mul(a, u, q) == 1)
            rows[pivot_row] = [field_mul(t, inv, q) for t in rows[pivot_row]]
        for i in range(pivot_row + 1, len(rows)):
            a = rows[i][j]
            if a:
                rows[i] = [x ^ field_mul(a, y, q) for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows): break
    return pivot_row


def mult_rank(n, coeff, q):
    # Basis elements indexed by squarefree bitmasks; product is 0 on intersections.
    N = 1 << n
    mat = [[0] * N for _ in range(N)]
    for a, c in coeff.items():
        if not c: continue
        for b in range(N):
            if a & b == 0: mat[a | b][b] ^= c
    return rank(mat, N, q)


def quadratic_rank(n, coeff, q):
    b = [[0] * n for _ in range(n)]
    for i, j in combinations(range(n), 2):
        v = coeff.get((1 << i) | (1 << j), 0)
        b[i][j] = v; b[j][i] = v
    return rank(b, n, q)


def predicted(n, coeff, q):
    r2 = quadratic_rank(n, coeff, q)
    assert r2 % 2 == 0
    r = r2 // 2
    return (2 ** n - 2 ** (n - r)) // 2, n - 2 * r


def coefficients(n, vec, q):
    masks = [m for m in range(1 << n) if m.bit_count() >= 2]
    return dict(zip(masks, vec))


def test_exhaustive_four():
    n, q = 4, 2
    distribution = Counter()
    parts = Counter()
    for bits in range(1 << 11):
        c = coefficients(n, [(bits >> i) & 1 for i in range(11)], q)
        got = mult_rank(n, c, q)
        formula, k = predicted(n, c, q)
        if k <= 2: assert got == formula, (c, got, formula)
        distribution[got] += 1
        parts[(k, got)] += 1
    assert distribution == {0:1, 1:1, 2:30, 4:1120, 6:896}, distribution
    assert sum(distribution.values()) == 2**11
    print('n=4 GF(2) exhaustive', sorted(distribution.items()))


def test_quadratic_forms_over_four():
    n, q = 4, 4
    masks = [m for m in range(1<<n) if m.bit_count()==2]
    counts = Counter()
    for vals in product(range(q), repeat=len(masks)):
        c = dict(zip(masks, vals))
        counts[quadratic_rank(n, c, q)] += 1
    assert counts == {0:1, 2:1071, 4:3024}, counts
    print('n=4 GF(4) alternating ranks',sorted(counts.items()))


def test_sampled():
    rand = random.Random(20261106)
    for q in (2,4):
        for n in (3,4,5,6):
            for _ in range(70 if n < 6 else 35):
                # Generate random symplectic canonical quadratic with r pairs,
                # and unrestricted higher-degree coefficients.
                r = rand.randint(0, n//2)
                c = {3 << (2*j):1 for j in range(r)}
                for m in range(1<<n):
                    if m.bit_count() >= 3: c[m] = rand.randrange(q)
                f, k = predicted(n, c, q)
                if k <= 2: assert mult_rank(n, c, q) == f, (q,n,r)
            print('sampled:', q, n)


def test_sharpness():
    for r in range(4):
        for k in range(3,6):
            n = 2*r+k
            if n > 9: continue
            omega = {3 << (2*j):1 for j in range(r)}
            cubic = 7 << (2*r)
            got0 = mult_rank(n, omega, 2)
            got1 = mult_rank(n, dict(omega, **{}) | {cubic:1}, 2)
            target0 = (2**n-2**(n-r))//2
            target1 = target0+2**(r+k-3)
            assert (got0,got1)==(target0,target1), (n,r,k,got0,got1,target0,target1)
            print('sharp:',n,r,k,got0,got1)

if __name__ == '__main__':
    test_exhaustive_four()
    test_quadratic_forms_over_four()
    test_sampled()
    test_sharpness()
    print('VERIFY_OK')
