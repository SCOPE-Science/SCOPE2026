#!/usr/bin/env python3
"""Independent finite homology check for the triangle-free clique-join theorem.

Only Python standard library. Enumerates all labelled triangle-free graphs on
1..5 vertices, forms the triangle-free-subset complex of their join with K_s,
and compares reduced homology over F_2 and F_3 with independently enumerated
independence complexes. The complete homotopy proof is mathematical, not finite.
"""
from itertools import combinations
from collections import defaultdict


def rank_mod_p(cols, p):
    pivots = {}
    rank = 0
    for col in cols:
        v = dict(col)
        while v:
            i = max(v)
            if i in pivots:
                z = v[i]
                for j, a in pivots[i].items():
                    w = (v.get(j, 0) - z * a) % p
                    if w:
                        v[j] = w
                    else:
                        v.pop(j, None)
            else:
                a = pow(v[i], -1, p)
                pivots[i] = {j: (w * a) % p for j, w in v.items()}
                rank += 1
                break
    return rank


def reduced_betti(faces, nverts, p):
    bins = defaultdict(list)
    for f in faces:
        bins[len(f) - 1].append(f)
    bins[-1] = [()]
    bdr = {}
    for d in range(0, nverts):
        low = {f: i for i, f in enumerate(bins[d - 1])}
        cols = []
        for f in bins[d]:
            terms = {}
            for j in range(len(f)):
                lower = f[:j] + f[j + 1:]
                terms[low[lower]] = 1 if j % 2 == 0 else p - 1
            cols.append(terms)
        bdr[d] = rank_mod_p(cols, p)
    return {d: (len(bins[d]) - bdr.get(d, 0) - bdr.get(d + 1, 0))
            for d in range(-1, nverts)
            if len(bins[d]) - bdr.get(d, 0) - bdr.get(d + 1, 0) != 0}


def all_faces(nverts, forbidden):
    return [face for r in range(nverts + 1)
            for face in combinations(range(nverts), r)
            if all(not all(v in face for v in bad) for bad in forbidden)]


def check(n, edges, s, p):
    edge_set = {frozenset(e) for e in edges}
    # Triangles are determined *from the complete graph*; do not inject the formula.
    all_edges = edge_set | {frozenset((a, b)) for a, b in combinations(range(n, n + s), 2)}
    all_edges |= {frozenset((a, b)) for a in range(n) for b in range(n, n + s)}
    triangles = [t for t in combinations(range(n + s), 3)
                 if all(frozenset(e) in all_edges for e in combinations(t, 2))]
    complex_faces = all_faces(n + s, triangles)
    left_betti = reduced_betti(complex_faces, n + s, p)

    # Independence complex independently defined by graph edges.
    independent_faces = all_faces(n, [tuple(sorted(e)) for e in edges])
    b = reduced_betti(independent_faces, n, p)
    predicted = defaultdict(int)
    predicted[1] += s * (s - 1) // 2
    for d, count in b.items():
        predicted[d + 1] += s * count
    predicted = {d: v for d, v in predicted.items() if v}
    assert left_betti == predicted, (n, edges, s, p, left_betti, predicted)
    return len(complex_faces), len(triangles)


def main():
    cases, faces, triangles = 0, 0, 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for bitmask in range(1 << len(pairs)):
            edges = [e for i, e in enumerate(pairs) if bitmask & (1 << i)]
            es = {frozenset(e) for e in edges}
            if any(all(frozenset(e) in es for e in combinations(t, 2))
                   for t in combinations(range(n), 3)):
                continue
            for s in (2, 3):
                for p in (2, 3):
                    nfaces, ntri = check(n, edges, s, p)
                    cases += 1
                    faces += nfaces
                    triangles += ntri
    # Larger geometric tests, not part of the labelled-graph census.
    for n in (6, 7):
        edges = [(i, (i + 1) % n) for i in range(n)]
        for s in (2, 3):
            for p in (2, 3):
                f, t = check(n, edges, s, p)
                faces += f
                triangles += t
                cases += 1
    print('TRIANGLE_FREE_CLIQUE_JOIN_HOMOLOGY_PASS')
    print('full_labelled_triangle_free_graphs_n_1_to_5 = 1 + 2 + 7 + 41 + 388')
    print('coefficient_fields = F2,F3')
    print('clique_sizes = 2,3')
    print('additional_cycles = C6,C7')
    print('checks =', cases)
    print('faces_visited =', faces)
    print('forbidden_triangle_instances =', triangles)


if __name__ == '__main__':
    main()
