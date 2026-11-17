#!/usr/bin/env python3
"""Dependency-free checks for ordered binary-parity wheel dynamics."""
from collections import Counter
from functools import reduce


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def divrem(a, b):
    if not b:
        raise ZeroDivisionError
    q = 0
    while a and a.bit_length() >= b.bit_length():
        d = a.bit_length() - b.bit_length()
        q ^= 1 << d
        a ^= b << d
    return q, a


def gcd(a, b):
    while b:
        _, r = divrem(a, b)
        a, b = b, r
    return a


def detpoly(matrix):
    m = [r.copy() for r in matrix]
    n = len(m)
    for k in range(n):
        nonzero = [j for j in range(k, n) if m[j][k]]
        if not nonzero:
            return 0
        pivot = min(nonzero, key=lambda j: m[j][k].bit_length())
        m[k], m[pivot] = m[pivot], m[k]
        j = k + 1
        while j < n:
            if not m[j][k]:
                j += 1
                continue
            q, remainder = divrem(m[j][k], m[k][k])
            if q:
                for c in range(k, n):
                    m[j][c] ^= mul(q, m[k][c])
            if remainder:
                m[k], m[j] = m[j], m[k]
                j = k + 1
            else:
                j += 1
    return reduce(mul, (m[i][i] for i in range(n)), 1)


def wheel(n):
    size = n + 1
    adj = [[0] * size for _ in range(size)]
    for i in range(1, size):
        adj[0][i] = adj[i][0] = 1
        j = (i % n) + 1
        adj[i][j] = adj[j][i] = 1
    return adj


def sweep_matrix(n):
    a = wheel(n)
    rows = [1 << i for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if a[i][j]:
                rows[i] ^= rows[j]
    return rows


def predicted(n):
    p = (1 << (n + 1)) | 1
    for j in range(3, n - 1):
        p ^= 1 << j
    if n % 4 in (0, 3):
        p ^= (1 << n) | (1 << 1)
    return p


def char_direct(n):
    a = wheel(n)
    m = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                m[i][j] = 3  # 1+t
            elif a[i][j]:
                m[i][j] = 2 if i > j else 1
    return detpoly(m)


def mmul(a, b):
    return [reduce(int.__xor__, (b[j] for j in range(len(b)) if (row >> j) & 1), 0)
            for row in a]


def rank(rows):
    basis = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = row
                break
            row ^= basis[pivot]
    return len(basis)


def mpow(a, power):
    cur = [1 << i for i in range(len(a))]
    while power:
        if power & 1:
            cur = mmul(a, cur)
        a = mmul(a, a)
        power >>= 1
    return cur


def minpoly(a):
    n = len(a)
    cur = [1 << i for i in range(n)]
    basis = {}
    for k in range(n + 1):
        v = sum(r << (i * n) for i, r in enumerate(cur))
        coef = 1 << k
        while v:
            p = v.bit_length() - 1
            if p not in basis:
                basis[p] = (v, coef)
                break
            oldv, oldc = basis[p]
            v ^= oldv
            coef ^= oldc
        else:
            return coef
        cur = mmul(a, cur)
    raise AssertionError('minimal polynomial degree too large')


def fixed_dim(n, d):
    a = sweep_matrix(n)
    a = mpow(a, d)
    return n + 1 - rank([row ^ (1 << i) for i, row in enumerate(a)])


def predicted_dim(n, d):
    p = predicted(n)
    bonus = 0
    if n % 4 == 0:
        # Divide out the two trivial 1-dimensional modules.
        p, remainder = divrem(p, 0b101)
        assert remainder == 0
        bonus = 2
    return bonus + gcd(p, (1 << d) | 1).bit_length() - 1


def brute_cycles(n):
    a = wheel(n)
    neighbors = [[j for j in range(n + 1) if a[i][j]] for i in range(n + 1)]
    def update(x):
        for i, nbrs in enumerate(neighbors):
            if sum((x >> j) & 1 for j in nbrs) % 2:
                x ^= 1 << i
        return x
    marked = set()
    dist = Counter()
    for start in range(1 << (n + 1)):
        if start in marked:
            continue
        x = start
        orbit = []
        while x not in marked:
            marked.add(x)
            orbit.append(x)
            x = update(x)
        assert x == start, 'invertible sweep should be a permutation'
        dist[len(orbit)] += 1
    return dict(sorted(dist.items()))


def main():
    for n in range(4, 26):
        assert predicted(n) == char_direct(n), n
    print('PASS: independent polynomial-matrix determinants n=4..25 (22 cases)', flush=True)
    for n in range(4, 81):
        p = predicted(n)
        want_min = p
        if n % 4 == 0:
            want_min, rem = divrem(p, 0b101)
            assert rem == 0
        assert minpoly(sweep_matrix(n)) == want_min, n
        for d in (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 20, 24, 30):
            assert fixed_dim(n, d) == predicted_dim(n, d), (n, d)
    print('PASS: direct matrix minimal polynomials n=4..80 (77 cases)', flush=True)
    print('PASS: 1078 independently ranked fixed-power spaces', flush=True)
    states = 0
    for n in range(4, 11):
        cycles = brute_cycles(n)
        states += 1 << (n + 1)
        assert sum(k * v for k, v in cycles.items()) == 1 << (n + 1)
        for d in range(1, 31):
            fixed = sum(length * count for length, count in cycles.items() if d % length == 0)
            assert fixed == (1 << predicted_dim(n, d)), (n, d)
        print('rim', n, 'primitive-orbit counts', cycles, flush=True)
    print('PASS: direct functional-graph enumeration n=4..10 (' + str(states) + ' states)', flush=True)


if __name__ == '__main__':
    main()
