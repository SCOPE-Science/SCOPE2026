"""Direct exhaustive checks of dissociation sets in two-subset Kneser graphs.

Requires only the Python standard library. Run: python verify.py
The unrestricted statements are mathematical theorems, not consequences of
these finite checks.
"""
from itertools import combinations
from math import comb


def build(n):
    edges = list(combinations(range(n), 2))
    neighbors = []
    for i, a in enumerate(edges):
        neighbors.append(sum(1 << j for j, b in enumerate(edges)
                             if j != i and len(set(a) & set(b)) == 0))
    return edges, neighbors


def valid(mask, neighbors):
    return all((mask & adj).bit_count() <= 1
               for i, adj in enumerate(neighbors) if (mask >> i) & 1)


def maximal(mask, neighbors):
    if not valid(mask, neighbors):
        return False
    return all(not valid(mask | (1 << i), neighbors)
               for i in range(len(neighbors)) if not (mask >> i) & 1)


def all_coefficients(n):
    N = comb(n, 2)
    a = [0] * (N + 1)
    a[0], a[1], a[2] = 1, N, comb(N, 2)
    a[3] = n * comb(n - 1, 3) + comb(n, 3) + 12 * comb(n, 4)
    for j in range(4, N + 1):
        if j <= n - 1:
            a[j] += n * comb(n - 1, j)
        if j <= 6:
            a[j] += comb(n, 4) * comb(6, j)
    return a


def maximal_coefficients(n):
    a = [0] * (comb(n, 2) + 1)
    a[6] = comb(n, 4)
    if n >= 5:
        a[n - 1] += n
    return a


def generated_maximal_masks(n, edges):
    masks = set()
    for support in combinations(range(n), 4):
        vertices = set(support)
        masks.add(sum(1 << i for i, a in enumerate(edges)
                      if set(a) <= vertices))
    if n >= 5:
        for center in range(n):
            masks.add(sum(1 << i for i, a in enumerate(edges)
                          if center in a))
    return masks


def main():
    tested = 0
    all_dissociation = 0
    all_maximal = 0
    for n in range(4, 8):
        edges, neighbors = build(n)
        a = [0] * (len(edges) + 1)
        m = [0] * (len(edges) + 1)
        for mask in range(1 << len(edges)):
            tested += 1
            if valid(mask, neighbors):
                a[mask.bit_count()] += 1
                all_dissociation += 1
                if maximal(mask, neighbors):
                    m[mask.bit_count()] += 1
                    all_maximal += 1
        assert a == all_coefficients(n), ('all-set coefficients', n)
        assert m == maximal_coefficients(n), ('maximal coefficients', n)
        actual = {mask for mask in range(1 << len(edges))
                  if maximal(mask, neighbors)}
        assert actual == generated_maximal_masks(n, edges), ('maximal families', n)
    assert tested == 2131008
    generated = 0
    for n in range(8, 13):
        edges, neighbors = build(n)
        masks = generated_maximal_masks(n, edges)
        assert len(masks) == comb(n, 4) + n
        assert all(maximal(mask, neighbors) for mask in masks)
        generated += len(masks)
    print('VERIFY_OK full_orders=4..7 subsets=%d dissociation_sets=%d maximal_sets=%d'
          ' polynomials=PASS structural_families=PASS generated_orders=8..12'
          ' generated_maximal_sets=%d' %
          (tested, all_dissociation, all_maximal, generated))


if __name__ == '__main__':
    main()
