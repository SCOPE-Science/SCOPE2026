#!/usr/bin/env python3
"""Exact finite certificate for genus-three hyperelliptic spin descent.

Uses only the Python standard library. No computer algebra system needed.
The geometric identification of spin structures is proved in RESULT.md.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, lcm
from pathlib import Path
import csv

N = 8
FULL = (1 << N) - 1


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    for a in range(minimum, n + 1):
        for suffix in partitions(n - a, a):
            yield (a,) + suffix


def permutation(part):
    p = list(range(N))
    start = 0
    for length in part:
        for j in range(length):
            p[start + j] = start + (j + 1) % length
        start += length
    assert start == N and sorted(p) == list(range(N))
    return tuple(p)


def image(mask, p):
    out = 0
    for i in range(N):
        if mask & (1 << i):
            out |= 1 << p[i]
    return out


def objects(k):
    masks = {sum(1 << i for i in S) for S in combinations(range(N), k)}
    if k == 4:
        masks = {min(x, FULL ^ x) for x in masks}
    return sorted(masks)


def action(mask, p, k):
    out = image(mask, p)
    return min(out, FULL ^ out) if k == 4 else out


def orbits(p, k):
    # Direct traversal of all 28 two-subsets and 35 complementary four-subsets.
    remaining = set(objects(k))
    counts = Counter()
    while remaining:
        start = min(remaining)
        cur = start
        length = 0
        while cur in remaining:
            remaining.remove(cur)
            length += 1
            cur = action(cur, p, k)
        assert cur == start
        counts[length] += 1
    assert sum(d * c for d, c in counts.items()) == (28 if k == 2 else 35)
    return dict(sorted(counts.items()))


def cycle_lengths(p):
    unseen = set(range(N))
    lengths = []
    while unseen:
        start = min(unseen)
        u = start
        size = 0
        while u in unseen:
            unseen.remove(u)
            u = p[u]
            size += 1
        assert u == start
        lengths.append(size)
    return lengths


def power(p, n):
    q = list(range(N))
    for _ in range(n):
        q = [p[x] for x in q]
    return tuple(q)


def independent_fixed_count(p, n):
    # Independent generating-function/Burnside count, not orbit traversal.
    sizes = cycle_lengths(power(p, n))
    fixed_odd = comb(sizes.count(1), 2) + sizes.count(2)
    coeff = [1, 0, 0, 0, 0]
    for length in sizes:
        for j in range(4, length - 1, -1):
            coeff[j] += coeff[j - length]
    anti = 2 ** len(sizes) if all(d % 2 == 0 for d in sizes) else 0
    assert (coeff[4] + anti) % 2 == 0
    fixed_even = 1 + (coeff[4] + anti) // 2
    return fixed_odd, fixed_even


def fixed_from_orbits(cycles, n):
    return sum(d * multiplicity for d, multiplicity in cycles.items() if n % d == 0)


def fmt(cycles):
    return " ".join(f"{d}:{multiplicity}" for d, multiplicity in cycles.items())


def run():
    parts = sorted(partitions(N))
    assert len(parts) == 22 and len(set(parts)) == 22
    records = []
    odd_spectra = defaultdict(list)
    even_spectra = defaultdict(list)
    first_two = defaultdict(list)
    first_three = defaultdict(list)
    for part in parts:
        p = permutation(part)
        odd = orbits(p, 2)
        ev35 = orbits(p, 4)
        even = Counter(ev35)
        even[1] += 1
        even = dict(sorted(even.items()))
        assert sum(d * m for d, m in even.items()) == 36
        values = []
        for n in range(1, max(3, lcm(*part)) + 1):
            by_traversal = fixed_from_orbits(odd, n), fixed_from_orbits(even, n)
            by_formula = independent_fixed_count(p, n)
            assert by_traversal == by_formula, (part, n, by_traversal, by_formula)
            if n <= 3:
                values.append(by_formula)
        assert len(values) == 3
        record = dict(partition=" ".join(map(str, part)),
                      odd_cycles=fmt(odd), even_cycles=fmt(even),
                      O1=values[0][0], E1=values[0][1],
                      O2=values[1][0], E2=values[1][1],
                      O3=values[2][0], E3=values[2][1])
        records.append(record)
        odd_spectra[tuple(odd.items())].append(part)
        even_spectra[tuple(even.items())].append(part)
        first_two[tuple(values[:2])].append(part)
        first_three[tuple(values[:3])].append(part)
    assert len(odd_spectra) == 19
    assert len(even_spectra) == 21
    assert len(first_two) == 19
    assert len(first_three) == 22
    two_collisions = sorted(tuple(map(tuple, v)) for v in first_two.values() if len(v) > 1)
    expected = sorted([
        ((1, 1, 3, 3), (2, 6)),
        ((1, 1, 6), (2, 3, 3)),
        ((1, 7), (3, 5)),
    ])
    assert two_collisions == expected, (two_collisions, expected)
    assert [(r['O1'],r['E1'],r['O2'],r['E2'],r['O3'],r['E3'])
            for r in records if r['partition'] in {'1 1 3 3','2 6'}] == [
                (1, 3, 1, 3, 28, 36),
                (1, 3, 1, 3, 4, 12),
            ]
    with Path(__file__).with_name('theta_spectra.csv').open(newline='',encoding='utf-8') as f:
        on_disk = list(csv.DictReader(f))
    assert len(on_disk) == 22
    assert [{k:str(v) for k,v in r.items()} for r in records] == on_disk
    print('THETA_GENUS_THREE_THREE_EXTENSION_INJECTION_VERIFIED')
    print('22 partitions; 19 odd spectra; 21 even spectra; 19 two-level fingerprints; 22 three-level fingerprints')


if __name__ == '__main__':
    run()
