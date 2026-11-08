#!/usr/bin/env python3
"""Exact finite checks for a sharp fundamental-pair Minkowski obstruction."""
from itertools import combinations, product


def comparable(p, q):
    return (p[0] <= q[0] and p[1] <= q[1]) or (q[0] <= p[0] and q[1] <= p[1])


def antichain(points):
    return all(not comparable(points[i], points[j])
               for i in range(len(points)) for j in range(i + 1, len(points)))


def width(points):
    return max((len(t) for r in range(len(points) + 1)
                for t in combinations(points, r) if antichain(t)), default=0)


def in_S_sum(d, points):
    # Exact inequalities: sum over each width-k subposet <= min(k,2)+min(k,d).
    for r in range(len(points) + 1):
        for q in combinations(points, r):
            if r > min(width(q), 2) + min(width(q), d):
                return False
    return True


def decomposable(points):
    n = len(points)
    for a_size in range(min(2, n) + 1):
        for inds in combinations(range(n), a_size):
            a = set(inds)
            if antichain([points[i] for i in a]) and antichain(
                    [points[i] for i in range(n) if i not in a]):
                return True
    return False


def double_star_count(h, d):
    # Count six-element subsets whose comparability graph is the connected
    # double star, whose two degree-three hubs are adjacent.
    pts = list(product(range(h), range(d)))
    n = len(pts)
    comps = [[int(i != j and comparable(pts[i], pts[j]))
              for j in range(n)] for i in range(n)]
    total = 0
    for inds in combinations(range(n), 6):
        deg = [sum(comps[i][j] for j in inds) for i in inds]
        if sorted(deg) != [1, 1, 1, 1, 3, 3]:
            continue
        hubs = [i for i, k in zip(inds, deg) if k == 3]
        if comps[hubs[0]][hubs[1]]:
            total += 1
    return total


def main():
    # Coordinates (row, column), 0-indexed; allowed in [5]x[4].
    witness = [(0, 3), (1, 2), (2, 0),
               (2, 3), (3, 1), (4, 0)]
    assert len(set(witness)) == 6
    assert in_S_sum(4, witness)
    assert not decomposable(witness)
    assert double_star_count(4, 4) == 0
    assert double_star_count(5, 4) == 1
    # The same six points embed in every [h]x[d] with h>=5 and d>=4.
    for d in range(4, 9):
        assert in_S_sum(d, witness)
        assert not decomposable(witness)
    # For d<=3, the all-parameter argument is by |s|<=d+2<=5
    # and Mirsky's height-two antichain partition, not finite testing.
    print('CERTIFICATE_OK')
    print('four_by_four_double_stars=', double_star_count(4, 4))
    print('five_by_four_double_stars=', double_star_count(5, 4))
    print('witness=', witness)


if __name__ == '__main__':
    main()
