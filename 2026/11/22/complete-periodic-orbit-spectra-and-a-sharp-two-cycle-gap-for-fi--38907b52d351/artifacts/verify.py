"""Exhaustive small-crown check of the full periodic-spectrum theorem.

Finite exhaustive checks do not replace the all-size proof in RESULT.md.
"""
from itertools import product
from math import gcd


def cycles(f):
    seen = set()
    found = []
    for i in range(len(f)):
        if i in seen:
            continue
        path = []
        first = {}
        j = i
        while j not in seen and j not in first:
            first[j] = len(path)
            path.append(j)
            j = f[j]
        if j in first:
            found.append(tuple(path[first[j]:]))
        seen.update(path)
    return found


def monotone(f):
    m = len(f)
    for i in range(0, m, 2):
        for j in ((i - 1) % m, (i + 1) % m):
            u, v = f[i], f[j]
            if u == v:
                continue
            if not (u % 2 == 0 and v % 2 == 1 and (u - v) % m in (1, m - 1)):
                return False
    return True


def construct_fixed(N, ell):
    m = 2 * N
    def F(j):
        if j <= ell:
            return j
        if j <= 2 * ell:
            return 2 * ell - j
        return 0
    return tuple(F(j) % m for j in range(m))


def construct_flip(N, b):
    m = 2 * N
    def F(j):
        if j <= 2 * b:
            return 2 * b - j
        if j <= 4 * b:
            return j - 2 * b
        return 2 * b
    return tuple(F(j) % m for j in range(m))


def check(N):
    m = 2 * N
    recorded = {}
    count = 0
    for start in range(m):
        for word in product((-1, 0, 1), repeat=m):
            sum_word = sum(word)
            if sum_word not in (-m, 0, m):
                continue
            walk = [start]
            for step in word:
                walk.append(walk[-1] + step)
            f = tuple(x % m for x in walk[:-1])
            if not monotone(f):
                continue
            assert walk[-1] % m == start
            degree = sum_word // m
            lengths = tuple(sorted(map(len, cycles(f))))
            recorded[(degree, lengths)] = recorded.get((degree, lengths), 0) + 1
            count += 1
            if degree == 0:
                a = lengths.count(1)
                b = lengths.count(2)
                assert len(lengths) == a + b
                assert (b == 0 and 1 <= a <= N + 1) or (a == 1 and 1 <= b <= N // 2)
            elif degree == 1:
                assert len(set(lengths)) == 1 and N % lengths[0] == 0
                assert lengths.count(lengths[0]) == m // lengths[0]
            else:
                assert lengths == (1, 1) + (2,) * (N - 1)
    expected_zero = {(1,) * a for a in range(1, N + 2)}
    expected_zero.update((1,) + (2,) * b for b in range(1, N // 2 + 1))
    assert {sig for (d, sig) in recorded if d == 0} == expected_zero
    for ell in range(N + 1):
        f = construct_fixed(N, ell)
        assert monotone(f)
        assert tuple(sorted(map(len, cycles(f)))) == (1,) * (ell + 1)
    for b in range(1, N // 2 + 1):
        f = construct_flip(N, b)
        assert monotone(f)
        assert tuple(sorted(map(len, cycles(f)))) == (1,) + (2,) * b
    for r in range(N):
        f = tuple((j + 2 * r) % m for j in range(m))
        p = N // gcd(N, r)
        assert monotone(f)
        assert tuple(sorted(map(len, cycles(f)))) == (p,) * (m // p)
        f = tuple((2 * r - j) % m for j in range(m))
        assert monotone(f)
        assert tuple(sorted(map(len, cycles(f)))) == (1, 1) + (2,) * (N - 1)
    assert {(d, sig) for d, sig in recorded if d == 1} == {(1, (p,) * (m // p)) for p in range(1, N + 1) if N % p == 0}
    assert {(d, sig) for d, sig in recorded if d == -1} == {(-1, (1, 1) + (2,) * (N - 1))}
    return count


if __name__ == '__main__':
    counts = [check(N) for N in (2, 3, 4)]
    assert counts == [36, 234, 1544], counts
    print('CROWN_DYNAMICS_VERIFY_OK')
