#!/usr/bin/env python3
"""Exact integral incidence verification for quartic del Pezzo conic pencils.

Python standard library only. Run: python verify.py
Uses the Picard classes of the blow-up at five general points and the
faithful even-signed-permutation action of the type-D5 Weyl group.
"""
from __future__ import annotations
import csv
import itertools
import math
from collections import defaultdict
from pathlib import Path


def smith_diagonal(matrix):
    """Unimodular Euclidean Smith reduction (including divisibility test)."""
    a = [list(map(int, row)) for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    k = 0
    while k < min(m, n):
        candidates = [(abs(a[i][j]), i, j)
                      for i in range(k, m) for j in range(k, n) if a[i][j]]
        if not candidates:
            break
        _, i, j = min(candidates)
        a[k], a[i] = a[i], a[k]
        for r in range(m):
            a[r][k], a[r][j] = a[r][j], a[r][k]
        while True:
            p = a[k][k]
            assert p != 0
            changed = False
            for i in range(k+1, m):
                if a[i][k]:
                    q = a[i][k] // p
                    for t in range(k, n):
                        a[i][t] -= q*a[k][t]
                    if a[i][k]:
                        a[i], a[k] = a[k], a[i]
                    changed = True
                    break
            if changed:
                continue
            for j in range(k+1, n):
                if a[k][j]:
                    q = a[k][j] // p
                    for r in range(k, m):
                        a[r][j] -= q*a[r][k]
                    if a[k][j]:
                        for r in range(m):
                            a[r][k], a[r][j] = a[r][j], a[r][k]
                    changed = True
                    break
            if changed:
                continue
            bad = next(((i, j) for i in range(k+1, m)
                        for j in range(k+1, n) if a[i][j] % p), None)
            if bad is not None:
                i, _ = bad
                for t in range(k, n):
                    a[k][t] += a[i][t]
                continue
            break
        if a[k][k] < 0:
            for t in range(k, n):
                a[k][t] = -a[k][t]
        k += 1
    diagonal = tuple(a[i][i] for i in range(k))
    assert all(x > 0 for x in diagonal)
    assert all(diagonal[i+1] % diagonal[i] == 0
               for i in range(len(diagonal)-1))
    assert all(a[i][j] == (diagonal[i] if i == j and i < len(diagonal) else 0)
               for i in range(m) for j in range(n))
    return diagonal


def cycles(perm):
    seen = set()
    out = []
    for i in range(len(perm)):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            cyc.append(j)
            seen.add(j)
            j = perm[j]
        out.append(cyc)
    return out


def signed_cycle_type(pi, flip):
    parts = []
    for cyc in cycles(pi):
        parts.append((len(cyc), '+' if math.prod(flip[i] for i in cyc) == 1 else '-'))
    return ','.join(f'{n}{s}' for n, s in sorted(parts))


def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))


def check_geometric_incidence():
    H = (1, 0, 0, 0, 0, 0)
    E = [tuple(1 if t == i+1 else 0 for t in range(6)) for i in range(5)]
    L = [sub(sub(H, E[i]), E[j]) for i in range(5) for j in range(i+1, 5)]
    C = sub((2, 0, 0, 0, 0, 0), tuple(sum(v[k] for v in E) for k in range(6)))
    curves = E + L + [C]
    F = [sub(H, E[i]) for i in range(5)]
    G = [sub((2, 0, 0, 0, 0, 0),
             tuple(sum(E[j][k] for j in range(5) if j != i) for k in range(6)))
         for i in range(5)]
    bundles = [(F[i], G[i]) for i in range(5)]
    B = [[int(sub(b, curve) in curves) for pair in bundles for b in pair]
         for curve in curves]
    assert len(set(curves)) == 16 and len(set(F+G)) == 10
    assert all(sum(row) == 5 for row in B)
    assert all(sum(row[2*i:2*i+2]) == 1
               for row in B for i in range(5))
    assert all(sum(B[r][j] for r in range(16)) == 8 for j in range(10))
    spins = [tuple(1 if row[2*i] else -1 for i in range(5)) for row in B]
    assert len(set(spins)) == 16
    assert all(math.prod(s) == -1 for s in spins)
    assert all(B[r][2*i+(0 if spin[i] == 1 else 1)] == 1
               for r, spin in enumerate(spins) for i in range(5))
    return B, spins


def invariant_incidence(B, spins, pi, flips):
    columns = [(i, s) for i in range(5) for s in (1, -1)]
    col_action = [columns.index((pi[i], s*flips[i])) for i, s in columns]
    row_action = []
    for spin in spins:
        nxt = [0]*5
        for i in range(5):
            nxt[pi[i]] = spin[i]*flips[i]
        row_action.append(spins.index(tuple(nxt)))
    col_orbits = cycles(col_action)
    row_orbits = cycles(row_action)
    matrix = [[sum(B[orbit[0]][j] for j in col_orbit)
               for col_orbit in col_orbits] for orbit in row_orbits]
    for orbit in row_orbits:
        for row in orbit:
            for j, col_orbit in enumerate(col_orbits):
                assert sum(B[row][c] for c in col_orbit) == matrix[row_orbits.index(orbit)][j]
    return matrix, len(row_orbits), len(col_orbits)


def multiply(g, h):
    """Composition g after h for signed permutations."""
    p, f = g
    q, e = h
    return (tuple(p[q[i]] for i in range(5)),
            tuple(e[i]*f[q[i]] for i in range(5)))


def inverse(g):
    p, f = g
    q = [0]*5
    for i, j in enumerate(p):
        q[j] = i
    return (tuple(q), tuple(f[q[j]] for j in range(5)))


def check_signed_classes(elements):
    """Confirm the 18 types are complete conjugacy classes, not merely labels."""
    grouped = defaultdict(set)
    for g in elements:
        grouped[signed_cycle_type(*g)].add(g)
    assert len(grouped) == 18
    for typ, cls in grouped.items():
        representative = next(iter(cls))
        conjugates = {multiply(multiply(g, representative), inverse(g))
                      for g in elements}
        assert conjugates == cls, typ


def main():
    B, spins = check_geometric_incidence()
    # Natural labels: C; E_i; L_ij in pentagon-edge/diagonal orbits.
    direct = [[0, 5], [4, 1], [2, 3], [2, 3]]
    assert smith_diagonal(direct) == (1, 10)
    expected = {}
    with open(Path(__file__).with_name('cases.csv'), newline='', encoding='utf-8') as handle:
        for r in csv.DictReader(handle):
            expected[r['signed_cycle_type']] = (int(r['weyl_elements']),
                int(r['line_orbits']), int(r['pencil_orbits']),
                int(r['rank']), int(r['free_rank']),
                tuple(map(int, r['torsion_factors'].split(':')))
                if r['torsion_factors'] else ())
    result = defaultdict(list)
    elements = []
    for pi in itertools.permutations(range(5)):
        for flips in itertools.product((-1, 1), repeat=5):
            if math.prod(flips) != 1:
                continue
            g = (tuple(pi), tuple(flips))
            elements.append(g)
            T, r, c = invariant_incidence(B, spins, pi, flips)
            diag = smith_diagonal(T)
            result[signed_cycle_type(pi, flips)].append((r, c, len(diag),
                r-len(diag), tuple(d for d in diag if d > 1)))
    check_signed_classes(elements)
    assert len(result) == len(expected) == 18
    assert sum(map(len, result.values())) == 1920
    for typ, examples in result.items():
        assert len(set(examples)) == 1, (typ, set(examples))
        actual = (len(examples), *examples[0])
        assert actual == expected[typ], (typ, actual, expected[typ])
    assert smith_diagonal(B) == (1, 1, 1, 1, 1, 2)
    print('PASS: 16 line classes, 10 conic pencils, and geometric Smith 1^5,2')
    print('PASS: 1920 W(D5) elements in 18 signed cycle types')
    print('PASS: 18 exact Frobenius-invariant Smith classifications match cases.csv')
    print('PASS: positive five-cycle trace matrix has Smith form 1,10')
    print('Torsion by number of types: ', {str(t):sum(v[0][4] == t for v in result.values()) for t in [(), (2,), (10,)]})


if __name__ == '__main__':
    main()
