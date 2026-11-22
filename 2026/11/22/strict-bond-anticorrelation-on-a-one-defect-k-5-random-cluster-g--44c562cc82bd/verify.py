#!/usr/bin/env python3
"""Exact finite polynomial certificate for the weighted K5 random-cluster model.

No external Python packages are needed. The exhaustive symbolic identities hold
for continuous real parameters; the rational checks are supplementary.
"""
import collections
import itertools
import json
from fractions import Fraction
from pathlib import Path

EDGES = tuple(itertools.combinations(range(5), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
FULL = (1 << len(EDGES)) - 1
DEFECT = EDGE_INDEX[(0, 1)]


def components(mask):
    parent = list(range(5))
    def root(t):
        while parent[t] != t:
            t = parent[t]
        return t
    for j, (u, v) in enumerate(EDGES):
        if mask & (1 << j):
            parent[root(u)] = root(v)
    return len({root(i) for i in range(5)})


COMP = tuple(components(t) for t in range(1024))


def add(p, r, multiplier=1):
    for mon, c in r.items():
        p[mon] += multiplier * c
    return p


def mul(p, r):
    d = collections.defaultdict(int)
    for (a, b, c), ca in p.items():
        for (x, y, z), cb in r.items():
            d[a + x, b + y, c + z] += ca * cb
    return {k: v for k, v in d.items() if v}


def normalize(p):
    return {k: v for k, v in p.items() if v}


def four_cells(e, f):
    a = {(0, 0): collections.defaultdict(int),
         (1, 0): collections.defaultdict(int),
         (0, 1): collections.defaultdict(int),
         (1, 1): collections.defaultdict(int)}
    excluded = (1 << e) | (1 << f)
    for mask in range(1024):
        bits = ((mask >> e) & 1, (mask >> f) & 1)
        other = mask & ~excluded
        h = (other >> DEFECT) & 1
        a[bits][(COMP[mask], other.bit_count() - h, h)] += 1
    return {key: normalize(value) for key, value in a.items()}


def raw_difference(e, f):
    T = four_cells(e, f)
    result = collections.defaultdict(int)
    add(result, mul(T[(1, 0)], T[(0, 1)]))
    add(result, mul(T[(0, 0)], T[(1, 1)]), -1)
    return normalize(result)


def quotient(e, f):
    """Exact division of the Rayleigh difference by q^2(1-q)."""
    diff = raw_difference(e, f)
    assert all(a >= 2 for a, b, c in diff), (e, f, 'q factor')
    blocks = collections.defaultdict(lambda: collections.defaultdict(int))
    for (a, b, c), coeff in diff.items():
        blocks[b, c][a - 2] += coeff
    out = collections.defaultdict(int)
    for (b, c), rows in blocks.items():
        running = 0
        degree = max(rows)
        for k in range(degree):
            running += rows.get(k, 0)
            if running:
                out[k, b, c] += running
        assert running == -rows.get(degree, 0), (e, f, b, c, 'not divisible')
    result = normalize(out)
    # Independently multiply the quotient and confirm the complete polynomial.
    reconstructed = collections.defaultdict(int)
    for (a, b, c), coeff in result.items():
        reconstructed[a + 2, b, c] += coeff
        reconstructed[a + 3, b, c] -= coeff
    assert normalize(reconstructed) == diff
    return result


def permutations():
    for xy in ((0, 1), (1, 0)):
        for rest in itertools.permutations((2, 3, 4)):
            perm = xy + rest
            yield tuple(EDGE_INDEX[tuple(sorted((perm[i], perm[j])))] for i, j in EDGES)


def orbit(pair):
    return {tuple(sorted((p[pair[0]], p[pair[1]]))) for p in permutations()}


def orbits():
    visited = set()
    result = []
    for pair in itertools.combinations(range(10), 2):
        if pair not in visited:
            o = orbit(pair)
            result.append((pair, len(o)))
            visited.update(o)
    assert len(visited) == 45 and len(result) == 8
    return result


def exceptional_positive(p):
    # The single negative-coefficient orbit is ((0,2),(1,3)).
    # P(q,v,w)=P0(v,w)+qP1+q^2P2+... ; all q>=1 terms are positive.
    assert all(coef >= 0 for (k, v, w), coef in p.items() if k >= 1)
    p0 = {(v, w): coef for (k, v, w), coef in p.items() if k == 0}
    subtraction = {
        (6, 0): 25, (5, 1): -50, (4, 2): 25,  # 25 v^4(v-w)^2
        (7, 0): 84, (6, 1): -20, (5, 2): 96,  # v^5(84v^2-20vw+96w^2)
    }
    remainder = collections.defaultdict(int, p0)
    for mon, coef in subtraction.items():
        remainder[mon] -= coef
    remainder = normalize(remainder)
    assert len(remainder) == 14 and all(coef > 0 for coef in remainder.values())
    # The quadratic is positive because its discriminant is negative:
    assert 20**2 < 4 * 84 * 96
    return remainder


def exact_checks():
    count = 0
    for q, v, w in itertools.product(
        (Fraction(1, 5), Fraction(2, 3), Fraction(4, 5)),
        (Fraction(1, 6), Fraction(3, 2)),
        (Fraction(1, 7), Fraction(5, 2))):
        moments = []
        Z = Fraction(0)
        for mask in range(1024):
            h = (mask >> DEFECT) & 1
            weight = q ** COMP[mask] * v ** (mask.bit_count() - h) * w ** h
            moments.append(weight)
            Z += weight
        for e, f in itertools.combinations(range(10), 2):
            Ee = sum(x for t, x in enumerate(moments) if t & (1 << e)) / Z
            Ef = sum(x for t, x in enumerate(moments) if t & (1 << f)) / Z
            Eef = sum(x for t, x in enumerate(moments) if (t & (1 << e)) and (t & (1 << f))) / Z
            cov = Eef - Ee * Ef
            assert cov < 0, (e, f, q, v, w)
            # Independent direct evaluation of the symbolic polynomial difference.
            P = quotient(e, f)
            evalP = sum(Fraction(k) * q**a * v**b * w**c for (a, b, c), k in P.items())
            xe = w if e == DEFECT else v
            xf = w if f == DEFECT else v
            assert cov == -(xe * xf * q**2 * (1-q) * evalP) / Z**2
            count += 1
    return count


def certificate_data():
    data = {'schema_version': 1,
            'graph_edges': [list(e) for e in EDGES],
            'defect_edge': [0, 1],
            'polynomial_variables': ['q', 'v', 'w'],
            'factor': 'q^2*(1-q)',
            'orbits': []}
    for (e, f), cardinality in orbits():
        p = quotient(e, f)
        data['orbits'].append({
            'pair_edge_indices': [e, f],
            'orbit_size': cardinality,
            'terms': [[a, b, c, coeff] for (a, b, c), coeff in sorted(p.items())]
        })
    return data


def main():
    data = certificate_data()
    path = Path(__file__).with_name('CERTIFICATE.json')
    saved = json.loads(path.read_text(encoding='utf-8'))
    assert data == saved, 'Stored coefficient certificate differs from direct exhaustive enumeration'
    all_orbits = data['orbits']
    counts = []
    for row in all_orbits:
        p = {(a, b, c): k for a, b, c, k in row['terms']}
        neg = [(abc, k) for abc, k in p.items() if k < 0]
        pair = tuple(row['pair_edge_indices'])
        if pair == (1, 5):
            assert neg == [((0, 5, 1), -50), ((0, 6, 1), -20)]
            exceptional_positive(p)
        else:
            assert not neg, (pair, neg)
            assert any(k > 0 for k in p.values())
        counts.append(len(p))
    checks = exact_checks()
    print('K5_RANDOM_CLUSTER_CERTIFICATE_PASSED',
          'edge_pair_orbits=8', 'edge_pairs=45',
          'coefficient_counts=' + ','.join(map(str, counts)),
          'exact_covariance_comparisons=' + str(checks))


if __name__ == '__main__':
    main()
