#!/usr/bin/env python3
"""Exact integral certificate for a punctured Kneser neighborhood complex.
Python standard library only. Run: python3 verify.py [certificate.json].
"""
import collections
import itertools
import json
import pathlib
import sys

DUADS = list(itertools.combinations(range(6), 2))
FAULT = (0, 1)

def faces(banned):
    remaining = [e for e in DUADS if e not in banned]
    out = {()}
    for center in remaining:
        neighbors = [DUADS.index(e) for e in remaining if not set(e).intersection(center)]
        for k in range(1, len(neighbors) + 1):
            out.update(itertools.combinations(neighbors, k))
    return out

def fv(cells):
    return [sum(len(s) == k + 1 for s in cells) for k in range(6)]

def simplicial_collapse(cells):
    active = set(cells)
    steps = []
    while True:
        pair = None
        for k in range(1, max(map(len, active))):
            possible = []
            for big in sorted(s for s in active if len(s) == k + 1):
                for small in itertools.combinations(big, k):
                    if small in active:
                        possible.append((small, big))
            lower = collections.Counter(small for small, _ in possible)
            for small, big in sorted(possible):
                if lower[small] == 1 and not any(set(small).issubset(h)
                    for h in active if len(h) > k + 1):
                    pair = (small, big)
                    break
            if pair is not None:
                break
        if pair is None:
            break
        small, big = pair
        assert small in active and big in active
        assert all(not set(small).issubset(other)
                   for other in active if other != big and len(other) > len(small))
        active.remove(small)
        active.remove(big)
        steps.append([list(small), list(big)])
    return active, steps

def inverse(word):
    return tuple(-g for g in reversed(word))

def cyclic_reduction(word):
    stack = []
    for g in word:
        if stack and stack[-1] == -g:
            stack.pop()
        else:
            stack.append(g)
    while len(stack) >= 2 and stack[0] == -stack[-1]:
        stack = stack[1:-1]
    return tuple(stack)

def fundamental_group_certificate(cells, expected_vertices, expected_betti):
    verts = sorted(s[0] for s in cells if len(s) == 1)
    edges = sorted(s for s in cells if len(s) == 2)
    triangles = sorted(s for s in cells if len(s) == 3)
    adj = {v: [] for v in verts}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    tree = set()
    seen = {verts[0]}
    queue = collections.deque([verts[0]])
    while queue:
        u = queue.popleft()
        for v in sorted(adj[u]):
            if v not in seen:
                seen.add(v)
                queue.append(v)
                tree.add(tuple(sorted((u, v))))
    assert len(seen) == len(verts) == expected_vertices and len(tree) == expected_vertices-1
    non_tree = [e for e in edges if e not in tree]
    generator = {e: i+1 for i, e in enumerate(non_tree)}
    assert len(generator) == len(edges) - len(verts) + 1
    def oriented_edge(a, b):
        edge = tuple(sorted((a, b)))
        return (() if edge in tree else
                ((generator[edge] if a < b else -generator[edge]),))
    relators = [cyclic_reduction(oriented_edge(a,b) + oriented_edge(b,c)
                                  + oriented_edge(c,a)) for a,b,c in triangles]
    removed = []
    remaining = set(generator.values())
    while remaining:
        options = []
        for idx, relation in enumerate(relators):
            for g in {abs(x) for x in relation}:
                if sum(abs(x) == g for x in relation) == 1:
                    occurrences = sum(sum(abs(x) == g for x in rr) for rr in relators)
                    options.append((len(relation), occurrences, idx, g))
        assert options, 'nontrivial group presentation left unresolved'
        _, _, idx, g = min(options)
        relation = relators.pop(idx)
        i = next(i for i,x in enumerate(relation) if abs(x) == g)
        relation = relation[i:] + relation[:i]
        replacement = (inverse(relation[1:]) if relation[0] > 0
                       else relation[1:])
        assert all(abs(x) != g for x in replacement)
        def substitute(word):
            out = []
            for x in word:
                if abs(x) == g:
                    out.extend(replacement if x > 0 else inverse(replacement))
                else:
                    out.append(x)
            return cyclic_reduction(out)
        relators = [substitute(rr) for rr in relators]
        remaining.remove(g)
        removed.append(g)
    assert all(not rr for rr in relators)
    assert len(removed) == len(non_tree) and len(relators) == expected_betti
    return {'tree': [list(e) for e in sorted(tree)],
            'elimination_generators': removed,
            'remaining_trivial_relators': len(relators)}

def relative_integer_certificate(full, punctured):
    relative = full - punctured
    basis = {k: set(s for s in relative if len(s) == k+1) for k in range(6)}
    differentials = {}
    for k in range(1, 6):
        differentials[k] = {
            s: {s[:j] + s[j+1:]: (-1)**j for j in range(len(s))
                if s[:j] + s[j+1:] in basis[k-1]}
            for s in basis[k]}
    def check_d_squared_zero():
        for k in range(2, 6):
            for s, vec in differentials[k].items():
                composed = collections.Counter()
                for r, val in vec.items():
                    for t, z in differentials[k-1][r].items():
                        composed[t] += val*z
                assert not any(composed.values())
    check_d_squared_zero()
    pivots = []
    while True:
        candidates = []
        for k in range(1, 6):
            for s, vec in differentials[k].items():
                for r, val in vec.items():
                    if abs(val) == 1:
                        cost = len(vec) * sum(r in v for v in differentials[k].values())
                        candidates.append((cost,k,s,r,val))
        if not candidates:
            break
        _,k,s,r,u = min(candidates)
        assert u in (-1,1)
        # Eliminate a primitive direct-summand chain pair over Z.
        for v in list(basis[k] - {s}):
            if r in differentials[k][v]:
                coefficient = differentials[k][v].pop(r)
                for q,z in differentials[k][s].items():
                    if q == r:
                        continue
                    new = differentials[k][v].get(q,0) - coefficient*z*u
                    if new:
                        differentials[k][v][q] = new
                    else:
                        differentials[k][v].pop(q,None)
        differentials[k].pop(s)
        basis[k].remove(s)
        basis[k-1].remove(r)
        if k+1 in differentials:
            for vec in differentials[k+1].values():
                vec.pop(s,None)
        if k-1 in differentials:
            differentials[k-1].pop(r)
        pivots.append([k, list(s), list(r), u])
        check_d_squared_zero()
    assert len(pivots) == 99
    assert [len(basis[k]) for k in range(6)] == [0,0,6,0,0,0]
    assert all(not vec for m in differentials.values() for vec in m.values())
    return {'relative_counts': fv(relative),
            'primitive_integer_pivots': pivots,
            'remaining_cells_by_dimension': [len(basis[k]) for k in range(6)]}

def main():
    full = faces(set())
    punctured = faces({FAULT})
    assert punctured <= full
    assert fv(full) == [15,105,260,225,90,15]
    assert fv(punctured) == [14,88,192,150,54,8]
    reduced, collapse_steps = simplicial_collapse(punctured)
    assert len(collapse_steps) == 202
    assert fv(reduced) == [14,44,44,0,0,0]
    group = fundamental_group_certificate(reduced, 14, 13)
    full_reduced, full_collapse_steps = simplicial_collapse(full)
    assert fv(full_reduced) == [15,55,60,0,0,0]
    full_group = fundamental_group_certificate(full_reduced, 15, 19)
    rel = relative_integer_certificate(full, punctured)
    cert = {'face_vector_full': fv(full),
            'face_vector_punctured': fv(punctured),
            'simplicial_collapse_pairs': collapse_steps,
            'collapsed_face_vector': fv(reduced),
            'fundamental_group': group,
            'full_complex_collapse_pairs': full_collapse_steps,
            'full_complex_collapsed_face_vector': fv(full_reduced),
            'full_complex_fundamental_group': full_group,
            'relative_chain': rel}
    if len(sys.argv) > 1:
        persisted = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
        assert cert == persisted, 'certificate differs from exact recomputation'
    else:
        print(json.dumps(cert,separators=(',',':')))
    print('PASS: punctured complex is simply connected and collapses to a 2-complex with Euler characteristic 14',file=sys.stderr)
    print('PASS: relative Z-chain complex reduces by 99 unit pivots to six 2-cells',file=sys.stderr)
    print('PASS: H2 punctured is Z^13, and inclusion has primitive cokernel Z^6',file=sys.stderr)

if __name__ == '__main__':
    main()
