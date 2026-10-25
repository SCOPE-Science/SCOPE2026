#!/usr/bin/env python3
"""Exact reproducibility checks for the bidirected-octahedron multipath complex.

Python 3 standard library only. All enumeration bounds and assertions are explicit.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations

# Opposite pairs are (0,1), (2,3), (4,5).
VERTICES = tuple(range(6))
ARCS = tuple((u, v) for u in VERTICES for v in VERTICES if u // 2 != v // 2)
ORDER = (10, 17, 12, 16, 0, 19, 5, 23, 21, 3, 20, 1,
         6, 15, 8, 7, 22, 13, 4, 18, 2, 14, 9, 11)


def is_multipath(edge_indices):
    """A directed degree-1 subgraph with no directed circuit is a path forest."""
    incoming = [0] * 6
    outgoing = [0] * 6
    successor = [-1] * 6
    for i in edge_indices:
        u, v = ARCS[i]
        incoming[v] += 1
        outgoing[u] += 1
        if incoming[v] > 1 or outgoing[u] > 1:
            return False
        successor[u] = v
    for start in VERTICES:
        seen = {start}
        cur = successor[start]
        while cur != -1:
            if cur in seen:
                return False
            seen.add(cur)
            cur = successor[cur]
    return True


def all_faces():
    # Six vertices: every directed path forest has at most five arcs.
    faces = {0}
    for k in range(1, 6):
        for indices in combinations(range(len(ARCS)), k):
            if is_multipath(indices):
                faces.add(sum(1 << i for i in indices))
    return faces


def make_morse_matching(faces):
    active = set(faces) - {0}
    pairs = []
    for pivot in ORDER:
        bit = 1 << pivot
        for lower in sorted(active):
            upper = lower | bit
            if not lower & bit and upper in active:
                active.remove(lower)
                active.remove(upper)
                pairs.append((lower, upper))
    return active, pairs


def check_acyclic(faces, pairs):
    nonempty = set(faces) - {0}
    matched_upper_to_lower = {}
    occupied = set()
    for lower, upper in pairs:
        assert lower in nonempty and upper in nonempty
        assert upper.bit_count() == lower.bit_count() + 1
        assert lower & upper == lower
        assert lower not in occupied and upper not in occupied
        occupied.add(lower)
        occupied.add(upper)
        matched_upper_to_lower[upper] = lower
    indegree = {face: 0 for face in nonempty}
    outgoing = defaultdict(list)
    covers = 0
    for upper in nonempty:
        for i in range(len(ARCS)):
            if not upper >> i & 1:
                continue
            lower = upper ^ (1 << i)
            if lower == 0:
                continue
            covers += 1
            if matched_upper_to_lower.get(upper) == lower:
                source, target = lower, upper
            else:
                source, target = upper, lower
            outgoing[source].append(target)
            indegree[target] += 1
    todo = deque(face for face in nonempty if indegree[face] == 0)
    visited = 0
    while todo:
        face = todo.popleft()
        visited += 1
        for nxt in outgoing[face]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                todo.append(nxt)
    assert visited == len(nonempty), 'The matching has a closed gradient path'
    return covers


def signed_boundary_rank(faces_by_dimension, degree):
    if degree == 0:
        return 1  # Reduced augmentation on nonempty vertex set.
    prev_index = {face: i for i, face in enumerate(faces_by_dimension[degree - 1])}
    basis = {}
    rank = 0
    for mask in faces_by_dimension[degree]:
        indices = [i for i in range(len(ARCS)) if mask >> i & 1]
        col = {prev_index[mask ^ (1 << bit)]: Fraction((-1) ** j)
               for j, bit in enumerate(indices)}
        while col:
            pivot = min(col)
            if pivot not in basis:
                scalar = col[pivot]
                basis[pivot] = {i: val / scalar for i, val in col.items()}
                rank += 1
                break
            scalar = col[pivot]
            for row, val in basis[pivot].items():
                updated = col.get(row, 0) - scalar * val
                if updated:
                    col[row] = updated
                else:
                    col.pop(row, None)
    return rank


def main():
    assert len(ARCS) == 24
    assert set(ORDER) == set(range(24))
    faces = all_faces()
    dimensions = defaultdict(list)
    for face in faces:
        dimensions[face.bit_count() - 1].append(face)
        if face:
            for i in range(len(ARCS)):
                if face >> i & 1:
                    assert face ^ (1 << i) in faces
    for d in dimensions:
        dimensions[d].sort()
    counts = {d: len(dimensions[d]) for d in range(-1, 5)}
    assert counts == {-1: 1, 0: 24, 1: 192, 2: 616, 3: 744, 4: 240}
    assert len(faces) == 1817
    maximal = Counter()
    for face in faces:
        if not any((face | (1 << i)) in faces for i in range(len(ARCS))
                   if not face >> i & 1):
            maximal[face.bit_count() - 1] += 1
    assert maximal == {3: 24, 4: 240}

    critical, pairs = make_morse_matching(faces)
    assert len(pairs) == 844
    critical_by_dimension = Counter(face.bit_count() - 1 for face in critical)
    assert critical_by_dimension == {0: 1, 2: 3, 3: 92, 4: 32}
    covers = check_acyclic(faces, pairs)
    assert covers == 6408

    ranks = {d: signed_boundary_rank(dimensions, d) for d in range(5)}
    assert ranks == {0: 1, 1: 23, 2: 169, 3: 444, 4: 208}
    betti = {d: len(dimensions[d]) - ranks[d] - ranks.get(d + 1, 0)
             for d in range(5)}
    assert betti == {0: 0, 1: 0, 2: 3, 3: 92, 4: 32}
    # Morse chain ranks agree with the rational Betti ranks. Since Morse
    # differentials are integer matrices, every such differential is zero.
    assert all(critical_by_dimension.get(d, 0) == betti[d]
               for d in range(1, 5))
    assert sum((-1) ** d * len(dimensions[d]) for d in range(-1, 5)) == -57
    print('VERIFIED_OCTAHEDRAL_MULTIPATH_HOMOLOGY')
    print('augmented_face_counts:', [counts[d] for d in range(-1, 5)])
    print('facet_counts_dim3_dim4:', [maximal[3], maximal[4]])
    print('matching_pairs:', len(pairs), 'directed_hasse_covers:', covers)
    print('critical_cells_dim0_to_dim4:',
          [critical_by_dimension.get(d, 0) for d in range(5)])
    print('signed_boundary_ranks_over_Q_dim0_to_dim4:',
          [ranks[d] for d in range(5)])
    print('integral_reduced_betti_dim0_to_dim4:',
          [betti[d] for d in range(5)])


if __name__ == '__main__':
    main()
