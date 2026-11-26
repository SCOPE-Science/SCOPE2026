#!/usr/bin/env python3
"""Exact arithmetic of Zariski chambers on smooth quartic del Pezzo surfaces.

Uses only Python's standard library. The 16 divisor classes on the blow-up of
five general plane points give an independent check of the even-subset model.
"""
import csv
import itertools
import json
import sys
from collections import Counter, defaultdict

EVEN = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
INDEX = {x: i for i, x in enumerate(EVEN)}
PERMS = tuple(itertools.permutations(range(5)))


def intersection(a, b):
    return a[0] * b[0] - sum(a[j] * b[j] for j in range(1, 6))


def divisor(v):
    m = v.bit_count()
    if m == 0:  # conic through all five blown-up points
        return (2, -1, -1, -1, -1, -1)
    if m == 2:  # line through indexed point pair
        return (1,) + tuple(-int(bool(v & (1 << i))) for i in range(5))
    if m == 4:  # exceptional divisor of missing index
        return (0,) + tuple(int(not bool(v & (1 << i))) for i in range(5))
    raise AssertionError(m)


def image_bits(v, p):
    return sum(1 << p[i] for i in range(5) if v & (1 << i))


def action(p, t):
    return tuple(INDEX[image_bits(v, p) ^ t] for v in EVEN)


def compose(g, h):
    # (g after h), with g(v)=p_g(v) xor t_g
    pg, tg = g
    ph, th = h
    return tuple(pg[ph[i]] for i in range(5)), tg ^ image_bits(th, pg)


def inverse(g):
    p, t = g
    pi = tuple(p.index(i) for i in range(5))
    return pi, image_bits(t, pi)


def signed_type(p, t):
    visited = set()
    positive, negative = [], []
    for i in range(5):
        if i in visited:
            continue
        orbit = []
        j = i
        while j not in visited:
            visited.add(j)
            orbit.append(j)
            j = p[j]
        assert j == i
        negative_parity = sum(int(bool(t & (1 << p[z]))) for z in orbit) % 2
        (negative if negative_parity else positive).append(len(orbit))
    return (tuple(sorted(positive)), tuple(sorted(negative)))


def cycles_of(perm):
    visited = set()
    counts = Counter()
    for i in range(len(perm)):
        if i in visited:
            continue
        j = i
        n = 0
        while j not in visited:
            visited.add(j)
            n += 1
            j = perm[j]
        assert j == i
        counts[n] += 1
    return dict(sorted(counts.items()))


def move_subset(mask, act):
    r = 0
    for i in range(16):
        if mask & (1 << i):
            r |= 1 << act[i]
    return r


def run():
    # Two independent definitions of the intersection graph.
    C = [divisor(v) for v in EVEN]
    assert len(set(C)) == 16
    for i in range(16):
        assert intersection(C[i], C[i]) == -1
        for j in range(i + 1, 16):
            assert intersection(C[i], C[j]) == int((EVEN[i] ^ EVEN[j]).bit_count() == 4)
    edges = [(i, j) for i in range(16) for j in range(i + 1, 16)
             if intersection(C[i], C[j]) == 1]
    assert len(edges) == 40
    assert all(sum(i in edge for edge in edges) == 5 for i in range(16))
    admissible = tuple(m for m in range(1 << 16)
                       if all(not (m & (1 << i) and m & (1 << j)) for i, j in edges))
    sizes = Counter(m.bit_count() for m in admissible)
    assert [sizes[i] for i in range(6)] == [1, 16, 80, 160, 120, 16]
    assert len(admissible) == 393
    index = {m: i for i, m in enumerate(admissible)}
    group = [(p, t) for p in PERMS for t in EVEN]
    assert len(group) == 1920
    classes = defaultdict(list)
    for g in group:
        p, t = g
        a = action(p, t)
        assert len(set(a)) == 16
        assert all(((EVEN[a[i]] ^ EVEN[a[j]]).bit_count() == 4) ==
                   ((EVEN[i] ^ EVEN[j]).bit_count() == 4)
                   for i in range(16) for j in range(i + 1, 16))
        classes[signed_type(p, t)].append(g)
    assert len(classes) == 18
    assert sum(len(c) for c in classes.values()) == 1920
    # Explicit conjugation verifies that the 18 signed types are entire classes.
    for typ, members in classes.items():
        g = members[0]
        orbit = set()
        for h in group:
            c = compose(compose(h, g), inverse(h))
            orbit.add(c)
            assert signed_type(*c) == typ
        assert orbit == set(members)
    rows = []
    for typ, members in sorted(classes.items()):
        identical = set()
        for g in members:
            a = action(*g)
            induced = tuple(index[move_subset(m, a)] for m in admissible)
            direct_cycles = cycles_of(induced)
            line_cycles = cycles_of(a)
            # Second method: fixed subsets are precisely unions of vertex orbits.
            visited = set()
            orbits = []
            for i in range(16):
                if i in visited: continue
                o = 0
                j = i
                while j not in visited:
                    visited.add(j)
                    o |= 1 << j
                    j = a[j]
                orbits.append(o)
            fixed_poly = [0] * 6
            for bits in range(1 << len(orbits)):
                m = 0
                for j, o in enumerate(orbits):
                    if bits >> j & 1:
                        m |= o
                if m in index:
                    fixed_poly[m.bit_count()] += 1
            assert fixed_poly[0] == 1
            assert sum(fixed_poly) == direct_cycles.get(1, 0)
            assert sum(k * v for k, v in direct_cycles.items()) == 393
            identical.add((tuple(sorted(direct_cycles.items())),
                           tuple(sorted(line_cycles.items())),
                           tuple(fixed_poly)))
        assert len(identical) == 1
        cc, lc, poly = identical.pop()
        rows.append({
            'positive_cycle_lengths': ','.join(map(str, typ[0])) or '-',
            'negative_cycle_lengths': ','.join(map(str, typ[1])) or '-',
            'class_size': len(members),
            'line_cycles': ';'.join(f'{k}^{v}' for k, v in lc),
            'fixed_support_polynomial_coefficients_degree_0_to_5': ';'.join(map(str, poly)),
            'rational_chambers': sum(poly),
            'chamber_cycles': ';'.join(f'{k}^{v}' for k, v in cc),
        })
    assert len(set(r['rational_chambers'] for r in rows)) == 10
    assert len(set(r['chamber_cycles'] for r in rows)) == 18
    assert len(set(r['line_cycles'] for r in rows)) == 12
    # Same exceptional-line Frobenius zeta, different chamber invariants.
    line_to_chambers = defaultdict(set)
    for r in rows:
        line_to_chambers[r['line_cycles']].add(r['rational_chambers'])
    assert line_to_chambers['2^8'] == {1, 7, 21}
    assert line_to_chambers['4^4'] == {1, 3, 5}
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'w', newline='', encoding='utf-8') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    print('VERIFIED 16 CURVES 40 INTERSECTIONS 393 CHAMBERS 1920 ELEMENTS 18 CLASSES')
    print('VERIFIED LINE-SPECTRA 12 CHAMBER-SPECTRA 18 BASE-COUNTS 10')
    print('VERIFIED LINE CYCLES 2^8 -> 1,7,21; 4^4 -> 1,3,5')
    return rows


if __name__ == '__main__':
    run()
