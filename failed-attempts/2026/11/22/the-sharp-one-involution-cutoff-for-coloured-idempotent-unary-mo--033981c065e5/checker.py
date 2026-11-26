"""Exact finite checks for order-two automorphisms of coloured idempotent maps.
Run: python3 checker.py (Python standard library only).
"""
from collections import Counter, defaultdict
from itertools import product, permutations
from math import comb, factorial


def add(a, b):
    c = Counter(a)
    c.update(b)
    return {k: v for k, v in c.items() if v}


def mul(a, b):
    c = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            c[i + j] += x * y
    return dict(c)


def power(a, n):
    z = {0: 1}
    for _ in range(n):
        z = mul(z, a)
    return z


def polynomial(q):
    # Distinct rigid components (each root colour and a set of leaf colours).
    weights = Counter({j + 1: q * comb(q, j) for j in range(q + 1)})
    types = []
    for w, count in sorted(weights.items()):
        types.extend([w] * count)
    R = {0: 1}
    for w in types:
        R = mul(R, {0: 1, w: 1})
    # One special component: exactly one pair of same-colour leaves.
    internal = mul(R, {3+j: q*q*comb(q-1, j) for j in range(q)})
    # The other mechanism: duplicate exactly one previously rigid component.
    duplicated = {}
    for w in types:
        rest = {0: 1}
        missed = False
        for v in types:
            if v == w and not missed:
                missed = True
                continue
            rest = mul(rest, {0: 1, v: 1})
        duplicated = add(duplicated, {k + 2*w: v for k, v in rest.items()})
    return add(internal, duplicated), R


def canon(f, colors, q):
    roots = [r for r in range(len(f)) if f[r] == r]
    return tuple(sorted((colors[r], tuple(sum(1 for x in range(len(f)) if x != r and f[x] == r and colors[x] == c) for c in range(q))) for r in roots))


def group_order_direct(f, colors):
    n = len(f)
    k = 0
    for p in permutations(range(n)):
        if all(colors[p[i]] == colors[i] and p[f[i]] == f[p[i]] for i in range(n)):
            k += 1
    return k


def group_order_from_fibres(t):
    mult = Counter(t)
    k = 1
    for (root_colour, leaves), copies in mult.items():
        factor = 1
        for a in leaves:
            factor *= factorial(a)
        k *= (factor ** copies) * factorial(copies)
    return k


def direct_test(q, nmax):
    F, R = polynomial(q)
    checked = 0
    checked_models = 0
    for n in range(1, nmax + 1):
        types = {}
        labeled_two = 0
        for f in product(range(n), repeat=n):
            if any(f[f[i]] != f[i] for i in range(n)):
                continue
            for colors in product(range(q), repeat=n):
                code = canon(f, colors, q)
                order = group_order_direct(f, colors)
                assert group_order_from_fibres(code) == order
                if code in types:
                    assert types[code] == order
                else:
                    types[code] = order
                if order == 2:
                    labeled_two += 1
                checked_models += 1
        count = sum(1 for order in types.values() if order == 2)
        assert count == F.get(n, 0), (q, n, count, F.get(n, 0))
        assert labeled_two == factorial(n) * count // 2, (q, n, labeled_two, count)
        checked += 1
    return checked, checked_models


def main():
    test_counts = []
    for q in range(1, 6):
        F, R = polynomial(q)
        cap = q * (2**(q-1)) * (q+2) + q+2
        assert max(F) == cap
        assert F[cap] == q*q
        assert set(n for n, v in F.items() if v) == set(range(2, cap+1))
        assert max(R) == q * (2**(q-1)) * (q+2)
        assert all(R.get(n, 0) > 0 for n in range(max(R)+1))
        test_counts.append((q, cap, sum(F.values()), F.get(2), F.get(3)))
    direct = [direct_test(1, 6), direct_test(2, 5), direct_test(3, 4)]
    print('FORMAL_CHECKS', test_counts)
    print('DIRECT_CHECKS', direct)
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
