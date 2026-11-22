"""Reproducibility checks for four-site parabolic sixth Fourier moments.

This script uses only Python's standard library. Its finite tests supplement,
but do not replace, the general algebraic argument in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations, combinations_with_replacement
from math import comb, factorial, isclose, pi
from cmath import exp
from random import Random


def collision_profile(p, sites):
    buckets = defaultdict(list)
    for I in combinations_with_replacement(range(4), 3):
        buckets[(sum(sites[i] for i in I) % p,
                 sum(sites[i] ** 2 for i in I) % p)].append(I)
    collisions = [v for v in buckets.values() if len(v) > 1]
    assert all(len(v) == 2 for v in collisions)
    if not collisions:
        return 'generic', buckets
    assert len(collisions) == 1
    a, b = collisions[0]
    delta = [a.count(i) - b.count(i) for i in range(4)]
    assert sorted(delta) in ([-3, 1, 1, 1], [-2, -1, 1, 2], [-1, -1, -1, 3])
    return ('unbalanced' if max(map(abs, delta)) == 3 else 'balanced'), buckets


def affine_copies(p, pattern):
    return {tuple(sorted((a + u * x) % p for x in pattern))
            for a in range(p) for u in range(1, p)}


def check_classification(p):
    group_a = set()
    if (p - 1) % 3 == 0:
        omega = next(x for x in range(2, p) if pow(x, 3, p) == 1)
        group_a = affine_copies(p, (0, 1, omega, pow(omega, 2, p)))
    group_b = affine_copies(p, (0, 1, 3, 4))
    assert len(group_a) == (p * (p - 1) // 3 if p % 3 == 1 else 0)
    assert len(group_b) == p * (p - 1) // 2
    assert not group_a.intersection(group_b)
    observed = defaultdict(int)
    for sites in combinations(range(p), 4):
        kind, _ = collision_profile(p, sites)
        observed[kind] += 1
        assert (kind == 'unbalanced') == (sites in group_a)
        assert (kind == 'balanced') == (sites in group_b)
    assert observed['generic'] == comb(p, 4) - len(group_a) - len(group_b)
    print('p =', p, 'total =', comb(p, 4), 'strata =', dict(observed))


def factorial_weight(triple):
    return factorial(3) // (factorial(triple.count(0)) * factorial(triple.count(1)) *
                            factorial(triple.count(2)) * factorial(triple.count(3)))


def moment_from_convolution(p, sites, c):
    kind, buckets = collision_profile(p, sites)
    out = 0.0
    for triples in buckets.values():
        z = 0j
        for triple in triples:
            z += factorial_weight(triple) * c[triple[0]] * c[triple[1]] * c[triple[2]]
        out += abs(z) ** 2
    return out


def moment_from_formula(p, sites, c):
    kind, buckets = collision_profile(p, sites)
    x = [abs(v) ** 2 for v in c]
    s = sum(x)
    e2 = sum(x[i] * x[j] for i, j in combinations(range(4), 2))
    e3 = sum(x[i] * x[j] * x[k] for i, j, k in combinations(range(4), 3))
    value = s**3 + 6 * s * e2 + 12 * e3
    if kind != 'generic':
        pair = next(v for v in buckets.values() if len(v) > 1)
        U, V = pair
        a = c[U[0]] * c[U[1]] * c[U[2]]
        b = c[V[0]] * c[V[1]] * c[V[2]]
        value += 2 * factorial_weight(U) * factorial_weight(V) * (a*b.conjugate()).real
    return value


def moment_from_fourier(p, sites, c):
    total = 0
    for u in range(p):
        for v in range(p):
            f = sum(c[j] * exp(-2j*pi*(u*t+v*t*t)/p)
                    for j, t in enumerate(sites))
            total += abs(f)**6
    return total / (p*p)


def check_moments():
    rng = Random(2609)
    tests = 0
    for p in (7, 11, 13):
        seen = set()
        for sites in combinations(range(p), 4):
            kind, _ = collision_profile(p, sites)
            if kind in seen:
                continue
            seen.add(kind)
            for _ in range(4):
                c = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
                     for _ in range(4)]
                a = moment_from_convolution(p, sites, c)
                b = moment_from_formula(p, sites, c)
                d = moment_from_fourier(p, sites, c)
                assert isclose(a, b, rel_tol=3e-12, abs_tol=1e-11)
                assert isclose(a, d, rel_tol=3e-12, abs_tol=1e-11)
                tests += 1
    print('full weighted convolution/Fourier/formula tests:', tests)


def check_sharp_constant():
    def poly(r):
        return r**4 + r**3 + 6*r*r - 3*r - 7
    lo, hi = 1., 2.
    assert poly(lo) < 0 < poly(hi)
    for _ in range(90):
        mid = (lo + hi)/2
        if poly(mid) > 0: hi = mid
        else: lo = mid
    r = (lo + hi)/2
    def objective(r):
        return (r**6 + 27*r**4 + 12*r**3 + 135*r*r + 93) / (r*r+3)**3
    assert 1.11 < r < 1.12
    assert 4.20 < objective(r) < 4.21
    for k in range(2001):
        t = k/200
        assert objective(t) <= objective(r) + 1e-12
    print('unique positive stationary root (Descartes):', repr(r))
    print('sharp sixth-power constant:', repr(objective(r)))

if __name__ == '__main__':
    for prime in (7, 11, 13, 17):
        check_classification(prime)
    check_moments()
    check_sharp_constant()
    print('All supplementary checks passed.')
