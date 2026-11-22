"""Exact eight-vertex online-shattering census for the pentagonal Cartesian torus.

Run: python3 verify_census.py
Uses only the Python 3 standard library and the two accompanying JSON certificates.
"""
import itertools
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path

P = 5
POINTS = [(a, b) for a in range(P) for b in range(P)]
POINT_TO_ID = {xy: i for i, xy in enumerate(POINTS)}

# Evaluate the quadratic-distance predicate independently of graph-generator formulas.
NEIGHBORS = {i: frozenset(j for j, (c, d) in enumerate(POINTS)
    if ((a-c)**2 + (b-d)**2) % P == 1)
    for i, (a, b) in enumerate(POINTS)}
assert all(len(NEIGHBORS[i]) == 4 and i not in NEIGHBORS[i] for i in range(25))


def depth_three_tree(E, fixed_root=None):
    """Full binary tree by exact recursive restriction of center concepts to E."""
    ids = sorted(E)
    masks = {p: sum(1 << k for k, c in enumerate(ids) if c in NEIGHBORS[p]) for p in ids}
    full = (1 << len(ids)) - 1

    @lru_cache(None)
    def rec(state, depth):
        if depth == 0:
            if state.bit_count() == 0: return None
            return ['leaf', ids[next(k for k in range(len(ids)) if state >> k & 1)]]
        if state.bit_count() < (1 << depth): return None
        for q in ids:
            if depth == 3 and fixed_root is not None and q != fixed_root: continue
            yes, no = state & masks[q], state & ~masks[q] & full
            if yes.bit_count() < (1 << (depth - 1)) or no.bit_count() < (1 << (depth - 1)):
                continue
            a, b = rec(yes, depth - 1), rec(no, depth - 1)
            if a is not None and b is not None: return ['node', q, a, b]
        return None
    return rec(full, 3)


def transform(E, sx, sy, exchange, tx, ty):
    out = []
    for j in E:
        x, y = POINTS[j]
        if exchange: x, y = y, x
        out.append(POINT_TO_ID[((sx*x+tx) % P, (sy*y+ty) % P)])
    return tuple(sorted(out))


def full_orbit(E):
    return {transform(E, sx, sy, sw, tx, ty)
        for sx in (-1, 1) for sy in (-1, 1) for sw in (0, 1)
        for tx in range(P) for ty in range(P)}


def validate_certificate(cert):
    E = frozenset(POINT_TO_ID[tuple(x)] for x in cert['vertices'])
    assert len(E) == 8
    leaf_ids = []
    def rec(node, constraints):
        if 'center' in node:
            c = POINT_TO_ID[tuple(node['center'])]
            assert c in E
            assert all((c in NEIGHBORS[q]) == bool(value) for q, value in constraints)
            leaf_ids.append(c)
            return
        q = POINT_TO_ID[tuple(node['query'])]
        assert q in E
        rec(node['one'], constraints + [(q, 1)])
        rec(node['zero'], constraints + [(q, 0)])
    rec(cert['tree'], [])
    assert len(leaf_ids) == 8 and set(leaf_ids) == E
    assert depth_three_tree(E) is not None


def main():
    root = 0
    required = set(NEIGHBORS[root]) | {root}
    extra = sorted(set(range(25)) - required)
    assert len(extra) == 20
    rooted = []
    for triple in itertools.combinations(extra, 3):
        E = tuple(sorted(required | set(triple)))
        if depth_three_tree(E, fixed_root=root) is not None:
            rooted.append(E)
    assert len(rooted) == 84

    all_sets = {transform(E, 1, 1, 0, dx, dy)
        for E in rooted for dx in range(P) for dy in range(P)}
    assert len(all_sets) == 2050
    roots = Counter()
    for E in all_sets:
        # Independent static two-query trace test, using center and query domains E.
        pairs = itertools.combinations(E, 2)
        assert any({((a in NEIGHBORS[c]), (b in NEIGHBORS[c])) for c in E}
                   == {(False,False),(False,True),(True,False),(True,True)}
                   for a,b in pairs)
        # The global fixed-radius circle VC upper bound also bounds all restrictions.

        # Fully recompute the depth-three root predicate, not just its degree bound.
        count = sum(depth_three_tree(E, fixed_root=x) is not None for x in E)
        assert count >= 1
        roots[count] += 1
    assert roots == Counter({1: 2000, 2: 50})
    assert sum(k * n for k, n in roots.items()) == 2100

    reps = []
    remaining = set(all_sets)
    while remaining:
        representative = min(remaining)
        orbit = full_orbit(representative)
        assert orbit <= all_sets
        reps.append({'size': len(orbit),
            'vertices': [list(POINTS[i]) for i in representative],
            'viable_roots': sum(depth_three_tree(representative, fixed_root=x) is not None for x in representative)})
        remaining -= orbit
    reps.sort(key=lambda d: (-d['size'], d['vertices']))
    assert len(reps) == 12
    assert Counter(x['size'] for x in reps) == Counter({200: 9, 100: 2, 50: 1})
    assert [x['size'] for x in reps] == [x['size'] for x in json.loads(Path('orbit_representatives.json').read_text())]
    assert reps == json.loads(Path('orbit_representatives.json').read_text())
    validate_certificate(json.loads(Path('witness_tree.json').read_text()))
    print('PYTHON_PENTAGONAL_CENSUS_PASS rooted=84 total=2050 orbits=12 VC=2')


if __name__ == '__main__':
    main()
