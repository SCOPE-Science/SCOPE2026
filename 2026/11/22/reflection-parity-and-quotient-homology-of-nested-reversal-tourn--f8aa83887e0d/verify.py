"""Finite checks for a reflected nested-arc tournament flag complex.

Run with Python 3. This verifier is a finite consistency check; the general
homotopy and integral character require the accompanying mathematical proof.
"""
from itertools import combinations


def face_lists(n, reversed_pairs):
    reversed_pairs = {tuple(sorted(pair)) for pair in reversed_pairs}
    forbidden = set()
    for i, j, k in combinations(range(n), 3):
        a = (i, j) not in reversed_pairs
        b = (i, k) not in reversed_pairs
        c = (j, k) not in reversed_pairs
        if (a and c and not b) or (not a and not c and b):
            forbidden.add((1 << i) | (1 << j) | (1 << k))
    faces = [[] for _ in range(n)]
    for mask in range(1, 1 << n):
        if not any(mask & f == f for f in forbidden):
            faces[mask.bit_count() - 1].append(mask)
    return faces


def reduced_mod_two_betti(faces):
    n = len(faces)
    rank = []
    for d in range(n - 1):
        row_index = {face: i for i, face in enumerate(faces[d])}
        pivots = {}
        for higher_face in faces[d + 1]:
            column = 0
            for v in range(n):
                if higher_face >> v & 1:
                    column ^= 1 << row_index[higher_face ^ (1 << v)]
            while column:
                p = column.bit_length() - 1
                if p not in pivots:
                    pivots[p] = column
                    break
                column ^= pivots[p]
        rank.append(len(pivots))
    return {d: len(faces[d]) - (rank[d-1] if d else 1)
            - (rank[d] if d < n-1 else 0) for d in range(n)}


def reflection_lefschetz(faces, n):
    trace = 0
    for d, level in enumerate(faces):
        fixed = 0
        for face in level:
            reflected = sum(1 << (n-1-i) for i in range(n) if face >> i & 1)
            if reflected == face:
                fixed += 1
        # On a reflection-invariant simplex, reversal of all vertex orders.
        orientation = (-1) ** (d * (d+1) // 2)
        trace += (-1) ** d * orientation * fixed
    return trace


def main():
    count = 0
    for r in range(1, 5):
        for center in range(1, 4):
            n = center + 2*r
            pairs = [(j, n-1-j) for j in range(r)]
            faces = face_lists(n, pairs)
            betti = reduced_mod_two_betti(faces)
            expected = {j: 1 for j in range(1, r+1)}
            observed = {j: rank for j, rank in betti.items() if rank}
            assert observed == expected, (n, pairs, observed, expected)
            assert reflection_lefschetz(faces, n) == r+1, (n, r)
            count += 1
    print('PASS: %d independent face/enumeration, reduced homology, and signed reflection Lefschetz checks' % count)


if __name__ == '__main__':
    main()
