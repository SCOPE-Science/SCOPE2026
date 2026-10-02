#!/usr/bin/env python3
"""Finite checks for the composite-chi conjugacy and cryptographic corollaries."""

from math import gcd


def bits(z, n):
    return [(z >> i) & 1 for i in range(n)]


def pack(xs):
    return sum((b & 1) << i for i, b in enumerate(xs))


def chi_nv(z, n, v):
    x = bits(z, n)
    y = [x[i] ^ (x[(i + v) % n] & x[(i + 2 * v) % n]) ^ x[(i + 2 * v) % n]
         for i in range(n)]
    return pack(y)


def chi_minus2v(z, n, v):
    x = bits(z, n)
    y = [x[i] ^ (x[(i - 2 * v) % n] & x[(i - v) % n]) ^ x[(i - v) % n]
         for i in range(n)]
    return pack(y)


def chi_std(z, ell):
    return chi_nv(z, ell, 1)


def cycles(n, v):
    seen = set()
    out = []
    for r in range(n):
        if r in seen:
            continue
        cyc = []
        a = r
        while a not in seen:
            seen.add(a)
            cyc.append(a)
            a = (a + v) % n
        out.append(cyc)
    return out


def to_blocks(z, n, v):
    x = bits(z, n)
    return [pack([x[i] for i in cyc]) for cyc in cycles(n, v)]


def block_involution(z, ell):
    x = bits(z, ell)
    return pack([x[(-i) % ell] ^ 1 for i in range(ell)])


def mobius_degree(values, n):
    a = values[:]
    for i in range(n):
        for m in range(1 << n):
            if (m >> i) & 1:
                a[m] ^= a[m ^ (1 << i)]
    return max((m.bit_count() for m, c in enumerate(a) if c), default=0)


def inverse_degree(fun, n):
    inv = [0] * (1 << n)
    for x in range(1 << n):
        inv[fun(x)] = x
    return max(mobius_degree([(inv[y] >> j) & 1 for y in range(1 << n)], n)
               for j in range(n))


def differential_uniformity(fun, n):
    vals = [fun(x) for x in range(1 << n)]
    best = 0
    for a in range(1, 1 << n):
        counts = {}
        for x in range(1 << n):
            b = vals[x] ^ vals[x ^ a]
            counts[b] = counts.get(b, 0) + 1
        best = max(best, max(counts.values()))
    return best


def main():
    cases = [(6, 2), (10, 2), (12, 4)]
    for n, v in cases:
        d = gcd(n, v)
        ell = n // d
        assert ell % 2 == 1
        for z in range(1 << n):
            b = to_blocks(z, n, v)
            out1 = to_blocks(chi_nv(z, n, v), n, v)
            assert out1 == [chi_std(a, ell) for a in b]
            out2 = to_blocks(chi_minus2v(z, n, v), n, v)
            assert out2 == [block_involution(chi_std(block_involution(a, ell), ell), ell)
                            for a in b]
        print(f"conjugacy PASS n={n} v={v} d={d} ell={ell}")

    for n, v in [(6, 2), (10, 2)]:
        ell = n // gcd(n, v)
        target_degree = (ell + 1) // 2
        deg1 = inverse_degree(lambda x, n=n, v=v: chi_nv(x, n, v), n)
        deg2 = inverse_degree(lambda x, n=n, v=v: chi_minus2v(x, n, v), n)
        assert deg1 == target_degree == deg2
        print(f"inverse-degree PASS n={n} v={v} degree={target_degree}")

    for n, v in [(6, 2), (10, 2)]:
        ell = n // gcd(n, v)
        if ell % 2 == 0:
            continue
        du = differential_uniformity(lambda x, n=n, v=v: chi_nv(x, n, v), n)
        assert du == 1 << (n - 2)
        print(f"differential-uniformity PASS n={n} v={v} delta={du}")

    print("PASS")


if __name__ == "__main__":
    main()
