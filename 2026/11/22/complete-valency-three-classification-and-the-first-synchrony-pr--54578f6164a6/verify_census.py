#!/usr/bin/env python3
"""Exact enumeration of connected four-cell valency-three zero-Hopf networks.

No third-party packages are required. Every nonnegative integer row-sum-three
adjacency matrix is visited exactly once. Isomorphism is simultaneous permutation
of row and column indices.
"""
from collections import Counter
from itertools import permutations, product
import csv
from pathlib import Path

N = 4
PERMS = tuple(permutations(range(N)))
ROWS = tuple(r for r in product(range(4), repeat=4) if sum(r) == 3)
EXPECTED_LABELED = {1: 1560, 2: 840, 3: 176}
EXPECTED_UNLABELED = {1: 65, 2: 36, 3: 8}
EXPECTED_SYNCHRONY = {1: {0:0, 1:47, 2:18},
                       2: {0:1, 1:27, 2:8},
                       3: {0:2, 1:5, 2:1}}


def det3(m):
    a, b, c, d, e, f, g, h, i = m
    return a * (e*i-f*h) - b * (d*i-f*g) + c * (d*h-e*g)


def det4(a):
    result = 0
    for j in range(4):
        minor = [a[i][k] for i in (1,2,3) for k in range(4) if k != j]
        result += (-1 if j % 2 else 1) * a[0][j] * det3(minor)
    return result


def connected(a):
    # Weak connectivity is connectivity of the underlying undirected multigraph.
    reached = {0}
    frontier = [0]
    while frontier:
        i = frontier.pop()
        for j in range(4):
            if j not in reached and (a[i][j] > 0 or a[j][i] > 0):
                reached.add(j)
                frontier.append(j)
    return len(reached) == 4


def canonical(a):
    return min(tuple(a[p[i]][p[j]] for i in range(4) for j in range(4))
               for p in PERMS)


def trace3(a):
    return sum(a[i][j] * a[j][k] * a[k][i]
               for i in range(4) for j in range(4) for k in range(4))


def alternate_coefficients(a):
    # Independent principal-minor computation of all coefficients of det(tI-A)
    e1 = sum(a[i][i] for i in range(4))
    e2 = sum(a[i][i]*a[j][j]-a[i][j]*a[j][i]
             for i in range(4) for j in range(i+1,4))
    e3 = sum(det3([a[i][j] for i in indices for j in indices])
             for indices in __import__('itertools').combinations(range(4), 3))
    e4 = det4(a)
    return e1, e2, e3, e4


def classify(a):
    # First criterion: Newton traces and determinant, without characteristic
    # polynomial or floating-point eigenvalues.
    tr1 = sum(a[i][i] for i in range(4))
    if tr1 != 3:
        return None
    tr2 = sum(a[i][j]*a[j][i] for i in range(4) for j in range(4))
    if (9-tr2) % 2:
        return None
    q = (9-tr2)//2
    if q not in (1,2,3):
        return None
    if trace3(a) != 27 or det4(a) != 0 or not connected(a):
        return None
    return q


def partitions():
    # Restricted-growth strings enumerate all fifteen partitions of four cells.
    out = []
    def build(prefix):
        if len(prefix) == 4:
            out.append(tuple(prefix))
            return
        for b in range(max(prefix)+2):
            build(prefix + [b])
    build([0])
    assert len(out) == 15
    return [p for p in out if 1 < len(set(p)) < 4]


def synchrony_count(a):
    # A polydiagonal is flow-invariant for every admissible scalar-cell field
    # exactly if each pair of cells in a block receives equal sums from
    # every input block (the balanced-equivalence criterion).
    found = 0
    for p in partitions():
        blocks = [[j for j in range(4) if p[j] == b]
                  for b in range(max(p)+1)]
        if all(sum(a[i][j] for j in target) ==
               sum(a[block[0]][j] for j in target)
               for block in blocks for i in block for target in blocks):
            found += 1
    return found


def unflatten(r):
    return tuple(tuple(r[4*i:4*i+4]) for i in range(4))


def reference_valency_two_check():
    # Reproduce the literature's nine-class four-cell, two-input baseline.
    rows2 = tuple(r for r in product(range(3),repeat=4) if sum(r)==2)
    assert len(rows2)==10
    classes2=set()
    for a in product(rows2,repeat=4):
        if sum(a[i][i] for i in range(4)) != 2:
            continue
        tr2=sum(a[i][j]*a[j][i] for i in range(4) for j in range(4))
        if (4-tr2) % 2:
            continue
        q=(4-tr2)//2
        if q<=0 or trace3(a)!=8 or det4(a)!=0 or not connected(a):
            continue
        assert alternate_coefficients(a)==(2,q,2*q,0)
        classes2.add(canonical(a))
    assert len(classes2)==9
    return len(classes2)


def run():
    assert len(ROWS) == 20
    assert len(partitions()) == 13
    assert reference_valency_two_check() == 9
    labeled = Counter()
    classes = {1:set(),2:set(),3:set()}
    fixed_counts = {q:Counter() for q in (1,2,3)}
    tested = 0
    for a in product(ROWS, repeat=4):
        tested += 1
        q = classify(a)
        # Second independent spectral test, for all exact positive-q candidates
        # that pass first trace filter; all accepted matrices must pass it.
        if q is None:
            continue
        assert alternate_coefficients(a) == (3, q, 3*q, 0)
        labeled[q] += 1
        classes[q].add(canonical(a))
        for i, p in enumerate(PERMS):
            if all(a[r][c] == a[p[r]][p[c]] for r in range(4) for c in range(4)):
                fixed_counts[q][i] += 1

    assert tested == 20**4 == 160000
    assert dict(labeled) == EXPECTED_LABELED, labeled
    assert {q: len(classes[q]) for q in classes} == EXPECTED_UNLABELED
    # Independent Burnside-orbit count, calculated from permutation stabilizers.
    for q in (1,2,3):
        assert sum(fixed_counts[q].values()) == 24*EXPECTED_UNLABELED[q]

    syn_counts = {q:Counter(synchrony_count(unflatten(r)) for r in classes[q])
                  for q in classes}
    for q in (1,2,3):
        assert dict(syn_counts[q]) == {k:v for k,v in EXPECTED_SYNCHRONY[q].items()
                                     if v}, (q,syn_counts[q])

    target = Path(__file__).with_name('canonical_representatives.csv')
    with target.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['omega_squared', 'proper_synchrony_count']+[f'a{i}{j}' for i in range(4) for j in range(4)])
        for q in (1,2,3):
            for r in sorted(classes[q]):
                writer.writerow([q,synchrony_count(unflatten(r)),*r])
    print('Literature valency-two baseline independently reproduced: nine classes')
    print('All',tested,'labeled matrices examined; no rounding was used')
    print('omega^2 | labeled | isomorphism classes | Burnside fixed incidences')
    for q in (1,2,3):
        print(q, labeled[q],len(classes[q]),sum(fixed_counts[q].values()))
    print('Total isomorphism classes:',sum(len(v) for v in classes.values()))
    print('Proper synchrony count distribution (zero, one, two):')
    for q in (1,2,3):
        print(q, [syn_counts[q].get(i,0) for i in range(3)])
    print('Canonical representative file:',target.name)

if __name__ == '__main__':
    run()
