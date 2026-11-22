#!/usr/bin/env python3
"""Exact finite certificate for Cayley-octad tetrad Frobenius spectra.

Python 3 standard library only. No external files or data dependencies.
The enumeration is exhaustive on 8 labelled points and all partitions of 8.
"""
from collections import Counter
from itertools import combinations
from math import factorial, gcd

V = tuple(range(8))
E = tuple(combinations(V, 2))


def partitions(n, bound=None):
    if not n:
        yield ()
    else:
        for x in range(min(n, n if bound is None else bound), 0, -1):
            for t in partitions(n - x, x):
                yield (x,) + t


def induced_perm(partition):
    p = list(range(8))
    i = 0
    for d in partition:
        for j in range(d):
            p[i + j] = i + (j + 1) % d
        i += d
    assert i == 8
    return tuple(p)


def image(tetrad, perm):
    return tuple(sorted(tuple(sorted((perm[u], perm[v]))) for u, v in tetrad))


def geometric_sets():
    square = set()
    for v in combinations(V, 4):
        a, b, c, d = v
        for ea in (((a,b), (b,c), (c,d), (a,d)),
                   ((a,b), (b,d), (c,d), (a,c)),
                   ((a,c), (b,c), (b,d), (a,d))):
            square.add(tuple(sorted(tuple(sorted(e)) for e in ea)))
    # Independently enumerate matchings by 4-subsets of the entire edge set.
    match = {tuple(sorted(es)) for es in combinations(E, 4)
             if len({x for e in es for x in e}) == 8}
    return square, match


def parity_sets():
    # Odd theta characteristics correspond to the 28 2-subsets.
    # Their fourfold sum vanishes in even-subsets modulo the all-one vector.
    zero = set()
    for es in combinations(E, 4):
        mask = 0
        for a, b in es:
            mask ^= (1 << a) ^ (1 << b)
        if mask == 0 or mask == 255:
            zero.add(tuple(es))
    return zero


def cycles(objects, perm):
    unseen = set(objects)
    out = Counter()
    while unseen:
        first = next(iter(unseen))
        cur = first
        size = 0
        while cur in unseen:
            unseen.remove(cur)
            size += 1
            cur = image(cur, perm)
        assert cur == first
        out[size] += 1
    return dict(sorted(out.items()))


def fixed_power(objects, perm, m):
    x = tuple(range(8))
    for _ in range(m):
        x = tuple(perm[v] for v in x)
    return sum(image(t, x) == t for t in objects)


def binomial(n, k):
    from math import comb
    return comb(n, k)


def main():
    sq, ma = geometric_sets()
    assert len(sq) == 210 and len(ma) == 105 and not (sq & ma)
    assert sq | ma == parity_sets()
    assert len(sq | ma) == 315
    parts = list(partitions(8))
    assert len(parts) == 22 and len(set(parts)) == 22
    weighted_fixed_sq = weighted_fixed_ma = weighted_fixed_bit = 0
    sum_class = 0
    have_exceptions = set()
    for part in parts:
        p = induced_perm(part)
        q = cycles(sq, p)
        m = cycles(ma, p)
        c = {d: q.get(d, 0) + m.get(d, 0) for d in sorted(q.keys() | m.keys())}
        assert sum(d * n for d, n in q.items()) == 210
        assert sum(d * n for d, n in m.items()) == 105
        # Cycle counts independently reconstructed from fixed-point counts.
        for family, report in [(sq, q), (ma, m), (sq | ma, c)]:
            for k in range(1, max(report) + 1):
                direct = fixed_power(family, p, k)
                inferred = sum(d * n for d, n in report.items() if k % d == 0)
                assert direct == inferred, (part, k)
        order = 1
        for d in part:
            order = order * d // gcd(order, d)
        splitting = 1
        for d in c:
            splitting = splitting * d // gcd(splitting, d)
        assert splitting == order
        rf = sum(tuple(sorted((p[a], p[b]))) == (a, b) for a, b in E)
        fixed_t = c.get(1, 0)
        no_five_seven = 5 not in part and 7 not in part
        assert (fixed_t > 0) == no_five_seven
        if rf == 0 and fixed_t > 0:
            have_exceptions.add(part)
        counts = Counter(part)
        class_size = factorial(8)
        for length, number in counts.items():
            class_size //= (length ** number) * factorial(number)
        sum_class += class_size
        weighted_fixed_sq += class_size * q.get(1, 0)
        weighted_fixed_ma += class_size * m.get(1, 0)
        weighted_fixed_bit += class_size * rf
        print(','.join(map(str, part)), 'Q', q, 'M', m, 'ALL', c,
              'rational_bitangents', rf, 'rational_tetrads', fixed_t)
    assert sum_class == factorial(8)
    assert weighted_fixed_sq == weighted_fixed_ma == weighted_fixed_bit == factorial(8)
    # The two types of tetrads are distinct S8-orbits, each with Burnside average 1.
    assert have_exceptions == {(8,), (4, 4), (4, 3, 1)}
    print('CAYLEY_OCTAD_TETRAD_FROBENIUS_VERIFIED_OK')


if __name__ == '__main__':
    main()
