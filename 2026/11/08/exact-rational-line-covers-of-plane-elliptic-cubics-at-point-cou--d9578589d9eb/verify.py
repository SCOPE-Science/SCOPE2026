"""Finite checks for the exact elliptic-cubic rational-line covering theorem.

The mathematical proof uses zero-sum partitions and near transversals;
finite verification here is corroboration and does not establish the general case.
Requires Python 3; scipy and numpy are optional for geometry checks.
"""
from itertools import product


def cyclic_near_cover(k):
    """Disjoint zero-sum triples with exactly three unused elements in Z/(6k)."""
    n, m = 6 * k, 2 * k
    triples = []
    for i in range(m - 1):
        j = i if i < k else i + 1
        ell = (-1 - i - j) % m
        triple = (3 * i, 3 * j + 1, 3 * ell + 2)
        assert sum(triple) % n == 0
        triples.append(triple)
    used = [a for triple in triples for a in triple]
    assert len(set(used)) == len(used) == n - 3
    remaining = set(range(n)) - set(used)
    assert len(remaining) == 3
    assert sum(remaining) % n == 3 * k
    return triples, remaining


def projective_lines(p):
    forms = [(a, b, 1) for a in range(p) for b in range(p)]
    forms += [(a, 1, 0) for a in range(p)] + [(1, 0, 0)]
    return forms


def plane_cubic(p, a, b):
    assert p > 3 and (4 * a ** 3 + 27 * b ** 2) % p
    affine = [(x, y) for x in range(p) for y in range(p)
              if (y * y - x ** 3 - a * x - b) % p == 0]
    return affine + [None]  # None represents [0:1:0].


def line_covers(p, a, b):
    pts = plane_cubic(p, a, b)
    lines = projective_lines(p)
    masks = []
    for A, B, C in lines:
        mask = 0
        for i, point in enumerate(pts):
            hit = B % p == 0 if point is None else (A * point[0] + B * point[1] + C) % p == 0
            if hit:
                mask |= 1 << i
        assert mask.bit_count() <= 3
        masks.append(mask)
    return pts, masks


def certify_small_field(p, a, b):
    # Exhaustive dynamic programming over covered subsets, feasible for |E| <= 12.
    pts, masks = line_covers(p, a, b)
    n = len(pts)
    assert n <= 12 and n % 3 == 0
    unique_involution = sum((x ** 3 + a * x + b) % p == 0 for x in range(p)) == 1
    predicted = n // 3 + int(unique_involution)
    cover = {0: 0}
    for mask in masks:
        nxt = dict(cover)
        for covered, number in cover.items():
            union = covered | mask
            if union not in nxt or nxt[union] > number + 1:
                nxt[union] = number + 1
        cover = nxt
    assert cover[(1 << n) - 1] == predicted
    return p, a, b, n, int(unique_involution), predicted


def main():
    for k in range(1, 501):
        cyclic_near_cover(k)
    print('CYCLIC_NEAR_COVER_CONSTRUCTION_OK 500')
    examples = ((5, 0, 1), (5, 1, 1), (7, 0, 1),
                (7, 0, 2), (11, 0, 1), (11, 1, 4))
    for sample in examples:
        print('EXHAUSTIVE_GEOMETRIC_COVER_OK', *certify_small_field(*sample))
    print('ELLIPTIC_CUBIC_LINE_COVER_CHECKS_OK')


if __name__ == '__main__':
    main()
