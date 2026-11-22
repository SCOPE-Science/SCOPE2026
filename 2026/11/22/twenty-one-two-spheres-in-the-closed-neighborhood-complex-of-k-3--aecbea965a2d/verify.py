#!/usr/bin/env python3
"""Exact finite simplicial and discrete-Morse certificate for a graph nerve.

Uses Python 3 standard library only; no precomputed topology data.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 4
WIDTH = 3
VERTICES = N * WIDTH


def graph_closed_facets():
    facets = set()
    for i in range(N):
        for a in range(WIDTH):
            labels = [WIDTH * i + b for b in range(WIDTH)]
            labels.extend((WIDTH * ((i - 1) % N) + a,
                           WIDTH * ((i + 1) % N) + a))
            assert len(set(labels)) == 5
            facets.add(sum(1 << q for q in labels))
    assert len(facets) == 12
    return facets


def enumerate_faces(facets):
    out = set()
    for facet in facets:
        bits = [i for i in range(VERTICES) if facet & (1 << i)]
        for k in range(1, len(bits) + 1):
            for combo in combinations(bits, k):
                out.add(sum(1 << i for i in combo))
    return out


def matching(faces, order):
    left = set(faces)
    pairs = []
    for vertex in order:
        bit = 1 << vertex
        chosen = []
        for f in sorted(left):
            if f & bit:
                continue
            g = f | bit
            if g in left:
                chosen.append((f, g))
        used = set()
        for f, g in chosen:
            assert f in left and g in left
            assert f not in used and g not in used
            assert (g ^ f) == bit and (f & g) == f
            used.add(f)
            used.add(g)
        left -= used
        pairs.extend(chosen)
    assert len(set(sum(([f, g] for f, g in pairs), []))) == 2 * len(pairs)
    assert 2 * len(pairs) + len(left) == len(faces)
    return pairs, left


def is_acyclic(faces, pairs):
    pairset = set(pairs)
    indegree = {f: 0 for f in faces}
    arcs = defaultdict(list)
    covers = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            if lower == 0:
                continue
            assert lower in faces
            if (lower, upper) in pairset:
                src, dest = lower, upper
            else:
                src, dest = upper, lower
            arcs[src].append(dest)
            indegree[dest] += 1
            covers += 1
    queue = deque(f for f, d in indegree.items() if d == 0)
    seen = 0
    while queue:
        f = queue.popleft()
        seen += 1
        for g in arcs[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
    assert seen == len(faces), f'closed gradient path: visited {seen}/{len(faces)}'
    return covers


def mod2_rank(lower, upper):
    positions = {f: i for i, f in enumerate(lower)}
    pivots = {}
    rank = 0
    for f in upper:
        column = 0
        bits = f
        while bits:
            bit = bits & -bits
            bits -= bit
            column ^= 1 << positions[f ^ bit]
        while column:
            pivot = column.bit_length() - 1
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot] = column
                rank += 1
                break
    return rank


def main():
    facets = graph_closed_facets()
    faces = enumerate_faces(facets)
    by_dim = {d: sorted(f for f in faces if f.bit_count() == d + 1)
              for d in range(5)}
    f_vector = tuple(len(by_dim[d]) for d in range(5))
    assert f_vector == (12, 54, 112, 60, 12)
    assert len(faces) == 250
    # Three independent pivot orders reconstruct the Morse certificate.
    orders = (
        tuple(range(VERTICES)),
        tuple(reversed(range(VERTICES))),
        tuple(sorted(range(VERTICES), key=lambda x: (x % WIDTH, x // WIDTH))),
    )
    outputs = []
    for order in orders:
        pairs, critical = matching(faces, order)
        covers = is_acyclic(faces, pairs)
        dimensions = dict(sorted(Counter(f.bit_count() - 1 for f in critical).items()))
        assert len(pairs) == 114
        assert dimensions == {0: 1, 2: 21}
        outputs.append((len(pairs), dimensions, covers))
    assert all(x == outputs[0] for x in outputs)
    # Independent simplicial boundary computation over F_2 (not Morse data).
    ranks = {d: mod2_rank(by_dim[d-1], by_dim[d]) for d in range(1, 5)}
    betti = {d: len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d+1, 0)
             for d in range(5)}
    assert ranks == {1: 11, 2: 43, 3: 48, 4: 12}
    assert betti == {0: 1, 1: 0, 2: 21, 3: 0, 4: 0}
    print('GRAPH K_3 square C_4')
    print('closed-neighborhood facets:', len(facets))
    print('nonempty simplices:', len(faces))
    print('face vector:', f_vector)
    print('pivot-orders:', len(orders))
    print('acyclic pairs per order:', outputs[0][0])
    print('cover incidences checked per order:', outputs[0][2])
    print('critical cells per order:', outputs[0][1])
    print('simplicial F2 boundary ranks:', tuple(ranks[d] for d in range(1, 5)))
    print('simplicial F2 Betti numbers:', tuple(betti[d] for d in range(5)))
    print('homotopy type: wedge of 21 two-spheres')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
