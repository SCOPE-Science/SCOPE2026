#!/usr/bin/env python3
"""Exact small-design consistency tests for a general analytic theorem."""
from itertools import combinations
from fractions import Fraction


def rank_rational(matrix):
    a = [[Fraction(t) for t in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    piv = 0
    for col in range(cols):
        lead = next((i for i in range(piv, rows) if a[i][col]), None)
        if lead is None:
            continue
        a[piv], a[lead] = a[lead], a[piv]
        factor = a[piv][col]
        a[piv] = [x / factor for x in a[piv]]
        for i in range(rows):
            if i != piv and a[i][col]:
                factor = a[i][col]
                a[i] = [u - factor * v for u, v in zip(a[i], a[piv])]
        piv += 1
        if piv == rows:
            break
    return piv


def verify_design(points, blocks, k, lam):
    v, b = len(points), len(blocks)
    r = lam * (v - 1) // (k - 1)
    assert r * (k - 1) == lam * (v - 1)
    assert b * k == v * r
    assert all(len(set(block)) == k for block in blocks)
    assert all(sum(p in block for block in blocks) == r for p in points)
    pairs = list(combinations(points, 2))
    q = [[int(set(pair).issubset(block)) for block in blocks] for pair in pairs]
    assert all(sum(row) == lam for row in q)
    bb = [[sum(i in block and j in block for block in blocks) for j in points] for i in points]
    assert bb == [[r if i == j else lam for j in points] for i in points]
    return q


def main():
    six = tuple(range(6))
    triples = [frozenset(t) for t in combinations(six, 3)]
    q = verify_design(six, triples, 3, 4)
    assert rank_rational(q) == 15
    h = [0] * len(triples)
    matched = ({0, 1}, {2, 3}, {4, 5})
    for j, triple in enumerate(triples):
        if all(len(triple.intersection(s)) == 1 for s in matched):
            h[j] = (-1) ** len(triple.intersection({1, 3, 5}))
    assert sorted(x for x in h if x) == [-1] * 4 + [1] * 4
    assert all(sum(x * y for x, y in zip(row, h)) == 0 for row in q)
    for sign in (-1, 0, 1):
        weights = [Fraction(1, 20) + Fraction(sign, 20) * x for x in h]
        assert sum(weights) == 1 and min(weights) >= 0
        assert all(sum(x * y for x, y in zip(row, weights)) == Fraction(4, 20) for row in q)

    points = [(x, y) for x in range(3) for y in range(3)]
    lines = []
    for m in range(3):
        for c in range(3):
            lines.append(frozenset((x, (m * x + c) % 3) for x in range(3)))
    for c in range(3):
        lines.append(frozenset((c, y) for y in range(3)))
    qaff = verify_design(points, lines, 3, 1)
    assert rank_rational(qaff) == len(lines)
    print('DESIGN_TRADE_EXACT_OK rank15 nullity5 affine9x12')


if __name__ == '__main__':
    main()
