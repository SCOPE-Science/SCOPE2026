#!/usr/bin/env python3
"""Exact support-polytope certificate and small-field rank test for a seven-character toric code.

Only standard-library integer arithmetic is used. The polynomial proof for all
prime powers is in RESULT.md; this program certifies its finite sublemma.
"""
from collections import Counter
from itertools import combinations

E = ((-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0))
P = set(E)


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(points):
    s = sorted(set(points))
    if len(s) <= 2:
        return tuple(s)
    low, high = [], []
    for point in s:
        while len(low) >= 2 and cross(low[-2], low[-1], point) <= 0:
            low.pop()
        low.append(point)
    for point in reversed(s):
        while len(high) >= 2 and cross(high[-2], high[-1], point) <= 0:
            high.pop()
        high.append(point)
    return tuple(low[:-1] + high[:-1])


def normal_form(points):
    minx = min(x for x, y in points)
    miny = min(y for x, y in points)
    return tuple(sorted((x - minx, y - miny) for x, y in points))


def residual(q):
    # Every translation of a shape fitting the width-two polygon is in [-2,2]^2.
    return tuple(sorted((a, b) for a in range(-3, 4) for b in range(-3, 4)
                        if all((x+a, y+b) in P for x, y in q)))


def area2(poly):
    if len(poly) < 3:
        return 0
    return abs(sum(poly[i][0] * poly[(i+1) % len(poly)][1]
                   - poly[(i+1) % len(poly)][0] * poly[i][1]
                   for i in range(len(poly))))


def newton_certificate():
    seen = set()
    for size in range(1, 8):
        for subset in combinations(E, size):
            seen.add(normal_form(convex_hull(subset)))
    qualified = []
    for q in seen:
        r = residual(q)
        if len(q) >= 2 and len(r) >= 3:
            qualified.append((q, r))
    assert len(qualified) == 5, qualified
    counts = Counter(len(q) for q, r in qualified)
    assert counts == {2: 3, 3: 2}, counts
    assert all(len(r) == 4 and area2(convex_hull(r)) == 2
               for q, r in qualified if len(q) == 2)
    assert all(len(r) == 3 and area2(convex_hull(r)) == 1
               and area2(convex_hull(q)) == 1
               for q, r in qualified if len(q) == 3)
    assert not any(len(q) >= 4 for q,r in qualified)
    print('NEWTON_3_RESIDUAL_SHAPES: 3 segments, 2 unit triangles; OK')
    for q, r in sorted(qualified):
        print('Q=', q, 'R=', r)


def rank_mod(rows, prime):
    if not rows:
        return 0
    A = [list(row) for row in rows]
    rank = 0
    for col in range(len(A[0])):
        pivot = next((i for i in range(rank, len(A)) if A[i][col] % prime), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][col], -1, prime)
        A[rank] = [(v * inv) % prime for v in A[rank]]
        for i in range(rank + 1, len(A)):
            factor = A[i][col]
            if factor:
                A[i] = [(x - factor * y) % prime
                        for x, y in zip(A[i], A[rank])]
        rank += 1
        if rank == len(A):
            break
    return rank


def eval_matrix(prime):
    return {(x, y): tuple(pow(x, a % (prime - 1), prime)
                         * pow(y, b % (prime - 1), prime) % prime
                         for a, b in E)
            for x in range(1, prime) for y in range(1, prime)}


def rank_certificates():
    prime = 5
    matrix = eval_matrix(prime)
    pts = tuple(matrix)
    for k, threshold, count in ((6, 5, 8008), (5, 4, 4368)):
        tested = 0
        minimum = 7
        for inds in combinations(range(len(pts)), k):
            minimum = min(minimum, rank_mod([matrix[pts[i]] for i in inds], prime))
            tested += 1
        assert tested == count and minimum == threshold, (k, tested, minimum)
        print('F5_ALL_%s_SUBSETS: %s subsets, minimum evaluation rank %s; OK' %
              (k, tested, minimum))
    for prime in (5, 7, 11):
        M = eval_matrix(prime)
        t = prime - 1
        a, b, c = 1, 2, 1
        fiber = [(a, y) for y in range(1, prime)]
        off = (b, c)
        assert off not in fiber
        s3 = fiber + [off]
        s4 = fiber
        assert rank_mod([M[p] for p in s3], prime) == 4
        assert rank_mod([M[p] for p in s4], prime) == 3
        print('F%s_CONSTRUCTIONS: r3 %s common zeros, r4 %s common zeros; OK' %
              (prime, t + 1, t))
    print('HEXAGON_HIGHER_WEIGHTS_VERIFIED')


if __name__ == '__main__':
    assert area2(convex_hull(E)) == 6
    newton_certificate()
    rank_certificates()
