#!/usr/bin/env python3
"""Independent direct trace enumeration for open-neighborhood Hamming families."""
from itertools import combinations, product
from math import comb

CASES = [(1, 2), (1, 3), (1, 5), (2, 2), (2, 3), (2, 4),
         (2, 5), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3),
         (5, 2), (6, 2)]

def formula(d, q):
    n = q ** d
    if d == 1 or (d, q) == (2, 2):
        pairs = 0
    elif q == 2:
        pairs = n * comb(d, 2) // 2
    else:
        pairs = n * (d * (q - 1) + comb(d, 2) * (q - 1) ** 2) // 2
    first = 0
    second = 0
    third = 0
    if d >= 2 and q >= 4:
        first = d * q ** (d - 1) * comb(q, 3)
        second = n * d * (d - 1) * comb(q - 1, 2) * (q - 1)
    if d >= 3 and (q >= 3 or d >= 4):
        third = n * comb(d, 3) * (q - 1) ** 3
    return (1, n, pairs, first + second + third), (first, second, third)

def check(d, q):
    vertices = list(product(range(q), repeat=d))
    n = len(vertices)
    all_centers = (1 << n) - 1
    membership_by_query = [0] * n
    for c, center in enumerate(vertices):
        for v, vertex in enumerate(vertices):
            if sum(a != b for a, b in zip(center, vertex)) == 1:
                membership_by_query[v] |= 1 << c
    def shattered(support):
        k = len(support)
        for pattern in range(1 << k):
            centers = all_centers
            for i, v in enumerate(support):
                mask = membership_by_query[v]
                centers &= mask if (pattern >> i) & 1 else (all_centers ^ mask)
                if not centers:
                    return False
        return True
    counts = [1]
    triple_types = [0, 0, 0]
    for k in (1, 2, 3):
        count = 0
        for support in combinations(range(n), k):
            actual = shattered(support)
            if k == 2:
                distance = sum(a != b for a, b in zip(vertices[support[0]], vertices[support[1]]))
                expected = ((distance == 1 and d >= 2 and q >= 3) or
                            (distance == 2 and (q >= 3 or d >= 3)))
                assert actual == expected, ('pair', d, q, support, actual, expected)
            if actual:
                count += 1
                if k == 3:
                    distances = sorted(sum(a != b for a, b in zip(vertices[u], vertices[v]))
                                       for u, v in combinations(support, 2))
                    choices = {(1, 1, 1): 0, (1, 2, 2): 1, (2, 2, 2): 2}
                    assert tuple(distances) in choices, ('unexpected triple type', d, q, support, distances)
                    triple_types[choices[tuple(distances)]] += 1
        counts.append(count)
    expected_counts, expected_types = formula(d, q)
    assert tuple(counts) == expected_counts, (d, q, counts, expected_counts)
    assert tuple(triple_types) == expected_types, (d, q, triple_types, expected_types)
    four_count = None
    if n <= 27:
        four_count = sum(shattered(S) for S in combinations(range(n), 4))
        assert four_count == 0, ('four-point shattering', d, q, four_count)
    print(f'd={d} q={q} n={n}: shattered[0..3]={counts} '
          f'triple-types={triple_types} four={four_count if four_count is not None else "proof-only"}')
    return n, counts

if __name__ == '__main__':
    for args in CASES:
        check(*args)
    print('ALL_QARY_OPEN_HAMMING_SHATTERING_CHECKS_PASS')
