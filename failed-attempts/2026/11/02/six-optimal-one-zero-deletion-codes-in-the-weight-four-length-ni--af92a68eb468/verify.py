#!/usr/bin/env python3
"""Exact rational verification of the five-symbol degree-five profile classification.

Usage: python3 verify.py cert_six_maxima.json
Requires only the Python 3 standard library.
"""
import itertools, json, sys
from fractions import Fraction
from pathlib import Path


def profiles(q, degree):
    def rec(prefix, remaining):
        if len(prefix) == q - 1:
            yield tuple(prefix + [remaining])
        else:
            for z in range(remaining + 1):
                yield from rec(prefix + [z], remaining - z)
    return list(rec([], degree))


def verify(path):
    doc = json.loads(Path(path).read_text(encoding='utf-8'))
    assert doc['schema_version'] == 1 and doc['dimension'] == 5 and doc['degree'] == 5
    v = profiles(5, 5)
    assert len(v) == 126
    n = len(v)
    index = {p: k for k, p in enumerate(v)}
    cliques = set()
    for a in profiles(5, 4):
        cliques.add(tuple(sorted(index[tuple(a[j] + (j == i) for j in range(5))] for i in range(5))))
    for a in profiles(5, 6):
        cliques.add(tuple(sorted(index[tuple(a[j] - (j == i) for j in range(5))] for i in range(5) if a[i])))
    cliques = sorted(cliques)
    cover_masks = []
    for c in cliques:
        assert len(set(c)) == len(c)
        assert all(sum(abs(v[i][z] - v[j][z]) for z in range(5)) == 2
                   for i, j in itertools.combinations(c, 2))
        cover_masks.append(sum(1 << i for i in c))
    closed = []
    for i, p in enumerate(v):
        closed.append(sum(1 << j for j, t in enumerate(v)
                          if sum(abs(p[z] - t[z]) for z in range(5)) <= 2))
    allmask = (1 << n) - 1
    proof_leaves = 0
    enum_leaves = 0
    maxima = []

    def bound(terms, alive, selected, target):
        nonlocal proof_leaves
        assert isinstance(terms, list)
        coverage = [Fraction(0) for _ in range(n)]
        weight_sum = Fraction(0)
        for j, num, den in terms:
            assert isinstance(j, int) and 0 <= j < len(cliques)
            assert isinstance(num, int) and isinstance(den, int) and num >= 0 and den > 0
            weight = Fraction(num, den)
            weight_sum += weight
            for i in cliques[j]:
                coverage[i] += weight
        assert selected + weight_sum < target
        assert all(coverage[i] >= 1 for i in range(n) if alive & (1 << i))
        proof_leaves += 1

    def prove_upper(node, alive, selected):
        if 'ub' in node:
            assert set(node) == {'ub'}
            bound(node['ub'], alive, selected, 27)
            return
        assert set(node) == {'v', 'ex', 'in'}
        k = node['v']
        assert isinstance(k, int) and 0 <= k < n and (alive & (1 << k))
        prove_upper(node['ex'], alive & ~(1 << k), selected)
        prove_upper(node['in'], alive & ~closed[k], selected + 1)

    def enumerate_maxima(node, alive, selected, set_mask):
        nonlocal enum_leaves
        if 'bound' in node:
            assert set(node) == {'bound'}
            bound(node['bound'], alive, selected, 26)
            enum_leaves += 1
            return
        if 'sol' in node:
            assert set(node) == {'sol'} and node['sol'] == 1 and selected == 26
            maxima.append(tuple(i for i in range(n) if set_mask & (1 << i)))
            return
        assert set(node) == {'vertex', 'excluded', 'included'}
        k = node['vertex']
        assert isinstance(k, int) and 0 <= k < n and (alive & (1 << k))
        enumerate_maxima(node['excluded'], alive & ~(1 << k), selected, set_mask)
        enumerate_maxima(node['included'], alive & ~closed[k], selected + 1,
                         set_mask | (1 << k))

    prove_upper(doc['upper_no_27'], allmask, 0)
    enumerate_maxima(doc['enumerate_26'], allmask, 0, 0)
    maxima = sorted(maxima)
    assert maxima == sorted(tuple(x) for x in doc['claimed_maximizers'])
    assert len(maxima) == len(set(maxima)) == 6
    assert all(len(s) == 26 and all(not (closed[i] & (1 << j))
                    for i, j in itertools.combinations(s, 2)) for s in maxima)

    base = frozenset(i for i, a in enumerate(v)
                     if sum(j * a[j] for j in range(5)) % 5 == 0)
    assert len(base) == 26
    orbit = set()
    for perm in itertools.permutations(range(5)):
        orbit.add(tuple(sorted(index[tuple(v[k][perm[j]] for j in range(5))]
                               for k in base)))
    assert len(orbit) == 6 and orbit == set(maxima)
    print('VERIFY_OK vertices=126 max_size=26 optimum_sets=6 symmetry_orbits=1 '
          f'upper_certificate_leaves={proof_leaves-enum_leaves} '
          f'enumeration_certificate_leaves={enum_leaves}')

if __name__ == '__main__':
    verify(sys.argv[1] if len(sys.argv) > 1 else 'cert_six_maxima.json')
