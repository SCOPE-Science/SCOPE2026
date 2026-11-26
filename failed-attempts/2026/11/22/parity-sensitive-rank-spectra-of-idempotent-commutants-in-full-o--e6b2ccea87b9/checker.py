"""Independent finite composition checks for idempotent-commutant rank spectra.

No external packages are required. The finite computations are corroboration,
not an all-size proof.
"""
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def target(n):
    m = n // 2
    result = []
    for r in range(n + 1):
        count = 2**n * choose(n, r)
        if r >= 1:
            count += 2**(n-r) * choose(n, r+1)
        if r >= 2:
            if n % 2 == 0:
                count += 2**(n-r) * (
                    4*choose(m+1, r+1) + choose(m, r))
            else:
                count += 2**(n-r) * (
                    4*choose(m+1, r+1) + 3*choose(m, r)
                    + 2*choose(m, r-1))
        result.append(count)
    return result


def all_maps(n):
    maps = set()
    for shift in range(n):
        allowed = [x for x in range(n) if x - shift >= 0]
        for mask in range(1 << len(allowed)):
            v = [-1] * n
            for j, x in enumerate(allowed):
                if (mask >> j) & 1:
                    v[x] = x - shift
            maps.add(tuple(v))
    for s in range(2, 2*n+1):
        allowed = [x for x in range(1, n+1) if 1 <= s-x <= x]
        for mask in range(1 << len(allowed)):
            if mask.bit_count() < 2:
                continue
            v = [-1] * n
            for j, x in enumerate(allowed):
                if (mask >> j) & 1:
                    v[x-1] = s-x-1
            maps.add(tuple(v))
    return maps


def compose(f, g):
    return tuple(g[f[x]] if f[x] >= 0 else -1 for x in range(len(f)))


def check(n):
    maps = all_maps(n)
    histogram = [0] * (n+1)
    for f in maps:
        assert all(y <= x for x, y in enumerate(f) if y >= 0)
        domain = [x for x, y in enumerate(f) if y >= 0]
        assert all(abs(f[x]-f[y]) == abs(x-y)
                   for x in domain for y in domain)
        r = len(domain)
        for bits in range(1 << n):
            e = tuple(i if (bits >> i) & 1 else -1 for i in range(n))
            if compose(e, f) == compose(f, e):
                histogram[r] += 1
    expected = target(n)
    assert histogram == expected, (n, histogram, expected)
    return len(maps), histogram


if __name__ == '__main__':
    for n in range(1, 9):
        size, hist = check(n)
        print(f'n={n} size={size} commuting_by_rank={hist}')
    print('ORDER_DECREASING_REFLECTION_COMMUTANTS_OK')
