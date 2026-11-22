"""Exact small-case checks for the connected-set Walsh spectrum of complete multipartite graphs.

The direct calculation constructs every connected vertex set, then applies a
Walsh-Hadamard transform; the predicted spectrum is computed from block counts.
Finite tests are diagnostics, not a proof of the all-order assertions.
"""
from itertools import combinations_with_replacement, product
from math import comb


def predicted(part_sizes):
    n = sum(part_sizes)
    r = len(part_sizes)
    support_size = (1 << n) - 1 - sum((1 << m) - 1 - m for m in part_sizes)
    counts = {}
    for ks in product(*(range(m + 1) for m in part_sizes)):
        if all(k == 0 for k in ks):
            multiplier = support_size
        else:
            multiplier = n + r - 1 - 2 * sum(ks) - sum(
                1 << m for k, m in zip(ks, part_sizes) if k == 0
            )
        multiplicity = 1
        for k, m in zip(ks, part_sizes):
            multiplicity *= comb(m, k)
        counts[multiplier] = counts.get(multiplier, 0) + multiplicity
    return counts


def direct(part_sizes):
    n = sum(part_sizes)
    r = len(part_sizes)
    parts = [i for i, m in enumerate(part_sizes) for _ in range(m)]
    indicator = []
    for mask in range(1 << n):
        hits = [0] * r
        for i in range(n):
            if mask & (1 << i):
                hits[parts[i]] += 1
        indicator.append(int(sum(x > 0 for x in hits) >= 2 or sum(hits) == 1))
    spectrum = indicator[:]
    step = 1
    while step < len(spectrum):
        for block in range(0, len(spectrum), 2 * step):
            for j in range(step):
                a, b = spectrum[block + j], spectrum[block + step + j]
                spectrum[block + j] = a + b
                spectrum[block + step + j] = a - b
        step *= 2
    counts = {}
    for value in spectrum:
        counts[value] = counts.get(value, 0) + 1
    return counts


def nullity_by_polynomials(part_sizes):
    n = sum(part_sizes)
    r = len(part_sizes)
    nullity = 0
    for z in range((1 << r) - 1):
        excluded_size = sum(1 << part_sizes[i] for i in range(r) if z >> i & 1)
        numerator = n + r - 1 - excluded_size
        if numerator % 2:
            continue
        degree = numerator // 2
        poly = [1]
        for i, m in enumerate(part_sizes):
            if z >> i & 1:
                continue
            factor = [0] + [comb(m, j) for j in range(1, m + 1)]
            nxt = [0] * (len(poly) + m)
            for a, av in enumerate(poly):
                for b, bv in enumerate(factor):
                    nxt[a + b] += av * bv
            poly = nxt
        if 0 <= degree < len(poly):
            nullity += poly[degree]
    return nullity


def run():
    checks = 0
    partitions = 0
    for r in range(2, 7):
        for part_sizes in combinations_with_replacement(range(1, 7), r):
            n = sum(part_sizes)
            if n > 11:
                continue
            actual = direct(part_sizes)
            expected = predicted(part_sizes)
            assert actual == expected, part_sizes
            checks += 1
            assert sum(actual.values()) == (1 << n)
            checks += 1
            nullity = actual.get(0, 0)
            assert nullity == nullity_by_polynomials(part_sizes), part_sizes
            checks += 1
            assert (nullity > 0) == bool((n + r) % 2), part_sizes
            checks += 1
            support_size = (1 << n) - 1 - sum((1 << m) - 1 - m for m in part_sizes)
            assert max(abs(a) for a in actual) == support_size
            checks += 1
            if not (n + r) % 2:
                assert min(abs(a) for a in actual) == 1
                checks += 1
            partitions += 1
    print(f"PASS: {partitions} part-size vectors, {checks} exact checks (all frequencies).")


if __name__ == "__main__":
    run()
