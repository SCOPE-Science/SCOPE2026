#!/usr/bin/env python3
"""Independent finite checks for embedded monogenic inverse-submonoid counts.

No external dependencies. This checks only finite cases, not asymptotic proofs.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial, gcd, lcm


def partitions(n, limit=None):
    if n == 0:
        yield ()
        return
    if limit is None:
        limit = n
    for j in range(min(n, limit), 0, -1):
        for rest in partitions(n - j, j):
            yield (j,) + rest


def phi(d):
    return sum(gcd(j, d) == 1 for j in range(1, d + 1))


def cyclic_subgroups(r):
    total = 0
    for lam in partitions(r):
        mult = Counter(lam)
        z = 1
        for j, m in mult.items():
            z *= j ** m * factorial(m)
        order = lcm(*lam) if lam else 1
        num = factorial(r) // z
        assert num % phi(order) == 0
        total += num // phi(order)
    return total


def expected(n):
    size = sum(comb(n, r) ** 2 * factorial(r) for r in range(n + 1))
    group_elements = sum(comb(n, r) * factorial(r) for r in range(n + 1))
    group_monoids = sum(comb(n, r) * cyclic_subgroups(r) for r in range(n + 1))
    acyclic = 1 if n == 0 else sum(
        comb(n - 1, k - 1) * factorial(n) // factorial(k)
        for k in range(1, n + 1)
    )
    assert (size - group_elements) % 2 == 0
    assert (acyclic + 1) % 2 == 0
    return size, group_elements, (size - group_elements) // 2 + group_monoids, (acyclic + 1) // 2


def all_partial_injections(n):
    yield (-1,) * n
    for r in range(1, n + 1):
        for domain in combinations(range(n), r):
            for image in permutations(range(n), r):
                f = [-1] * n
                for x, y in zip(domain, image):
                    f[x] = y
                yield tuple(f)


def inverse(f):
    g = [-1] * len(f)
    for x, y in enumerate(f):
        if y >= 0:
            g[y] = x
    return tuple(g)


def compose(f, g):
    return tuple(-1 if v < 0 else g[v] for v in f)


def inverse_closure(f):
    identity = tuple(range(len(f)))
    generators = (f, inverse(f))
    queue = [identity]
    seen = {identity}
    for h in queue:
        for gen in generators:
            k = compose(h, gen)
            if k not in seen:
                seen.add(k)
                queue.append(k)
    return frozenset(seen)


def nilpotent(f):
    empty = (-1,) * len(f)
    curr = tuple(range(len(f)))
    for _ in range(len(f) + 1):
        if curr == empty:
            return True
        curr = compose(curr, f)
    return curr == empty


def test():
    expected_m = [1, 2, 6, 24, 126, 838, 6841, 65411, 711969]
    expected_z = [1, 1, 2, 7, 37, 251, 2026, 18817, 197177]
    for n in range(9):
        _, _, m, z = expected(n)
        assert m == expected_m[n], (n, m)
        assert z == expected_z[n], (n, z)
    print('FORMULA_VALUES_OK n=0..8')
    for n in range(1, 7):
        closures = defaultdict(list)
        for f in all_partial_injections(n):
            closures[inverse_closure(f)].append(f)
        size, group_elements, m, z = expected(n)
        assert sum(map(len, closures.values())) == size
        assert len(closures) == m, (n, len(closures), m)
        nil_monoids = sum(any(nilpotent(f) for f in fs) for fs in closures.values())
        assert nil_monoids == z, (n, nil_monoids, z)
        for fs in closures.values():
            nongroup = [f for f in fs if set(i for i, y in enumerate(f) if y >= 0) != set(y for y in f if y >= 0)]
            if nongroup:
                assert len(fs) == 2
                assert fs[0] == inverse(fs[1])
        print('DIRECT_CLOSURES_OK n={} total={} monogenic={} nilpotent={}'.format(n, size, m, z))
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
