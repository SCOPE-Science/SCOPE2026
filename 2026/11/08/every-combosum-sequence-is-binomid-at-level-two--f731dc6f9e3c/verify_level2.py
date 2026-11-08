#!/usr/bin/env python3
"""Exact finite tests of the level-two ComboSum binomid inequality."""
from random import Random


def check(bits, limit):
    a = [0] + [(bits >> (n - 1)) & 1 for n in range(1, limit + 1)]
    for x in range(1, limit + 1):
        if not a[x]:
            continue
        for y in range(1, limit - x + 1):
            if a[y] and not a[x + y]:
                return None  # the set is not additively closed in the range
    f = [0]
    for n in range(1, limit + 1):
        f.append(f[-1] + a[n])
    count = 0
    for u in range(limit):
        for k in range(1, limit - u):
            d1 = f[u + k] - f[u] - f[k]
            d2 = f[u + k + 1] - f[u] - f[k + 1]
            assert d1 >= 0 and d2 >= 0
            assert d1 + d2 + a[1] - a[u + 1] >= 0, (bits, limit, u, k)
            if u and a[u + 1] and a[k + 1] and not a[1]:
                assert d1 >= 1, (bits, limit, u, k, 'strict lemma')
            count += 1
    return count


def main():
    N = 16
    semigroups = 0
    checks = 0
    for bits in range(1 << N):
        c = check(bits, N)
        if c is not None:
            semigroups += 1
            checks += c
    rng = Random(20230204)
    rcount = 0
    for _ in range(180):
        N = 180
        gens = rng.sample(range(2, 80), rng.randrange(1, 7))
        a = [False] * (N + 1)
        for i in range(1, N + 1):
            a[i] = any(i == g or (i > g and a[i - g]) for g in gens)
        bits = sum((1 << (i - 1)) for i in range(1, N + 1) if a[i])
        c = check(bits, N)
        assert c is not None
        rcount += c
    print(f'PASS: {semigroups} exhaustively enumerated closed masks through 16; {checks} level-two comparisons.')
    print(f'PASS: 180 generated semigroups through 180; {rcount} level-two comparisons.')
    # Direct independent rational-coefficient test for mixed-prime ComboSum sequences.
    from fractions import Fraction
    examples = 0
    for _ in range(75):
        M = 75
        a = [False] * (M + 1)
        b = [False] * (M + 1)
        aa = rng.sample(range(2, 26), 3)
        bb = rng.sample(range(2, 26), 3)
        for j in range(1, M + 1):
            a[j] = any(j == g or (j > g and a[j - g]) for g in aa)
            b[j] = any(j == g or (j > g and b[j - g]) for g in bb)
        f = [1] + [(-1 if rng.randrange(2) else 1) * (2 if a[j] else 1) * (3 if b[j] else 1) for j in range(1, M + 1)]
        c = [1] + [Fraction(f[j] * f[j + 1], f[1] * f[2]) for j in range(1, M)]
        for n in range(1, M):
            assert c[n].denominator == 1
        for n in range(1, 40):
            for k in range(n + 1):
                v = Fraction(1)
                for j in range(k):
                    v *= Fraction(c[n - j], c[j + 1])
                assert v.denominator == 1, (aa, bb, n, k, v)
                examples += 1
    print(f'PASS: {examples} directly reconstructed mixed-prime signed generalized binomial coefficients.')

if __name__ == '__main__':
    main()
