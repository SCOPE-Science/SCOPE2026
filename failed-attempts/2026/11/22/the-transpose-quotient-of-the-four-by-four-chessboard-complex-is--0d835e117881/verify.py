#!/usr/bin/env python3
"""Reconstruct the four-by-four chessboard transpose orbit space and replay a finite collapse certificate.

Only the standard library is used. The separate chessboard connectivity and
orbit-space fundamental-group theorems are mathematical prerequisites.
"""
import collections
import itertools
import json
from pathlib import Path

SIDE = 4


def transpose_mask(mask):
    out = 0
    for i in range(SIDE):
        for j in range(SIDE):
            if mask & (1 << (SIDE*i+j)):
                out |= 1 << (SIDE*j+i)
    return out


def canonical_flag(flag):
    opposite = tuple(transpose_mask(s) for s in flag)
    return min(flag, opposite)


def rook_faces():
    out = [[] for _ in range(SIDE+1)]
    for k in range(1,SIDE+1):
        for rows in itertools.combinations(range(SIDE), k):
            for cols in itertools.permutations(range(SIDE), k):
                out[k].append(sum(1 << (SIDE*r+c) for r,c in zip(rows,cols)))
        out[k] = sorted(set(out[k]))
    return out


def orbit_flags(faces):
    by_dimension = [[] for _ in range(SIDE)]
    for k in range(1,SIDE+1):
        for top in faces[k]:
            cells = [1 << a for a in range(SIDE**2) if top & (1 << a)]
            for length in range(1,k+1):
                for cuts in itertools.combinations(range(1,k), length-1):
                    for order in itertools.permutations(cells):
                        partial, flag = 0, []
                        for index, cell in enumerate(order, start=1):
                            partial |= cell
                            if index in cuts or index == k:
                                flag.append(partial)
                        by_dimension[length-1].append(canonical_flag(tuple(flag)))
    return [sorted(set(v)) for v in by_dimension]


def signed_boundaries(orbits):
    index = [{f:i for i,f in enumerate(cells)} for cells in orbits]
    out = [None]
    for d in range(1, SIDE):
        columns = []
        for simplex in orbits[d]:
            boundary = collections.Counter()
            for j in range(d+1):
                face = canonical_flag(simplex[:j]+simplex[j+1:])
                boundary[index[d-1][face]] += (-1)**j
            columns.append(dict(sorted((a,b) for a,b in boundary.items() if b)))
        out.append(columns)
    return out


def verify_fundamental_group(orbits):
    """Collapse a maximal tree and eliminate the full triangular presentation."""
    v_index = {v: j for j, v in enumerate(orbits[0])}
    e_index = {e: j for j, e in enumerate(orbits[1])}
    endpoints = [(v_index[canonical_flag((e[0],))],
                  v_index[canonical_flag((e[1],))]) for e in orbits[1]]
    adj = [[] for _ in orbits[0]]
    for j, (a, b) in enumerate(endpoints):
        adj[a].append((b, j))
        adj[b].append((a, j))
    tree, seen, queue = set(), {0}, collections.deque([0])
    while queue:
        a = queue.popleft()
        for b, j in adj[a]:
            if b not in seen:
                seen.add(b)
                queue.append(b)
                tree.add(j)
    assert len(seen) == len(orbits[0]) and len(tree) == len(orbits[0])-1
    generators = {j: 1+i for i, j in enumerate(k for k in range(len(orbits[1])) if k not in tree)}
    assert len(generators) == 462

    def reduced(word):
        s = []
        for g in word:
            if s and s[-1] == -g:
                s.pop()
            else:
                s.append(g)
        while len(s) > 1 and s[0] == -s[-1]:
            s = s[1:-1]
        return s

    def inverse(word):
        return [-g for g in reversed(word)]

    def edge_word(a, b):
        forward = a.bit_count() < b.bit_count()
        e = canonical_flag((a, b) if forward else (b, a))
        j = e_index[e]
        if j in tree:
            return []
        return [generators[j]*(1 if forward else -1)]

    relations = [reduced(edge_word(a,b)+edge_word(b,c)+edge_word(c,a))
                 for a,b,c in orbits[2]]
    assert len(relations) == 768
    remaining = set(generators.values())
    eliminations = 0
    while remaining:
        best = None
        for rid, relation in enumerate(relations):
            appearances = collections.Counter(abs(g) for g in relation)
            unique = [g for g, count in appearances.items() if count == 1 and g in remaining]
            if unique:
                candidate = (len(relation), rid, min(unique))
                if best is None or candidate < best:
                    best = candidate
        assert best is not None, 'Fundamental-group elimination stalled'
        _, rid, g = best
        r = relations[rid]
        j = next(j for j, val in enumerate(r) if abs(val) == g)
        conjugate = r[j:] + r[:j]
        tail = conjugate[1:]
        substitute = inverse(tail) if conjugate[0] > 0 else tail
        replacement_relations = []
        for r_id, word in enumerate(relations):
            if r_id == rid:
                continue
            replaced = []
            for letter in word:
                if abs(letter) == g:
                    replaced.extend(substitute if letter > 0 else inverse(substitute))
                else:
                    replaced.append(letter)
            replacement_relations.append(reduced(replaced))
        relations = replacement_relations
        remaining.remove(g)
        eliminations += 1
    assert eliminations == 462
    assert not any(relations)
    return eliminations


def verify():
    cert = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
    assert cert['schema_version'] == 1
    faces = rook_faces()
    assert [len(a) for a in faces[1:]] == [16,72,96,24]
    flags = orbit_flags(faces)
    count = [len(c) for c in flags]
    assert count == [125,586,768,300]
    assert sum((-1)**d * count[d] for d in range(4)) == 7
    bd = signed_boundaries(flags)
    # Every orbit of a barycentric simplex has trivial action on its ordered
    # vertices: vertex ranks in a flag are strictly increasing.
    for d in range(1,4):
        for col in bd[d]:
            assert len(col) == d+1
            assert set(map(abs,col.values())) == {1}
    # Integral cellular boundary squares vanish.
    for d in (2,3):
        for col in bd[d]:
            accum = collections.Counter()
            for row,coefficient in col.items():
                for idx,val in bd[d-1][row].items():
                    accum[idx] += coefficient*val
            assert all(v == 0 for v in accum.values())
    assert len(cert['top_collapses']) == 300
    active_triangles = set(range(count[2]))
    active_tetrahedra = set(range(count[3]))
    above = [set() for _ in range(count[2])]
    for j,col in enumerate(bd[3]):
        for i in col:
            above[i].add(j)
    for i,j in cert['top_collapses']:
        assert isinstance(i,int) and isinstance(j,int)
        assert i in active_triangles and j in active_tetrahedra
        assert above[i] & active_tetrahedra == {j}, (i,j)
        assert bd[3][j][i] in (1,-1)
        active_triangles.remove(i)
        active_tetrahedra.remove(j)
    assert not active_tetrahedra
    assert len(active_triangles) == 468
    # A 2-dimensional deformation retract remains. Its Euler characteristic
    # is seven. The geometric quotient is simply connected by chessboard
    # connectivity plus the orbit-space fundamental-group theorem. Hence it
    # has free H_2 of rank six and is a wedge of six 2-spheres.
    assert count[0] - count[1] + len(active_triangles) == 7
    # Van Kampen's cellular presentation, independently of a connectivity theorem:
    # 462 generators after a spanning tree, all eliminated via 462 valid Tietze steps.
    assert verify_fundamental_group(flags) == 462
    print('CHESSBOARD_TRANSPOSE_4X4_WEDGE6_OK')
    print('original_faces=(16,72,96,24)')
    print('quotient_orbit_cells=(125,586,768,300)')
    print('certified_top_collapses=300 remaining_cells=(125,586,468) chi=7')
    print('fundamental_group_tietze_eliminations=462 generators_remaining=0')


if __name__ == '__main__':
    verify()
