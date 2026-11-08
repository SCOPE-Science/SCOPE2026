#!/usr/bin/env python3
"""Construct automorphisms explicitly and partition optimal codes into orbits."""
from itertools import product, permutations, combinations
from collections import Counter

P = list(product(range(4), repeat=2))
ind = {p: i for i, p in enumerate(P)}
D = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}


def multiply(m, x, y):
    return ((m[0] * x + m[1] * y) % 4,
            (m[2] * x + m[3] * y) % 4)


def shrikhande_group():
    matrices = [m for m in product(range(4), repeat=4)
                if {multiply(m, *v) for v in D} == D]
    assert len(matrices) == 12
    out = []
    for m in matrices:
        for a, b in P:
            out.append(tuple(ind[((multiply(m, x, y)[0] + a) % 4,
                                  (multiply(m, x, y)[1] + b) % 4)]
                             for x, y in P))
    assert len(set(out)) == 192
    return out


def rook_group():
    out = []
    for f, g in product(permutations(range(4)), repeat=2):
        for flip in (False, True):
            out.append(tuple(ind[(f[y], g[x]) if flip else (f[x], g[y])]
                             for x, y in P))
    assert len(set(out)) == 1152
    return out


def edges(name):
    if name == 'Shrikhande':
        return {frozenset((i, j)) for i, (a, b) in enumerate(P)
                for j, (c, d) in enumerate(P) if i < j
                and ((c - a) % 4, (d - b) % 4) in D}
    return {frozenset((i, j)) for i, (a, b) in enumerate(P)
            for j, (c, d) in enumerate(P) if i < j
            and ((a == c) != (b == d))}


def global_ld(selected, edgeset):
    other = set(range(16)) - selected
    seen = set()
    for v in other:
        s = frozenset(u for u in selected if frozenset((u, v)) in edgeset)
        if not s or len(s) == len(selected) or s in seen:
            return False
        seen.add(s)
    return True


for name, group, expected in (
    ('Shrikhande', shrikhande_group(), {192: 6, 96: 3, 48: 1}),
    ('Rook', rook_group(), {576: 3, 144: 1}),
):
    E = edges(name)
    # The local neighborhood action is faithful: all nine outside vertices
    # are distinguished by their two neighbors of a selected root.
    for root in range(16):
        near = {i for i in range(16) if frozenset((root, i)) in E}
        far = set(range(16)) - near - {root}
        assert len(near) == 6 and len(far) == 9
        traces = [frozenset(i for i in near if frozenset((v, i)) in E)
                  for v in far]
        assert all(len(trace) == 2 for trace in traces)
        assert len(set(traces)) == 9
        in_neighbor_degrees = [sum(frozenset((i, j)) in E for j in near)
                               for i in near]
        assert sorted(in_neighbor_degrees) == [2] * 6
        if name == 'Shrikhande':
            seen = {next(iter(near))}
            todo = list(seen)
            while todo:
                v = todo.pop()
                for w in near - seen:
                    if frozenset((v, w)) in E:
                        seen.add(w)
                        todo.append(w)
            assert seen == near  # six-cycle rather than two triangles
        else:
            assert sum(frozenset((i, j)) in E
                       for i, j in combinations(near, 2)) == 6
    for p in group:
        assert {frozenset((p[i], p[j])) for a in E for i, j in [tuple(a)]} == E
    candidates = {frozenset(c) for c in combinations(range(16), 5)
                  if global_ld(set(c), E)}
    orbit_lengths = []
    while candidates:
        s = min(candidates, key=lambda z: tuple(sorted(z)))
        orbit = {frozenset(p[i] for i in s) for p in group}
        assert orbit <= candidates
        candidates -= orbit
        orbit_lengths.append(len(orbit))
    assert dict(Counter(orbit_lengths)) == expected
    print(f'{name}: automorphisms={len(group)}, optimal-orbit-sizes={dict(Counter(orbit_lengths))}')
print('PASS verify_symmetry')
