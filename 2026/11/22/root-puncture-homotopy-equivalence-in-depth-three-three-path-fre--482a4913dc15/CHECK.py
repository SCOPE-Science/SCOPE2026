"""Exhaustive small-case checks for depth-three 2-independence complexes.

Run: python3 CHECK.py
The general theorem is proved by relative simplicial collapses in RESULT.md;
finite computations here independently test the domain and two collapses.
"""
from collections import defaultdict
import heapq


def bits(s):
    while s:
        v = s & -s
        yield v
        s ^= v


def complexes(branches):
    """branches[i][j] is the positive leaf count below second-level vertex j."""
    adjacency = [0]
    first = []
    edges = []
    for block in branches:
        a = len(adjacency)
        adjacency.append(0)
        first.append(a)
        edges.append((0, a))
        for q in block:
            b = len(adjacency)
            adjacency.append(0)
            edges.append((a, b))
            for _ in range(q):
                c = len(adjacency)
                adjacency.append(0)
                edges.append((b, c))
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a
    K, D, L, U = [], [], [], []
    for s in range(1 << len(adjacency)):
        if any((adjacency[v] & s).bit_count() > 1 for v in range(len(adjacency)) if s & (1 << v)):
            continue
        K.append(s)
        if s & 1:
            L.append(s >> 1)
        else:
            D.append(s >> 1)
            if all(not(s & (1 << v)) for v in first):
                U.append(s >> 1)
    assert len(K) == len(D) + len(L)
    return K, D, L, U


def relative_collapse(complex_faces, target_faces):
    """Find a sequence of free face / maximal coface removals relative to target."""
    alive = set(complex_faces)
    target = set(target_faces)
    assert target <= alive
    supers = {s: 0 for s in alive}
    for face in alive:
        for bit in bits(face):
            if face ^ bit in supers:
                supers[face ^ bit] += 1
    heap = []
    for face in alive:
        if face and face not in target and not supers[face]:
            heapq.heappush(heap, (-face.bit_count(), face))
    number = 0
    while heap:
        _, top = heapq.heappop(heap)
        if top not in alive or supers[top]:
            continue
        eligible = [top ^ bit for bit in bits(top) if top ^ bit in alive and top ^ bit not in target and supers[top ^ bit] == 1]
        if not eligible:
            continue
        bottom = min(eligible)
        for removed in (top, bottom):
            alive.remove(removed)
            for bit in bits(removed):
                face = removed ^ bit
                if face in alive:
                    supers[face] -= 1
                    assert supers[face] >= 0
                    if face and face not in target and not supers[face]:
                        heapq.heappush(heap, (-face.bit_count(), face))
        number += 1
    assert alive == target, (len(alive), len(target), len(alive - target))
    assert 2 * number == len(complex_faces) - len(target_faces)
    return number


def reduced_betti_mod2(faces):
    graded = defaultdict(list)
    for face in faces:
        graded[face.bit_count()].append(face)
    ranks = {}
    for k in range(2, max(graded) + 1):
        index = {f: i for i, f in enumerate(graded[k - 1])}
        pivots = {}
        for f in graded[k]:
            col = 0
            for bit in bits(f):
                col ^= 1 << index[f ^ bit]
            while col:
                p = col.bit_length() - 1
                if p not in pivots:
                    pivots[p] = col
                    break
                col ^= pivots[p]
        ranks[k] = len(pivots)
    answer = {}
    for k in range(1, max(graded) + 1):
        dimension = len(graded[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0) - (k == 1)
        if dimension:
            answer[k - 1] = dimension
    return answer


def run():
    samples = [
        ('binary height three', [[2, 2], [2, 2]], 15, 1, 7),
        ('unequal leaf multiplicities', [[2, 3], [2, 2]], 16, 2, 7),
    ]
    for name, branches, size, expected_rank, degree in samples:
        K, D, L, U = complexes(branches)
        assert size == 1 + sum(1 + sum(1 + q for q in block) for block in branches)
        d_pairs = relative_collapse(D, U)
        l_pairs = relative_collapse(L, U)
        assert reduced_betti_mod2(K) == {}
        assert reduced_betti_mod2(U) == {degree: expected_rank}
        assert reduced_betti_mod2(D) == {degree: expected_rank}
        assert reduced_betti_mod2(L) == {degree: expected_rank}
        print(f'{name}: vertices={size}; faces K/D/L/U={len(K)}/{len(D)}/{len(L)}/{len(U)}; D->U pairs={d_pairs}; L->U pairs={l_pairs}; Htilde(U) F2 degree {degree} rank {expected_rank}; Htilde(K) zero; PASS')
    print('All checked finite cases PASS; the arbitrary-parameter theorem is proved symbolically in RESULT.md.')


if __name__ == '__main__':
    run()
