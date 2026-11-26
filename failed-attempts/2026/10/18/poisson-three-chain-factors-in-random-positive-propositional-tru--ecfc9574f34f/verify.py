"""Standalone finite checks for positive truth-set lattices from Boolean valuations.

Run: python3 verify.py. Uses only the Python standard library.
"""
from fractions import Fraction
from itertools import combinations, product


def close_formulas(generators, full, negation):
    family = {0, full} | set(generators)
    changed = True
    while changed:
        prev = set(family)
        if negation:
            family.update(full ^ u for u in prev)
        for a in prev:
            for b in prev:
                family.add(a | b)
                family.add(a & b)
        changed = len(family) > len(prev)
    return family


def is_leq(x, y):
    return x & ~y == 0


def order_upsets(rows):
    n = len(rows)
    return {u for u in range(1 << n)
            if all(not ((u >> i) & 1) or ((u >> j) & 1)
                   for i in range(n) for j in range(n)
                   if is_leq(rows[i], rows[j]))}


def comparable(x, y):
    return is_leq(x, y) or is_leq(y, x)


def checks():
    exhaustive = 0
    matching = 0
    for m in range(4):
        for n in range(5):
            if m * n > 12:
                continue
            for rows in product(range(1 << m), repeat=n):
                gens = [sum(((r >> j) & 1) << i for i, r in enumerate(rows))
                        for j in range(m)]
                full = (1 << n) - 1
                positive = close_formulas(gens, full, False)
                actual_upsets = order_upsets(rows)
                assert positive == actual_upsets, (m, n, rows, positive, actual_upsets)
                boolean = close_formulas(gens, full, True)
                distinct = len(set(rows)) == n
                assert (len(boolean) == (1 << n)) == distinct
                edges = [(i, j) for i in range(n) for j in range(i + 1, n)
                         if comparable(rows[i], rows[j])]
                degrees = [sum(i in edge for edge in edges) for i in range(n)]
                if distinct and max(degrees, default=0) <= 1:
                    assert len(positive) == 3 ** len(edges) * 2 ** (n - 2 * len(edges))
                    matching += 1
                exhaustive += 1

    moments = 0
    for m in range(1, 7):
        vectors = range(1 << m)
        ordered = sum(comparable(a, b) for a in vectors for b in vectors)
        prob = Fraction(ordered, 2 ** (2 * m))
        expected = 2 * Fraction(3, 4)**m - Fraction(1, 2)**m
        assert prob == expected
        triplets = sum(comparable(a, b) and comparable(a, c)
                       for a in vectors for b in vectors for c in vectors)
        joint = Fraction(triplets, 2 ** (3 * m))
        assert joint <= 4 * Fraction(5, 8)**m
        moments += 1

    print(f"VERIFY_OK {exhaustive} exhaustive finite valuations; "
          f"{matching} matching-poset factorizations; {moments} exact moment bounds")


if __name__ == '__main__':
    checks()
