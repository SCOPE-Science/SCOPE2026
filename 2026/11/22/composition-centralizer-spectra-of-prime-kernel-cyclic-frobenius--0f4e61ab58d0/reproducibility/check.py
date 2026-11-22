"""Independent finite-group checks for a rank and centralizer classification.

Run: python3 reproducibility/check.py
Only Python standard library is needed.
"""
from collections import Counter
from math import gcd


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def data(p, r):
    assert p > 2 and (p - 1) % r == 0 and r >= 3
    u = next(x for x in range(2, p) if pow(x, r, p) == 1
             and all(pow(x, j, p) != 1 for j in range(1, r)))
    elems = [(s, t, 1) for s in range(1, p) for t in range(p)]
    elems += [(0, t, k) for k in range(1, r) for t in range(p)]
    elems.append((0, 0, 0))
    assert len(elems) == p * (p + r - 2) + 1
    return u, elems


def apply(f, x, p, r, u):
    s, t, k = f
    i, j = x
    term = sum(pow(u, k * h, p) for h in range(j)) % p
    return ((s * i + t * term) % p, (k * j) % r)


def multiply(x, y, p, r, u):
    return ((x[0] + pow(u, x[1], p) * y[0]) % p,
            (x[1] + y[1]) % r)


def compose(f, g, p, r, u):
    s, t, k = f
    a, b, l = g
    term = sum(pow(u, k * h, p) for h in range(l)) % p
    return ((s * a) % p, (s * b + t * term) % p, (k * l) % r)


def expected_spectrum(p, r):
    n = p * (p + r - 2) + 1
    spectrum = Counter({n: 2, p + 1: p - 1})
    spectrum[p + r - 1] += p * (p - 2)
    for d in divisors(r):
        if d < r:
            spectrum[r + (p - 1) * d] += p * phi(r // d)
    return spectrum


def verify(p, r, full=False):
    u, elements = data(p, r)
    s = set(elements)
    n = len(elements)
    assert (0, 0, 0) in s and (1, 0, 1) in s
    for f in elements:
        assert compose(f, (1, 0, 1), p, r, u) == f
        assert compose((1, 0, 1), f, p, r, u) == f
        assert compose(f, (0, 0, 0), p, r, u) == (0, 0, 0)
        assert compose((0, 0, 0), f, p, r, u) == (0, 0, 0)
    matrix_spectrum = Counter()
    centralizer = {}
    for f in elements:
        centralizer[f] = sum(compose(f, g, p, r, u) == compose(g, f, p, r, u)
                             for g in elements)
        matrix_spectrum[centralizer[f]] += 1
    assert matrix_spectrum == expected_spectrum(p, r), (p, r, matrix_spectrum, expected_spectrum(p, r))
    # Exact image orders, idempotent count, and entire commuting-pair count.
    rank_hist = Counter()
    for f in elements:
        s0, t0, k = f
        rank = p * r if s0 else (1 if k == 0 else r // gcd(k, r))
        rank_hist[rank] += 1
    target_hist = Counter({1: 1, p * r: p * (p - 1)})
    for d in divisors(r):
        if d > 1:
            target_hist[d] += p * phi(d)
    assert rank_hist == target_hist
    num_prime_factors = sum(1 for d in range(2, r + 1) if r % d == 0 and all(d % h for h in range(2, int(d**.5) + 1)))
    retracts = sum(compose(f, f, p, r, u) == f for f in elements)
    assert retracts == p * (2**num_prime_factors - 1) + 2
    # Explicit conjugations, using the unit group rather than theoretical orbit size.
    auts = [f for f in elements if f[0] != 0]
    todo = set(elements)
    orbit_sizes = []
    while todo:
        x = next(iter(todo))
        orbit = set()
        for a in auts:
            inv = next(v for v in auts if compose(a, v, p, r, u) == (1, 0, 1))
            orbit.add(compose(compose(a, x, p, r, u), inv, p, r, u))
        assert orbit <= todo
        todo -= orbit
        orbit_sizes.append(len(orbit))
    assert len(orbit_sizes) == p + r
    assert sum(orbit_sizes) == n
    # Directly evaluate each map as an actual function on the group, and independently
    # check the generator formula, group-homomorphism law, and centralizers.
    if full:
        group = [(i, j) for i in range(p) for j in range(r)]
        maps = {f: tuple(apply(f, x, p, r, u) for x in group) for f in elements}
        assert len(set(maps.values())) == n
        index = {g: i for i, g in enumerate(group)}
        for f, values in maps.items():
            for x in group:
                for y in group:
                    assert values[index[multiply(x, y, p, r, u)]] == multiply(values[index[x]], values[index[y]], p, r, u)
            for g, other in maps.items():
                left = tuple(values[index[v]] for v in other)
                right = tuple(other[index[v]] for v in values)
                assert (left == right) == (compose(f, g, p, r, u) == compose(g, f, p, r, u))
    print('PASS', 'p', p, 'r', r, 'action', u, 'endomorphisms', n,
          'orbits', len(orbit_sizes), 'retractions', retracts,
          'commuting_ordered', sum(centralizer.values()),
          'centralizer_spectrum', sorted(matrix_spectrum.items()))


if __name__ == '__main__':
    for p, r, full in [(7, 3, True), (13, 3, True), (13, 4, True),
                       (13, 6, True), (17, 8, False), (19, 9, False),
                       (31, 15, False)]:
        verify(p, r, full=full)
    print('FROBENIUS_ENDOMORPHISM_CENTRALIZER_CHECKS_PASSED')
