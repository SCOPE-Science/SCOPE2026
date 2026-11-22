#!/usr/bin/env python3
"""Standalone finite certificates for multipath complexes of two small theta graphs.

Uses Python standard library. Every valid face, every Morse incidence and every
nonzero integer boundary entry is generated afresh from the graph definition.
"""
from collections import defaultdict, Counter, deque

CASES = [((2, 2, 4), (15, 13, 1, 7, 4, 6, 10, 2), (1, 0, 1, 6, 4)),
         ((2, 3, 3), (15, 13, 9, 7, 11, 3), (1, 0, 1, 6, 6))]


def graph(arms):
    edges = []
    vertex = 2
    for length in arms:
        path = [0] + list(range(vertex, vertex + length - 1)) + [1]
        vertex += length - 1
        edges.extend(zip(path[:-1], path[1:]))
    arcs = sorted([e for e in edges] + [(b, a) for a, b in edges])
    return vertex, arcs


def enumerate_faces(arms):
    n, arcs = graph(arms)
    assert n == 7 and len(arcs) == 16
    faces = {0}
    for mask in range(1, 1 << len(arcs)):
        # The property is hereditary: every proper subface must be valid.
        if any((mask ^ (1 << j)) not in faces for j in range(len(arcs))
               if mask & (1 << j)):
            continue
        indeg = outdeg = 0
        outgoing = {}
        for j, (u, v) in enumerate(arcs):
            if not mask & (1 << j):
                continue
            if indeg & (1 << v) or outdeg & (1 << u):
                break
            indeg |= 1 << v
            outdeg |= 1 << u
            outgoing[u] = v
        else:
            for start in outgoing:
                current = outgoing[start]
                while current in outgoing and current != start:
                    current = outgoing[current]
                if current == start:
                    break
            else:
                faces.add(mask)
    return arcs, faces


def independently_generate_faces(arms):
    # A second face generation using recursive include/exclude, not the
    # downward-closure dynamic predicate used in enumerate_faces.
    count, arcs = graph(arms)
    result = set()
    def rec(i, mask, outgoing, incoming):
        if i == len(arcs):
            result.add(mask)
            return
        rec(i + 1, mask, outgoing, incoming)
        u, v = arcs[i]
        if u in outgoing or v in incoming:
            return
        w = v
        while w in outgoing:
            w = outgoing[w]
            if w == u:
                return
        if w == u:
            return
        outgoing[u] = v
        incoming.add(v)
        rec(i + 1, mask | (1 << i), outgoing, incoming)
        del outgoing[u]
        incoming.remove(v)
    rec(0, 0, {}, set())
    return result


def count_by_dimension(faces):
    return dict(sorted(Counter(f.bit_count() - 1 for f in faces if f).items()))


def check_matching(faces, pivots):
    rest = set(faces) - {0}
    paired = []
    for vertex in pivots:
        bit = 1 << vertex
        matches = [(f, f | bit) for f in rest if not (f & bit) and
                   (f | bit) in rest]
        assert matches, ('empty stage', vertex)
        assert len({a for a, b in matches}) == len(matches)
        for small, large in matches:
            assert small in rest and large in rest and large.bit_count() == small.bit_count() + 1
            rest.remove(small)
            rest.remove(large)
        paired.extend(matches)
    # Every lower-dimensional-face -> upper-dimensional-face Hasse incidence is
    # reversed precisely for matching pairs. Exhaustive DAG check rules out cycles.
    face_index = {f: i for i, f in enumerate(sorted(faces - {0}))}
    matched = set(paired)
    n = len(face_index)
    degrees = [0] * n
    adj = [[] for _ in range(n)]
    for large in face_index:
        for j in range(large.bit_length()):
            if not large & (1 << j):
                continue
            small = large ^ (1 << j)
            if not small:
                continue
            assert small in face_index
            src, dst = (small, large) if (small, large) in matched else (large, small)
            si, di = face_index[src], face_index[dst]
            adj[si].append(di)
            degrees[di] += 1
    ready = deque(i for i, d in enumerate(degrees) if d == 0)
    seen = 0
    while ready:
        u = ready.popleft()
        seen += 1
        for v in adj[u]:
            degrees[v] -= 1
            if degrees[v] == 0:
                ready.append(v)
    assert seen == n, ('closed gradient path', seen, n)
    critical_counts = count_by_dimension(rest)
    assert len(paired) * 2 + len(rest) + 1 == len(faces)
    return critical_counts, len(paired), len(rest), seen


def boundary_rows(by_dimension, degree):
    lower = {m: j for j, m in enumerate(by_dimension[degree - 1])}
    rows = [dict() for _ in lower]
    for col, large in enumerate(by_dimension[degree]):
        positions = [j for j in range(large.bit_length()) if large & (1 << j)]
        for loc, bit in enumerate(positions):
            row = lower[large ^ (1 << bit)]
            rows[row][col] = -1 if loc % 2 else 1
    return rows


def unit_smith_rank(rows):
    """Unimodular integer Smith reduction; accepts ONLY matrices with all invariant factors 1.

    All operations are integer elementary row/column transformations, but with
    each unit pivot we clear its column using row operations and then remove its
    row and column. The remaining submatrix has the same integral cokernel as
    the original after removing a free unit summand.
    """
    rows = {i: dict(r) for i, r in enumerate(rows) if r}
    indexed = defaultdict(set)
    for i, row in rows.items():
        for j in row:
            indexed[j].add(i)
    steps = 0
    while rows:
        chosen = None
        for i, r in rows.items():
            for j, v in r.items():
                if abs(v) == 1:
                    cost = (len(r) - 1) * (len(indexed[j]) - 1)
                    if chosen is None or cost < chosen[0]:
                        chosen = cost, i, j, v
                        if cost == 0:
                            break
            if chosen is not None and chosen[0] == 0:
                break
        assert chosen is not None, ('non-unit Smith block', rows)
        _, i, j, unit = chosen
        pivot_row = rows[i]
        for other in list(indexed[j]):
            if other == i:
                continue
            factor = rows[other][j] * unit
            for k, val in list(pivot_row.items()):
                newval = rows[other].get(k, 0) - factor * val
                if newval:
                    rows[other][k] = newval
                    indexed[k].add(other)
                else:
                    rows[other].pop(k, None)
                    indexed[k].discard(other)
            if not rows[other]:
                del rows[other]
        for k in pivot_row:
            indexed[k].discard(i)
        del rows[i]
        indexed.pop(j, None)
        steps += 1
    return steps


def verify_boundary_squared(bydim):
    for degree in range(2, max(bydim) + 1):
        codomain = {f: i for i, f in enumerate(bydim[degree - 2])}
        for face in bydim[degree]:
            terms = Counter()
            bits = [j for j in range(face.bit_length()) if face & (1 << j)]
            for i, a in enumerate(bits):
                rem = face ^ (1 << a)
                bits2 = [j for j in range(rem.bit_length()) if rem & (1 << j)]
                for k, b in enumerate(bits2):
                    terms[rem ^ (1 << b)] += (-1) ** (i + k)
            assert all(v == 0 for v in terms.values())
            assert all(f in codomain for f in terms)


def main():
    for arms, pivots, expected_morse in CASES:
        arcs, faces = enumerate_faces(arms)
        assert faces == independently_generate_faces(arms), "independent enumeration disagrees"
        assert len(faces) in (681, 687)
        fv = count_by_dimension(faces)
        bydim = {k: sorted(m for m in faces if m and m.bit_count() == k + 1) for k in fv}
        verify_boundary_squared(bydim)
        critical, match_count, _, seen = check_matching(faces, pivots)
        morse = tuple(critical.get(k, 0) for k in range(5))
        assert morse == expected_morse, (arms, morse, expected_morse)
        assert 5 not in critical and 0 in critical
        ranks = {0: 0}
        for k in range(1, max(fv) + 1):
            ranks[k] = unit_smith_rank(boundary_rows(bydim, k))
        betti = {k: fv[k] - ranks.get(k, 0) - ranks.get(k + 1, 0) for k in fv}
        expect_h4 = 4 if arms == (2, 2, 4) else 6
        assert betti == {0: 1, 1: 0, 2: 0, 3: 5, 4: expect_h4, 5: 0}
        print('ARMS', arms)
        print('ORDERED_ARCS', arcs)
        print('FULL_F_VECTOR', fv, 'INCLUDING_EMPTY', len(faces))
        print('MORSE_PIVOTS', pivots, 'PAIRS', match_count, 'DAG_CHECKED_VERTICES', seen)
        print('MORSE_CRITICAL', critical)
        print('UNIT_INTEGER_SMITH_RANKS', ranks)
        print('INTEGRAL_BETTI', betti)
        print('WEDGE_TYPE: 5 spheres S^3 and', expect_h4, 'spheres S^4')
        print('CHECKS_OK')

if __name__ == '__main__':
    main()
