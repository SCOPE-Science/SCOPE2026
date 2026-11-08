#!/usr/bin/env python3
"""Standalone exact finite verification of a Pappus dominance-complex homotopy result.

No external packages or files. Run: python3 pappus_dominance_verify.py
Integer masks use vertices 0,...,17. The simplicial orientation is increasing.
"""
from array import array
from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256

N = 18
LCF = (5, 7, -7, 7, -7, -5) * 3
ORDER_A = tuple(range(N))
ORDER_B = (8, 10, 16, 7, 11, 13, 6, 5, 1, 14, 3, 4, 2, 9, 0, 15, 12, 17)


def graph():
    nhood = [1 << v for v in range(N)]
    edges = set()
    for v in range(N):
        edges.add(tuple(sorted((v, (v + 1) % N))))
        edges.add(tuple(sorted((v, (v + LCF[v]) % N))))
    assert len(edges) == 27
    for u, v in edges:
        assert u != v
        nhood[u] |= 1 << v
        nhood[v] |= 1 << u
    assert all(mask.bit_count() == 4 for mask in nhood)
    assert all((u - v) % 2 for u, v in edges)
    return nhood, edges


def all_faces(nhood):
    full = (1 << N) - 1
    faces = set()
    count_agree = 0
    for s in range(1 << N):
        forbidden = not any((s & nh) == nh for nh in nhood)
        d = full ^ s
        by_dominating = all(d & nh for nh in nhood)
        assert forbidden == by_dominating
        count_agree += 1
        if forbidden and s:
            faces.add(s)
    assert count_agree == (1 << N)
    return faces


def toggle_matching(faces, order):
    unmatched = set(faces)
    pair = {}
    for v in order:
        bit = 1 << v
        for low in list(unmatched):
            up = low | bit
            if not low & bit and up in unmatched:
                unmatched.remove(low)
                unmatched.remove(up)
                pair[low] = up
    assert 2 * len(pair) + len(unmatched) == len(faces)
    assert len(set(pair).union(pair.values()).union(unmatched)) == len(faces)
    return pair, unmatched


def verify_acyclic(faces, pair):
    # Reverse matched cover relations; orient all other Hasse covers downward.
    indeg = array('i', [0]) * (1 << N)
    covers = 0
    for up in faces:
        for j in range(N):
            if not up & (1 << j):
                continue
            low = up ^ (1 << j)
            if not low:
                continue
            if pair.get(low) == up:
                indeg[up] += 1
            else:
                indeg[low] += 1
            covers += 1
    q = deque(s for s in faces if not indeg[s])
    visited = 0
    while q:
        s = q.popleft()
        visited += 1
        for j in range(N):
            bit = 1 << j
            if s & bit:
                low = s ^ bit
                if low and pair.get(low) != s:
                    indeg[low] -= 1
                    if not indeg[low]:
                        q.append(low)
            elif pair.get(s) == (s | bit):
                up = s | bit
                indeg[up] -= 1
                if not indeg[up]:
                    q.append(up)
    assert visited == len(faces), (visited, len(faces))
    return covers, visited


def oriented_boundary(top):
    for j, v in enumerate(i for i in range(N) if top & (1 << i)):
        yield top ^ (1 << v), (1 if j % 2 == 0 else -1)


def morse_boundary(pair, critical):
    critical8 = sorted(s for s in critical if s.bit_count() == 9)
    critical9 = sorted(s for s in critical if s.bit_count() == 10)
    indices = {s: i for i, s in enumerate(critical8)}
    # Unit-pivot chain cancellation: a lower matched 8-cell is replaced
    # by the signed other 8-faces of its matched 9-coface.
    @lru_cache(maxsize=None)
    def reduced_8(s):
        if s in indices:
            return ((indices[s], 1),)
        if s not in pair:
            return ()  # this 8-cell is paired as an upper cell with a 7-cell
        up = pair[s]
        boundary = tuple(oriented_boundary(up))
        pivots = [a for t, a in boundary if t == s]
        assert len(pivots) == 1 and abs(pivots[0]) == 1
        a = pivots[0]
        vec = Counter()
        for t, b in boundary:
            if t == s:
                continue
            for col, value in reduced_8(t):
                vec[col] -= a * b * value
        return tuple(sorted((col, value) for col, value in vec.items() if value))

    matrix = []
    for top in critical9:
        row = Counter()
        for s, a in oriented_boundary(top):
            for col, value in reduced_8(s):
                row[col] += a * value
        matrix.append(tuple(row.get(i, 0) for i in range(len(critical8))))
    return critical8, critical9, matrix, reduced_8.cache_info()


def main():
    nhood, edges = graph()
    faces = all_faces(nhood)
    fvector = sorted(Counter(s.bit_count() - 1 for s in faces).items())
    assert len(faces) == 118562
    assert dict(fvector) == {0:18,1:153,2:816,3:3042,4:8316,
                             5:16953,6:25650,7:28134,8:21422,
                             9:10575,10:3042,11:423,12:18}
    euler_reduced = sum((-1)**(s.bit_count()-1) for s in faces) - 1
    assert euler_reduced == 1
    facets = [s for s in faces if all((s >> j & 1) or s | (1 << j) not in faces
                                           for j in range(N))]
    assert dict(Counter(s.bit_count()-1 for s in facets)) == {8:2,10:72,11:189,12:18}
    print('graph vertices=18 edges=27 degree=3 bipartite=yes')
    print('all 262144 subsets checked by two independent face criteria')
    print('nonempty_faces=',len(faces),'fvector=',fvector)
    print('facets=',len(facets),'facet_dimensions=',sorted(Counter(s.bit_count()-1 for s in facets).items()))
    print('reduced_euler=',euler_reduced)
    for name, order, expected_critical, expected_matrix in (
       ('A', ORDER_A, [(0,1),(8,87382),(8,174762),(8,205674),(9,205692),(9,222570)],[(0,0,-1),(0,0,1)]),
       ('B', ORDER_B, [(0,256),(8,87637),(8,182954),(9,187084)],[(0,0)]),
    ):
        pair, critical = toggle_matching(faces, order)
        covers, visited = verify_acyclic(faces, pair)
        dims = sorted((s.bit_count()-1,s) for s in critical)
        assert dims == expected_critical
        assert covers == 900162
        _, _, matrix, memo = morse_boundary(pair, critical)
        assert matrix == expected_matrix, (name,matrix)
        digest = sha256(''.join(f'{low}:{pair[low]}\n' for low in sorted(pair)).encode('ascii')).hexdigest()
        print(f'matching_{name}: pairs={len(pair)} critical={dims} covers={covers} acyclic_nodes={visited}')
        print(f'matching_{name}: integral_Morse_d9_rows={matrix} reduction_states={memo.misses} pair_sha256={digest}')
    print('INTEGRAL_PAPPUS_DOMINANCE_WEDGE_CHECK_PASS')

if __name__ == '__main__':
    main()
