#!/usr/bin/env python3
"""Independent first-occurrence check for the M_16 matching-complex result.

Rebuild all ordinary matching complexes of M_{2n}, 2 <= n <= 8;
compute their exact signed Morse chain complexes and Smith invariants,
then report reduced integral Betti degrees. Requires verify_m16.py and sympy.
"""
from collections import Counter
from verify_m16 import (graph_edges, face_complex, verified_acyclic_matching,
                        morse_differentials, smith)


def reduced_profile(n):
    edges = graph_edges(n)
    faces = face_complex(edges)
    pairs, critical, _ = verified_acyclic_matching(faces, len(edges))
    cells, differentials = morse_differentials(critical, pairs)
    ranks = {k: len(smith(D)) for k, D in differentials.items()}
    homology = {k: len(cells[k]) - ranks[k] - ranks.get(k + 1, 0)
                for k in range(0, 9)}
    return len(edges), len(faces), {k: v for k, v in homology.items() if v}, \
        {k: smith(D) for k, D in differentials.items() if D.rows and D.cols and smith(D)}


def main():
    results = {}
    for n in range(2, 9):
        edges, faces, betti, _ = reduced_profile(n)
        results[n] = betti
        print('M', 2 * n, 'edges', edges, 'faces', faces, 'reduced_integral_betti', betti)
        assert len(betti) == 1 if n < 8 else len(betti) == 2
    assert results[8] == {4: 2, 5: 4}
    print('FIRST_MIXED_AT_M16_OK')

if __name__ == '__main__':
    main()
