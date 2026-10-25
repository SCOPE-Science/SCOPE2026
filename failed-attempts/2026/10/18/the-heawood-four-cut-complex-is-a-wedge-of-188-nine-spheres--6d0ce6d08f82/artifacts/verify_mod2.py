#!/usr/bin/env python3
"""Independent reduced simplicial homology over the field of two elements.

Builds the Heawood four-cut complex afresh; does not use any Morse matching.
Run: python3 artifacts/verify_mod2.py
"""
from collections import defaultdict
from itertools import combinations


def main():
    n = 14
    graph = [0] * n
    for line in range(7):
        for shift in (0, 1, 3):
            a, b = (line + shift) % 7, 7 + line
            graph[a] |= 1 << b
            graph[b] |= 1 << a

    def connected(mask):
        seen = mask & -mask
        while True:
            new = seen
            b = seen
            while b:
                bit = b & -b
                new |= graph[bit.bit_length() - 1] & mask
                b ^= bit
            if new == seen:
                return seen == mask
            seen = new

    by_size = defaultdict(set)
    full = (1 << n) - 1
    for vertices in combinations(range(n), 4):
        removed = sum(1 << v for v in vertices)
        if not connected(removed):
            face = full ^ removed
            while True:
                by_size[face.bit_count()].add(face)
                if not face:
                    break
                face = (face - 1) & (full ^ removed)
    boundary_ranks = {}
    for count in range(1, max(by_size) + 1):
        lower = {face: i for i, face in enumerate(sorted(by_size[count - 1]))}
        pivots = {}
        for face in by_size[count]:
            column = 0
            bits = face
            while bits:
                bit = bits & -bits
                column ^= 1 << lower[face ^ bit]
                bits ^= bit
            while column:
                lead = column.bit_length()
                if lead not in pivots:
                    pivots[lead] = column
                    break
                column ^= pivots[lead]
        boundary_ranks[count] = len(pivots)
    betti = {count - 1: len(faces) - boundary_ranks.get(count, 0)
             - boundary_ranks.get(count + 1, 0)
             for count, faces in by_size.items() if count > 0}
    assert betti.get(9) == 188
    assert all(value == 0 for degree, value in betti.items() if degree != 9)
    print('reduced-mod2-nonzero-betti',
          [(degree, value) for degree, value in sorted(betti.items()) if value], flush=True)
    print('boundary-ranks', sorted(boundary_ranks.items()), flush=True)
    print('MOD2_VERIFY_OK', flush=True)


if __name__ == '__main__':
    main()
