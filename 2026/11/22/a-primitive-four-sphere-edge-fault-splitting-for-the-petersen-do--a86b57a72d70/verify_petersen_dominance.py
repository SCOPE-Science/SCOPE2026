#!/usr/bin/env python3
"""Exact finite verifier for the Petersen dominance-complex edge-fault pair.

Requires only Python 3 standard library. A face mask has bit i for the
lexicographically i-th 2-subset of {0,1,2,3,4}; edges join disjoint pairs.
The 0-mask represents the augmented empty simplex of dimension -1.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

ORDER = (2, 5, 1, 3, 7, 8, 6, 0, 9, 4)
VERTICES = tuple(combinations(range(5), 2))
EDGES = tuple((i, j) for i in range(10) for j in range(i+1, 10)
              if set(VERTICES[i]).isdisjoint(VERTICES[j]))
ALL_MASK = (1 << 10) - 1


def dominance_faces(edge_set, method=0):
    adj = [set([i]) for i in range(10)]
    for i, j in edge_set:
        adj[i].add(j)
        adj[j].add(i)
    close = [sum(1 << v for v in adj[i]) for i in range(10)]
    if method == 0:
        return {s for s in range(1 << 10) if all((s & n) != n for n in close)}
    # Independent reconstruction by testing the complementary dominating set.
    result = set()
    for s in range(1 << 10):
        dom = ALL_MASK ^ s
        if all((dom & n) != 0 for n in close):
            result.add(s)
    return result


def morse_match(face_set):
    """Staged Boolean-coordinate matching, including augmented empty face."""
    remaining = set(face_set)
    pairs = []
    for vertex in ORDER:
        bit = 1 << vertex
        for a in sorted(remaining):
            b = a | bit
            if not a & bit and b in remaining:
                remaining.remove(a)
                remaining.remove(b)
                pairs.append((a, b))
    return pairs, remaining


def verify_acyclic(face_set, pairs):
    """Topological-sort every directed Hasse arrow, reversals for matched edges."""
    matched = set(pairs)
    assert len(matched) == len(pairs)
    seen = set()
    for a, b in pairs:
        assert a in face_set and b in face_set
        assert b.bit_count() == a.bit_count()+1 and a & b == a
        assert a not in seen and b not in seen
        seen.add(a); seen.add(b)
    in_degree = {s: 0 for s in face_set}
    out = defaultdict(list)
    for b in face_set:
        for bit_index in range(10):
            bit = 1 << bit_index
            if not b & bit: continue
            a = b ^ bit
            if a not in face_set: continue
            if (a, b) in matched:
                source, target = a, b
            else:
                source, target = b, a
            out[source].append(target)
            in_degree[target] += 1
    queue = deque(v for v,d in in_degree.items() if not d)
    count = 0
    while queue:
        v = queue.popleft(); count += 1
        for w in out[v]:
            in_degree[w]-=1
            if in_degree[w] == 0: queue.append(w)
    assert count == len(face_set), (count, len(face_set))
    return sum(map(len,out.values()))


def gf2_rank(columns):
    basis = {}
    for column in columns:
        while column:
            pivot = column.bit_length() - 1
            if pivot in basis: column ^= basis[pivot]
            else:
                basis[pivot] = column
                break
    return len(basis)


def betti(face_set, reduced):
    dims = defaultdict(list)
    for face in face_set:
        if face or reduced:
            dims[face.bit_count()-1].append(face)
    for k in dims: dims[k].sort()
    rank = {}
    for k in sorted(dims):
        if k == -1: continue
        row = {face:i for i, face in enumerate(dims[k-1])}
        columns = []
        for face in dims[k]:
            boundary = 0
            for bit in range(10):
                if face & (1<<bit):
                    subface = face ^ (1<<bit)
                    if subface in row: boundary ^= 1 << row[subface]
            columns.append(boundary)
        rank[k] = gf2_rank(columns)
    values = {k:len(dims[k])-rank.get(k,0)-rank.get(k+1,0)
              for k in dims if k >= 0}
    return {k:b for k,b in values.items() if b}, {k:len(v) for k,v in dims.items()}


def main():
    assert len(VERTICES) == 10 and len(EDGES) == 15
    x = dominance_faces(EDGES)
    assert x == dominance_faces(EDGES,1)
    assert x == {0} | (x - {0})
    assert EDGES[0] == (0,7)
    y = dominance_faces(EDGES[1:])
    assert y == dominance_faces(EDGES[1:],1)
    assert y <= x
    relative = x - y
    assert 0 not in relative
    expected_critical = {
        'intact': {4:11},
        'deleted': {4:7},
        'relative': {4:4},
    }
    saved_matchings = {}
    saved_critical = {}
    for label, faces in [('intact',x),('deleted',y),('relative',relative)]:
        matching, critical = morse_match(faces)
        arrows = verify_acyclic(faces,matching)
        saved_matchings[label] = matching
        saved_critical[label] = critical
        dim_counts = dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
        assert dim_counts == expected_critical[label], (label,dim_counts)
        b,counts=betti(faces, reduced=(label!='relative'))
        assert b == expected_critical[label], (label,b)
        print(label, 'nonempty faces by dimension',
              {k:v for k,v in sorted(counts.items()) if k>=0},
              'pairs',len(matching),'critical',dim_counts,'GF2 Betti',b,
              'directed Hasse arrows',arrows)
    # The subcomplex matching and the relative matching also form a single
    # acyclic matching on the ambient complex; this checks the CW-pair claim.
    combined = saved_matchings['deleted'] + saved_matchings['relative']
    assert len(combined) == 321
    assert verify_acyclic(x, combined) == 2740
    assert len(saved_critical['deleted'] | saved_critical['relative']) == 11
    assert not (saved_critical['deleted'] & saved_critical['relative'])
    # Every graph edge is the image of (0,7) under some permutation of five labels.
    perms = __import__('itertools').permutations(range(5))
    orbit = set()
    for perm in perms:
        i=VERTICES.index(tuple(sorted(perm[z] for z in VERTICES[0])))
        j=VERTICES.index(tuple(sorted(perm[z] for z in VERTICES[7])))
        orbit.add(tuple(sorted((i,j))))
    assert orbit == set(EDGES)
    for edge in EDGES:
        fs = dominance_faces(tuple(e for e in EDGES if e!=edge))
        assert len(fs)==len(y)
        assert sum((-1)**(s.bit_count()-1) for s in fs if s)==8
    print('PASS: full inclusion pair, acyclic augmented/relative Morse matchings,')
    print('      mod-2 chain ranks, independent face enumeration, and all 15 edge positions.')

if __name__=='__main__':
    main()
