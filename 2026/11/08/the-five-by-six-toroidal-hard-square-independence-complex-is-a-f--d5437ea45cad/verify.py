"""Exhaustive discrete-Morse certificate for C5 □ C6.

Run: python3 verify.py
Only the Python standard library is used. The empty face is included.
"""
from collections import Counter, deque
from itertools import product

CASES = {(5, 6): (199821, 99910, 1, 5)}


def grid_neighbors(m, n):
    adj = []
    for r in range(m):
        for c in range(n):
            nb = {((r + 1) % m)*n+c, ((r - 1) % m)*n+c,
                  r*n+(c + 1) % n, r*n+(c - 1) % n}
            assert len(nb) == 4
            adj.append(sum(1 << w for w in nb))
    for v, s in enumerate(adj):
        assert not (s & (1 << v))
        for w in range(m*n):
            assert bool(s & (1 << w)) == bool(adj[w] & (1 << v))
    return adj


def independent_faces(adj):
    faces = [0]
    for v, nb in enumerate(adj):
        faces.extend([s | (1 << v) for s in faces if not (s & nb)])
    assert len(faces) == len(set(faces))
    return faces


def independent_row_counts(m, n):
    # Independent implementation using 2^n row patterns and compatibility
    # of consecutive rows, including the wrap-around from last to first.
    valid = [s for s in range(1 << n)
             if not any((s & (1 << c)) and (s & (1 << ((c+1) % n)))
                        for c in range(n))]
    result = Counter()
    for rows in product(valid, repeat=m):
        if any(rows[i] & rows[(i+1) % m] for i in range(m)):
            continue
        result[sum(s.bit_count() for s in rows)] += 1
    return result


def greedy_pivot_matching(faces, n):
    unmatched = set(faces)
    pairs = []
    for v in range(n):
        bit = 1 << v
        lowers = [s for s in unmatched if not (s & bit) and (s | bit) in unmatched]
        for s in lowers:
            assert s in unmatched and s | bit in unmatched
            unmatched.remove(s)
            unmatched.remove(s | bit)
            pairs.append((s, s | bit))
    assert len({s for a,b in pairs for s in (a,b)}) == 2 * len(pairs)
    assert len(unmatched) + 2 * len(pairs) == len(faces)
    return pairs, unmatched


def hasse_acyclicity(faces, pairs):
    # Every covering edge of the entire face poset is constructed. Reverse
    # exactly the matched edges; Kahn sorting must visit every simplex.
    face_set = set(faces)
    matched = set(pairs)
    indegree = {s:0 for s in faces}
    out = {s:[] for s in faces}
    incidences = 0
    for top in faces:
        bits = top
        while bits:
            bit = bits & -bits
            low = top ^ bit
            assert low in face_set
            if (low, top) in matched:
                a,b = low, top
            else:
                a,b = top, low
            out[a].append(b)
            indegree[b] += 1
            incidences += 1
            bits ^= bit
    assert incidences == sum(s.bit_count() for s in faces)
    queue = deque(s for s in faces if indegree[s] == 0)
    processed = 0
    while queue:
        s = queue.popleft()
        processed += 1
        for t in out[s]:
            indegree[t] -= 1
            if indegree[t] == 0:
                queue.append(t)
    assert processed == len(faces), (processed, len(faces))
    return incidences


def main():
    for (m, n), (expected_faces, expected_pairs, expected_critical, dim) in CASES.items():
        adj = grid_neighbors(m, n)
        faces = independent_faces(adj)
        f = Counter(s.bit_count() for s in faces)
        assert f == independent_row_counts(m, n), 'independent row enumeration disagrees'
        assert len(faces) == expected_faces
        pairs, critical = greedy_pivot_matching(faces, m*n)
        assert len(pairs) == expected_pairs
        assert len(critical) == expected_critical
        assert all(s.bit_count() == dim+1 for s in critical)
        assert (0, 1) in pairs
        incidences = hasse_acyclicity(faces, pairs)
        reduced_euler = sum((1 if (k-1)%2 == 0 else -1)*v for k,v in f.items())
        assert reduced_euler == expected_critical * ((-1)**dim)
        print('graph=C%d_cartesian_C%d' % (m,n))
        print('faces_including_empty=%d' % len(faces))
        print('nonempty_f_vector=%s' % (tuple(f[k] for k in range(1,max(f)+1)),))
        print('independent_row_enumeration=AGREES')
        print('matching_pairs=%d' % len(pairs))
        print('empty_face_matched=True')
        print('critical_faces=%d' % len(critical))
        print('critical_dimension=%d' % dim)
        print('critical_masks=%s' % sorted(critical))
        print('hasse_cover_relations=%d' % incidences)
        print('acyclic_toposort_vertices=%d' % len(faces))
        print('reduced_euler=%d' % reduced_euler)
        print('homotopy_type=wedge_%d_S%d' % (expected_critical,dim))
    print('ALL_CHECKS_PASS')


if __name__=='__main__':
    main()
