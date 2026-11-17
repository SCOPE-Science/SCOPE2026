#!/usr/bin/env python3
"""Exact, standard-library finite Morse certificates for two-point-punctured Hamming Rips complexes.

Run: python3 verify_two_puncture.py
A nonempty simplex is a tuple of integer-encoded binary words. All checks are exhaustive for 3 <= n <= 5.
"""
import json
from collections import Counter, deque
from itertools import combinations

PIVOTS = json.loads('''{"3,1": [5, 4, 2, 3, 7, 6], "3,2": [5, 4, 1, 2, 7, 6], "3,3": [4, 3, 1, 2, 6, 5], "4,1": [7, 12, 11, 9, 6, 14, 8, 5, 2, 3, 4, 15, 13, 10], "4,2": [7, 12, 11, 9, 6, 14, 8, 5, 1, 2, 4, 15, 13, 10], "4,3": [6, 12, 11, 9, 5, 14, 8, 4, 1, 2, 3, 15, 13, 10], "4,4": [3, 1, 14, 6, 4, 8, 2, 12, 13, 10, 9, 11, 7, 5], "5,1": [31, 23, 28, 21, 25, 26, 18, 30, 5, 15, 6, 22, 7, 11, 10, 17, 3, 16, 24, 8, 9, 2, 4, 20, 29, 19, 12, 27, 14, 13], "5,2": [31, 23, 28, 21, 25, 26, 18, 30, 5, 15, 6, 22, 7, 11, 10, 17, 2, 16, 24, 8, 9, 1, 4, 20, 29, 19, 12, 27, 14, 13], "5,3": [31, 23, 28, 21, 25, 26, 18, 30, 4, 15, 5, 22, 6, 11, 10, 17, 2, 16, 24, 8, 9, 1, 3, 20, 29, 19, 12, 27, 14, 13], "5,4": [19, 22, 1, 13, 26, 9, 2, 29, 25, 21, 18, 30, 28, 6, 14, 17, 31, 7, 24, 16, 8, 4, 12, 3, 27, 23, 11, 20, 10, 5], "5,5": [15, 9, 8, 25, 13, 3, 26, 28, 10, 6, 1, 14, 18, 12, 17, 21, 4, 16, 11, 20, 30, 23, 7, 19, 24, 5, 2, 27, 29, 22]}''')
EXPECTED = {(3,1):(1,0,35), (3,2):(1,0,35), (3,3):(2,1,26),
            (4,1):(3,3,258), (4,2):(3,3,258), (4,3):(3,1,240), (4,4):(3,1,240),
            (5,1):(3,32,1427), (5,2):(3,32,1427), (5,3):(3,29,1392),
            (5,4):(3,29,1392), (5,5):(3,29,1392)}

def simplices(n, d):
    vertices = tuple(v for v in range(1 << n) if v not in (0, (1 << d) - 1))
    adj = {v: {w for w in vertices if w != v and (v ^ w).bit_count() <= 2}
           for v in vertices}
    result = set()
    def walk(face, candidates):
        for i, v in enumerate(candidates):
            enlarged = face + (v,)
            result.add(enlarged)
            walk(enlarged, tuple(w for w in candidates[i + 1:] if w in adj[v]))
    walk((), vertices)
    assert all(all((a ^ b).bit_count() <= 2 for a, b in combinations(face,2)) for face in result)
    return result

def matching(faces, pivots):
    unused = set(faces)
    pairs = []
    for v in pivots:
        for low in sorted((face for face in unused if v not in face), key=lambda a: (len(a), a)):
            upper = tuple(sorted(low + (v,)))
            if low in unused and upper in unused:
                unused.remove(low)
                unused.remove(upper)
                pairs.append((low, upper))
    return unused, pairs

def is_acyclic(faces, pairs):
    reverse = {(upper, lower) for lower, upper in pairs}
    outgoing = {face: [] for face in faces}
    indegree = {face: 0 for face in faces}
    for face in faces:
        for drop in face:
            if len(face) == 1:
                continue
            smaller = tuple(v for v in face if v != drop)
            if (face, smaller) in reverse:
                source, target = smaller, face
            else:
                source, target = face, smaller
            outgoing[source].append(target)
            indegree[target] += 1
    todo = deque(face for face in faces if indegree[face] == 0)
    visited = 0
    while todo:
        source = todo.popleft()
        visited += 1
        for target in outgoing[source]:
            indegree[target] -= 1
            if not indegree[target]:
                todo.append(target)
    return visited == len(faces)

def mod_two_reduced_betti(faces):
    layers = {k: sorted(face for face in faces if len(face) == k + 1)
              for k in range(max(map(len, faces)))}
    ranks = {}
    for k in range(1, len(layers)):
        index = {face: i for i, face in enumerate(layers[k-1])}
        pivot = {}
        for face in layers[k]:
            bitcol = 0
            for sub in combinations(face, k):
                bitcol ^= (1 << index[sub])
            while bitcol:
                j = bitcol.bit_length() - 1
                if j not in pivot:
                    pivot[j] = bitcol
                    break
                bitcol ^= pivot[j]
        ranks[k] = len(pivot)
    return {k: len(layers[k]) - ranks.get(k, 0) - ranks.get(k+1, 0) - (k == 0)
            for k in layers}

def main():
    for n in range(3, 6):
        for d in range(1, n+1):
            key = '%d,%d' % (n,d)
            faces = simplices(n,d)
            degree, mult, expected_faces = EXPECTED[n,d]
            assert len(faces) == expected_faces, (n,d,len(faces))
            pivots = PIVOTS[key]
            assert len(pivots) == (1 << n)-2 and set(pivots) == {f[0] for f in faces if len(f)==1}
            critical, pairs = matching(faces, pivots)
            assert 2*len(pairs)+len(critical)==len(faces)
            assert all(low in faces and hi in faces and len(low)+1 == len(hi)
                       and set(low) < set(hi) for low, hi in pairs)
            expected = {0: 1}
            if mult:
                expected[degree] = mult
            critical_profile = dict(Counter(len(face)-1 for face in critical))
            assert critical_profile == expected, (n,d,critical_profile)
            assert is_acyclic(faces, pairs), (n,d,'cycle in directed Hasse graph')
            betti = mod_two_reduced_betti(faces)
            for k, rank in betti.items():
                assert rank == (mult if k == degree else 0), (n,d,betti)
            print('n=%d d=%d faces=%d pairs=%d critical=%s homotopy=%s DAG=PASS mod2=PASS' %
                  (n,d,len(faces),len(pairs),str(sorted(critical_profile.items())),
                   ('point' if not mult else '%s*S^%d' % (mult,degree))))
    print('TWO_PUNCTURE_RIPS_FINITE_INTEGRAL_HOMOTOPY_PASS cases=12')
if __name__ == '__main__':
    main()
