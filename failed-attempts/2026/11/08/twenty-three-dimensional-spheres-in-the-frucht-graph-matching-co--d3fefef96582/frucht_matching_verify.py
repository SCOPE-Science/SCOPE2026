#!/usr/bin/env python3
"""Exact finite certificate for the ordinary matching complex of the Frucht graph.

Python 3 standard library only. Edges are reconstructed from the classical
12-vertex LCF representation. Every matching and every face-poset cover is
enumerated, and an explicit acyclic matching is checked independently.
"""
from collections import Counter, deque

LCF = (-5, -2, -4, 2, 5, -2, 2, 5, -2, -5, 4, 2)
PIVOTS = (9, 3, 4, 17, 15, 1, 0, 8, 13, 12, 2, 14, 10, 16, 6, 11, 5, 7)


def graph_edges():
    e = set()
    for v, d in enumerate(LCF):
        e.add(tuple(sorted((v, (v + 1) % 12))))
        e.add(tuple(sorted((v, (v + d) % 12))))
    return sorted(e)


def all_faces(edges):
    # Enumerate every subset of the eighteen graph edges, testing disjointness.
    ans = set()
    used = [0] * len(edges)
    for i, (a, b) in enumerate(edges):
        used[i] = (1 << a) | (1 << b)
    for bits in range(1, 1 << len(edges)):
        covered = 0
        ok = True
        for j in range(len(edges)):
            if bits & (1 << j):
                if covered & used[j]:
                    ok = False
                    break
                covered |= used[j]
        if ok:
            ans.add(bits)
    return ans


def independent_face_enumeration(edges):
    # Independent recursive enumeration, extending only disjoint matchings.
    output = set()
    def visit(pos, edge_bits, used_vertices):
        if pos == len(edges):
            if edge_bits:
                output.add(edge_bits)
            return
        visit(pos + 1, edge_bits, used_vertices)
        a, b = edges[pos]
        vertices = (1 << a) | (1 << b)
        if used_vertices & vertices == 0:
            visit(pos + 1, edge_bits | (1 << pos), used_vertices | vertices)
    visit(0, 0, 0)
    return output


def discrete_morse(faces):
    # Match sigma with sigma+{pivot} only while both survive. Each face
    # belongs to at most one matching pair.
    alive = set(faces)
    pairs = []
    for j in PIVOTS:
        bit = 1 << j
        for small in sorted(alive):
            large = small | bit
            if small in alive and not(small & bit) and large in alive:
                pairs.append((small, large))
                alive.remove(small)
                alive.remove(large)
    return pairs, alive


def verify_acyclicity(faces, pairs, n_edges):
    # The Hasse orientation is reversed precisely on matched covering edges.
    matched = set(pairs)
    out = {s: [] for s in faces}
    indeg = {s: 0 for s in faces}
    num_covers = 0
    for small in faces:
        for j in range(n_edges):
            bit = 1 << j
            large = small | bit
            if small & bit or large not in faces:
                continue
            num_covers += 1
            if (small, large) in matched:
                head, tail = small, large
            else:
                head, tail = large, small
            out[tail].append(head)
            indeg[head] += 1
    queue = deque(s for s, degree in indeg.items() if degree == 0)
    topological_count = 0
    while queue:
        s = queue.popleft()
        topological_count += 1
        for t in out[s]:
            indeg[t] -= 1
            if indeg[t] == 0:
                queue.append(t)
    assert topological_count == len(faces), 'Morse matching has a directed cycle'
    return num_covers, topological_count


def boundary_rank_mod_p(lower, upper, p):
    # Sparse column Gaussian elimination of the simplicial boundary.
    index = {s: i for i, s in enumerate(lower)}
    pivots = {}
    for s in upper:
        col = {}
        position = 0
        for i in range(18):
            if not(s & (1 << i)):
                continue
            b = s & ~(1 << i)
            coef = 1 if position % 2 == 0 else p - 1
            idx = index[b]
            col[idx] = coef
            position += 1
        while col:
            r = max(col)
            if r not in pivots:
                inv = pow(col[r], -1, p)
                pivots[r] = {k: (v * inv) % p for k, v in col.items()}
                break
            mult = col[r]
            for k, value in pivots[r].items():
                new = (col.get(k, 0) - mult * value) % p
                if new:
                    col[k] = new
                else:
                    col.pop(k, None)
    return len(pivots)


def main():
    edges = graph_edges()
    assert len(LCF) == 12 and len(edges) == 18
    degrees = Counter(v for e in edges for v in e)
    assert len(degrees) == 12 and set(degrees.values()) == {3}
    faces = all_faces(edges)
    assert faces == independent_face_enumeration(edges)
    fvector = Counter(s.bit_count()-1 for s in faces)
    assert [fvector[i] for i in range(6)] == [18,117,333,397,152,8]
    # Record every inclusion-maximal matching, rather than merely top-size ones.
    facets = [s for s in faces if not any((s | (1 << j)) in faces
                                        for j in range(len(edges)) if not(s & (1 << j)))]
    facet_sizes = dict(sorted(Counter(s.bit_count() for s in facets).items()))
    assert facet_sizes == {4:21, 5:104, 6:8}, facet_sizes
    # A concrete K4 minor shows that the graph is not outerplanar.
    branches = [{0, 11, 6, 7}, {10, 1, 2, 3}, {8, 9, 4}, {5}]
    assert len(set.union(*branches)) == 12 and all(branches[i].isdisjoint(branches[j])
                          for i in range(4) for j in range(i+1,4))
    for part in branches:
        visited = {next(iter(part))}
        while True:
            expanded = visited | {b for a,b in edges if a in visited and b in part} | {a for a,b in edges if b in visited and a in part}
            if expanded == visited: break
            visited = expanded
        assert visited == part
    for i in range(4):
        for j in range(i+1,4):
            assert any((a in branches[i] and b in branches[j]) or
                       (b in branches[i] and a in branches[j]) for a,b in edges)
    pairs, critical = discrete_morse(faces)
    assert len(pairs) == 502
    assert len(set(s for a,b in pairs for s in (a,b))) == 1004
    assert Counter(s.bit_count()-1 for s in critical) == {0:1,3:20}
    covers, processed = verify_acyclicity(faces, pairs, len(edges))
    assert covers == 3629 and processed == 1025
    groups = [[s for s in sorted(faces) if s.bit_count() == i + 1] for i in range(6)]
    ranks = {}
    for p in (2,3,5):
        rr = [boundary_rank_mod_p(groups[i-1], groups[i], p) for i in range(1,6)]
        assert rr == [17,100,233,144,8], (p,rr)
        ranks[p] = rr
    print('FRUCHT_MATCHING_CERTIFICATE')
    print('LCF:',list(LCF))
    print('edges:', edges)
    print('face_vector:', [fvector[i] for i in range(6)])
    print('nonempty_faces:', len(faces))
    print('maximal_matching_size_profile:', facet_sizes)
    print('K4_minor_branch_sets:', [sorted(x) for x in branches])
    print('matched_pairs:',len(pairs))
    print('critical_vector:', sorted(Counter(s.bit_count()-1 for s in critical).items()))
    print('critical_vertex_edge_index:', (next(s for s in critical if s.bit_count()==1)).bit_length()-1)
    print('face_poset_covers:',covers)
    print('topological_sort_vertices:',processed)
    print('boundary_ranks_F2_F3_F5:',ranks)
    print('reduced_betti:',{3:20})
    print('FRUCHT_MATCHING_WEDGE_20_S3_PASS')

if __name__ == '__main__':
    main()
