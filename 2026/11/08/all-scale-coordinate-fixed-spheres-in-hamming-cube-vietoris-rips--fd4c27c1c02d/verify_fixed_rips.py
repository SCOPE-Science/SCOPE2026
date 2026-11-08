#!/usr/bin/env python3
"""Exact small-case checks for coordinate-permutation fixed Hamming Rips spaces.

The mathematical proof is uniform; these calculations independently test the
weight-orbit model, each fold, and reduced mod-two homology in finite ranges.
"""
from itertools import combinations
from collections import defaultdict


def weight(x):
    return x.bit_count()


def orbit_model_from_cube(n, r):
    layers = [[x for x in range(1 << n) if weight(x) == i] for i in range(n + 1)]
    permitted = set()
    for i, O in enumerate(layers):
        if all((x ^ y).bit_count() <= r for x, y in combinations(O, 2)):
            permitted.add(i)
    compatible = set()
    for i, j in combinations(sorted(permitted), 2):
        if all((x ^ y).bit_count() <= r for x in layers[i] for y in layers[j]):
            compatible.add((i, j))
    return permitted, compatible


def orbit_model_formula(n, r):
    a = r // 2
    t = n - r
    permitted = set(range(a + 1)) | set(range(n - a, n + 1))
    compatible = set()
    for i, j in combinations(sorted(permitted), 2):
        if i <= a and j <= a:
            good = True
        elif i >= n - a and j >= n - a:
            good = True
        else:
            good = abs(i - (n - j)) >= t
        if good:
            compatible.add((i, j))
    return permitted, compatible


def band_graph(a, t):
    vertices = [('L', i) for i in range(a + 1)] + [('R', i) for i in range(a + 1)]
    E = {v: set() for v in vertices}
    for i in range(a + 1):
        for j in range(a + 1):
            if abs(i - j) < t:
                x, y = ('L', i), ('R', j)
                E[x].add(y)
                E[y].add(x)
    return E


def step_fold(E, u, v):
    assert u in E and v in E and u != v
    assert v not in E[u]
    assert E[u] <= E[v], (u, v, E[u], E[v])
    for w in list(E[v]):
        E[w].remove(v)
    del E[v]


def canonical_folds(a, t):
    E = band_graph(a, t)
    record = []
    for b in range(0, a + 1, t):
        for j in range(b + 1, min(a, b + t - 1) + 1):
            u, v = ('L', b), ('L', j)
            step_fold(E, u, v)
            record.append((u, v))
        for j in range(b + 1, min(a, b + t - 1) + 1):
            u, v = ('R', b), ('R', j)
            step_fold(E, u, v)
            record.append((u, v))
    remaining = set(E)
    expected = {('L', b) for b in range(0, a + 1, t)} | {('R', b) for b in range(0, a + 1, t)}
    assert remaining == expected
    for v, N in E.items():
        assert len(N) == 1
        assert next(iter(N)) == ('R' if v[0] == 'L' else 'L', v[1])
    assert len(record) == 2 * (a + 1 - ((a // t) + 1))
    return record


def independent_faces(E):
    vertices = sorted(E)
    faces = {frozenset()}
    for v in vertices:
        faces |= {s | {v} for s in list(faces) if not (s & E[v])}
    return faces


def check_actual_collapses(a, t):
    E = band_graph(a, t)
    faces = independent_faces(E)
    expected_end = 3 ** (a // t + 1)
    for u, v in canonical_folds(a, t):
        assert u in E and v in E and E[u] <= E[v]
        lower = sorted((s for s in faces if v in s and u not in s), key=lambda x: (-len(x), tuple(sorted(x))))
        for s in lower:
            top = s | {u}
            assert s in faces and top in faces
            # An elementary free pair has exactly one remaining coface of its lower face.
            cofaces = [f for f in faces if s < f]
            assert cofaces == [top], (a, t, u, v, s, len(cofaces))
            faces.remove(s)
            faces.remove(top)
        step_fold(E, u, v)
        assert faces == independent_faces(E)
    assert len(faces) == expected_end, (a, t, len(faces), expected_end)
    return len(faces)


def reduced_betti_f2(faces):
    by_size = defaultdict(list)
    for s in faces:
        by_size[len(s)].append(tuple(sorted(s)))
    by_size = {k: sorted(v) for k, v in by_size.items()}
    ranks = {}
    for k in range(1, max(by_size) + 1):
        columns = by_size.get(k, ())
        index = {s: i for i, s in enumerate(by_size[k-1])}
        pivots = {}
        for simplex in columns:
            c = 0
            for j in range(k):
                f = simplex[:j] + simplex[j + 1:]
                c ^= 1 << index[f]
            while c:
                p = c.bit_length() - 1
                if p not in pivots:
                    pivots[p] = c
                    break
                c ^= pivots[p]
        ranks[k] = len(pivots)
    return {k - 1: len(by_size[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
            for k in by_size if k >= 1}


def fixed_faces(n, r):
    permitted, compatible = orbit_model_from_cube(n, r)
    faces = {frozenset()}
    for i in sorted(permitted):
        faces |= {s | {i} for s in list(faces)
                  if all((min(i, j), max(i, j)) in compatible for j in s)}
    return faces


def main():
    orbit_cases = 0
    homology_cases = 0
    for n in range(1, 11):
        for r in range(0, n):
            direct = orbit_model_from_cube(n, r)
            closed = orbit_model_formula(n, r)
            assert direct == closed, (n, r, direct, closed)
            orbit_cases += 1
            faces = fixed_faces(n, r)
            reduced = reduced_betti_f2(faces)
            d = (r // 2) // (n - r)
            assert {k: v for k, v in reduced.items() if v} == {d: 1}, (n, r, reduced, d)
            homology_cases += 1
    fold_cases = 0
    for t in range(1, 21):
        for a in range(0, 61):
            canonical_folds(a, t)
            fold_cases += 1
    collapse_cases = 0
    for t in range(1, 5):
        for a in range(0, 7):
            check_actual_collapses(a, t)
            collapse_cases += 1
    print('FULL_WEIGHT_ORBIT_COMPARISONS_OK', orbit_cases)
    print('EXACT_MOD2_FIXED_HOMOLOGY_CHECKS_OK', homology_cases)
    print('ALL_CANONICAL_BAND_FOLD_SEQUENCES_OK', fold_cases)
    print('EXPLICIT_ELEMENTARY_INDEPENDENCE_COLLAPSES_OK', collapse_cases)
    print('ALL_SCALE_COORDINATE_FIXED_SPHERES_VERIFIED')


if __name__ == '__main__':
    main()
