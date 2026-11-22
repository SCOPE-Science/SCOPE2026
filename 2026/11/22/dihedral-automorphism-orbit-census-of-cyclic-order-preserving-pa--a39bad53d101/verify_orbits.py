"""Finite, independent checks of dihedral conjugacy counts in cyclic-order-preserving partial injections.

No symbolic or asymptotic claim is inferred from the finite checks.
"""
from collections import Counter
from itertools import combinations
from math import comb, gcd, factorial


def maps(n):
    yield (-1,) * n
    for k in range(1, n + 1):
        for domain in combinations(range(n), k):
            for image in combinations(range(n), k):
                for shift in range(k):
                    f = [-1] * n
                    for j, x in enumerate(domain):
                        f[x] = image[(j + shift) % k]
                    yield tuple(f)


def domain_rank(f):
    return sum(x >= 0 for x in f)


def commuting(f, p):
    return all(f[p[i]] == (-1 if f[i] < 0 else p[f[i]]) for i in range(len(f)))


def rotations(n):
    return [tuple((i + s) % n for i in range(n)) for s in range(n)]


def reflections(n):
    return [tuple((s - i) % n for i in range(n)) for s in range(n)]


def predicted_rotation(n, s, k):
    if k == 0:
        return 1
    g = gcd(n, s)
    d = n // g
    if k % d:
        return 0
    l = k // d
    return k * comb(g, l) ** 2


def predicted_reflection(n, f, k):
    if k == 0:
        return 1
    m = (n - f) // 2
    out = 0
    for j in range(f + 1):
        if k < j or (k - j) % 2:
            continue
        t = (k - j) // 2
        if 0 <= t <= m:
            out += (1 if k % 2 else 2) * comb(f, j)**2 * comb(m, t)**2
    return out


def orbit_counts_formula(n):
    p = [0] * (n + 1)
    for s in range(n):
        for k in range(n + 1):
            p[k] += predicted_rotation(n, s, k)
    for r in reflections(n):
        f = sum(i == r[i] for i in range(n))
        for k in range(n + 1):
            p[k] += predicted_reflection(n, f, k)
    assert all(x % (2 * n) == 0 for x in p)
    return tuple(x // (2 * n) for x in p)


def totient(n):
    return sum(gcd(i, n) == 1 for i in range(1, n + 1))


def total_formula(n):
    a = sum(totient(n // g) * comb(2 * g, g) for g in range(1, n + 1) if n % g == 0)
    if n % 2:
        return (a + 6 * comb(n - 1, (n - 1) // 2)) // 4
    return (a + 2 * comb(n, n // 2) + 8 * comb(n - 2, (n - 2) // 2)) // 4


def check_direct(n):
    rows = list(maps(n))
    rots, refs = rotations(n), reflections(n)
    assert len(rows) == 1 + n * comb(2 * n, n) // 2
    predicted = orbit_counts_formula(n)
    burnside = [0] * (n + 1)
    for s, p in enumerate(rots):
        counts = Counter(domain_rank(f) for f in rows if commuting(f, p))
        for k in range(n + 1):
            assert counts[k] == predicted_rotation(n, s, k), (n,s,k,counts[k])
            burnside[k] += counts[k]
    for s, p in enumerate(refs):
        counts = Counter(domain_rank(f) for f in rows if commuting(f, p))
        fixed_vertices = sum(i == p[i] for i in range(n))
        for k in range(n + 1):
            assert counts[k] == predicted_reflection(n, fixed_vertices, k), (n,s,k,counts[k])
            burnside[k] += counts[k]
    assert tuple(x // (2 * n) for x in burnside) == predicted
    assert sum(predicted) == total_formula(n)
    # Build the actual orbit graph independently of Burnside for modest dimensions.
    if n <= 6:
        visited = set()
        counts = [0] * (n + 1)
        for v in rows:
            if v in visited:
                continue
            k = domain_rank(v)
            counts[k] += 1
            for p in rots + refs:
                pinv = [0] * n
                for j, x in enumerate(p):
                    pinv[x] = j
                conjugate = [-1] * n
                for i in range(n):
                    if v[i] >= 0:
                        conjugate[p[i]] = p[v[i]]
                visited.add(tuple(conjugate))
        assert tuple(counts) == predicted, (n, counts, predicted)
        assert len(visited) == len(rows)
    return (n, len(rows), predicted)

if __name__ == '__main__':
    for n in range(3, 8):
        print('n, monoid size, rank-orbit vector:', check_direct(n))
    for n in range(3, 19):
        assert sum(orbit_counts_formula(n)) == total_formula(n)
    print('CYCLIC_ORIENTED_INVERSE_MONOID_ORBIT_CHECKS_PASSED')
