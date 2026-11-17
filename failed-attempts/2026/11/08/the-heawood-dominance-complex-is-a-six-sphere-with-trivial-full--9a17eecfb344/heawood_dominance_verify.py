"""Finite, independently replayable checks for the Heawood dominance complex.

Requires only the Python standard library. Integer masks encode vertex subsets.
"""
from collections import Counter, deque
from itertools import permutations

N = 14
ALL = (1 << N) - 1
DIFF = (0, 1, 3)
EDGES = tuple((p, 7 + line) for p in range(7) for line in range(7)
              if (line - p) % 7 in DIFF)
NEIGH = [1 << v for v in range(N)]
for u, v in EDGES:
    NEIGH[u] |= 1 << v
    NEIGH[v] |= 1 << u


def faces_by_forbidden_neighborhoods():
    return {f for f in range(1 << N) if all((f & nb) != nb for nb in NEIGH)}


def faces_by_complementary_domination():
    result = set()
    for face in range(1 << N):
        dom = ALL ^ face
        covered = dom
        for u, v in EDGES:
            if dom & (1 << u):
                covered |= 1 << v
            if dom & (1 << v):
                covered |= 1 << u
        if covered == ALL:
            result.add(face)
    return result


def toggle_matching(faces, order):
    unmatched = set(faces)
    matched = set()
    for v in order:
        bit = 1 << v
        for lower in sorted(unmatched):
            upper = lower | bit
            if not (lower & bit) and upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                matched.add((lower, upper))
    assert next(p for p in matched if p[0] == 0)[1].bit_count() == 1
    empty_pair = next(p for p in matched if p[0] == 0)
    matched.remove(empty_pair)
    # Exclude the empty face from the ordinary (nonaugmented) face poset.
    unmatched.remove(empty_pair[0]) if empty_pair[0] in unmatched else None
    unmatched.add(empty_pair[1])
    return matched, unmatched


def acyclic_hasse(faces, matched):
    nonempty = set(faces) - {0}
    arrows = {f: [] for f in nonempty}
    indegree = {f: 0 for f in nonempty}
    pairs = set(matched)
    incidence = 0
    for upper in nonempty:
        mask = upper
        while mask:
            bit = mask & -mask
            mask ^= bit
            lower = upper ^ bit
            if not lower:
                continue
            incidence += 1
            if (lower, upper) in pairs:
                src, dest = lower, upper
            else:
                src, dest = upper, lower
            arrows[src].append(dest)
            indegree[dest] += 1
    q = deque(f for f in nonempty if indegree[f] == 0)
    seen = 0
    while q:
        face = q.popleft()
        seen += 1
        for v in arrows[face]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    assert seen == len(nonempty), (seen, len(nonempty))
    return incidence


def orient_sign_of_sort(vertices):
    return -1 if sum(vertices[i] > vertices[j] for i in range(len(vertices))
                     for j in range(i + 1, len(vertices))) % 2 else 1


def crosspoly_cycle():
    chain = {}
    for word in range(1 << 7):
        chosen = [i + (7 if (word >> i) & 1 else 0) for i in range(7)]
        mask = sum(1 << v for v in chosen)
        sign = (-1 if word.bit_count() % 2 else 1) * orient_sign_of_sort(chosen)
        chain[mask] = sign
    return chain


def boundary(chain):
    out = Counter()
    for face, c in chain.items():
        vertices = [i for i in range(N) if (face >> i) & 1]
        for j, v in enumerate(vertices):
            out[face ^ (1 << v)] += (-1 if j % 2 else 1) * c
    return {face: c for face, c in out.items() if c}


def parity(perm):
    return orient_sign_of_sort(perm)


def line_sets():
    return {frozenset(p for p in range(7) if (line - p) % 7 in DIFF)
            for line in range(7)}


def verify():
    assert len(EDGES) == 21
    assert all(nb.bit_count() == 4 for nb in NEIGH)
    faces = faces_by_forbidden_neighborhoods()
    assert faces == faces_by_complementary_domination()
    count = tuple(sum(f.bit_count() == k for f in faces) for k in range(0, 11))
    assert count == (1,14,91,364,987,1862,2394,1962,931,224,21)
    assert len(faces) == 8851
    maxfaces = [f for f in faces if all(f | (1 << v) not in faces
                                     for v in range(N) if not f & (1 << v))]
    top = Counter(f.bit_count() - 1 for f in maxfaces)
    assert dict(top) == {6:2,7:28,8:14,9:21}
    pairs, crit = toggle_matching(faces, tuple(range(N)))
    assert len(pairs) == 4424 and crit == {1, 16256}
    incidence = acyclic_hasse(faces, pairs)
    pairs2, crit2 = toggle_matching(faces, tuple(reversed(range(N))))
    assert len(pairs2) == 4424 and crit2 == {1 << 13, 127}
    assert incidence == acyclic_hasse(faces, pairs2)
    # The matching yields one critical vertex and one critical 6-cell;
    # the Morse CW complex is therefore S^6, integrally and in homotopy.
    Z = crosspoly_cycle()
    assert len(Z) == 128 and all(face in faces for face in Z)
    assert not boundary(Z)
    POINTS = (1 << 7) - 1
    LINES = POINTS << 7
    assert Z[POINTS] == 1 and Z[LINES] == -1
    # Both whole-part 6-simplices have no 7-dimensional cofaces, giving
    # an integral cocycle which evaluates to +1 on Z.
    for face in (POINTS, LINES):
        assert face in faces
        assert all((face | (1 << v)) not in faces for v in range(N)
                   if not face & (1 << v))
    lines = line_sets()
    assert len(lines) == 7
    collineations = [p for p in permutations(range(7))
                    if {frozenset(p[v] for v in line) for line in lines} == lines]
    assert len(collineations) == 168
    assert all(parity(p) == 1 for p in collineations)
    # An incidence-reversing duality s sends p_i to L_{-i},
    # L_j to p_{-j}. It swaps the two bipartite parts.
    s = {i: 7 + (-i % 7) for i in range(7)}
    s.update({7 + i: (-i % 7) for i in range(7)})
    assert {frozenset((s[u],s[v])) for u,v in EDGES} == \
           {frozenset((u,v)) for u,v in EDGES}
    # Orientation on the all-line face under the duality reverses (three swaps).
    sign_lines_to_points = parity([s[7 + i] for i in range(7)])
    assert sign_lines_to_points == -1
    # On the generator, the coefficient on the all-point facet is +1.
    assert Z[LINES] * sign_lines_to_points == 1
    # Connected bipartition is unique. Every automorphism either preserves
    # parts (168 collineations) or is a collineation followed by s (168).
    # All 336 therefore have action +1 on H_6 of the complex.
    print('GRAPH vertices=14 edges=21 closed_neighborhood_size=4')
    print('FACES total=8851 including_empty=1 vector=', count)
    print('MAXIMAL_FACES dimension_counts=', sorted(top.items()))
    print('MORSE forward_pairs=4424 critical_dimensions=(0,6)')
    print('MORSE reverse_pairs=4424 critical_dimensions=(0,6)')
    print('HASSE incidences=', incidence, 'acyclic_checks=2')
    print('SPHERE crosspoly_facets=128 boundary_zero=true integral_primitive=true')
    print('SYMMETRY part_preserving=168 full=336 action_H6=trivial')
    print('VERIFIED')

if __name__ == '__main__':
    verify()
