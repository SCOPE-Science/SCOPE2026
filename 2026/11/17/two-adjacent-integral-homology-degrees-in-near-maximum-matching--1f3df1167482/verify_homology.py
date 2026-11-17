"""Finite independent rank checks for near-maximum matching avoidance.

The signed integral proof is the Mayer--Vietoris argument in RESULT.md;
these explicit finite-field tests are independent corroboration, not a proof
for infinitely many cycle lengths or integral torsion-freeness.
"""
from itertools import combinations


def test_cycle_pair(n, m):
    """Build faces directly from forbidden matchings, then compute GF(2) ranks."""
    edges = ([(i, (i + 1) % n) for i in range(n)] +
             [(n + i, n + (i + 1) % m) for i in range(m)])
    threshold = n // 2 + m // 2 - 1
    forbidden = []
    for subset in combinations(range(n + m), threshold):
        ends = [v for j in subset for v in edges[j]]
        if len(set(ends)) == len(ends):
            forbidden.append(sum(1 << j for j in subset))
    face_by_dimension = {}
    count = 0
    for mask in range(1 << (n + m)):
        if any(mask & bad == bad for bad in forbidden):
            continue
        if mask:
            face_by_dimension.setdefault(mask.bit_count() - 1, []).append(mask)
            count += 1
    dimensions = sorted(face_by_dimension)
    ranks = {}
    for degree in dimensions:
        if degree == 0:
            ranks[degree] = 0
            continue
        row_index = {face: i for i, face in enumerate(face_by_dimension[degree - 1])}
        pivot = {}
        for face in face_by_dimension[degree]:
            column = 0
            for i in range(n + m):
                if face >> i & 1:
                    column ^= 1 << row_index[face ^ (1 << i)]
            while column:
                head = column.bit_length() - 1
                if head in pivot:
                    column ^= pivot[head]
                else:
                    pivot[head] = column
                    break
        ranks[degree] = len(pivot)
    betti = {degree: len(cells) - ranks[degree] - ranks.get(degree + 1, 0)
             for degree, cells in face_by_dimension.items()}
    betti[0] -= 1
    s = n // 2 + m // 2
    expected = {2 * s - 6: 2, 2 * s - 5: 1}
    observed = {degree: rank for degree, rank in betti.items() if rank}
    assert observed == expected, (n, m, observed, expected)
    return count, observed


def main():
    examples = [(6, 6), (6, 7), (7, 7), (6, 8), (8, 8)]
    for pair in examples:
        faces, ranks = test_cycle_pair(*pair)
        print(f'cycles={pair} nonempty_faces={faces} reduced_betti_GF2={ranks} PASS')
    print('TWO_CYCLE_NEAR_MAX_HOMOLOGY_GF2_PASS', len(examples), 'configurations')


if __name__ == '__main__':
    main()
