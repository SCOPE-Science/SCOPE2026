#!/usr/bin/env python3
"""Exact small-case checks for a cubical-graph zonotope sphere theorem.

No floating-point decisions are needed. Python 3.10+; standard library only.
"""
from itertools import product
from random import Random


def edges_of_cube(d):
    n = 1 << d
    return [(v, v ^ (1 << j)) for v in range(n) for j in range(d) if v < (v ^ (1 << j))]


def crossing(mask, edges):
    return sum(((mask >> a) ^ (mask >> b)) & 1 for a, b in edges)


def run():
    checks = 0
    summary = []
    rand = Random(220919)
    for d in range(1, 10):
        n = 1 << d
        e = edges_of_cube(d)
        r2 = min(n, (d + 1) ** 2)
        if d <= 4:
            masks = range(1, 1 << n)
            mode = 'exhaustive'
        else:
            masks = [1 << v for v in range(n)] + [(1 << n) - 1]
            masks += [((1 << k) - 1) for k in range(1, min(n, 30))]
            masks += [sum(1 << v for v in range(n) if (v & ((1 << s) - 1)) == 0) for s in range(1, d + 1)]
            masks += [rand.getrandbits(n) or 1 for _ in range(2500 if d < 8 else 750)]
            mode = 'sampled'
        equality = set()
        count = 0
        for mask in masks:
            k = mask.bit_count()
            b = crossing(mask, e)
            numerator = (k + b) ** 2
            assert numerator >= r2 * k, (d, mask, k, b, r2)
            checks += 1
            count += 1
            if numerator == r2 * k:
                equality.add(mask)
                assert (k == n and d <= 5) or (k == 1 and d >= 6), (d, k)
                checks += 1
        assert ((1 << n) - 1 in equality) == (d <= 5)
        checks += 1
        if d >= 6:
            assert len({m for m in equality if m.bit_count() == 1}) == n
            checks += 1
        sign = [1 if v.bit_count() % 2 == 0 else -1 for v in range(n)]
        farthest = sign[:]
        for a, b in e:
            if sign[a] > sign[b]:
                farthest[a] += 1
                farthest[b] -= 1
            else:
                farthest[a] -= 1
                farthest[b] += 1
        assert all(farthest[v] == (d + 1) * sign[v] for v in range(n))
        assert sum(x * x for x in farthest) == n * (d + 1) ** 2
        checks += 2
        summary.append((d, n, r2, n * (d + 1) ** 2, mode, count, len(equality)))

    # Independent endpoint-sign enumeration of the entire Minkowski sum in low dimension.
    for d in (1, 2):
        n = 1 << d
        e = edges_of_cube(d)
        max_r2 = n * (d + 1) ** 2
        touches = set()
        for signs in product((-1, 1), repeat=n + len(e)):
            vec = list(signs[:n])
            for j, (a, b) in enumerate(e):
                vec[a] += signs[n + j]
                vec[b] -= signs[n + j]
            norm2 = sum(v * v for v in vec)
            assert norm2 <= max_r2
            if norm2 == max_r2:
                touches.add(tuple(vec))
            checks += 1
        assert len(touches) == 2
        checks += 1
    for line in summary:
        print('dimension=%d graph_vertices=%d inradius_squared=%d outer_radius_squared=%d mode=%s cuts_checked=%d equality_cut_samples=%d' % line)
    print('TOTAL_ASSERTIONS=', checks)
    print('VERIFICATION_PASSED')


if __name__ == '__main__':
    run()
