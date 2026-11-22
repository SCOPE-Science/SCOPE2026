"""Finite consistency checks for the long-chord bounded-independence theorem.

Uses independent subset-face construction and combinatorial link identification.
Run with: python3 verify_chord.py
"""
from itertools import combinations
from collections import defaultdict


def graph_edges(n, d=None):
    e = {frozenset((i, (i + 1) % n)) for i in range(n)}
    if d is not None:
        e.add(frozenset((0, d)))
    return e


def allowed_faces(n, edges):
    forbidden = [sum(1 << i for i in t)
                 for t in combinations(range(n), 3)
                 if all(frozenset(p) not in edges for p in combinations(t, 2))]
    out = defaultdict(list)
    # No 5-face if the graph contains no triangle and no five-cycle.
    for k in range(5):
        for t in combinations(range(n), k):
            mask = sum(1 << i for i in t)
            if all((mask & bad) != bad for bad in forbidden):
                out[k - 1].append(t)
    return out


def gf2_rank(columns):
    pivots = {}
    for v in columns:
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def mod2_betti(faces):
    ranks = {}
    for k in range(0, 4):
        lower = {f: i for i, f in enumerate(faces[k - 1])}
        cols = [sum(1 << lower[f[:j] + f[j + 1:]] for j in range(len(f)))
                for f in faces[k]]
        ranks[k] = gf2_rank(cols)
    return {k: len(faces[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
            for k in range(0, 4)}


def link(faces, pair):
    pq = set(pair)
    return {tuple(v for v in f if v not in pq) for fs in faces.values()
            for f in fs if pq.issubset(f)}


def predicted_links(n, d):
    u = [1, n - 1]
    v = [d - 1, d + 1]
    old = {()} | {(x,) for x in u + v}
    old |= {tuple(sorted((x, y))) for x in u for y in v}
    new = set(old)
    new.update((i,) for i in range(1, n) if i != d)
    for path in (list(range(1, d)), list(range(d + 1, n))):
        new.update(tuple(sorted((x, y))) for x, y in zip(path, path[1:]))
    return old, new


def main():
    checks = 0
    last = None
    for n in range(12, 19):
        old_faces = allowed_faces(n, graph_edges(n))
        assert all(len(f) < 5 for fs in old_faces.values() for f in fs)
        assert mod2_betti(old_faces) == {0: 0, 1: 0, 2: 0, 3: 1}
        for d in range(6, n - 5):
            new_faces = allowed_faces(n, graph_edges(n, d))
            assert all(len(f) < 5 for fs in new_faces.values() for f in fs)
            assert mod2_betti(new_faces) == {0: 0, 1: 0, 2: 0, 3: 3}
            old_link = link(old_faces, (0, d))
            new_link = link(new_faces, (0, d))
            expected_old, expected_new = predicted_links(n, d)
            assert old_link == expected_old, (n, d, 'old link mismatch')
            assert new_link == expected_new, (n, d, 'new link mismatch')
            for size in range(1, 5):
                old = set(old_faces[size - 1]); new = set(new_faces[size - 1])
                assert old <= new
                assert all({0, d}.issubset(f) for f in new - old)
            checks += 1
            last = (n, d, tuple(len(new_faces[k]) for k in range(0, 4)))
    # A non-cycle host: two heptagons linked by a six-edge path.
    # The old graph has cycle rank two; the added edge raises it to three.
    n = 19
    e = {frozenset((i, (i+1) % 7)) for i in range(7)}
    e |= {frozenset((7+i, 7+(i+1) % 7)) for i in range(7)}
    e |= {frozenset(p) for p in zip([0,14,15,16,17,18], [14,15,16,17,18,7])}
    a, b = 3, 10
    old = allowed_faces(n, e)
    new = allowed_faces(n, e | {frozenset((a,b))})
    assert mod2_betti(old) == {0:0, 1:0, 2:0, 3:3}
    assert mod2_betti(new) == {0:0, 1:0, 2:0, 3:6}
    actual_old, actual_new = link(old,(a,b)), link(new,(a,b))
    na = {next(iter(edge-{a})) for edge in e if a in edge}
    nb = {next(iter(edge-{b})) for edge in e if b in edge}
    predicted_old = {()} | {(v,) for v in na|nb}
    predicted_old |= {tuple(sorted((x,y))) for x in na for y in nb}
    predicted_new = set(predicted_old)
    predicted_new.update((v,) for v in range(n) if v not in (a,b))
    predicted_new.update(tuple(sorted(edge)) for edge in e if a not in edge and b not in edge)
    assert actual_old == predicted_old
    assert actual_new == predicted_new
    assert len([f for f in actual_new if len(f)==2 and f not in actual_old]) - len([f for f in actual_new if len(f)==1 and f not in actual_old]) == 3
    assert checks == sum(n - 11 for n in range(12, 19))
    print('CHORDED_CYCLE_CASES', checks)
    print('BARBELL_CASE', '19 vertices, ranks 3 -> 6, relative rank 3')
    print('LAST', last)
    print('INTEGRAL_RELATIVE_LINK: primitive free incidence lattice of rank b+1 (proved algebraically, not inferred from GF2)')
    print('LONG_CHORD_CHECK_PASS')


if __name__ == '__main__':
    main()
