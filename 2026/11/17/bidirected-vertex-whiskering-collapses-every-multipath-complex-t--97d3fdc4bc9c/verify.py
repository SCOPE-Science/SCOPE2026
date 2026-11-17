#!/usr/bin/env python3
"""Finite checks of the bidirectional-whiskering multipath collapse.

Run with Python 3. No third-party packages are required.
"""
from itertools import combinations
from collections import Counter
import json


def whisker_arcs(n, core):
    core = sorted(set(core))
    assert all(0 <= u < n and 0 <= v < n and u != v for u, v in core)
    pendants = [(v, n + v) for v in range(n)] + [(n + v, v) for v in range(n)]
    return core + pendants, len(core)


def legal(subset, arcs, vertex_count):
    nxt, prv = {}, {}
    for i in subset:
        u, v = arcs[i]
        if u in nxt or v in prv:
            return False
        nxt[u] = v
        prv[v] = u
    for v in range(vertex_count):
        x, seen = v, set()
        while x in nxt:
            if x in seen:
                return False
            seen.add(x)
            x = nxt[x]
    return True


def enumerate_faces(arcs, core_count, vertex_count):
    faces = []
    successor, predecessor = {}, {}
    def visit(i, mask):
        if i == len(arcs):
            faces.append(mask)
            return
        visit(i + 1, mask)
        u, v = arcs[i]
        if u in successor or v in predecessor:
            return
        x = v
        while x in successor:
            if x == u:
                return
            x = successor[x]
        if x == u:
            return
        successor[u], predecessor[v] = v, u
        visit(i + 1, mask | (1 << i))
        del successor[u]
        del predecessor[v]
    visit(0, 0)
    return set(faces)


def collapse_check(n, core, independent=True):
    arcs, k = whisker_arcs(n, core)
    faces = enumerate_faces(arcs, k, 2 * n)
    if independent:
        brute = {m for m in range(1 << len(arcs))
                 if legal((i for i in range(len(arcs)) if m & (1 << i)), arcs, 2 * n)}
        assert brute == faces, ('enumeration mismatch', n, core)
    original_size = len(faces)
    core_mask = (1 << k) - 1
    core_fibers = {}
    for f in faces:
        r = f & core_mask
        if r:
            core_fibers.setdefault(r, []).append(f)
    total_pairs = 0
    for r in sorted(core_fibers, key=lambda r: (-r.bit_count(), r)):
        ins, outs = [0] * n, [0] * n
        for i in range(k):
            if r & (1 << i):
                u, v = arcs[i]
                outs[u] += 1
                ins[v] += 1
        endpoints = [v for v in range(n) if ins[v] + outs[v] == 1]
        assert endpoints, ('nonempty core path forest without endpoint', r)
        p = min(endpoints)
        # For a path start add leaf -> core; for a path end add core -> leaf.
        wanted = (n+p, p) if outs[p] else (p, n+p)
        pivot = arcs.index(wanted)
        bit = 1 << pivot
        lows = [f for f in core_fibers[r] if not f & bit]
        lows.sort(key=lambda f: (-f.bit_count(), f))
        assert len(lows) * 2 == len(core_fibers[r]), (r, len(lows))
        for lower in lows:
            upper = lower | bit
            assert lower in faces and upper in faces, ('missing pair', n, r, lower)
            # Check that lower is an elementary free face right now.
            other = [i for i in range(len(arcs))
                     if not lower & (1 << i) and lower | (1 << i) in faces]
            assert other == [pivot], ('non-free face', n, r, lower, other, pivot)
            faces.remove(lower)
            faces.remove(upper)
            total_pairs += 1
    expected = {f for f in range(1 << len(arcs))
                if not f & core_mask and
                all(not ((f >> (k + v)) & 1 and (f >> (k + n + v)) & 1)
                    for v in range(n))}
    assert faces == expected, ('wrong surviving complex', n, len(faces), len(expected))
    assert len(faces) == 3 ** n
    assert total_pairs * 2 + 3 ** n == original_size
    assert sum((-1)**(f.bit_count()-1) for f in faces) == (-1)**(n-1)
    return {'n':n,'core_arcs':k,'original_augmented_faces':original_size,
            'collapse_pairs':total_pairs,'remaining_augmented_faces':len(faces)}


def run():
    tests = []
    def add(n, arcs, brute=True):
        tests.append(collapse_check(n, arcs, brute))
    for n in range(1,6):
        add(n, [], True)
    for n in range(2,6):
        add(n, [(i,i+1) for i in range(n-1)], True)
        add(n, [(i,i+1) for i in range(n-1)] + [(i+1,i) for i in range(n-1)], True)
    for n in range(3,7):
        add(n, [(i,(i+1)%n) for i in range(n)], True if n <= 5 else False)
        add(n, [(i,(i+1)%n) for i in range(n)] + [((i+1)%n,i) for i in range(n)], True if n <= 5 else False)
    for n in (3,4):
        add(n, [(u,v) for u in range(n) for v in range(n) if u!=v], True)
    add(5, [(0,1),(1,2),(2,0),(2,3),(3,4),(4,2),(1,4),(4,0)], True)
    assert len(tests)==5+8+8+2+1
    # Cycle-corona face count is a bonus closed formula, not inferred from these tests.
    for z in tests:
        if z['n'] >= 3 and z['core_arcs'] == 2*z['n']:
            pass
    print(json.dumps({'status':'PASS','tested_digraphs':len(tests),
                      'total_original_faces':sum(t['original_augmented_faces'] for t in tests),
                      'total_explicit_free_face_pairs':sum(t['collapse_pairs'] for t in tests),
                      'cases':tests},indent=2))
if __name__ == '__main__':
    run()
