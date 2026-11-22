"""Finite checks for ordinary matching complexes of short-arm multi-theta graphs.

No external dependencies. The finite checks do not replace the all-parameter
acyclic-fiber argument in the accompanying proof.
"""
from collections import defaultdict, deque
from itertools import combinations


def actual_faces(a, b):
    # Two poles are 'u','v'; each path has fresh interior vertices.
    edges = []
    for i in range(a + b):
        if i < a:
            edges.extend([('u', ('c', i)), (('c', i), 'v')])
        else:
            edges.extend([('u', ('s', i)), (('s', i), ('t', i)),
                          (('t', i), 'v')])
    edges = [frozenset(e) for e in edges]
    faces = {frozenset()}
    # Independently enumerate partial matchings by scanning graph edges.
    def rec(t, used, matching):
        if t == len(edges):
            faces.add(frozenset(matching))
            return
        rec(t + 1, used, matching)
        if not (edges[t] & used):
            rec(t + 1, used | edges[t], matching + [t])
    rec(0, set(), [])
    # Map edge indices to canonical x/y/z symbols.
    names = []
    for i in range(a + b):
        names.extend([('x', i), ('z', i)] if i < a
                     else [('x', i), ('y', i - a), ('z', i)])
    return {frozenset(names[k] for k in face) for face in faces}


def parameter_faces(a, b):
    n = a + b
    faces = set()
    for x in [None] + list(range(n)):
        for z in [None] + list(range(n)):
            if x is not None and z == x and x < a:
                continue
            outer = (({('x', x)} if x is not None else set()) |
                     ({('z', z)} if z is not None else set()))
            free = [('y', j) for j in range(b)
                    if x != a + j and z != a + j]
            for k in range(len(free) + 1):
                for Y in combinations(free, k):
                    faces.add(frozenset(outer | set(Y)))
    return faces


def matching(a, b, faces):
    pairs = {}
    critical = set()
    nonempty = faces - {frozenset()}
    for face in nonempty:
        outer = frozenset(v for v in face if v[0] != 'y')
        free = [j for j in range(b)
                if ('x', a + j) not in outer and
                   ('z', a + j) not in outer]
        if not free:
            critical.add(face)
        else:
            pivot = ('y', free[0])
            if not outer and face == frozenset({('y', 0)}):
                critical.add(face)
                continue
            mate = face ^ frozenset({pivot})
            if mate == frozenset():
                critical.add(face)
                continue
            pairs[face] = mate
    for face, mate in pairs.items():
        assert mate in nonempty and pairs[mate] == face
        assert len(face ^ mate) == 1
    assert len(pairs) + len(critical) == len(nonempty)
    return pairs, critical


def acyclic(faces, pairs):
    # Hasse arcs: matched cover lower->higher, otherwise higher->lower.
    fs = sorted(faces - {frozenset()}, key=lambda x: (len(x), sorted(x)))
    outs = defaultdict(list)
    indeg = {f: 0 for f in fs}
    for high in fs:
        for v in high:
            low = high - {v}
            if not low:
                continue
            source, target = ((low, high) if pairs.get(low) == high
                              else (high, low))
            outs[source].append(target)
            indeg[target] += 1
    Q = deque(f for f in fs if indeg[f] == 0)
    removed = 0
    while Q:
        f = Q.popleft()
        removed += 1
        for g in outs[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                Q.append(g)
    assert removed == len(fs), (removed, len(fs))


def expected(a, b):
    if b >= 3:
        return {0: 1}
    if b == 2:
        return {0: 1, 1: 2}
    if b == 1:
        return {0: 3, 1: 2 * a + 1}
    return None


def gf2_betti(faces):
    bydim = defaultdict(list)
    for f in faces:
        bydim[len(f) - 1].append(f)
    ranks = {}
    for d in range(max(bydim) + 1):
        index = {f: i for i, f in enumerate(bydim[d - 1])}
        basis = {}
        for f in bydim[d]:
            v = 0
            for u in f:
                v ^= 1 << index[f - {u}]
            while v:
                lead = v.bit_length() - 1
                if lead in basis:
                    v ^= basis[lead]
                else:
                    basis[lead] = v
                    break
        ranks[d] = len(basis)
    # Reduced H_0 subtracts the augmentation boundary rank 1.
    result = {}
    for d in range(max(bydim) + 1):
        dim = len(bydim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
        if dim:
            result[d] = dim
    return result


def predicted_homology(a, b):
    if b >= 3:
        return {}
    if b == 2:
        return {1: 2}
    if b == 1:
        assert a >= 1
        return {1: 2 * a - 1}
    if a == 2:
        return {0: 1}
    assert a >= 3
    return {1: a * a - 3 * a + 1}


def main():
    tests = 0
    total_faces = 0
    for a in range(7):
        for b in range(7):
            if not (2 <= a + b <= 9):
                continue
            faces = actual_faces(a, b)
            assert faces == parameter_faces(a, b), (a, b)
            total_faces += len(faces)
            if b:
                pairs, crit = matching(a, b, faces)
                counts = defaultdict(int)
                for f in crit:
                    counts[len(f) - 1] += 1
                assert dict(counts) == expected(a, b), (a, b, dict(counts))
                acyclic(faces, pairs)
            else:
                assert all(len(f) <= 2 for f in faces)
            bb = gf2_betti(faces)
            assert bb == predicted_homology(a, b), (a, b, bb)
            tests += 1
    print(f'PASS: {tests} distinct (a,b) graph instances; {total_faces} total faces')
    print('PASS: independently enumerated graph matchings equal fiber descriptions')
    print('PASS: all proposed face-poset pairings valid and acyclic')
    print('PASS: exact critical-cell counts and mod-two homology agree')
    print('LIMIT: finite checks are not an infinite-parameter or integral proof')


if __name__ == '__main__':
    main()
