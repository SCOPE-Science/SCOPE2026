#!/usr/bin/env python3
"""Exact arithmetic of the 120 Bertini-pair types; Python standard library only.

For an ordered eight-point blow-up in general position, geometric odd-theta
tritangent planes form two labelled copies of the 2-subsets, one copy of the
3-subsets (equivalently complementary 5-subsets), and the singleton set.
This code checks the induced S8-permutation for all 22 cycle types.
"""
import csv
import itertools
import math
import sys
from collections import Counter
from pathlib import Path


def partitions(total, least=1):
    if total == 0:
        yield ()
        return
    for k in range(least, total + 1):
        for other in partitions(total - k, k):
            yield (k,) + other


def cycle_permutation(lengths):
    v = list(range(sum(lengths)))
    i = 0
    for length in lengths:
        for j in range(length):
            v[i + j] = i + ((j + 1) % length)
        i += length
    return tuple(v)


def geometric_objects():
    items = []
    for i in range(8):
        items.append(('point', (i,)))
    for subset in itertools.combinations(range(8), 2):
        items.append(('line', subset))
    for subset in itertools.combinations(range(8), 3):
        items.append(('conic', subset))
    for subset in itertools.combinations(range(8), 2):
        items.append(('cubic_pair', subset))
    assert len(items) == 120 and len(set(items)) == 120
    return items


def apply(p, obj):
    kind, vertices = obj
    return kind, tuple(sorted(p[x] for x in vertices))


def orbit_spectrum(p, objects):
    left = set(objects)
    spectrum = Counter()
    while left:
        ob = min(left)
        cur = ob
        cyc = []
        while cur in left:
            left.remove(cur)
            cyc.append(cur)
            cur = apply(p, cur)
        assert cur == ob, (p, cur, ob)
        spectrum[len(cyc)] += 1
    assert sum(size * count for size, count in spectrum.items()) == len(objects)
    return dict(sorted(spectrum.items()))


def fixed_by_cycle_spectrum(spectrum, n):
    return sum(k * count for k, count in spectrum.items() if n % k == 0)


def formula_from_base_cycle_lengths(parts, n):
    # Each original d-cycle splits into gcd(d,n) cycles of length d/gcd(d,n)
    counts = Counter()
    for d in parts:
        g = math.gcd(d, n)
        counts[d // g] += g
    f, twos, threes = counts[1], counts[2], counts[3]
    return (f + 2 * (math.comb(f, 2) + twos)
            + math.comb(f, 3) + f * twos + threes)


def collect():
    objects = geometric_objects()
    data = []
    for part in partitions(8):
        p = cycle_permutation(part)
        s = orbit_spectrum(p, objects)
        order = math.lcm(*part)
        for n in range(1, order + 1):
            by_permutation = fixed_by_cycle_spectrum(s, n)
            by_formula = formula_from_base_cycle_lengths(part, n)
            assert by_permutation == by_formula, (part, n, by_permutation, by_formula)
        row = dict(
            partition='+'.join(map(str, part)),
            T1=fixed_by_cycle_spectrum(s, 1),
            T2=fixed_by_cycle_spectrum(s, 2),
            T3=fixed_by_cycle_spectrum(s, 3),
            full_permutation_cycle_spectrum=';'.join(f'{k}:{v}' for k, v in s.items()),
            frobenius_order=order,
        )
        data.append(row)
    assert len(data) == 22
    for k, ntypes in [(1, 13), (2, 20), (3, 22)]:
        sig = {tuple(row[f'T{j}'] for j in range(1, k + 1)) for row in data}
        assert len(sig) == ntypes, (k, len(sig))
    groups = {}
    for row in data:
        key = row['T1'], row['T2']
        groups.setdefault(key, []).append(row['partition'])
    collisions = {key: values for key, values in groups.items() if len(values) > 1}
    assert collisions == {(4, 6): ['1+1+6', '2+3+3'], (1, 1): ['1+7', '3+5']}, collisions
    assert next(row for row in data if row['partition'] == '1+7')['T3'] == 1
    assert next(row for row in data if row['partition'] == '3+5')['T3'] == 10
    return data


def main():
    rows = collect()
    out = Path(__file__).resolve().parent / 'tritangent_22_spectra.csv'
    with out.open('w', newline='', encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print('PASS: 120 Bertini pairs; 22 S8 classes; prefix signatures 13,20,22; sharp degree 3')
    print('PASS: direct subset orbit calculations agree with cycle formula at every period')
    print(f'CSV: {out.name}, {len(rows)} rows')

if __name__ == '__main__':
    main()
