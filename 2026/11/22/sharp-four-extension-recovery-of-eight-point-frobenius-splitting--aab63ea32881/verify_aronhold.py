#!/usr/bin/env python3
"""Exact finite checks of Aronhold-heptad Frobenius reconstruction.

Uses only the Python standard library. The underlying geometric theorem and
its human-readable proof are stated separately in RESULT.md.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, lcm
from pathlib import Path
import csv

N = 8
EDGES = tuple(combinations(range(N), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
B = tuple((1 << u) | (1 << v) for u, v in EDGES)


def aronhold_definition():
    # An unordered seven-set of odd theta characteristics (pairs of branches)
    # is Aronhold iff every triple sums to an even characteristic.
    pair = [[((a & b).bit_count() % 2) for b in B] for a in B]
    triples = tuple(combinations(range(7), 3))
    out = set()
    for seven in combinations(range(28), 7):
        if all((pair[seven[i]][seven[j]] ^ pair[seven[i]][seven[k]] ^
                pair[seven[j]][seven[k]]) == 1 for i, j, k in triples):
            out.add(seven)
    return out


def aronhold_graphs():
    # 8 seven-edge stars; 280 four-stars plus triangles on the other vertices.
    out = set()
    for center in range(N):
        out.add(tuple(sorted(EDGE_INDEX[tuple(sorted((center, v)))]
                             for v in range(N) if v != center)))
        for triangle in combinations((v for v in range(N) if v != center), 3):
            leaves = [v for v in range(N) if v != center and v not in triangle]
            seven_edges = ([tuple(sorted((center, v))) for v in leaves] +
                           list(combinations(triangle, 2)))
            out.add(tuple(sorted(EDGE_INDEX[e] for e in seven_edges)))
    return out


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    for k in range(min(n, largest or n), 0, -1):
        for tail in partitions(n - k, k):
            yield (k,) + tail


def permutation_from_partition(part):
    sigma = []
    for length in part:
        start = len(sigma)
        sigma.extend(range(start + 1, start + length))
        sigma.append(start)
    assert len(sigma) == N
    return tuple(sigma)


def power(sigma, n):
    out = tuple(range(N))
    for _ in range(n):
        out = tuple(sigma[out[i]] for i in range(N))
    return out


def cycle_type(sigma):
    seen = set()
    sizes = []
    for x in range(N):
        if x in seen:
            continue
        y = x
        length = 0
        while y not in seen:
            seen.add(y)
            length += 1
            y = sigma[y]
        assert y == x
        sizes.append(length)
    return Counter(sizes)


def fixed_formula(sigma):
    t = cycle_type(sigma)
    f = t[1]
    return f + 4 * comb(f, 4) + f * (f - 1) * t[2] + f * t[3]


def action_cycles(sigma, aronhold, index):
    ep = [EDGE_INDEX[tuple(sorted((sigma[u], sigma[v])))] for u, v in EDGES]
    image = [index[tuple(sorted(ep[e] for e in a))] for a in aronhold]
    assert set(image) == set(range(288))
    seen = set()
    counts = Counter()
    for x in range(288):
        if x in seen:
            continue
        y, k = x, 0
        while y not in seen:
            seen.add(y)
            y = image[y]
            k += 1
        assert y == x
        counts[k] += 1
    return counts


def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_mod(a, b, prime=3):
    a = poly_trim(a)
    b = poly_trim(b)
    if not b:
        raise ZeroDivisionError
    inverse = pow(b[-1], -1, prime)
    while len(a) >= len(b):
        d = len(a) - len(b)
        scale = a[-1] * inverse % prime
        for j, v in enumerate(b):
            a[j+d] = (a[j+d]-scale*v) % prime
        a = poly_trim(a)
    return a


def is_irreducible(poly, prime=3):
    degree = len(poly) - 1
    assert poly[-1] % prime == 1
    for d in range(1, degree//2 + 1):
        for i in range(prime**d):
            q=[]
            for _ in range(d):
                q.append(i%prime)
                i//=prime
            if not poly_mod(poly, q+[1], prime):
                return False
    return True


def main():
    a = aronhold_definition()
    graphs = aronhold_graphs()
    assert len(a) == len(graphs) == 288
    assert a == graphs, 'The graph parametrization must equal the theta definition.'
    ordered = sorted(a)
    index = {s: i for i, s in enumerate(ordered)}
    rows = []
    for part in partitions(N):
        sigma = permutation_from_partition(part)
        cycles = action_cycles(sigma, ordered, index)
        assert sum(k*v for k,v in cycles.items()) == 288
        order = lcm(*part)
        for n in range(1, order + 1):
            from_orbits = sum(k*v for k, v in cycles.items() if n%k == 0)
            expected = fixed_formula(power(sigma, n))
            assert from_orbits == expected, (part, n, from_orbits, expected)
        rows.append(dict(partition=','.join(map(str, part)),
                         H1=fixed_formula(sigma),
                         H2=fixed_formula(power(sigma, 2)),
                         H3=fixed_formula(power(sigma, 3)),
                         H4=fixed_formula(power(sigma, 4)),
                         cycle_type=' '.join(f'{d}^{cycles[d]}' for d in sorted(cycles))))
    assert len(rows) == 22
    assert len({r['cycle_type'] for r in rows}) == 22
    counts = []
    for n in range(1, 5):
        signatures = defaultdict(list)
        for r in rows:
            signatures[tuple(r[f'H{i}'] for i in range(1, n+1))].append(r['partition'])
        counts.append(len(signatures))
        if n == 3:
            collision = sorted(tuple(v) for v in signatures.values() if len(v) > 1)
            assert collision == [('8', '4,4')], collision
    assert counts == [12,19,21,22]
    assert tuple(next(r for r in rows if r['partition']=='8')[f'H{i}'] for i in range(1,5)) == (0,0,0,0)
    assert tuple(next(r for r in rows if r['partition']=='4,4')[f'H{i}'] for i in range(1,5)) == (0,0,0,288)
    # Explicit F_3 models proving the two sharp cycle types are realized.
    f8 = [2,0,1,0,0,0,0,0,1]              # x^8+x^2+2
    g4 = [2,1,0,0,1]                        # x^4+x+2
    h4 = [2,2,0,0,1]                        # x^4+2x+2
    assert all(is_irreducible(f) for f in (f8,g4,h4))
    file = Path(__file__).with_name('aronhold_22_types.csv')
    with file.open(newline='', encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        expected = list(reader)
    assert expected == [{k:str(v) for k,v in r.items()} for r in rows], 'CSV differs from the independently recomputed spectrum table'
    print('ARONHOLD_288_THETA_GRAPH_EQUALITY_22_SPLITTINGS_4_EXTENSIONS_VERIFIED')
    print('First-n distinct signatures:', counts)
    print('Sharp: (8) and (4,4) share (0,0,0) and split at degree 4.')

if __name__ == '__main__':
    main()
