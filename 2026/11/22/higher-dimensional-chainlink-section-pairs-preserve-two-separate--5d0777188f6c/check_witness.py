"""Exact reconstruction of two complementary chainlink three-polytopes."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations


def solve(A, b):
    rows = [list(map(Q, row)) + [Q(y)] for row, y in zip(A, b)]
    for j in range(4):
        i = next((i for i in range(j, 4) if rows[i][j]), None)
        if i is None:
            return None
        rows[i], rows[j] = rows[j], rows[i]
        pivot = rows[j][j]
        rows[j] = [x / pivot for x in rows[j]]
        for i in range(4):
            if i != j:
                factor = rows[i][j]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[j])]
    return tuple(row[-1] for row in rows)


def polygon_area(points):
    pts = sorted(set(points))
    if len(pts) < 3:
        return Q(0)
    hull = [pts[0]]
    while True:
        p = hull[-1]
        q = next(x for x in pts if x != p)
        for r in pts:
            cross = (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])
            dist = lambda w: sum((x - y) ** 2 for x, y in zip(p, w))
            if cross < 0 or (cross == 0 and dist(r) > dist(q)):
                q = r
        if q == hull[0]:
            break
        assert q not in hull
        hull.append(q)
    return abs(sum(p[0] * q[1] - p[1] * q[0]
                   for p, q in zip(hull, hull[1:] + hull[:1]))) / 2


def witness(height):
    a, ell = (4, 5, 6, 7), 2
    I = [tuple(int(i == j) for j in range(4)) for i in range(4)]
    halfspaces = [(tuple(-x for x in I[i]), 0, 'coordinate') for i in range(4)]
    halfspaces += [(I[i], a[i], 'coordinate') for i in range(4)]
    halfspaces += [(tuple(x - y for x, y in zip(I[i], I[(i+1) % 4])),
                    a[i] - ell, 'link') for i in range(4)]
    dot = lambda u, v: sum(x * y for x, y in zip(u, v))
    pts = set()
    for planes in combinations(halfspaces, 3):
        v = solve([(1, 1, 1, 1)] + [n for n, _, _ in planes],
                  [height] + [b for _, b, _ in planes])
        if v is not None and all(dot(v, n) <= b for n, b, _ in halfspaces):
            pts.add(v)
    counts, areas = Counter(), Counter()
    for n, b, kind in halfspaces:
        i, j = max(combinations(range(4), 2), key=lambda pair: abs(n[pair[0]] - n[pair[1]]))
        # The square of the full-plane Jacobian numerator is the determinant
        # of the Gram matrix of the height normal and n. The projection minor
        # has magnitude |n[i]-n[j]|. Numerators: sqrt(3), sqrt(8).
        minor = abs(n[i] - n[j])
        u, v = [w for w in range(4) if w not in (i, j)]
        area = polygon_area([(pt[u], pt[v]) for pt in pts if dot(pt, n) == b])
        if area:
            counts[kind] += 1
            areas[kind] += area / minor
    return len(pts), dict(counts), dict(areas)


if __name__ == '__main__':
    for height, vertices in [(9, 16), (13, 15)]:
        V, counts, areas = witness(height)
        assert V == vertices and counts == {'coordinate': 7, 'link': 4}
        assert areas == {'coordinate': Q(43), 'link': Q(49, 2)}
        F = sum(counts.values())
        print(height, (V, V + F - 2, F), counts, areas)
