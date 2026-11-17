#!/usr/bin/env python3
"""Recompute integral homology of the ordinary symmetry orbit of a forest complex.
No third-party dependencies. Run: python3 verify_k33.py
"""
import itertools
from collections import Counter

EDGES = tuple((i, j) for i in range(3) for j in range(3))

def is_forest(mask):
    parent = list(range(6))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for e, (i, j) in enumerate(EDGES):
        if mask >> e & 1:
            a, b = root(i), root(3 + j)
            if a == b:
                return False
            parent[a] = b
    return True

FACES = tuple(x for x in range(1, 1 << 9) if is_forest(x))
FSET = set(FACES)
SUBSETS = {f: tuple(h for h in FACES if h != f and h & f == h) for f in FACES}

def symmetries(include_swap):
    out = set()
    for a in itertools.permutations(range(3)):
        for b in itertools.permutations(range(3)):
            for flip in ((False, True) if include_swap else (False,)):
                if flip:
                    v = tuple(3+b[i] for i in range(3)) + tuple(a[i] for i in range(3))
                else:
                    v = tuple(a[i] for i in range(3)) + tuple(3+b[i] for i in range(3))
                p = []
                for i, j in EDGES:
                    x, y = v[i], v[3+j]
                    if x >= 3: x, y = y, x
                    p.append(EDGES.index((x, y-3)))
                out.add(tuple(p))
    return sorted(out)

def run(include_swap):
    G = symmetries(include_swap)
    assert len(G) == (72 if include_swap else 36)
    transforms = {f: tuple(sum(1 << p[e] for e in range(9) if f >> e & 1) for p in G) for f in FACES}
    def canon(chain):
        return min(tuple(transforms[f][i] for f in chain) for i in range(len(G)))
    # Orbit-chain enumeration by extension of canonical representatives.
    cells = [sorted({canon((f,)) for f in FACES})]
    for d in range(1, 5):
        nxt = set()
        for chain in cells[d-1]:
            last = chain[-1]
            for f in FACES:
                if f != last and (f & last) == last:
                    nxt.add(canon(chain + (f,)))
        cells.append(sorted(nxt))
    indexes = [{f: i for i, f in enumerate(c)} for c in cells]
    # Matrices as column dictionaries, integer coefficients in chain-rank orientation.
    bd = {}
    for d in range(1, 5):
        bd[d] = {}
        for j, chain in enumerate(cells[d]):
            col = {}
            for k in range(d+1):
                face = canon(chain[:k] + chain[k+1:])
                i = indexes[d-1][face]
                col[i] = col.get(i, 0) + (-1)**k
            col = {i: v for i, v in col.items() if v}
            bd[d][j] = col
    # Original integral chain condition, not only reduced output.
    for d in range(2, 5):
        for col in bd[d].values():
            comp = {}
            for mid, coef in col.items():
                for i, v in bd[d-1][mid].items():
                    comp[i] = comp.get(i, 0) + coef*v
            assert all(v == 0 for v in comp.values()), (d, comp)
    # Independently count orbit-flags by Burnside; flags are fixed iff every term is.
    fixed_totals = [0]*5
    for gi in range(len(G)):
        fixed = {f for f in FACES if transforms[f][gi] == f}
        ending = {f: [0]*5 for f in fixed}
        for f in sorted(fixed, key=lambda t: t.bit_count()):
            ending[f][0] = 1
            for h in SUBSETS[f]:
                if h in fixed:
                    for d in range(1, 5):
                        ending[f][d] += ending[h][d-1]
        for a in ending.values():
            for d in range(5):
                fixed_totals[d] += a[d]
    assert all(z % len(G) == 0 for z in fixed_totals)
    burnside = [z // len(G) for z in fixed_totals]
    assert burnside == [len(c) for c in cells], (burnside, list(map(len,cells)))
    # Exact chain-homotopy-safe elimination of unit boundary entries.
    # At each step a degree-d generator and a degree-(d-1) generator
    # form an acyclic summand; Schur complement removes it integrally.
    active = [set(range(len(x))) for x in cells]
    cancel = Counter()
    while True:
        pivot = None
        for d in (4,3,2,1):
            for j, col in sorted(bd[d].items(), key=lambda kv: (len(kv[1]), kv[0])):
                i = next((i for i,v in sorted(col.items()) if abs(v) == 1), None)
                if i is not None:
                    pivot = d,j,i
                    break
            if pivot: break
        if not pivot: break
        d, j, i = pivot
        col = bd[d][j]
        unit = col[i]
        assert abs(unit)==1
        for k, other in bd[d].items():
            if k == j or i not in other: continue
            t = other[i] // unit
            for r, v in col.items():
                y = other.get(r,0)-t*v
                if y: other[r]=y
                else: other.pop(r,None)
        del bd[d][j]
        for other in bd[d].values(): other.pop(i,None)
        if d < 4:
            for other in bd[d+1].values(): other.pop(j,None)
        if d > 1: del bd[d-1][i]
        active[d].remove(j)
        active[d-1].remove(i)
        cancel[d] += 1
    counts = [len(x) for x in active]
    assert counts == [1,0,0,0,1], counts
    assert all(not any(col.values()) for mat in bd.values() for col in mat.values())
    assert list(map(len,cells)) == ([14,92,260,315,135] if include_swap else [20,162,504,630,270])
    print('full group' if include_swap else 'shore preserving', 'order',len(G),
          'cells', list(map(len,cells)), 'burnside',burnside,
          'unit cancellations', dict(sorted(cancel.items())), 'reduced cells',counts)
    return cells,bd

if __name__ == '__main__':
    assert Counter(f.bit_count() for f in FACES) == Counter({1:9,2:36,3:84,4:117,5:81})
    print('cover: forest face counts',dict(sorted(Counter(f.bit_count() for f in FACES).items())),
          'reduced Euler', -1+sum((-1)**(f.bit_count()-1) for f in FACES))
    run(False)
    run(True)
    print('PASS: valid integral orbit complexes; exact unit-cancellation certificate')
