#!/usr/bin/env python3
"""Exact elementary certificate for the Fano-incidence independence complex.

Run with Python 3.9+ and no third-party packages. All assertions are mathematical
checks over finite integer and binary data; there is no randomized step.
"""
from collections import Counter, defaultdict, deque

POINTS = tuple(range(1, 8))                 # all nonzero vectors in F_2^3
NV = 14                                     # points 0..6; lines 7..13
BIT = 1 << NV
PIVOTS = (8, 10, 5, 9, 3, 11, 13, 2, 6, 0, 1, 7, 12, 4)


def parity(x):
    return x.bit_count() & 1


def has_edge(face):
    return any((face >> (p-1)) & (face >> (7+l-1)) & 1
               for p in POINTS for l in POINTS if parity(p & l) == 0)


def faces_by_bitmask():
    return set(face for face in range(BIT) if not has_edge(face))


def faces_by_backtracking():
    # Different construction: build all independent sets vertex by vertex.
    adj = [set() for _ in range(NV)]
    for p in POINTS:
        for l in POINTS:
            if not parity(p & l):
                adj[p-1].add(7+l-1)
                adj[7+l-1].add(p-1)
    out = set()
    def visit(pos, chosen):
        if pos == NV:
            out.add(sum(1 << v for v in chosen))
            return
        visit(pos+1, chosen)
        if not (adj[pos] & set(chosen)):
            visit(pos+1, chosen+(pos,))
    visit(0, ())
    return out


def toggle_matching(faces):
    unpaired = set(faces)
    pairs = []
    for vertex in PIVOTS:
        for lower in sorted(tuple(unpaired)):
            upper = lower | (1 << vertex)
            if not lower & (1 << vertex) and upper in unpaired:
                unpaired.remove(lower)
                unpaired.remove(upper)
                pairs.append((lower, upper))
    return pairs, unpaired


def acyclicity_certificate(faces, pairs):
    matched = set(pairs)
    outdegree = defaultdict(list)
    indegree = {f: 0 for f in faces}
    incidences = 0
    for upper in faces:
        for v in range(NV):
            if upper & (1 << v):
                lower = upper ^ (1 << v)
                if lower not in faces:
                    continue
                if (lower, upper) in matched:
                    before, after = lower, upper
                else:
                    before, after = upper, lower
                outdegree[before].append(after)
                indegree[after] += 1
                incidences += 1
    q = deque(f for f in faces if indegree[f] == 0)
    visited = 0
    while q:
        v = q.popleft()
        visited += 1
        for w in outdegree[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                q.append(w)
    assert visited == len(faces), (visited, len(faces))
    return incidences


def action_of_matrix(mat):
    def apply(v):
        return sum((parity(v & mat[i]) << i) for i in range(3))
    p = tuple(POINTS.index(apply(v)) for v in POINTS)
    lines = []
    for l in POINTS:
        candidates = [b for b in POINTS
                      if all(parity(apply(v) & b) == parity(v & l)
                             for v in POINTS)]
        assert len(candidates) == 1
        lines.append(7 + POINTS.index(candidates[0]))
    return p + tuple(lines)


def matrices_and_actions():
    # A matrix is determined by its three row bit-masks, each 0..7.
    result = []
    for r0 in range(8):
        for r1 in range(8):
            for r2 in range(8):
                mat = (r0, r1, r2)
                perm = action_of_matrix(mat) if independent_rows(mat) else None
                if perm is not None:
                    assert sorted(perm) == list(range(NV))
                    result.append(perm)
    assert len(result) == 168
    assert len(set(result)) == 168
    return result


def independent_rows(rows):
    space = {0}
    for r in rows:
        space = space | {v ^ r for v in space}
    return len(space) == 8


def element_order(perm):
    p = tuple(range(NV))
    for i in range(1, 9):
        p = tuple(perm[x] for x in p)
        if p == tuple(range(NV)):
            return i
    raise AssertionError('order exceeds 8')


def fixed_face_character(perm, faces):
    # Direct signed reduced Lefschetz enumeration, all 458 faces.
    lef = 0
    for face in faces:
        occupied = [i for i in range(NV) if face & (1 << i)]
        images = [perm[i] for i in occupied]
        if sorted(images) != occupied:
            continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images))
                         for j in range(i + 1, len(images)))
        lef += (-1 if ((len(occupied) - 1 + inversions) % 2) else 1)
    return -lef  # only reduced H_3 is nonzero


def orbit_independence_character(perm):
    # Independent orbit-polynomial: invariant faces are unions of cycles;
    # each included cycle contributes a factor -1 to -reduced Lefschetz.
    unvisited = set(range(NV))
    orbits = []
    while unvisited:
        start = min(unvisited)
        cur = start
        cyc = []
        while cur in unvisited:
            unvisited.remove(cur)
            cyc.append(cur)
            cur = perm[cur]
        assert cur == start
        orbits.append(sum(1 << v for v in cyc))
    allowed = [mask for mask in orbits if not has_edge(mask)]
    independent_polynomial_at_minus_one = 0
    for sel in range(1 << len(allowed)):
        union = 0
        for k,mask in enumerate(allowed):
            if sel & (1 << k): union |= mask
        if not has_edge(union):
            independent_polynomial_at_minus_one += -1 if parity(sel) else 1
    return independent_polynomial_at_minus_one


def main():
    faces = faces_by_bitmask()
    assert faces == faces_by_backtracking()
    assert len(faces) == 458
    assert Counter(f.bit_count()-1 for f in faces) == {
        -1:1,0:14,1:70,2:154,3:147,4:56,5:14,6:2}
    pairs, critical = toggle_matching(faces)
    assert len(pairs) == 226
    assert Counter(f.bit_count()-1 for f in critical) == {3:6}
    assert acyclicity_certificate(faces, pairs) == 1582
    # The empty face is paired with one vertex; remove that augmented pair
    # to obtain a matching with one critical vertex and six critical 3-cells.
    empty_pair = next((a,b) for a,b in pairs if a == 0)
    assert empty_pair[1].bit_count() == 1
    unaug_pairs = [pair for pair in pairs if pair != empty_pair]
    nonempty_faces = faces - {0}
    assert acyclicity_certificate(nonempty_faces, unaug_pairs) == 1568

    actions = matrices_and_actions()
    traces = defaultdict(set)
    counts = Counter()
    for perm in actions:
        order = element_order(perm)
        x = fixed_face_character(perm, faces)
        y = orbit_independence_character(perm)
        assert x == y, (order, x, y)
        traces[order].add(x)
        counts[order] += 1
    assert dict(counts) == {1:1,2:21,3:56,4:42,7:48}
    assert dict(traces) == {1:{6},2:{-2},3:{0},4:{2},7:{-1}}
    # The color-preserving action is a sum of conjugate complex 3-dimensional
    # characters (character norm 2), with no invariant vectors.
    assert sum(counts[k]*next(iter(traces[k])) for k in counts) == 0
    assert sum(counts[k]*next(iter(traces[k]))**2 for k in counts) == 336

    # Point-line duality p <-> hyperplane p is a graph automorphism since
    # incidence p.l=0 is symmetric. The entire graph automorphism group
    # consists of the 168 collineations and their 168 duality composites.
    tau = tuple(range(7,14)) + tuple(range(7))
    assert sorted(tau) == list(range(NV))
    all_edges = {tuple(sorted((p-1,7+l-1))) for p in POINTS for l in POINTS
                 if parity(p & l) == 0}
    assert len(all_edges) == 21
    outer = set()
    outer_orders = Counter()
    for g in actions:
        sw = tuple(g[tau[i]] for i in range(NV))
        assert sw not in actions
        assert {tuple(sorted((sw[i], sw[j]))) for i,j in all_edges} == all_edges
        assert fixed_face_character(sw, faces) == 0
        assert orbit_independence_character(sw) == 0
        outer.add(sw)
        outer_orders[element_order(sw)] += 1
    assert len(outer) == 168
    assert set(actions).isdisjoint(outer)
    assert dict(outer_orders) == {2:28,6:56,8:84}
    # Complete character inner product on the full 336-element group is 1:
    # the 6-dimensional rational representation is absolutely irreducible.
    assert (sum(counts[k]*next(iter(traces[k]))**2 for k in counts)
            + sum(0**2 for _ in outer)) == 336
    print('VERIFY_OK faces=458 hasse=1582 matching_pairs=226 critical_3=6 '
          'GL3_order=168 color_swaps=168 full_order=336 '
          'inner_character=1:6,2:-2,3:0,4:2,7:-1 '
          'outer_character=0 outer_orders=2:28,6:56,8:84 '
          'full_character_norm=1 direct_signed_faces=orbit_polynomial')


if __name__ == '__main__':
    main()
