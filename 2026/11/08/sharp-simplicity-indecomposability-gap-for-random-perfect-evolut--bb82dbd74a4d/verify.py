"""Finite-field verification of connected-support and one-way-cut counts.

Usage: python verify.py
All enumeration ranges are complete for the listed finite fields and matrix sizes.
"""
from itertools import product
from math import comb


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    p = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                p ^= 1 << (i + j)
    if p & 8:
        p ^= 0b1110  # x(x^2+x+1)
    if p & 4:
        p ^= 0b111  # x^2+x+1
    return p


def inv(a, q):
    assert a
    return next(b for b in range(1, q) if mul(a, b, q) == 1)


def nonsingular(mat, q):
    n = len(mat)
    a = [list(row) for row in mat]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return False
        a[j], a[pivot] = a[pivot], a[j]
        pivot_inv = inv(a[j][j], q)
        for i in range(j + 1, n):
            if a[i][j]:
                f = mul(a[i][j], pivot_inv, q)
                for k in range(j, n):
                    a[i][k] = add(a[i][k], (-f * a[j][k]) % q, q) if q != 4 else a[i][k] ^ mul(f, a[j][k], q)
    return True


def connected(mat, directed):
    n = len(mat)
    def reachable(transpose):
        visited = {0}
        stack = [0]
        while stack:
            i = stack.pop()
            for j in range(n):
                if j in visited:
                    continue
                edge = mat[j][i] if transpose else mat[i][j]
                if not directed:
                    edge = mat[i][j] or mat[j][i]
                if edge:
                    visited.add(j)
                    stack.append(j)
        return len(visited) == n
    return reachable(False) and (not directed or reachable(True))


def gl(n, q):
    r = 1
    for i in range(n):
        r *= q**n - q**i
    return r


def indecomposable_counts(n, q):
    c = [0] * (n + 1)
    for m in range(1, n + 1):
        c[m] = gl(m, q) - sum(comb(m-1,k-1) * c[k] * gl(m-k, q) for k in range(1,m))
    return c


def check(n, q):
    cuts = [mask for mask in range(1, (1 << n) - 1)]
    counts = {mask: [0, 0] for mask in cuts}
    simple = 0
    indec = 0
    total = 0
    for entries in product(range(q), repeat=n*n):
        mat = [entries[i*n:(i+1)*n] for i in range(n)]
        if not nonsingular(mat, q):
            continue
        total += 1
        simple += connected(mat, True)
        indec += connected(mat, False)
        for mask in cuts:
            s = [i for i in range(n) if (mask >> i) & 1]
            t = [i for i in range(n) if not ((mask >> i) & 1)]
            out_zero = all(mat[i][j] == 0 for i in s for j in t)
            if out_zero:
                counts[mask][0] += 1
                if all(mat[j][i] == 0 for i in s for j in t):
                    counts[mask][1] += 1
    assert total == gl(n,q), (n,q,total,gl(n,q))
    assert indec == indecomposable_counts(n,q)[n]
    for mask in cuts:
        k = mask.bit_count()
        expected_out = gl(k,q) * gl(n-k,q) * q**(k*(n-k))
        expected_block = gl(k,q) * gl(n-k,q)
        assert counts[mask] == [expected_out, expected_block], (n,q,mask,counts[mask],expected_out,expected_block)
    print(f"q={q} n={n} total={total} simple={simple} indecomposable={indec} cut_checks={len(cuts)}")


if __name__ == '__main__':
    for n,q in [(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)]:
        check(n,q)
    print('VERIFY_OK cases=6')
