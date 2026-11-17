#!/usr/bin/env python3
"""Exact finite simplicial-chain verification for two seven-vertex tournaments.

Run: python3 checks/verify.py
Only Python standard library is required. Everything is computed from arc lists.
"""
from collections import defaultdict
from itertools import combinations


def arcs(n, reverse):
    a, b = reverse
    assert 0 <= a < b < n
    return tuple((b, a) if (i, j) == reverse else (i, j)
                 for i in range(n) for j in range(i + 1, n))


def is_multipath(arc_indices, directed_arcs):
    edges = tuple(directed_arcs[i] for i in arc_indices)
    if len({u for u, v in edges}) != len(edges):
        return False
    if len({v for u, v in edges}) != len(edges):
        return False
    next_vertex = dict(edges)
    # Every component is a finite directed path iff it is cycle-free.
    for start in next_vertex:
        current = start
        seen = set()
        while current in next_vertex:
            if current in seen:
                return False
            seen.add(current)
            current = next_vertex[current]
    return True


def enumerate_brute(n, reversal):
    edge_list = arcs(n, reversal)
    return {comb for size in range(n)
            for comb in combinations(range(len(edge_list)), size)
            if is_multipath(comb, edge_list)}


def enumerate_extend(n, reversal):
    edge_list = arcs(n, reversal)
    result = {()}
    # A second enumeration: extend each valid face by later arc indices.
    stack = [()]
    while stack:
        face = stack.pop()
        for new in range((face[-1] + 1) if face else 0, len(edge_list)):
            candidate = face + (new,)
            if is_multipath(candidate, edge_list):
                assert candidate not in result
                result.add(candidate)
                stack.append(candidate)
    return result


def face_layers(faces):
    by = defaultdict(list)
    for face in sorted(faces, key=lambda x: (len(x), x)):
        by[len(face)].append(face)
    return by


def gf2_rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                vector ^= pivots[pivot]
            else:
                pivots[pivot] = vector
                break
    return len(pivots)


def boundary_ranks(by, n):
    columns = {}
    rows = {}
    for size in range(1, n):
        prev = {f: i for i, f in enumerate(by[size - 1])}
        cofaces = {f: i for i, f in enumerate(by[size])}
        column_vectors = []
        row_vectors = [0] * len(by[size - 1])
        for face in by[size]:
            col = 0
            for j in range(size):
                subface = face[:j] + face[j + 1:]
                pos = prev[subface]
                col ^= 1 << pos
                row_vectors[pos] ^= 1 << cofaces[face]
            column_vectors.append(col)
        columns[size] = gf2_rank(column_vectors)
        rows[size] = gf2_rank(row_vectors)
        assert columns[size] == rows[size], ('transpose rank mismatch', size)
    return columns


def verify_case(n, reversal, expected=None):
    faces = enumerate_brute(n, reversal)
    independently_enumerated = enumerate_extend(n, reversal)
    assert faces == independently_enumerated
    by = face_layers(faces)
    counts = tuple(len(by[size]) for size in range(n))
    ranks = boundary_ranks(by, n)
    betti = {size - 1: counts[size] - ranks.get(size, 0)
             - ranks.get(size + 1, 0) for size in range(1, n)}
    nonzero = {degree: count for degree, count in betti.items() if count}
    # Verify the chain condition independently of rank calculations:
    # each codimension-two subface occurs twice in a simplex boundary.
    for size in range(2, n):
        for face in by[size]:
            twice_boundary = set()
            for i in range(size):
                f = face[:i] + face[i + 1:]
                for j in range(size - 1):
                    subface = f[:j] + f[j + 1:]
                    if subface in twice_boundary:
                        twice_boundary.remove(subface)
                    else:
                        twice_boundary.add(subface)
            assert not twice_boundary
    if expected is not None:
        exp_counts, exp_ranks, exp_betti = expected
        assert counts == exp_counts, (reversal, counts)
        assert tuple(ranks[s] for s in range(1, n)) == exp_ranks
        assert nonzero == exp_betti, (reversal, nonzero)
    return counts, ranks, nonzero


def directed_triangles(n, reversal):
    edge_list = set(arcs(n, reversal))
    count = 0
    for a, b, c in combinations(range(n), 3):
        if ((a, b) in edge_list and (b, c) in edge_list
                and (c, a) in edge_list) or (
                (a, c) in edge_list and (c, b) in edge_list
                and (b, a) in edge_list):
            count += 1
    return count


def main():
    f = (1, 21, 142, 370, 351, 93, 3)
    cases = [
        ((0, 2), f, (1, 20, 122, 242, 90, 3), {2: 6, 3: 19}),
        ((1, 3), f, (1, 20, 122, 248, 90, 3), {3: 13}),
    ]
    for reversal, counts, ranks, betti in cases:
        assert directed_triangles(7, reversal) == 1
        answer = verify_case(7, reversal, (counts, ranks, betti))
        print('n=7 reversal', reversal, 'faces_by_cardinality', answer[0],
              'boundary_ranks', tuple(answer[1][k] for k in range(1, 7)),
              'reduced_F2_betti', answer[2], 'PASS')
    for n in range(3, 7):
        outputs = [verify_case(n, (a, a + 2)) for a in range(n - 2)]
        assert all(o[0] == outputs[0][0] and o[2] == outputs[0][2]
                   for o in outputs)
        print('n=', n, 'two-step reversals checked=', len(outputs),
              'face_vector=', outputs[0][0],
              'reduced_F2_betti=', outputs[0][2], 'PASS', sep='')
    print('NEAR_TRANSITIVE_TOURNAMENT_FVECTOR_HOMOLOGY_CHECK_PASS')


if __name__ == '__main__':
    main()
