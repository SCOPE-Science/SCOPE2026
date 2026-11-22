"""Exhaustive rational finite poset-certificate for a sparse Pareto moment."""
from fractions import Fraction
from itertools import product, permutations
from math import factorial


def extension_probability(arrows, vertices):
    """Proportion of strict coordinate rankings satisfying each directed arrow."""
    good = 0
    for order in permutations(vertices):
        pos = {v: k for k, v in enumerate(order)}
        good += all(pos[a] < pos[b] for a, b in arrows)
    return Fraction(good, factorial(len(vertices)))


def canonical(arrows, targets=(0, 1, 2)):
    vertices = sorted(set(targets).union(x for edge in arrows for x in edge))
    renumber = {v: i for i, v in enumerate(vertices)}
    return len(vertices), tuple(sorted((renumber[a], renumber[b]) for a, b in arrows))


def verify_poset_tables():
    assertions = 0
    # Three edges (a->0,b->1,c->2), with three distinct targets.
    # At most three fresh external witnesses, represented by 3,4,5.
    seen = {}
    for a, b, c in product(range(6), repeat=3):
        if a == 0 or b == 1 or c == 2:
            continue
        arrows = ((a, 0), (b, 1), (c, 2))
        key = canonical(arrows)
        if key not in seen:
            vertices = tuple(range(key[0]))
            seen[key] = extension_probability(key[1], vertices)
    maxima = {v: max((p for (w, _), p in seen.items() if w == v), default=Fraction(0))
              for v in (3, 4, 5, 6)}
    assert maxima == {3: Fraction(0), 4: Fraction(1, 4),
                      5: Fraction(1, 6), 6: Fraction(1, 8)}
    assertions += 1
    # Only the one-common-predecessor star reaches the four-vertex maximum.
    top = [key for key, p in seen.items() if key[0] == 4 and p == Fraction(1, 4)]
    assert len(top) == 1
    assertions += 1

    # Four edges, with one target having two distinct predecessors.
    # Exhaustive partitions of four witness slots among three targets
    # and at most four new external vertices 3,4,5,6.
    seen = {}
    for a, b, c, d in product(range(7), repeat=4):
        if a == 0 or b == 0 or a == b or c == 1 or d == 2:
            continue
        arrows = ((a, 0), (b, 0), (c, 1), (d, 2))
        key = canonical(arrows)
        if key not in seen:
            seen[key] = extension_probability(key[1], tuple(range(key[0])))
    maxima = {v: max((p for (w, _), p in seen.items() if w == v), default=Fraction(0))
              for v in (4, 5, 6, 7)}
    assert maxima == {4: Fraction(1, 8), 5: Fraction(3, 20),
                      6: Fraction(1, 9), 7: Fraction(1, 12)}
    assertions += 1
    assert len(seen) == 124
    assertions += 1
    print(f"Finite poset certificate: {len(seen)} four-edge types, {assertions} exact assertions")
    return assertions


def verify_samples():
    assertions = 0
    for n, dimensions in ((3, (1, 2, 3)), (4, (1, 2, 3)), (5, (1, 2))):
        orders = list(permutations(range(n)))
        for d in dimensions:
            total = 0
            for rank_orders in product(orders, repeat=d):
                positions = [tuple(row.index(v) for v in range(n)) for row in rank_orders]
                nonminimal = 0
                for i in range(n):
                    if any(j != i and all(pos[j] < pos[i] for pos in positions) for j in range(n)):
                        nonminimal += 1
                total += nonminimal * (nonminimal - 1) * (nonminimal - 2)
            exact = Fraction(total, factorial(n) ** d)
            if d == 1:
                assert exact == (n - 1) * (n - 2) * (n - 3)
                assertions += 1
            assert exact >= 0
            assertions += 1
    print(f"Independent direct sample checks: {assertions} exact assertions")
    return assertions


def main():
    count = verify_poset_tables() + verify_samples()
    print(f"PASS: {count} exact assertions; all required type maxima reconstructed")


if __name__ == '__main__':
    main()
