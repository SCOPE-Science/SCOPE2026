"""Finite exhaustive checks for the nilpotent-chain join theorem."""
from collections import Counter, defaultdict
from itertools import product
from math import factorial


def maps(n):
    def rec(a):
        x = len(a)
        if x == n + 1:
            f = tuple(a)
            assert f[0] == 0
            yield f
            return
        for y in range(a[-1], x):
            yield from rec(a + [y])
    return list(rec([0]))


def nu(f):
    t, d = len(f) - 1, 0
    while t:
        t = f[t]
        d += 1
    return d


def special_maps(colors, k):
    n = len(colors) + 1
    ds = [[0] * (n + 1) for _ in range(k)]
    for i in range(k):
        for x in range(1, n + 1):
            ds[i][x] = 1 + sum(a == i for a in colors[:x - 1])
    fs = []
    for d in ds:
        f = [0]
        for x in range(1, n + 1):
            f.append(max(y for y in range(x) if d[y] == d[x] - 1))
        fs.append(tuple(f))
    return tuple(fs)


def check(k, n):
    es = maps(n)
    codes = [(f, nu(f)) for f in es]
    seen = Counter()
    total = 0
    for t in product(codes, repeat=k):
        fs = [f for f, _ in t]
        heights = tuple(a for _, a in t)
        N = 1 + sum(a - 1 for a in heights)
        h = tuple(max(f[x] for f in fs) for x in range(n + 1))
        s = nu(h)
        assert s <= min(n, N), (k, n, heights)
        if n == N and s == N:
            seen[heights] += 1
        total += 1
    for heights in product(range(1, n + 1), repeat=k):
        if 1 + sum(a - 1 for a in heights) != n:
            continue
        den = 1
        for a in heights:
            den *= factorial(a - 1)
        expectation = factorial(n - 1) // den
        assert seen[heights] == expectation, (k, n, heights, seen[heights], expectation)
        cs = []
        for i, a in enumerate(heights):
            cs += [i] * (a - 1)
        distinct = set(product(*[range(k) for _ in range(n - 1)]))
        examples = set()
        for w in distinct:
            if Counter(w) != Counter(cs):
                continue
            fs = special_maps(w, k)
            assert tuple(nu(f) for f in fs) == heights
            assert all(max(f[x] for f in fs) == x - 1 for x in range(1, n + 1))
            examples.add(fs)
        assert len(examples) == expectation
    print(f'EXACT_CENSUS k={k} n={n} tuples={total} verified')

if __name__ == '__main__':
    for n in range(1, 9):
        check(2, n)
    for n in range(1, 6):
        check(3, n)
    check(4, 4)
    print('JOIN_NILPOTENCY_AND_MULTINOMIAL_CHECKS_PASSED')
