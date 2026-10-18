#!/usr/bin/env python3
"""Exact certificate for quartic-graph unimodular fourth-moment phase equality at 13.
Public reproducibility checker; standard library only.
"""
from collections import Counter, defaultdict
from itertools import combinations

P = 13

def relation_data():
    fibers = defaultdict(list)
    for x in range(P):
        for y in range(x, P):
            fibers[((x + y) % P, (pow(x, 4, P) + pow(y, 4, P)) % P)].append((x, y))
    rows, names = [], []
    for key, pairs in sorted(fibers.items()):
        for x, y in pairs[1:]:
            a, b = pairs[0]
            v = [0] * P
            for i in (x, y):
                v[i] += 1
            for i in (a, b):
                v[i] -= 1
            rows.append(v)
            names.append((a, b, x, y, key))
    return fibers, rows, names

def determinant(rows):
    n = len(rows)
    if n == 0:
        return 1
    a = [r[:] for r in rows]
    if any(len(r) != n for r in a):
        raise ValueError("not square")
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]

def modrank(rows, mod):
    a = [[v % mod for v in row] for row in rows]
    n = len(a)
    m = len(a[0]) if n else 0
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, mod)
        a[r] = [(x * inv) % mod for x in a[r]]
        for i in range(n):
            if i == r:
                continue
            h = a[i][col]
            if h:
                a[i] = [(x - h * y) % mod for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r

def minor(rows, ri, ci):
    return determinant([[rows[i][j] for j in ci] for i in ri])

def run():
    fibers, rows, names = relation_data()
    assert len(fibers) == 76
    assert Counter(map(len, fibers.values())) == {1: 61, 2: 15}
    assert len(rows) == len(names) == 15
    expected = [
        (1, 12, 5, 8), (4, 9, 6, 7), (2, 11, 3, 10),
        (5, 9, 6, 8), (3, 12, 5, 10), (1, 2, 5, 11),
        (6, 11, 7, 10), (1, 4, 6, 12), (2, 4, 9, 10),
        (3, 4, 9, 11), (1, 7, 9, 12), (2, 7, 3, 6),
        (2, 8, 11, 12), (1, 10, 3, 8), (4, 8, 5, 7),
    ]
    assert [lab[:4] for lab in names] == expected
    energy = sum(sum(1 if x == y else 2 for x, y in pairs) ** 2 for pairs in fibers.values())
    assert energy == 445
    values = sorted({pow(t, 4, P) for t in range(P)})
    assert values == [0, 1, 3, 9]
    # Verify the Singer perfect-difference-set property and its pair-sum consequence.
    differences = [(u - v) % P for u in values for v in values if u != v]
    assert sorted(differences) == list(range(1, P))
    pair_sums = [(u + v) % P for i, u in enumerate(values) for v in values[i:]]
    assert len(pair_sums) == len(set(pair_sums)) == 10
    for pairs in fibers.values():
        if len(pairs) > 1:
            image_pairs = [tuple(sorted((pow(x, 4, P), pow(y, 4, P)))) for x, y in pairs]
            assert len(set(image_pairs)) == 1
    # Four explicit integer nullvectors: indicator functions of quartic-value fibers.
    for val in values:
        vv = [int(pow(t, 4, P) == val) for t in range(P)]
        assert all(sum(a * b for a, b in zip(row, vv)) == 0 for row in rows)
    # Additive characters give one further kernel vector modulo 13.
    assert all(sum(row[t] * t for t in range(P)) % P == 0 for row in rows)
    r8 = [0, 4, 5, 8, 9, 10, 11, 14]
    c8 = [2, 3, 4, 6, 8, 9, 11, 12]
    r9 = [0, 1, 2, 7, 8, 11, 12, 13, 14]
    c9 = [2, 3, 4, 5, 6, 8, 9, 10, 12]
    assert minor(rows, r8, c8) == 1
    assert minor(rows, r9, c9) == 13
    # The first four indicators are independent over Q and F13; t is independent
    # from them modulo 13 because it is nonconstant on every nonzero fiber.
    assert modrank(rows, 13) == 8
    assert modrank(rows, 2) == 9
    # The exact Smith determinantal divisors are delta_8=1, delta_9=13:
    # rank_Q <=9 from the four displayed integer nullvectors and >=9
    # from the minor 13. Modulo 13 rank 8 forces 13 to divide every
    # 9x9 minor; the exhibited determinant 13 forces delta_9=13.
    # Therefore the cokernel is Z^4 + Z/13, proving exhaustive phases.
    assert all(sum(v * ((t * 7 + values.index(pow(t, 4, P)) * 2) % P)
                   for t, v in enumerate(row)) % P == 0 for row in rows)
    assert any(sum(v * (1 if t == 1 else 0) for t, v in enumerate(row)) % P
               for row in rows)
    print("VERIFY_OK prime=13 fibers=76 nontrivial_fibers=15 energy=445"
          " rank_Q=9 rank_mod13=8 delta8=1 delta9=13 phase_components=13 torus_dimension=4")

if __name__ == "__main__":
    run()
