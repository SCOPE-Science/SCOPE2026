"""Exact-arithmetic checks for three-site Rule-90 trace dimensions.

Run: python3 verify_three_probe.py
This script is independent of the text proof and uses no external packages.
"""
from itertools import product
from math import gcd


def combine(a, b, p):
    c = {}
    for i, v in a.items():
        for j, w in b.items():
            n = (c.get(i + j, 0) + v * w) % p
            if n:
                c[i + j] = n
            else:
                c.pop(i + j, None)
    return c


def gaussian_rank(rows, p):
    pivots = {}
    for row in rows:
        row = dict(row)
        while row:
            top = max(row)
            if top not in pivots:
                inv = pow(row[top], -1, p)
                pivots[top] = {j: v * inv % p for j, v in row.items()}
                break
            scale = row[top]
            for j, v in pivots[top].items():
                r = (row.get(j, 0) - scale * v) % p
                if r:
                    row[j] = r
                else:
                    row.pop(j, None)
    return len(pivots)


def traces(p, h, k, t):
    f = {-1: 1, 1: 1}
    cur = {0: 1}
    rows = []
    for s in range(t):
        for i in (0, h, k):
            rows.append({e + i: v for e, v in cur.items()})
        cur = combine(cur, f, p)
    return rows


def add(a, b, p, sign=1):
    out = dict(a)
    for e, v in b.items():
        c = (out.get(e, 0) + sign * v) % p
        if c:
            out[e] = c
        else:
            out.pop(e, None)
    return out


def Bs(p, m):
    # B_0=0, B_1=1, B_{n+1}=u B_n-B_{n-1}
    x, y = {}, {0: 1}
    out = [x, y]
    for _ in range(1, m):
        z = add({e + 1: v for e, v in y.items()}, x, p, -1)
        x, y = y, z
        out.append(z)
    return out


def poly_gcd(a, b, p):
    a, b = dict(a), dict(b)
    while b:
        m = max(b)
        lead = b[m]
        u = dict(a)
        while u and max(u) >= m:
            deg = max(u) - m
            fac = u[max(u)] * pow(lead, -1, p) % p
            u = add(u, {deg + e: fac * v % p for e, v in b.items()}, p, -1)
        a, b = b, u
    if not a:
        return {}
    inv = pow(a[max(a)], -1, p)
    return {e: v * inv % p for e, v in a.items()}


def exact_distribution(p, h, k, t):
    rows = traces(p, h, k, t)
    support = sorted(set().union(*(set(x) for x in rows)))
    freq = {}
    for x in product(range(p), repeat=len(support)):
        initial = dict(zip(support, x))
        y = tuple(sum(initial.get(e, 0) * v for e, v in row.items()) % p for row in rows)
        freq[y] = freq.get(y, 0) + 1
    r = 3 * t - max(0, t - k + gcd(h, k))
    assert len(freq) == p ** r
    assert set(freq.values()) == {p ** (len(support) - r)}
    return len(freq), len(support)


def main():
    total = 0
    for p in (2, 3, 5, 7):
        for k in range(2, 19):
            for h in range(1, k):
                for t in range(1, 23):
                    r = gaussian_rank(traces(p, h, k, t), p)
                    target = 3 * t - max(0, t - k + gcd(h, k))
                    assert r == target, (p, h, k, t, r, target)
                    total += 1
    gcd_checks = 0
    for p in (2, 3, 5, 7):
        B = Bs(p, 42)
        for n in range(1, 42):
            for m in range(1, 42):
                assert poly_gcd(B[m], B[n], p) == B[gcd(m, n)]
                gcd_checks += 1
    relations = 0
    for p in (2, 3, 5, 7):
        B = Bs(p, 35)
        for k in range(2, 35):
            for h in range(1, k):
                f = {-1: 1, 1: 1}
                # B_k z^h - B_h z^k - B_{k-h} = 0 mod the Rule-90 field relation.
                # Verify by evaluating B_j(f) as Laurent polynomials.
                def at_f(poly):
                    accum = {}
                    power = {0: 1}
                    for j in range(max(poly, default=-1) + 1):
                        if j in poly:
                            scaled = {e: (v * poly[j]) % p for e, v in power.items()}
                            accum = add(accum, scaled, p)
                        power = combine(power, f, p)
                    return accum
                left = add({e + h: v for e, v in at_f(B[k]).items()},
                           {e + k: v for e, v in at_f(B[h]).items()}, p, -1)
                left = add(left, at_f(B[k - h]), p, -1)
                assert not left, (p, h, k, left)
                relations += 1
    dist = []
    for ex in ((2, 1, 2, 2), (2, 1, 3, 3), (2, 2, 4, 3), (3, 1, 2, 2)):
        dist.append((ex, exact_distribution(*ex)))
    print(f'VERIFY_OK all_prime_field_ranks={total} Laurent_relations={relations} strong_divisibility={gcd_checks} full_distributions={len(dist)}')
    for ex, ans in dist:
        print('distribution', ex, 'output_patterns=', ans[0], 'input_sites=', ans[1])

if __name__ == '__main__':
    main()
