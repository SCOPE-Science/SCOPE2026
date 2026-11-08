"""Standalone exact checks for embedded cyclic transformation monoids.
Only Python standard library is needed. No external files or services are read.
"""
from collections import Counter
from functools import lru_cache
from itertools import product, permutations
from math import comb, factorial, gcd, prod


def divisors(k):
    return [d for d in range(1, k + 1) if k % d == 0]


def mobius(k):
    answer = 1
    prime = 2
    while prime * prime <= k:
        if k % prime == 0:
            k //= prime
            if k % prime == 0:
                return 0
            answer = -answer
            while k % prime == 0:
                k //= prime
        prime += 1
    return -answer if k > 1 else answer


def totient(k):
    return sum(gcd(j, k) == 1 for j in range(1, k + 1))


@lru_cache(None)
def permutations_order_dividing(s, d):
    # Independent cycle containing vertex 0 has length ell dividing d.
    values = [1] + [0] * s
    for k in range(1, s + 1):
        values[k] = sum(
            comb(k - 1, ell - 1) * factorial(ell - 1) * values[k - ell]
            for ell in divisors(d) if ell <= k
        )
    return values[s]


@lru_cache(None)
def permutations_exact_order(s, p):
    return sum(
        mobius(p // d) * permutations_order_dividing(s, d)
        for d in divisors(p)
    )


@lru_cache(None)
def forest_at_most_height(m, s, h):
    if m == 0:
        return 1 if h >= 0 else 0
    if h <= 0:
        return 0
    # Each nonroot vertex chooses a parent in the previous distance layer.
    def visit(remaining, layer_sizes, multinomial, weight):
        if remaining == 0:
            return multinomial * weight
        if len(layer_sizes) == h:
            return 0
        parent_count = s if not layer_sizes else layer_sizes[-1]
        return sum(
            visit(remaining - a, layer_sizes + (a,),
                  multinomial * comb(remaining, a),
                  weight * parent_count ** a)
            for a in range(1, remaining + 1)
        )
    return visit(m, (), 1, 1)


def predicted(n, h, p, s):
    if s < 1 or s > n or h < 0 or h > n - s:
        return 0
    exact_forests = (forest_at_most_height(n - s, s, h)
                     - forest_at_most_height(n - s, s, h - 1))
    generated = comb(n, s) * permutations_exact_order(s, p) * exact_forests
    factor = totient(p) if h <= 1 else 1
    assert generated % factor == 0
    return generated // factor


def dynamics(f):
    n = len(f)
    seen = set()
    cycles = []
    for v in range(n):
        if v in seen:
            continue
        trajectory, pos = [], {}
        u = v
        while u not in seen and u not in pos:
            pos[u] = len(trajectory)
            trajectory.append(u)
            u = f[u]
        if u in pos:
            cycles.append(tuple(trajectory[pos[u]:]))
        seen.update(trajectory)
    cyclic_points = set().union(*(set(c) for c in cycles))
    p = 1
    for cycle in cycles:
        p = p * len(cycle) // gcd(p, len(cycle))
    max_distance = 0
    for v in range(n):
        u, distance = v, 0
        while u not in cyclic_points:
            distance += 1
            u = f[u]
        max_distance = max(max_distance, distance)
    return max_distance, p, len(cyclic_points)


def cyclic_submonoid(f):
    n = len(f)
    power, images = tuple(range(n)), set()
    while power not in images:
        images.add(power)
        power = tuple(f[power[i]] for i in range(n))
    return frozenset(images)


def direct_permutation_order(pi):
    seen, order = set(), 1
    for i in range(len(pi)):
        if i not in seen:
            u, count = i, 0
            while u not in seen:
                seen.add(u)
                count += 1
                u = pi[u]
            order = order * count // gcd(order, count)
    return order


for s in range(1, 7):
    direct = Counter(direct_permutation_order(pi)
                     for pi in permutations(range(s)))
    for p, count in direct.items():
        assert count == permutations_exact_order(s, p), (s, p, count)

for n in range(1, 7):
    maps_by_trait = Counter()
    monoid_trait = {}
    for f in product(range(n), repeat=n):
        trait = dynamics(f)
        maps_by_trait[trait] += 1
        key = cyclic_submonoid(f)
        if key in monoid_trait:
            assert monoid_trait[key] == trait
        else:
            monoid_trait[key] = trait
    direct_submonoids = Counter(monoid_trait.values())
    periods = {p for h, p, s in maps_by_trait}
    formula_submonoids = {
        (h, p, s): predicted(n, h, p, s)
        for p in periods
        for h in range(n)
        for s in range(1, n + 1)
        if predicted(n, h, p, s) > 0
    }
    assert direct_submonoids == formula_submonoids, (n, direct_submonoids, formula_submonoids)
    for (h, p, s), count in maps_by_trait.items():
        divisor = totient(p) if h <= 1 else 1
        assert count == divisor * direct_submonoids[h, p, s]
    assert sum(direct_submonoids.values()) == len(monoid_trait)
    print('n=%d transformations=%d embedded_submonoids=%d distinct_embedded=%d CHECK_OK' %
          (n, n ** n, len(monoid_trait), len(monoid_trait)))
print('VERIFY_OK')
