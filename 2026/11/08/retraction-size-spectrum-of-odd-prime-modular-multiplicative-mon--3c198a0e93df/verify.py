"""Independent finite-ring checks of multiplicative retraction formulas.

Run with Python 3; no dependencies.
"""
from collections import Counter
from math import gcd, prod


def phi(p, j):
    return (p - 1) * p ** (j - 1)


def idempotent_parameters(p, e):
    n = p ** e
    order = phi(p, e)
    for t in range(order):
        if (t * t - t) % order:
            continue
        yield t, 0
        for a in range(p, n, p):
            if a % (p * p) == 0:
                continue
            c = a // p
            if pow(c, t, p ** (e - 1)) == 1:
                yield t, a


def map_from_parameters(p, e, t, a):
    n = p ** e
    out = []
    for x in range(n):
        if x == 0:
            out.append(0)
            continue
        y, v = x, 0
        while y % p == 0:
            y //= p
            v += 1
        out.append((pow(a, v, n) * pow(y, t, n)) % n)
    return tuple(out)


def prime_powers(m):
    values = []
    d = 2
    while d * d <= m:
        if m % d == 0:
            b = 1
            while m % d == 0:
                m //= d
                b *= d
            values.append(b)
        d += 1
    if m > 1:
        values.append(m)
    return values


def predicted_total(p, e):
    factors = prime_powers(p - 1)
    return 1 + 2 ** (len(factors) + 1) + (1 + p ** (e - 2)) * prod(1 + v for v in factors)


def predicted_distribution(p, e):
    n = phi(p, e)
    answer = Counter({1: 1})
    for t in range(n):
        if t * t % n != t:
            continue
        sizes = [phi(p, j) // gcd(t, phi(p, j)) for j in range(1, e + 1)]
        answer[1 + sizes[-1]] += 1
        answer[1 + sum(sizes)] += gcd(t, phi(p, e - 1))
    return answer


def run():
    scenarios = [(3, 2), (3, 3), (3, 4), (5, 2), (5, 3), (7, 2)]
    exhaustive_multiplicativity = 0
    for p, e in scenarios:
        n = p ** e
        observed = Counter({1: 1})
        seen = {tuple([1] * n)}
        for t, a in idempotent_parameters(p, e):
            f = map_from_parameters(p, e, t, a)
            assert f not in seen, (p, e, t, a, 'nonunique parameterization')
            seen.add(f)
            assert all(f[f[x]] == f[x] for x in range(n)), (p, e, t, a, 'composition')
            if n <= 25:
                for x in range(n):
                    for y in range(n):
                        assert f[(x * y) % n] == f[x] * f[y] % n
                        exhaustive_multiplicativity += 1
            observed[len(set(f))] += 1
        expected = predicted_distribution(p, e)
        assert observed == expected, (p, e, observed, expected)
        assert sum(observed.values()) == predicted_total(p, e)
        print(f'p={p} e={e} retracts={sum(observed.values())} image_distribution={sorted(observed.items())}')
    print(f'VERIFY_OK configurations={len(scenarios)} multiplicative_pairs={exhaustive_multiplicativity}')


if __name__ == '__main__':
    run()
